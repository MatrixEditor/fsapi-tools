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

import inspect
import enum

from xml.etree import ElementTree
from dataclasses import dataclass
from typing import Any, Iterator, Type, Union

from ._enum import get_enum

# ============================================================================
# Web FSAPI:
#
# Some manufacturers selling devices that utilize the Frontier Smart chipset
# offer an integrated web API. The API comprises various endpoints that can be
# accessed by making GET requests with the appropriate API method. These
# endpoints are defined using 'nodes' following this format:
#
#     - netRemote.sys.info.friendlyName
#
# This Python implementation of the API stores more nodes than a single device
# may need to handle. The firmware file for each device contains all available
# web nodes. Nonetheless, this implementation offers standard FSAPI nodes and
# DAB+ nodes.
#
# Internal mapping is accomplished by processing a "Meta" class defined within
# each node class. Subsequently, the node classes will be stored in a
# dictionary, mapped to their specified path. To facilitate rapid access to
# the stored nodes, a NodePath class is utilized, enabling access to the
# various nodes.
# ============================================================================

# This map stores all the defined nodes and maps them to their specified
# paths. If a duplicate path is given, the creator class will raise a runtime
# exception.
_TYPE_MAP: dict[str, Type[Node]] = {}

_KEYS = (
    # Specifies the path of the defined node class. This value should be
    # unique.
    "path",
    # The name can be used as a display name for graphical use cases.
    "name",
    # If som enodes are only availble on special devices, they should be
    # listed here with their modules.
    "modules",
    # The prototype is crucial, because it helps to de-serialize the
    # incoming XML data. There is also a possibility to definte the
    # prototype to be "generic" or "dynamic".
    "prototype",
    # While processing the java source code of the UNDOK app, the defined
    # node classes have stored attributes linked to each corresponding
    # node:
    #       - notifying: indicating whther GET_NOTIFIES is applicable
    #       - cacheable: whether the property can be cached on the radio
    #       - readonly: the node can be queried using a readonlay operation
    "notifying",
    "cacheable",
    "readonly",
    # A list of API methods that can be used with this node.
    "methods",
    # Additional documentation which is designed to help a developer when
    # designing new scripts.
    "__doc__",
    # Enum default values
    "defaults",
)


class ArgType(enum.IntEnum):
    """Value types for node prototypes.

    Argument types are used by node prototypes to enable appropriate
    de-serialization of incoming data.
    """

    ARG_TYPE_C8 = 0x10
    """C8-Array (char array), type: str"""
    ARG_TYPE_E8 = 0x11
    """Type defined by an Enum, type: int"""
    ARG_TYPE_U8 = 0x12
    """Unsigned Int8, type: int"""
    ARG_TYPE_U16 = 0x13
    """Unsigned Int16, type: int"""
    ARG_TYPE_U32 = 0x14
    """Unsigned Int32, type: int"""
    ARG_TYPE_S8 = 0x15
    """Signed Int8, type: int"""
    ARG_TYPE_S16 = 0x16
    """Signed Int16, type: int"""
    ARG_TYPE_S32 = 0x17
    """Signed Int32, type: int"""
    ARG_TYPE_U = 0x18
    """Array of data, type: str"""
    ARG_TYPE_UNKNOWN = -1
    """Invalid type, will be mapped to str"""

    def to_python(self, value: str) -> Any:
        """
        Convert the given value to a Python object based on the ArgType.

        This method is used to convert a string representation of a value to
        a Python object of the appropriate type based on the ArgType.

        :param value: The value as a string to be converted.
        :type value: str
        :return: The Python object representing the converted value.
        """
        if self in (ArgType.ARG_TYPE_C8, ArgType.ARG_TYPE_U, ArgType.ARG_TYPE_UNKNOWN):
            # REVISIT: Looking at the javascript implementation of the FSAPI,
            # an array tag may be hex encoded.
            return value
        try:
            return int(value)
        except ValueError:
            return value


