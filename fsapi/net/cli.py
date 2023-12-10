# MIT License

# Copyright (c) 2023 MatrixEditor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import annotations

import argparse
import pathlib
import texttable
import typing as t

from xml.etree import ElementTree
from colorama import Fore

from fsapi.net import (
    FSDevice,
    nodes,
    Node,
    dynamic,
    FSResponse,
    IntEnumValue,
    Method,
    NodeE8,
    wrap,
    Status,
)
from fsapi.isu import (
    find_update,
    url_find_update,
    UpdateStatus,
    url_get_update,
    get_update,
    UpdateError,
)
from fsapi.isu.util import DataclassPrinter


# Internal use only!
class NodePrinter(DataclassPrinter):
    def _print(self, *msg) -> None:
        self.print_msg(Fore.LIGHTBLACK_EX, *msg)

    def get_format(self, name: str, value) -> str:
        if isinstance(value, IntEnumValue):
            result = f"<{value.stringvalue}: {value}>"
            result_c = Fore.CYAN + result
            return result_c if self.colorized else result
        return super().get_format(name, value)

    def print_cls(self, node_class: t.Type[Node], indent=3) -> None:
        self._print(" " * indent, f"> {node_class.name} ({node_class.__name__}):")
        for key in ("path", "readonly", "cacheable", "notifying"):
            # Default attributes will be printed first
            self._print(
                " " * (indent + 4),
                f"- {key}:",
                self.get_format("", getattr(node_class, key)),
            )

        self._print(
            " " * (indent + 4),
            "- type:" + Fore.RESET,
            self.get_format("", node_class.__base__),
        )
        self._print(" " * (indent + 4), "- prototype:")
        if node_class.prototype is dynamic:
            # As dynamic prototypes can't be displayed yet, we have to
            # introcude a hint ot the user.
            self.print_msg(Fore.LIGHTYELLOW_EX, " " * (indent + 8), "/dynamic/")
        else:
            for i, argument in enumerate(node_class.prototype):
                # each value in an array will be represented as follows:
                # [<index>] => '<name>'
                #    - length: <length>
                #    - type: <type>
                msg = " " * (indent + 8) + self.get_array_format(i)
                self.out(msg + self.get_format("", argument.name))
                self._print(
                    " " * (indent + 12),
                    "- length:",
                    self.get_format("", argument.length),
                )
                self._print(
                    " " * (indent + 12),
                    "- type:",
                    self.get_format("", argument.type),
                )

        if issubclass(node_class, NodeE8):
            self._print(" " * (indent + 4), "- enum values:")
            for key, value in node_class.defaults.items():
                key = self.get_format("key", key)
                value = self.get_format("value", value)
                self.out(" " * (indent + 8) + self.get_array_format(key) + value)

    def print_fsresponse(self, response: FSResponse, indent=3) -> None:
        if response.node is not None:
            path_fmt = self.get_format("", response.node.cls.path) + Fore.RESET
        else:
            # REVISIT: The node's path won't be displayed if an error occurred
            path_fmt = self.get_msg(Fore.RED, "/error/") + Fore.RESET
        method_fmt = self.get_format("", response.method) + Fore.RESET
        msg = "> FSResponse" + Fore.RESET + "(%s, %s)" % (path_fmt, method_fmt)
        self._print(msg)
        self._print(
            " " * (indent),
            "- status:",
            self.get_format("", response.status),
        )
        if response.node is not None and response.node.value is not None:
            node = response.node
            self.print_node(node, indent=indent)

    def print_node(self, node: Node, indent=3) -> None:
        if node.cls.is_list:
            self._print(" " * indent, "- value:")
            for i, item in enumerate(node.value):
                # Same format as specified above with the node's prototype
                msg = " " * (indent + 4) + self.get_array_format(item["key"])
                self.out(msg + self.get_format("", type(item)))
                for key, val in item.attrib.items():
                    if key == "key":
                        continue
                    self._print(
                        " " * (indent + 8),
                        f"- {key}:",
                        self.get_format(key, val),
                    )
        else:
            self._print(
                " " * indent,
                "- value:",
                self.get_format("", node.value),
            )

    def print_url(self, url: str):
        self._print("> URL:", self.get_format("url", url))

    def print_err(self, error: Exception, indent=0):
        self.print_msg(
            Fore.RED, " " * indent, f"- {error.__class__.__name__}:", str(error)
        )


