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

import enum
import dataclasses
import urllib3
import typing as t

from xml.etree import ElementTree
from urllib.parse import quote

from fsapi.netconfig import FSNetConfiguration
from fsapi.net import Node, NodePath


class Method(enum.Enum):
    """WebAPI method (discovered ones)"""

    GET = "GET"
    GET_MULTIPLE = "GET_MULTIPLE"
    SET = "SET"
    SET_MULTIPLE = "SET_MUTLIPLE"
    LIST_GET = "LIST_GET"
    LIST_GET_NEXT = "LIST_GET_NEXT"
    LIST_GET_PREV = "LIST_GET_PREV"
    CREATE_SESSION = "CREATE_SESSION"
    DELETE_SESSION = "DELETE_SESSION"
    GET_NOTIFIES = "GET_NOTIFIES"


class Status(enum.Enum):
    """All possible response statuses discovered in firmware binaries."""

    FS_OK = "FS_OK"
    """If everything goes right the status is set to ``FS_OK``"""

    FS_PACKET_BAD = "FS_PACKET_BAD"
    """
    This status code will be returned if a value should be applied to
    a read-only node and therefore can not be executed.
    """

    FS_TIMEOUT = "FS_TIMEOUT"
    """The device takes too long to respond."""

    FS_FAIL = "FS_FAIL"
    """
    If the parameters given in the url are mot matching the node criteria, the
    request will fail. In addition, this API returns ``FS_FAIL`` whenever an
    invalid response is received.
    """

    FS_REPLY_TOO_BIG = "FS_REPLY_TOO_BIG"
    """Response code for requests that result in a large output."""

    FS_LIST_END = "FS_LIST_END"
    """The navigated item is not present within the selected list."""

    FS_NODE_BLOCKED = "FS_NODE_BLOCKED"
    """Certain commands can only be used when the unit is in the correct mode."""

    FS_NODE_DOES_NOT_EXIST = "FS_NODE_DOES_NOT_EXIST"
    """The referenced node is not available on the target device."""

    FS_REQUEST_INVALID = "FS_REQUEST_INVALID"
    """Same as ``FS_FAIL``, but the command has not been executed yet."""

    FS_UNKNOWN_STATUS = "FS_UNKNOWN_STATUS"
    """API status to mark invalid status codes."""

    ### Internal error messages ###
    FS_XML_ERROR = "FS_XML_ERROR"


FS_DEFAULT_PIN = "1234"


@dataclasses.dataclass(frozen=True)
class FSResponse:
    """De-serialized response of a XML request."""

    method: Method
    """The used API method"""

    node: Node
    """The de-serialized node with its value (may be None)"""

    status: Status
    """The status of this response"""

    @property
    def success(self) -> bool:
        """Returns whether the response has been parsed successfully."""
        return self.status == Status.FS_OK


_NodeType = t.Union[type, str, NodePath]