class NodeBase(type):
    """Base class for node classes.

    In order to enable access to all defined nodes this class will add
    each defined node class that specifies a "path" to an internal map.
    Attributes are defined using an inner "Meta" class that stores special
    class attributes:

    >>> class foo_nt(Node):
    ...     class Meta:
    ...         path = "foo.bar"
    ...         name = "Foo node"
    ...         prototype = [Argument(type=ArgType.ARG_TYPE_U16)]
    ...

    Using the global *nodes* instance makes it easier to create instances of
    the previously defined node class.

    >>> path = nodes / "foo" / "bar"
    >>> if path.exists():
    ...     node: foo_nt = path.create()
    ...

    Note that all attributes defined in the meta class will be accessable
    as class properties of the defined node class. For instance:

    >>> node_class = path.get_node_type()
    >>> node_class.path
    'foo.bar'
    >>> node.path
    AttributeError: 'foo.bar' object has no attribute 'path'
    """

    def __new__(cls, name, bases, attrs: dict, **kwargs):
        super_new = super().__new__

        new_class = super_new(cls, name, bases, attrs, **kwargs)
        meta = dict.fromkeys(_KEYS)
        for key, value in attrs.items():
            if key == "Meta" and inspect.isclass(value):
                items = value.__dict__
                # We rather iterate over all keys than using update()
                # on the final dictionary as we don't want to store
                # special variables.
                for a_key in _KEYS:
                    if a_key in items:
                        meta[a_key] = items[a_key]

        # Add verifications
        node_path = meta["path"]
        if node_path is not None:
            if meta["prototype"] is None:
                raise ValueError("Node protorype is null!")

            node_path = str(node_path).lower() # normalization
            if node_path in _TYPE_MAP:
                raise ValueError(f"Node path already exists: {node_path}")

            setattr(new_class, "_meta", meta)
            _TYPE_MAP[node_path] = new_class
        # just return the class as usual
        return new_class

    def read(cls: Type[Node], tree: ElementTree.Element) -> Node:
        """Converts XML input into the corresponding node object.

        This method will automatically convert XML list structures to node
        list items **only if** the desired node class extends the :class:`NodeList`
        class.

        >>> class foo_nt(Node):
        ...     ... # meta is defined here
        ...
        >>> node = foo_nt.read(xml_element)

        :param cls: the node class
        :type cls: Type[Node]
        :param tree: the fsapiResponse XML element
        :type tree: ElementTree.Element
        :raises ValueError: if there is an invalid prototype
        :return: the created node object storing the node's value
        :rtype: Node
        """
        if cls.is_list:
            # Automatically create a list node
            return cls.read_list(tree)

        value_node = tree.find("value")
        if value_node is None:
            # Return node object without a value
            return cls()

        prototype = cls.prototype
        if prototype is not dynamic:
            child_count = len(value_node)
            # The response should store only one node specifying the value
            # type and its serialized representation.
            if len(prototype) == 1 and child_count >= 1:
                # We only use the first node
                value = str(value_node[0].text).strip()
                value = prototype[0].type.to_python(value)
                if issubclass(cls, NodeE8):
                    value = IntEnumValue.create(value, cls.defaults[value])
            else:
                raise ValueError("Unsupported prototype or invalid response format!")

        # Dynamic prototype handling: We create a list of NodeValue
        # objects that contain their value type and the value representation.
        else:
            value = []
            # TODO: what if the response is a list
            if tree.find("item") is not None:
                return cls.read_list(tree)

            for child_node in value_node:
                node_name = child_node.tag
                node_value = str(child_node.text).strip()

                value_type, cleaned = cls._to_python(node_value, node_name)
                # The python type will be inferred automatically if possible
                value.append(NodeValue(value_type, cleaned))

            # Remove the list if we only have one element
            if len(value) == 1:
                value = value[0]

        return cls(value=value)

    def read_list(cls: Type[NodeList], tree: ElementTree.Element) -> Node:
        """Converts XML input to a node extending the :class:`NodeList` class.

        :param cls: the node class
        :type cls: Type[NodeList]
        :param tree: the fsapiResponse XML element
        :type tree: ElementTree.Element
        :return: a node object storing a list of :class:`NodeListItem` objects
        :rtype: Node
        """
        values = []
        # The input tree should be aligned as follows:
        # ...
        # <item key="0">
        #   <field name="friendlyName"><c8_array>DeviceName</c8_array></field>
        #   ...
        # </item>
        # ...
        prototype = cls.prototype
        for item_node in tree.findall("item"):
            key = item_node.get("key", None)
            # The element will be placed at the end of the list is it is
            # invalid.
            if key is None:
                key = -1
            else:
                # REVISIT: possible exception here
                key = int(key)

            attrib = {"key": key}
            for field_node in item_node.findall("field"):
                name = field_node.attrib["name"]
                value_node = field_node[0]
                value = str(value_node.text).strip()
                if prototype is dynamic:
                    # same as in read(): the dynamic prototype will try to convert
                    # the corresponding values.
                    attrib[name] = NodeValue(*cls._to_python(value, value_node.tag))
                else:
                    for argument in prototype:
                        # The stored argument converts the input data to the corresponding
                        # python object.
                        if argument.name.lower() == name.lower():
                            # REVISIT: special treatment for enum values
                            value = argument.type.to_python(value)
                            if argument.type == ArgType.ARG_TYPE_E8:
                                enum_defaults = get_enum(name, path=cls.path)
                                if enum_defaults is None:
                                    attrib[name] = value
                                else:
                                    # Using this small workaround we can get the actual enum value
                                    enum_value = enum_defaults._value2member_map_.get(
                                        value, value
                                    )
                                    attrib[name] = enum_value
                            else:
                                attrib[name] = value
                            break

            values.append(NodeListItem(attributes=attrib))
        # Create a new list with the collected node list items.
        return cls(items=values)

    def _to_python(self, value: str, tag: str) -> tuple:
        # Clean the node name and remove unnecessary array specification
        if "_array" in tag:
            tag = tag.replace("_array", "")

        if tag == "array":
            name = ArgType.ARG_TYPE_U.name
        else:
            name = f"ARG_TYPE_{tag.upper()}"
        value_type = ArgType.ARG_TYPE_UNKNOWN
        for arg_type in ArgType:
            if arg_type.name == name:
                value_type = arg_type
                break

        return value_type, value_type.to_python(value)

    @property
    def cacheable(cls) -> bool:
        """Specifies whether this node is cacheable."""
        return cls._meta["cacheable"]

    @property
    def prototype(cls) -> list[Argument] | _Dynamic:
        """Returns the prototype if this node."""
        return cls._meta["prototype"]

    @property
    def notifying(cls) -> bool:
        """Specifies whether GET_NODTIFIES is applicable."""
        return cls._meta["notifying"]

    @property
    def readonly(cls) -> bool:
        """Returns true if only non-write operations are permitted."""
        return cls._meta["readonly"]

    @property
    def path(cls) -> str:
        """Defines the unique path of a node."""
        return cls._meta["path"]

    @property
    def name(cls) -> str:
        """Graphical display name"""
        return cls._meta["name"] or cls.__name__

    @property
    def description(cls) -> str:
        """Documentation of the node."""
        return cls._meta["__doc__"] or cls.__doc__

    @property
    def is_list(cls) -> bool:
        """Returns whether this class is a list class."""
        for class_ in cls.__bases__:
            if class_ == NodeList:
                return True

        return False

    @property
    def defaults(cls) -> dict[int, str]:
        return cls._meta["defaults"] or {}


