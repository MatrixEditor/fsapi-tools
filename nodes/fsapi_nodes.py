import pathlib
import re
import typing as t
import argparse

RE_EXTENDS = r"nds [\w<>]* impl"
RE_ENUM = r"enum \w* {(\s*\S*\s*|})"
RE_NAME = r"class \w* e"
RE_IS_CACHEABLE = r"IsCacheable.*\s.*\s.*}"
RE_IS_NOTIFYING = r"IsNotifying.*\s.*\s.*}"
RE_IS_READONLY = r"IsReadOnly.*\s.*\s.*}"
RE_NODE_NAME = r"Name.*\s.*\s.*}"
RE_PROTOTYPE_ARGS = r"Prototype == null(\s*.*\s*|})"

NODE_FMT = """
class %s(%s):
    class Meta:
%s
%s"""

ANONYMOUS_NODE_FMT = """
class %s_nt(Node):
    class Meta:
%s"""

def data_type_from_str(data_type: str) -> int:
    if "U32" in data_type:
        return 0x14
    if "U16" in data_type:
        return 0x13
    if "U8" in data_type:
        return 0x12
    if "S32" in data_type:
        return 0x17
    if "S16" in data_type:
        return 0x16
    if "S8" in data_type:
        return 0x15
    if "E8" in data_type:
        return 0x11
    if "C8" in data_type:
        return 0x10


def get_meta(values: dict) -> str:
    return "\n".join([f"        {key}={value}" for key, value in values.items()])


def new_node(cls_name, base_name, meta: dict, init="") -> str:
    return NODE_FMT % (cls_name, base_name, get_meta(meta), init)

def new_anonymous_node(cls_name: str, meta: dict) -> str:
    return ANONYMOUS_NODE_FMT % (cls_name, get_meta(meta))

def extends(java_class: str) -> str:
    return re.search(RE_EXTENDS, java_class).group()[4:-5]


def get_class_name(java_class: str) -> str:
    return re.search(RE_NAME, java_class).group()[6:-2]


def is_cacheable(java_class: str) -> bool:
    return True if "true" in re.search(RE_IS_CACHEABLE, java_class).group() else False


def is_notifying(java_class: str) -> bool:
    return True if "true" in re.search(RE_IS_NOTIFYING, java_class).group() else False


def is_readonly(java_class: str) -> bool:
    return True if "true" in re.search(RE_IS_READONLY, java_class).group() else False


def get_node_name(java_class: str) -> str:
    node_name = re.search(RE_NODE_NAME, java_class).group()
    return node_name[node_name.find('"') + 1 : node_name.rfind('"')]


def get_enum_class(java_class: str) -> str:
    enum_type = java_class[java_class.find("enum") + 4 :]
    content = enum_type[enum_type.find("{")+1: enum_type.find("}")]
    return content.replace("\n", "").replace(" ", "")


def get_list_prototype(java_class) -> t.List[str]:
    prototype = java_class[java_class.find("Prototype == null") :]
    return prototype[prototype.find("{") + 1 : prototype.find("}")].split("\n")


def create_nodes(path_list: t.Iterable[pathlib.Path]) -> t.Generator[str, t.Any, None]:
    for path in path_list:
        if path.is_dir():
            continue

        with open(str(path), "r", encoding="utf-8") as fp:
            java_class = fp.read()

        base_class = extends(java_class)
        class_name = get_class_name(java_class)
        node_name = get_node_name(java_class)
        meta = {}
        init = ""

        meta["cacheable"] = is_cacheable(java_class)
        meta["notifying"] = is_notifying(java_class)
        meta["readonly"] = is_readonly(java_class)
        meta["path"] = f'"{node_name}"'
        meta["name"] = f'"{class_name}"'

        if "NodeE8" in base_class:
            if "<" in base_class:
                base_class = base_class[: base_class.find("<")]
            # prepare enum class type
            enum_class = get_enum_class(java_class)
            values = []
            for line in enum_class.split(","):
                if line:
                    values.append(line)

            values_fmt = ", ".join([f'{i}: "{val}"' for i, val in enumerate(values)])
            prototype = "[Argument(type=ARG_TYPE_E8)]"
            meta["defaults"] = "{%s}" % values_fmt
        elif base_class == "NodeList":
            content = get_list_prototype(java_class)
            args = []
            for argument in content:
                if "arrayList.add" not in argument:
                    continue

                name, data_type, length = argument[argument.rfind("(") + 1 :].split(
                    ", "
                )
                if '"' in name:
                    name = name[1:-1]
                else:
                    name = '$' + name
                length = length[: length.find(")")]
                args.append(
                    f"Argument(name=\"{name}\", length={length}, type={data_type_from_str(data_type)})"
                )

            prototype = "[" + ",".join(args) + "]"
        else:
            prototype = "[Argument(type=ARG_TYPE_%s)]" % base_class.replace("Node", "")

        meta["prototype"] = prototype
        cls_name = node_name.replace(".", "_") + "_nt"
        yield new_node(cls_name, base_class, meta, init=init)


def is_node_class(java_path: pathlib.Path) -> bool:
    return "Base" in java_path.name and "BaseClasses.java" != java_path.name

def _process_nodes(argv):
    base_path = pathlib.Path(argv.path)
    if argv.from_file:
        nodes = []
        with open(str(base_path), "r", encoding="utf-8") as fp:
            for line in fp.readlines():
                line = line.strip()
                if not line:
                    continue
                name = f'"{line}"'
                cls_name = line.replace(".", "_")
                nodes.append(new_anonymous_node(cls_name, {"path": f'"{line}"', "name": name, "prototype": "dynamic"}))
    else:
        nodes = create_nodes(filter(is_node_class, base_path.iterdir()))

    with open(argv.output, "w", encoding="utf-8") as fp:
        fp.write("from fsapi.netremote.basenode import *\n\n")
        for node in nodes:
            fp.write("\n" + node)

def _list_nodes(argv):
    base_path = pathlib.Path(argv.path)
    for path in filter(is_node_class, base_path.iterdir()):
        if path.is_dir():
            continue

        with open(str(path), "r", encoding="utf-8") as fp:
            java_class = fp.read()

        print(get_node_name(java_class))
        del java_class

def main(cmd=None):
    parser = argparse.ArgumentParser()
    parsers = parser.add_subparsers()

    build_parser = parsers.add_parser("build", help="Create node classes.")
    build_parser.add_argument("path", help="Starting directory.")
    build_parser.add_argument("output", help="Output path.")
    build_parser.add_argument("-f", '--from-file', action="store_true")
    build_parser.set_defaults(fn=_process_nodes)

    list_parser = parsers.add_parser("list", help="Displays all nodes")
    list_parser.add_argument("path", help="Starting directory.")
    list_parser.set_defaults(fn=_list_nodes)
    argv = parser.parse_args(cmd)

    argv.fn(argv)

if __name__ == "__main__":
    main()
