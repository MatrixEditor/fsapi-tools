.. _api_examples:

============
API Examples
============

This comprehensive guide is designed to help you understand and utilize the various
functionalities provided by this library in your projects.

ISU API
-------

This API is utilized by the :ref:`isutool <isutool>` to perform firmware binary inspection
for Frontier Smart. Please refer to the isutool documentation for detailed instructions on
how to leverage this API's capabilities and effectively interact with Frontier Smart firmware binaries.

Parsing ISU Files
~~~~~~~~~~~~~~~~~

.. code-block:: python
    :caption: Create an ISU instance
    :linenos:

    from fsapi.isu import ISU

    # It is only possible to read file inputstreams
    isu = ISU.parse_file("firmware.isu.bin")
    # Or just use the '<<' operator
    isu = ISU << "firmware.isu.bin"

Getting Data of an Archive File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to retrieve the (un)compressed file bytes of an archive file, you need to perform
various steps.

.. code-block:: python
    :caption: Getting file bytes of an archive file
    :linenos:

    from fsapi.isu import ISU, IndexEntryType

    isu = ISU << "firmware.isu.bin"
    archive = isu.archive
    # We first need an entry that contains file data. You can either
    # iterater over all elements or you know, what entry you would
    # like to export
    entry = ... or archive.index.entries[0]
    # The entry must be of type 'File'
    assert entry.type == IndexEntryType.File
    # The ISU instance will extract the bytes for us
    data = isu.get_archive_file(entry.content, archive)


Creating Data Sections
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :caption: Creating new ISUDataSection objects
    :linenos:

    from fsapi.isu import ISU

    isu = ISU << "firmware.isu.bin"
    # Assume we have found a data section at a specific offset
    offset = ...
    section = isu.get_data_section(offset)


Generating an update URL
~~~~~~~~~~~~~~~~~~~~~~~~

With a simple function, you can generate the URL where a firmware binary is located. Here's an
example of how you can achieve this:

.. code-block:: python
    :caption: Generating an URL where the firmware binary is located
    :linenos:

    from fsapi.isu import ISU, url_get_update

    # We can use the version and customisation from a firmware binary
    isu = ISU << "firmware.isu.bin"
    name = f"{isu.customisation}_V{isu.version}"
    # The url should store the firmware binary
    url = url_get_update(name)


FS API
------

The FSAPI (Frontier Smart API) is utilized for communication and control of Frontier Smart's
internet radio devices. The following examples demonstrate how you can interact with these
devices:

.. code-block:: python
    :linenos:

    from fsapi.net import nodes, FSDevice, wrap

    # First, create the radio object
    device = FSDevice("127.0.0.1")

    # Create a new session id (only one at a time)
    device.new_session()

    # In order to simplify the usage of the FSDevice class
    api = wrap(device)
    friendly_name = api.friendly_name
    # or manually
    response = device.get(nodes / "netRemote.sys.info.friendlyName")
    if response.status == FS_OK:
        #_ Again, type(content) = nodes.BaseSysInfoFriendlyName
        friendly_name = response.content.value

        # Apply a new name via wrapper
        api.friendly_name = "FooBar"
        # or manually
        device.put(nodes / "netRemote.sys.info.friendlyName", value="FooBar")

    # get all elements of a list
    valid_modes = api.ls_valid_modes()
    # get a certain amount of elements beginning at index 3
    valid_mpdes = api.ls_valid_modes(_pos=3, max_items=10)

Fetching all notifies
~~~~~~~~~~~~~~~~~~~~~

A simple :class:`FSDevice` object provides the possibility to fetch all notify values. Be
aware that too many notifies would result in a timout caused by the device.

.. code-block:: python
    :linenos:

    from fsapi.net import nodes, FSDevice, wrap

    # First, create the radio object
    device = FSDevice("127.0.0.1")

    # Create a new session id (only one at a time)
    device.new_session()
    notifies: list[Node] = device.get_notifies()