class NodePath:
    """A class to search and navigate to implemented nodes.

    *NodePath* objects store some utility attributes and capabilities that
    help searching for implemented notes. For instance, the following code
    searches for all implemented nodes starting with the path *"netRemote.misc"*:

    >>> path = NodePath("netRemote") / "misc"
    >>> list(path.iter_nodes())
    ['netRemote.misc.fsDebug.component', 'netRemote.misc.fsDebug.traceLevel', ...]

    This class is designed to provide access to implemented node classes, create
    new instances of nodes and to be able to search for specific nodes. In order
    to verfiy that a certain node is implemented, there is a verification method:

    >>> path = NodePath("netRemote") / "misc" / "fsDebug.component"
    >>> path.exists()
    True
    >>> path.create()
    Node(path="netRemote.misc.fsDebug.component", has_value=True)
    """

    def __init__(self, name: str, base: str = None) -> None:
        self.parent = base
        self.path = ".".join([base, name]) if base else name
        self.name = name
        self.depth = self.path.count(".") + 1

    def __repr__(self) -> str:
        return f"Path '{self.path}'"

    def __str__(self) -> str:
        return self.path

    def __truediv__(self, __name: str) -> NodePath:
        return NodePath(__name, base=self.path)

    def exists(self) -> bool:
        """Verifies that a certain node exists.

        :return: True if the node is implemented, false otherwise
        :rtype: bool
        """
        return self.path.lower() in _TYPE_MAP

    def create(self, *args, **kwargs) -> Node:
        """Creates a new instance of a node with the given argument values.

        :return: the new node instance
        :rtype: Node
        :raises KeyError: if the node path does not exists
        """
        return _TYPE_MAP[self.path.lower()](*args, **kwargs)

    def get_node_type(self) -> Type[Node]:
        """Returns the node type.

        :return: the type of the implemented node
        :rtype: Type[Node]
        :raises KeyError: if the node path does not exists
        """
        return _TYPE_MAP[self.path.lower()]

    def iter_nodes(self) -> Iterator[str]:
        """Iterates over all nodes that start with this path.

        :return: all filtered nodes as an iterator
        :rtype: Iterator[str]
        """
        return iter(filter(lambda x: x.startswith(self.path.lower()), _TYPE_MAP))

    def from_xml(self, tree: ElementTree.ElementTree) -> Node:
        """Tries to convert the given XML tree to a node.

        :param tree: the XML response of the device
        :type tree: ElementTree.ElementTree
        :raises KeyError: if the node does not exists
        :return: the new node instance
        :rtype: Node
        """
        if not self.exists():
            raise KeyError(f"Node '{self.path}' does not exist!")

        return self.get_node_type().read(tree)