def _setup_device(host, pin, force_session, simulate, pp=None):
    device = FSDevice(host=host, pin=pin)
    if force_session:
        if simulate:
            pp.print_url(device.get_url(Method.CREATE_SESSION))
        else:
            device.new_session()
    return device


def _raw(device, pp, *elements, **argv):
    tree = device.request("/".join(["fsapi"] + list(elements)), config=None, **argv)
    if isinstance(tree, ElementTree.Element):
        ElementTree.indent(tree)
        print(ElementTree.tostring(tree).decode())
    else:
        pp._print("> Invalid response:", tree)


# COMMMAND: VIEW
def View(value: str, search=False, disable_color=False, **kwds) -> None:
    """
    With this command a user should be able to inspect defined node classes
    and search for available ones.

    :param value: the search string or
    :type value: str
    :param search: whether a search should be performed, defaults to False
    :type search: bool, optional
    :param disable_color: whether to disable colorized output, defaults to False
    :type disable_color: bool, optional
    """
    pp = NodePrinter(colorized=not disable_color)
    path = nodes / value
    if search:
        values = list(path.iter_nodes())
        if len(values) == 0:
            pp.print_msg(Fore.YELLOW, "[!] No results for input:", path)
        else:
            pp.print_msg(Fore.LIGHTBLACK_EX, "> Result of search:")
            for i, node_path in enumerate(values):
                msg = " " * 3 + pp.get_array_format(i)
                pp.out(msg + pp.get_format("", node_path))
    else:
        if not path.exists():
            pp.print_msg(Fore.RED, "[!] No node at path:", path)
        else:
            pp.print_cls(path.get_node_type(), 0)


# COMMAND: GET
def Get(
    host: str,
    pin: str,
    nodes: t.List[str],
    force_session=False,
    disable_color=False,
    simulate=False,
    raw=False,
) -> None:
    """Fetches a value for a spefic node."""
    pp = NodePrinter(colorized=not disable_color)
    device = _setup_device(host, pin, force_session, simulate, pp)
    if simulate:
        if len(nodes) == 1:
            pp.print_url(device.get_url(Method.GET, nodes[0]))
        else:
            pp.print_url(device.get_url(Method.GET_MULTIPLE, node=nodes))
        return

    if not raw:
        responses = device.get(*nodes)
        if isinstance(responses, list):
            for response in responses:
                pp.print_fsresponse(response)
                print()
        else:
            pp.print_fsresponse(responses)
    else:
        if len(nodes) == 1:
            _raw(device, pp, Method.GET.name, nodes[0])
        else:
            _raw(device, pp, Method.GET_MULTIPLE.name, node=nodes)


# COMMAND: LIST
def List(
    host: str,
    pin: str,
    node: str,
    pos=-1,
    max_items=0xFFFF,
    disable_color=False,
    force_session=False,
    simulate=False,
    raw=False,
) -> None:
    """Fetches values from a list node"""
    pp = NodePrinter(colorized=not disable_color)
    device = _setup_device(host, pin, force_session, simulate, pp)
    if simulate:
        pp.print_url(
            device.get_url(Method.LIST_GET_NEXT, node, pos, maxItems=max_items)
        )
    else:
        if not raw:
            response = device.list_get_next(node, maxItems=max_items, _pos=pos)
            pp.print_fsresponse(response)
        else:
            _raw(device, pp, Method.LIST_GET_NEXT.name, node)


# COMMAND: SET
def Set(
    host: str,
    pin: str,
    node: str,
    value: str,
    disable_color=False,
    force_session=False,
    simulate=False,
    raw=False,
) -> None:
    """Tries to apply a new value to a given node."""
    pp = NodePrinter(colorized=not disable_color)
    device = _setup_device(host, pin, force_session, simulate, pp)
    if simulate:
        pp.print_url(device.get_url(Method.SET, node, value=value))
    else:
        if not raw:
            response = device.put(node, value=value)
            pp.print_fsresponse(response)
        else:
            _raw(device, pp, Method.SET.name, node, value=value)