class FSDevice:
    """Client to communicate with FS devices.

    This class acts as a HTTP client that automatically parses XML responses
    and wraps their values to the corresponding nodes.

    >>> device = FSDevice("127.0.0.1")
    >>> response = device.get(nodes / "netRemote.sys.info.version")
    >>> if response.success:
    ...     version: str = response.node.value

    When querying list nodes, there is a possiblity to choose the current
    navigation item:

    >>> response = device.get_list(nodes / "...", _pos=5)

    To enable session usage, just let the device request a new session and the
    session id will be sent within all requests.

    >>> device.new_session() # new value will be applied directly
    >>> response = device.get(nodes / "...")
    >>> status = device.close_session()

    :param host: the target host
    :type host: str
    :param port: the web server port, defaults to 80
    :type port: int, optional
    :param pin: the PIN to use, defaults to FS_DEFAULT_PIN
    :type pin: str, optional
    :param sid: initial session id, can be set using create_session, defaults to -1
    :type sid: int, optional
    :param config: the network configuration, defaults to None
    :type config: FSNetConfiguration, optional
    :param create_session: indicates whether a new session should be created, defaults to False
    :type create_session: bool, optional
    """

    def __init__(
        self,
        host: str,
        port: int = 80,
        pin: str = FS_DEFAULT_PIN,
        sid: int = -1,
        config: FSNetConfiguration = None,
        create_session=False,
    ) -> None:
        self.host = host
        self.port = port
        self.pin = pin or FS_DEFAULT_PIN
        self.config = config
        self.sid = sid
        if create_session and sid in (None, -1):
            # The new value will be mapped automatically
            self.new_session()

    def get(self, *__nodes: t.Iterable[_NodeType]) -> t.Union[FSResponse, t.List[FSResponse]]:
        nodes = list(__nodes)
        if len(nodes) == 1:
            return self.node_request(Method.GET, nodes[0])

        return self.node_request_multiple(Method.GET_MULTIPLE, nodes)

    def put(self, node: _NodeType, **argv) -> FSResponse:
        return self.node_request(Method.SET, node, **argv)

    def get_list(self, node: _NodeType, **argv) -> FSResponse:
        # use get_list(..., _pos=3) for navigation
        # _pos=-1 All items
        # _pos=X items after position X
        return self.node_request(Method.LIST_GET, node, **argv)

    def list_get_next(self, node: _NodeType, **argv) -> FSResponse:
        return self.node_request(Method.LIST_GET_NEXT, node, **argv)

    def list_get_prev(self, node: _NodeType, **argv) -> FSResponse:
        return self.node_request(Method.LIST_GET_PREV, node, **argv)

    def get_notifies(self) -> t.List[Node]:
        if self.sid is None or self.sid == -1:
            # NOTE: The unit will only execute this command if the user sends
            # a valid Session ID
            self.new_session()

        elements = ["fsapi", Method.GET_NOTIFIES.name]
        tree = self.request("/".join(elements), self.config)
        result = []
        if tree is not None:
            status = self._get_status(tree)
            if status != Status.FS_OK:
                return result

            for notify_node in tree.findall("notify"):
                node_path = NodePath(notify_node.get("node", ""))
                if not node_path.exists():
                    continue

                result.append(self._unmarshal(node_path, notify_node))
        return result

    def new_session(self) -> int:
        elements = ["fsapi", Method.CREATE_SESSION.name]
        tree = self.request("/".join(elements), config=self.config)
        if tree is None:
            return -1

        status = self._get_status(tree)
        if status != Status.FS_OK:
            return -1

        session_id_node = tree.find("sessionId")
        self.sid = int(session_id_node.text.strip())
        return self.sid

    def close_session(self) -> Status:
        elements = ["fsapi", Method.DELETE_SESSION.name]
        tree = self.request("/".join(elements), config=self.config)
        if tree is None:
            return Status.FS_FAIL

        self.sid = -1
        return self._get_status(tree)

    def node_request(
        self,
        method: Method,
        node: _NodeType,
        config: FSNetConfiguration = None,
        **argv,
    ) -> FSResponse:
        """Performs a single webAPI request.

        This method can be called in different situations and will always
        behave the same: First, it creates the URL to be called. Next, the
        result of that call will be converted into an :class:`FSResponse`
        object.

        .. warning::
            Use this function only if you known what you are doing, otherwise you
            may run into errors.

        :param method: the API method to use
        :type method: Method
        :param node: the
        :type node: _NodeType
        :param config: _description_, defaults to None
        :type config: FSNetConfiguration, optional
        :return: _description_
        :rtype: FSResponse
        """
        node_path = self._to_node_path(node)
        path_elements = ["fsapi", method.name, str(node_path)]
        # list nodes should be handled differently
        pos = argv.pop("_pos", "-1")
        if method.name.startswith(Method.LIST_GET.name):
            path_elements.append(str(pos))

        tree = self.request("/".join(path_elements), config or self.config, **argv)
        if tree in (-1, -2):
            status = Status.FS_XML_ERROR if tree == -2 else Status.FS_TIMEOUT
            return FSResponse(method=method, node=None, status=status)

        status = self._get_status(tree)
        if status != Status.FS_OK:
            return FSResponse(method=method, node=None, status=status)

        node = self._unmarshal(node_path, tree)
        return FSResponse(method=method, node=node, status=status)

    def node_request_multiple(
        self,
        method: Method,
        nodes: t.List[_NodeType],
        config: FSNetConfiguration = None,
        **argv,
    ) -> t.List[FSResponse]:
        """Performs a multiple node request.

        :param method: the API method
        :type method: Method
        :param nodes: the list of nodes to query
        :type nodes: t.List[_NodeType]
        :param config: the network configuration, defaults to None
        :type config: FSNetConfiguration, optional
        :return: a list of response objects storing the de-serialized data.
        :rtype: t.List[FSResponse]
        """
        node_paths = list(map(self._to_node_path, nodes))
        path_elements = ["fsapi", method.name]
        result = []
        argv["node"] = list(map(str, node_paths))
        tree = self.request("/".join(path_elements), config or self.config, **argv)
        if tree in (-1, -2):
            return result

        # The structure of a GET multiple response can be defined as follows:
        # <fsapiGetMultipleResponse>
        #     <fsapiResponse>
        #         <node>netRemote.sys.net.wlan.connectedSSID</node>
        #         <status>FS_OK</status>
        #         <value><array></array></value>
        #     </fsapiResponse>
        #     ...
        # </fsapiGetMultipleResponse>
        for fsapi_response in tree.findall("fsapiResponse"):
            node_element = fsapi_response.find("node")
            status = self._get_status(fsapi_response)
            if node_element is None:
                # Insert invalid reponse
                result.append(FSResponse(method, node=None, status=status))
            else:
                node_path = NodePath(node_element.text.strip())
                node = self._unmarshal(node_path, fsapi_response)
                result.append(FSResponse(method, node=node, status=status))

        return result

    def request(
        self, path: str, config: FSNetConfiguration, **argv
    ) -> ElementTree.ElementTree | None:
        """Performs a HTTP request and parses its XML response.

        This method will try to avoid raising exceptions and returns None
        on invalid response data. The PIN has to be included in the optional
        arguments of this function.

        :param path: the request uri without leading slash, e.g. "fsapi/GET/netRemote.sys.info.version"
        :type path: str
        :param config: the network configuration
        :type config: FSNetConfiguration
        :return: the parsed XML response as element tree
        :rtype: ElementTree.ElementTree | None
        """
        try:
            url = self._create_url(path, parameters=argv)
            if config:
                response = config.delegate_request("GET", url, timeout=5)
            else:
                pool = urllib3.PoolManager()
                response = pool.request("GET", url, timeout=5)

            return ElementTree.fromstring(response.data)
        except urllib3.exceptions.PoolError:
            return -1
        except ElementTree.ParseError:
            return -2

    def get_url(self, method: Method, *elements, **parameters) -> str:
        """Creates a new URL that can be used to perform an API request.

        Example:
            >>> device.get_url(Method.GET_NOTIFIES)
            'http://127.0.0.1:80/fsapi/GET_NOTIFIES?pin=1234'

        :param method: the API method
        :type method: Method
        :return: the fully qualified URL
        :rtype: str
        """
        path = "/".join(["fsapi", method.name] + list(map(str, elements)))
        return self._create_url(path, parameters=parameters)

    def _create_url(self, path: str, parameters: dict) -> str:
        host = self.host
        port = self.port
        query_str = self._build_parameters(parameters)
        return f"http://{host}:{port}/{path}?{query_str}"

    def _build_parameters(self, parameters: dict) -> str:
        # NOTE: These parameters must occur before any other custom
        # parameter as GET_MULTIPLE would result in errors.
        query_params = [f"pin={self._quote(self.pin)}"]
        if self.sid is not None and self.sid != -1:
            query_params.append(f"sid={self._quote(self.sid)}")

        for key in parameters:
            name = self._quote(key)
            value = parameters[key]
            if isinstance(value, list):
                for list_element in value:
                    query_params.append(f"{name}={self._quote(list_element)}")
            else:
                query_params.append(f"{name}={self._quote(value)}")
        return "&".join(query_params)

    def _unmarshal(self, node_path: NodePath, tree: ElementTree.ElementTree) -> Node:
        node_type = node_path.get_node_type()
        return node_type.read(tree)

    def _get_status(self, tree: ElementTree.ElementTree) -> Status:
        status_node = tree.find("status")
        if status_node is None:
            return Status.FS_FAIL

        status_text = str(status_node.text).strip()
        for status in Status:
            if status.value == status_text:
                return status

        return Status.FS_UNKNOWN_STATUS

    def _to_node_path(self, node: _NodeType) -> NodePath:
        if isinstance(node, NodePath):
            node_path = node
        elif isinstance(node, str):
            node_path = NodePath(node)
        elif isinstance(node, type) and issubclass(node, Node):
            node_path = NodePath(node.path)
        else:
            raise TypeError(f"Invalid node path type: {type(node)}")

        return node_path

    def _quote(self, obj: t.Any) -> str:
        return quote(str(obj))