class Node(metaclass=NodeBase):
    """Base class of all node classes.

    Each node stores a value and the node class stores the node's meta
    information.  Be aware of the difference, a node object is designed
    to store a node's value, NOT the meta information. Those are linked
    to the class instance.

    >>> path = NodePath("netRemote.sys.info.version")
    >>> node_class = path.get_node_type()
    >>> node_class.path
    "netRemote.sys.info.version"
    >>> node = path.create()
    >>> node.path
    AttributeError: '...' object has no attribute 'path'

    :param value: the node's value
    """

    def __init__(self, value=None) -> None:
        self.__value = value

    def __repr__(self) -> str:
        return 'Node(path="%s", has_value=%s)' % (self.cls.path, self.value is not None)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return __value.value == self.value
        return super().__eq__(__value)

    @property
    def value(self) -> int | str | list[NodeListItem] | NodeValue:
        """The node's value

        :return: the currently applied node value or None
        :rtype: int | str | list[NodeListItem] | NodeValue
        """
        return self.__value

    @value.setter
    def value(self, value) -> None:
        """Sets a new value after validating it.

        :param value: the new value
        """
        self.__value = self._clean_value(value)

    def _clean_value(self, value):
        """Validates the new node value (see :class:`NodeInt` for more info)

        :param value: the new value
        :meta: public
        """
        return value

    @property
    def cls(self) -> Type[Node]:
        """The node' class (quick access property)"""
        return self.__class__

    def has_method(self, method: str) -> bool:
        """Checks whether the provided method is allowed"""
        methods = self._meta["methods"]
        if methods == "__all__":
            return True

        return method in methods

    def supports_module(self, module_name: str) -> bool:
        """Checks whether the provided FS module is supported."""
        modules = self._meta["modules"]
        if modules == "__all__":
            return True

        return module_name in modules


@dataclass(frozen=True)
class Argument:
    """Defines an argument within a node prototype.

    A node's prototype contains arguments in order to parse XML responses
    back to python values.

    :param name: The name of this argument, default "value"
    :type name: str
    :param length: the length of this value, 1 := one element
    :type length: int
    :param type: the argument type used to parse the XML content
    :type type: :class:`ArgType`
    """

    name: str = "value"
    length: int = 1
    type: ArgType = ArgType.ARG_TYPE_UNKNOWN


class NodeInt(Node):
    """Defines an integer node with an acceptable range of values.

    >>> node = NodeInt(minimum=0, maximum=10)
    >>> node.value = 11
    ValueError: Expected value between 0 and 10 - got 11

    :param value: the node's value
    :type value: int
    :param minimum: the minimum value that gets accepted
    :type minimum: int
    :param maximum: the maximum value that gets accepted
    :type maximum: int
    """

    def __init__(self, value=None, minimum=0, maximum=0) -> None:
        super().__init__(value)
        self.minimum = minimum
        self.maximum = maximum

    def _clean_value(self, value: int):
        if self.minimum <= value <= self.maximum:
            return value

        raise ValueError(
            "Expected value between %d and %d - got %d"
            % (self.minimum, self.maximum, value)
        )


class NodeS8(NodeInt):
    """Signed Int8 node (min: -127, max: 127)"""

    def __init__(self, value: int = 0) -> None:
        super().__init__(value, -127, 127)


class NodeS16(NodeInt):
    """Signed Int16 node (min: -0x7FFF, max: 0x7FFF)"""

    def __init__(self, value: int = 0) -> None:
        super().__init__(value, -0x7FFF, 0x7FFF)


class NodeS32(NodeInt):
    """Signed Int32 node (min: -0x7FFFFFFF, max: 0x7FFFFFFF)"""

    def __init__(self, value: int = 0) -> None:
        super().__init__(value, -0x7FFFFFFF, 0x7FFFFFFF)


class NodeU8(NodeInt):
    """Unsigned Int8 node (min: 0, max: 255)"""

    def __init__(self, value: int = 0) -> None:
        super().__init__(value, 0, 0xFF)


