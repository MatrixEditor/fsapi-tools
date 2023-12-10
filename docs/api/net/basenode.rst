.. _net-api_base:

===========
WebAPI Core
===========

.. automodule:: fsapi.net

.. autoattribute:: fsapi.net.nodes

  Global path object for defined API nodes.

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



.. autoattribute:: fsapi.net.dynamic

  Specifier for dynamic prototypes.

  If the structure of a certain node is not clear, the "dynamic" prototype
  can be used temporarily to parse incoming XML data.

  >>> class foo_nt(Node):
  ...     class Meta:
  ...         path = "foo.bar"
  ...         prototype = dynamic
  ...

  Note that list nodes should extend the :class:`NodeList` class as the
  parsing workflow is slightly different.

.. autoclass:: NodeBase
  :members:

.. autoclass:: Node
  :members:

.. autoclass:: NodePath
  :members:

.. autoclass:: ArgType
  :members:

.. autoclass:: Argument
  :members:

.. autoclass:: NodeValue
  :members:


Node Classes
~~~~~~~~~~~~

.. autoclass:: NodeInt
  :members:

.. autoclass:: NodeList
  :members:

.. autoclass:: NodeListItem
  :members:

.. autoclass:: NodeS8
  :members:

.. autoclass:: NodeS16
  :members:

.. autoclass:: NodeS32
  :members:

.. autoclass:: NodeU8
  :members:

.. autoclass:: NodeU16
  :members:

.. autoclass:: NodeU32
  :members:

.. autoclass:: NodeE8
  :members:

.. autoclass:: NodeC8
  :members:

