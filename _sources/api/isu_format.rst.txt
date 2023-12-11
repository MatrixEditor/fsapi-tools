.. _isu_format:

============
ISU - Format
============

The "isu_format" module includes structure definitions for the binary ISU format and
provides an API to interact with those files. In previous versions of this project,
you had to select the appropriate ISUInspector class. However, with recent updates,
this class is no longer required, making the API more user-friendly.

Here's an example of how to use the API:

    >>> from fsapi.isu_format import ISU
    >>> isu = ISU.parse_file("/path/to/file")
    >>> # Or with the lshift operator
    >>> isu = ISU << "/path/to/file"

By calling the ``parse_file`` method from the ISU class and providing the path to the
file, you will now be able to inspect the binary.

.. autoclass:: fsapi.isu.format.ISU
    :members:

.. autoclass:: fsapi.isu.format.it_data_fields
    :members:

.. autoclass:: fsapi.isu.format.isu_core_t
    :members:


Structures
----------

This section comprises a list of structures used internally for parsing ISU files. In
this documentation, all structures will be presented in a pattern format that can be
employed within the ImHex editor.

.. code-block:: c++
    :linenos:
    :caption: isu::Header

    // header structure
    struct ISUHeader {
        le u32 magic; // 0x1176; file signature
        le u32 length;
        le u32 isu_version;

        char version[32]; // version string (padded)
        char customisation[64];// firmware string (padded)

        if (this.length == 0xA2) {
            // Extended headers contain major and minor version strings
            char major_version[6];
            char minor_version[32];
        }

        type::GUID uuid; // maybe a UUID (never valid)
    };

.. note::
    You can access all fields displayed in a structure definition within python
    code. For instance::

        >>> isu = ISU.parse_file("firmware.isu.bin")
        >>> header = isu.header
        >>> header.customisation
        'ir-mmi-FS2026-0500-0795'

    Integer types will be mapped to ``int``, string fields to python strings, function
    declarations to python functions and so on. Optional values will be *None* if not
    present

.. code-block:: c++
    :linenos:
    :caption: isu::DataField and isu::DataSection

    struct ISUDataField {
        le u16 length; // the size of this struct
        le u16 unknown_1;
        le u16 name_length;
        le u16 flags; // not sure
        char name[16]; // padded

        if (this.length == 32) {
            le u32 value;
            le u32 unknown_2;
        }
    };

    // Use this field with caution
    struct DataSection {
        le u8 magic; // always 128 = 0x80
        le u8 length;
        le u8 data[this.length];
    };

Directory Archive Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Python implementation of directory archive structures is special and will
be demonstrated using Python class definitions.

.. code-block:: python

    class IndexEntryType(enum.IntEnum):
        File = 0x00
        Directory = 0x01

    class ISUArchiveIndexEntry:
        type: IndexEntryType
        name_length: int
        name: str
        content: ISUArchiveIndexDirectoryEntry | ISUArchiveIndexFileEntry

    class ISUArchiveIndexFileEntry:
        size: int
        offset: int
        compressed_size: int

    class ISUArchiveIndexDirectoryEntry:
        entry_count: int
        entries: list[ISUArchiveIndexEntry]

    class ISUArchiveIndex:
        length: int
        name: bytes # always 0
        entry_count: int
        entries: list[ISUArchiveIndexEntry]

    class ISUArchive:
        magic: bytes
        size: int
        unknown_1: int
        index_size: int
        index: ISUArchiveIndex
        data: bytes