class NodeU16(NodeInt):
    """Unsigned Int16 node (min: 0, max: 0xFFFF)"""

    def __init__(self, value: int = 0) -> None:
        super().__init__(value, 0, 0xFFFF)


class NodeU32(NodeInt):
    """Unsigned Int32 node (min: 0, max: 0xFFFFFFFF)"""

    def __init__(self, value: int = 0) -> None:
        super().__init__(value, 0, 0xFFFFFFFF)


class IntEnumValue(int):
    """Internal class (use .stringvalue to get the value's name)"""

    stringvalue: str
    """The name of this enum value."""

    @staticmethod
    def create(value: int, name: str) -> IntEnumValue:
        enum_value = IntEnumValue(value)
        enum_value.stringvalue = name
        return enum_value


class NodeE8(Node):
    """Enum node. (internal mapping contains enum names)"""

    def __init__(self, value=None, defaults=None) -> None:
        super().__init__(value)
        self.defaults = defaults

    @property
    def enum_value(self) -> str | Any | None:
        """Returns the associated value's name (if present)

        :return: the value's names
        :rtype: str | Any
        """
        return self.defaults.get(self.value, None)

    def _clean_value(self, value):
        if value in self.defaults:
            return IntEnumValue.create(value, self.defaults[value])

        return super()._clean_value(value)


class NodeC8(Node):
    """Character array node (string)"""

    def __init__(self, value=None, max_size: int = 1024) -> None:
        super().__init__(value)
        self.mex_size = max_size


NodeU = NodeC8
"""NodeU: Array of data (mapped to string)"""


@dataclass(frozen=True)
class NodeValue:
    """Anonymous value class.

    When using dynamic prototypes, this class is used to represent
    the values in a XML response.

    :param type: the argument type
    :param: value: the stored value (enum values won't be covered)
    """

    type: ArgType
    value: int | str | None = None


_NodeListItemValue = Union[str, NodeE8, int, NodeValue]


class NodeListItem:
    """Content item of a :class:`NodeList`."""

    def __init__(self, attributes: dict = None) -> None:
        self.attrib = attributes if attributes else {}

    def __getitem__(self, __key) -> _NodeListItemValue:
        if not __key or __key not in self.attrib:
            return None
        return self.attrib[__key]

    def __repr__(self) -> str:
        return f"NodeListItem({repr(self.attrib)})"

    @property
    def fields(self) -> list[str]:
        """Returns a list of field names.

        :return: all field names stored by this item.
        :rtype: list[str]
        """
        return list(self.attrib)

    def get(self, field_name: str, __default=None) -> _NodeListItemValue | None:
        """Return the value for key if key is in the attribites, else default.

        :param field_name: the field's name
        :type field_name: str
        :param __default: the default return value, defaults to None
        :return: the stored, converted python representation
        :rtype: _NodeListItemValue | None
        """
        return self.attrib.get(field_name, __default)


class NodeList(Node):
    """Special node that contains multiple items.

    You can use this class with the len function or within a loop.

    >>> node_list = ...
    >>> len(node_list)
    2
    >>> for item in node_list:
    ...     # inspect item

    :param items: a list of :class:`NodeListItem` objects
    :type items: list
    """

    def __init__(self, items: list = None) -> None:
        super().__init__(value=items or [])

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Iterator[NodeListItem]:
        return iter(self.items)

    @property
    def items(self) -> list[NodeListItem]:
        """Returns the stored items as a list.

        :return: the stored list items
        :rtype: list[NodeListItem]
        """
        return self.value


_Dynamic = object

dynamic = _Dynamic()
"""Specifier for dynamic prototypes.

If the structure of a certain node is not clear, the "dynamic" prototype
can be used temporarily to parse incoming XML data.

>>> class foo_nt(Node):
...     class Meta:
...         path = "foo.bar"
...         prototype = dynamic
...

Note that list nodes should extend the :class:`NodeList` class as the
parsing workflow is slightly different.
"""

nodes = NodePath("")
"""Global path object for defined API nodes.

This object can be used to search for registered node classes. For instance,
following this control flow leads to all available nodes:

>>> available_nodes = list(nodes.iter_nodes())

Each node is mapped to a unique path, which can be accessed by using the true
div operation in python:

>>> nodes / "foo" / "bar"
Path 'foo.bar'

Alternatively, the amount of operations can be reduced by specifying the
complete path directly:

>>> nodes / "foo.bar"
Path 'foo.bar'
"""