# COMMAND: GET_NOTIFIES
def GetNotifies(
    host: str,
    pin: str,
    disable_color=False,
    simulate=False,
    force_session=False,
    raw=False,
    **kwds,
) -> None:
    """Queries all notifies of the target device"""
    pp = NodePrinter(colorized=not disable_color)
    device = _setup_device(host, pin, force_session, simulate, pp)

    if raw:
        # Just print the XML data and return
        _raw(device, pp, Method.GET_NOTIFIES.name)
        return

    result = device.get_notifies()
    pp._print("> Got %d notifies:" % len(result))
    for node in result:
        pp.print_node(node, 0)


# COMMAND: UPDATE CHECK
def CheckForUpdate(
    target: str,
    pin: str,
    simulate=False,
    force_session=False,
    disable_color=False,
    **kwds,
) -> None:
    """Queries for an update."""
    pp = NodePrinter(colorized=not disable_color)
    # create device and query version information
    device = _setup_device(target, pin, force_session, simulate, pp)
    api = wrap(device)
    version = api.version
    mac = api.radio_id
    if simulate:
        pp.print_url(url_find_update(mac, *version.split("_V")))
    else:
        request = find_update(mac, *version.split("_V"))
        if request.error is not None:
            error = request.error
            pp.print_err(error)
        elif not request.has_update:
            # REVISIT: maybe add further explanation of the issue here
            pp.print_msg(Fore.YELLOW, "[!] No Update available.")
        elif request.status == UpdateStatus.FOUND:
            for element in request.updates:
                pp.print_object(element)


# COMMAND: UPDATE FETCH
def FetchUpdate(
    target: str,  # IP address or file
    pin: str,
    dest: str,
    file=False,
    simulate=False,
    force_session=False,
    disable_color=False,
    **kwds,
) -> None:
    """Download of firmware binaries"""
    pp = NodePrinter(colorized=not disable_color)
    out_path = pathlib.Path(dest)
    if not file:
        # Donwload firmware by using the target device's information
        device = _setup_device(target, pin, force_session, simulate, pp)
        api = wrap(device)
        versions = [api.version]
    else:
        with open(target, "r", encoding="utf-8") as fp:
            versions = [x.strip() for x in fp.readlines()]

    for version in versions:
        if not version:
            continue  # sort out invalid strings

        if simulate:
            pp.print_url(url_get_update(version))
        else:
            url = url_get_update(version)
            dst = out_path
            if dst.is_dir():
                # REVISIT: Some binaries contain other suffixes
                dst = dst / f"{version}.isu.bin"
            try:
                pp._print("> Downloading firmware for:", pp.get_format("", version))
                get_update(str(dst), url)
                pp.print_msg(Fore.GREEN, " " * 3, f"- [out] '{dst}'")
            except UpdateError as err:
                pp.print_err(err, indent=3)


# COMMAND: SCAN
def Scan(
    target: str,
    pin: str,
    force_session=False,
    disable_color=False,
    simulate=False,
    show_invalid=False,
    **kwds,
) -> None:
    # Nodes that can be modified
    mod_nodes = texttable.Texttable()
    # List nodes
    list_nodes = texttable.Texttable()
    # Invalid results
    inv_nodes = texttable.Texttable(0)

    for table in (mod_nodes, list_nodes, inv_nodes):
        table.add_row(["Path", "Status"])
        table.set_cols_align(["l", "l"])
        table.set_deco(texttable.Texttable.HEADER)

    pp = NodePrinter(colorized=not disable_color)
    pp._print(f"> Scanning device at {pp.get_format('', target)}")
    device = _setup_device(target, pin, force_session, simulate, pp)
    for node in nodes.iter_nodes():
        method = Method.GET
        node_cls = (nodes / node).get_node_type()
        if node_cls.is_list:
            method = Method.LIST_GET_NEXT

        if simulate:
            pp.print_url(device.get_url(method, node))
            continue

        if node_cls.is_list:
            response = device.list_get_next(node)
        else:
            response = device.get(node)

        status_fmt = pp.get_format("", response.status) + Fore.RESET
        if response.status == Status.FS_OK:
            tbl = list_nodes
            if method == Method.GET:
                tbl = mod_nodes

            tbl.add_row([node, status_fmt])
        else:
            inv_nodes.add_row([node, status_fmt])

    if not simulate:
        pp._print("> Results for standard nodes:")
        pp.out(mod_nodes.draw())
        pp._print("\n> Results for list nodes:")
        pp.out(list_nodes.draw())
        if show_invalid:
            pp._print("\n> Invalid results:")
            pp.out(inv_nodes.draw())


