.. _api-net_nodes:

==============
Node Reference
==============

There are some documentations of the Web FSAPI available, but none of them list
all nodes with their types and possible defaults. In this improved view of nodes,
an effort is made to provide an explanation for each node, along with an example
view. Before introducing the nodes, the structure of this reference will be
explained.

This reference stores each sub-command group in a separate document. You can
find the list of links to all available nodes at the end of this document.

.. hint::
    TIP: Use STRG+F to search for your node of interest.

Reference Structure
-------------------

Each node description adheres to a pre-defined scheme, which includes the full
name, capabilities, an example, and the node's type.

.. note::
    All documentation pages will be generated based on the python class definitions.

.. code-block:: text

    <display_name> (<node_path>)
    ----------------------------

    <description>

    <capabilities_table>

    [<enum_defaults>]

    <example_view>


- ``<display_name>``:
    This field refers to the ``name`` attribute of the *"Meta"* class of a node class
    definition.

- ``<node_path>``:
    The unique fully qualified node path is provided in the headline to facilitate HTML
    searching using CTRL+F..

- ``<description>``:
    An extensive description is extracted from the node's class-doc attribute. If a
    new documentation needs to be added, it must be placed as a class-doc comment.

- ``<capabilities_table>``:
    A simple table is provided, listing the node's type, whether it supports notifies,
    and whether it is cacheable.

- ``<enum_defaults>``:
    Some nodes are derived from an enum-typed node, and the value mapping will be
    included in this section.

- ``<example_view>``:
    A code block illustrating an example response of a device. Examples will be stored
    as XML files in the ``nodes/examples/`` directory of the repository.


NetRemote Nodes
---------------

.. toctree::
    :caption: NetRemote Nodes


    netRemote/netRemote-airplay
    netRemote/netRemote-avs
    netRemote/netRemote-bluetooth
    netRemote/netRemote-platform
    netRemote/netRemote-sys
    netRemote/netRemote-debug
    netRemote/netRemote-multichannel
    netRemote/netRemote-cast
    netRemote/netRemote-play
    netRemote/netRemote-spotify
    netRemote/netRemote-multiroom
    netRemote/netRemote-misc
    netRemote/netRemote-test
    netRemote/netRemote-nav
    netRemote/netRemote-fsdca