def main(args=None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-C", "--disable-color", action="store_true", help="Disables colorized output"
    )
    parser.add_argument(
        "-X",
        "--simulate",
        help="Simulates the request and prints the used URL.",
        action="store_true",
    )
    parser.add_argument(
        "-F",
        "--force-session",
        action="store_true",
        help="Creates a new session before running the command.",
    )
    parser.add_argument(
        "--raw", action="store_true", help="Prints XML output instead of pretty print."
    )
    sb = parser.add_subparsers(description="Commands of this tool.")

    view_parser = sb.add_parser("view", help="Views properties of a node class")
    view_parser.add_argument("value", help="The node path or search value")
    view_parser.add_argument(
        "-S",
        "--search",
        action="store_true",
        help="Searches for nodes with the provided base path.",
    )
    view_parser.set_defaults(fn=View)

    get_parser = sb.add_parser("get", help="Fetches the value for the given nodes.")
    get_parser.add_argument("nodes", nargs="+", help="The node paths to query.")
    get_parser.add_argument("host", help="The target host's ip address or domain name.")
    get_parser.add_argument("--pin", default="1234", help="The device's PIN.")
    get_parser.set_defaults(fn=Get)

    list_parser = sb.add_parser("list", help="Fetches values from a list node")
    list_parser.add_argument("node", help="The node path (unique identifier).")
    list_parser.add_argument(
        "host", help="The target host's ip address or domain name."
    )
    list_parser.add_argument("--pin", default="1234", help="The device's PIN.")
    list_parser.add_argument("--pos", default=-1, help="The starting index position.")
    list_parser.add_argument(
        "-N", "--max-items", default=0xFFFF, help="The number of items to return."
    )
    list_parser.set_defaults(fn=List)

    set_parser = sb.add_parser(
        "set", help="Tries to apply a new value to a given node."
    )
    set_parser.add_argument(
        "node", help="The node path (e.g. netRemote.sys.info.friendlyName)."
    )
    set_parser.add_argument("value", help="The new value to apply.")
    set_parser.add_argument("host", help="The target host's ip address or domain name.")
    set_parser.add_argument("--pin", default="1234", help="The device's PIN.")
    set_parser.set_defaults(fn=Set)

    notifies_parser = sb.add_parser(
        "get-notifies", help="Queries all notifies of the target device"
    )
    notifies_parser.add_argument(
        "host", help="The target host's ip address or domain name."
    )
    notifies_parser.add_argument("--pin", default="1234", help="The device's PIN.")
    notifies_parser.set_defaults(fn=GetNotifies)

    update_parser = sb.add_parser("update", help="Firmware update related context.")
    usb = update_parser.add_subparsers()
    update_check_parser = usb.add_parser("check", help="Queries for an update.")
    update_check_parser.add_argument("target", help="IP address or device version.")
    update_check_parser.add_argument("--pin", default="1234", help="The device's PIN.")
    update_check_parser.set_defaults(fn=CheckForUpdate)

    update_fetch_parser = usb.add_parser("fetch", help="Download of firmware binaries")
    update_fetch_parser.add_argument(
        "target", help="The target IP address of input file."
    )
    update_fetch_parser.add_argument(
        "-f",
        "--file",
        action="store_true",
        help="Specifies that an input file should be used.",
    )
    update_fetch_parser.add_argument("--pin", default="1234", help="The device's PIN.")
    update_fetch_parser.add_argument("dest", help="The destination file or directory.")
    update_fetch_parser.set_defaults(fn=FetchUpdate)

    scan_parser = sb.add_parser("scan", help="Scans for known nodes on a device.")
    scan_parser.add_argument("target", help="The device to scan. (ip address)")
    scan_parser.add_argument("--pin", default="1234", help="The device's PIN.")
    scan_parser.add_argument(
        "-I", "--show-invalid", action="store_true", help="Include invalid results"
    )
    scan_parser.set_defaults(fn=Scan)

    argv = parser.parse_args(args).__dict__
    argv.pop("fn")(**argv)
