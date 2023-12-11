.. _isu_firmware_structure:

=====================
FS Firmware Structure
=====================

This document provides a comprehensive examination of the firmware binaries
utilized for updating Frontier Smart devices, offering a more in-depth analysis
of their content and functionality.

.. note::
    It is also worth noting that all numbers utilized in the dicovered structures use
    little endian ancoded integers.


Header Structure
----------------

There is a specific file header for the update files that contains additional
information about the firmware file. It's important to note that all of the
inspected binary files have nearly identical header structures. Therefore,
the basic structure can be defined as follows:

.. code-block:: c++
    :caption: Pattern definition to parse ISU header
    :linenos:

    #include <type/guid.pat>

    namespace isu {
        struct Header {
            le u32 magic; // 0x1176; file signature
            le u32 length;
            le u32 isu_version:
            char version[32]; // version string (padded)
            char customisation[64]; // firmware string (padded)
            if (this.length == 0xA2) {
                // Extended headers contain major and minor version strings
                char major_version[6];
                char minor_version[32];
            }
            type::GUID uuid; // maybe a UUID (never valid)
        };
    }

ISU Header
~~~~~~~~~~

This pattern can be used to parse both default and so-called extended ISU headers.
For instance, the following image displays the binary header with highlighted sections,
providing a visual representation of the header structure.

.. image:: graphics/isu_header_marker.png
    :align: center
    :name: ISU Header Structure

.. raw:: html

    <br>

The next table shows the associated values:

.. image:: graphics/isu_header_values.png
    :align: center

.. raw:: html

    <br>

ISU Extended Header
~~~~~~~~~~~~~~~~~~~

If we now examine the so-called extended ISU headers, which are exclusively found in
``fsccp-scb`` product firmwares, it becomes apparent that they contain two additional
fields that might indicate the major and minor version of the embedded operating system
being used.

.. image:: graphics/isu_extended_header_marker.png
    :align: center

.. raw:: html

    <br>

The next table shows the associated values:

.. image:: graphics/isu_extended_header_values.png
    :align: center
    :name: ISU Extended Header Structure

.. raw:: html

    <br>


Data Fields
-----------

.. warning::
    Please note that the information provided in this chapter is not 100 percent validated;
    most of it is based on assumptions. Therefore, it is important to approach this chapter
    with caution and consider the information as speculative rather than definitive.

During the analysis of certain firmware binaries, sections with peculiar names such as
"DecompBuffer" were discovered. For the purpose of reference, we will refer to each of these
sections as a ``DataField``. It can be described as follows:

.. code-block:: c++
    :linenos:

    namespace isu {
        struct DataField {
            le u16 length; // maybe? (is the size of this struct)
            le u16 unknown_1;
            le u16 name_length;
            le u16 flags; // unknown
            char name[16]; // padded string

            if (this.length == 32) {
                le u32 value;
                le u32 unknown_2;
            }
        };
    }

The additional length check is necessary because firmware binaries of the Venice 8 module include
an extra field named "CompSSSize" that does not have any associated value data. Below is an
illustration of all possible data fields:

.. image:: graphics/isu_data_field_marker.png
    :align: center

.. raw:: html

    <br>

The following table presents the associated values for the identified data fields in the
Venice 8 module firmware binary:

.. image:: graphics/isu_data_field_values.png
    :align: center
    :name: DataField list of ir-mmi-FS2028-0000-0032_V3.2.7.42548-20.isu.bin

.. raw:: html

    <br>

One interesting fact is that ``"CompSize"`` refers to the compressed core data of the firmware
binary.

Data Sections
~~~~~~~~~~~~~

This chapter refers to sections that encompass lists of "DataFields." The analyzed firmware
binaries contained multiple structures that can be consolidated into a general "DataSection"
structure.

.. code-block:: c++

    namespace isu {
        struct DataSection {
            le u8 magic; // always 128
            le u8 length;
            le u8 data[this.length];
        };
    }

Since this structure has not been validated, it will not be taken into consideration for
further analysis.

Directory Archive
-----------------

Directory archives are widely used and considered as a common structure in use today. As
the name implies, these archives store a directory that provides information about all
the files, including their names, offsets, and lengths. These archives are typically
simple and straightforward to read.

The structure can once again be defined using the pattern language. Since we will be
defining multiple structures, we will split the definition into several parts. First,
we will define the header:

.. code-block:: c++
    :linenos:

    namespace archive { // in namespace isu
        struct Header {
            char magic[4]; // FSH1
            le u32 size;
            le u16 unknown_1;
            le u32 index_size;
            isu::archive::Index index; // tbd
        };
    }

Before we declare the archive index, let's quickly examine the highlighted values to better
understand our current situation.

.. image:: graphics/isu_archive_header_marker.png
    :align: center

.. raw:: html

    <br>

Note that we replaced the ``isu::archive::Index`` with a raw data block as this structure will
be defined in the next section.

.. image:: graphics/isu_archive_header_values.png
    :align: center

.. raw:: html

    <br>

Directory Archive Index
~~~~~~~~~~~~~~~~~~~~~~~

The Directory archive begins with a header tag called ``FSH1``. Immediately after that, the size of
the archive and the size of the index are presented as 32-bit numbers. The actual structure of each
entry in the archive index is as follows:

.. code-block:: c++
    :linenos:
    :caption: isu::archive::IndexEntry

    namespace archive {
        enum IndexEntryType : u8 {
            File = 0x00,
            Directory
        };

        struct IndexEntry {
            isu::archive::IndexEntryType type;
            le u8 name_length;
            char name[this.name_length];

            if (this.type == isu::archive::IndexEntryType::Directory) {
                le u8 entry_count;
                isu::archive::IndexEntry entries[this.entry_count];
            } else {
                le u32 size; // file is compressed if size != compressed_size
                le u32 offset;
                le u32 compressed_size;
            }
        };
    }

.. note::
    The offset is in relation to the start of the directory archive header, so
    an absolute offset may be computed with::

        absolute_position = OFFSET(archive_header) + entry.offset


Now, let's return to the binary file and apply the defined structure to view
all the contents of an ISU Archive Entry.

.. image:: graphics/isu_archive_entry_marker.png
    :align: center

.. raw:: html

    <br>

The following table displays the values for a directory index entry and a file entry:

.. image:: graphics/isu_archive_entry_values.png
    :align: center

.. raw:: html

    <br>

Finally, we can define the "root" index, which is placed directly after the archive header. Note
that it contains an empty name.

.. code-block:: c++
    :linenos:

    namespace archive { // within namespace isu
        struct Index {
            le u8 length;
            char name[this.length];
            le u8 entry_count;
            isu::archive::IndexEntry entries[this.entry_count];
        };
    }

Since the fully marked directory archive would be too colorful to list here, it will not be included.

Contents of a Directory Archive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The structure of a defined directory archive in ISU-Files (except for ``FS2028``) doesn't differ much.
The tree structure can be represented as follows:

.. code:: text

    icons/
    web/
        css/
        images/
        iperf/ (optional)
        js/
        languages/
        <HTML-Files>
    FwImage/

Please note that this representation is a simplified visual representation of the directory structure
within the archive. The structure itself reveals some interesting information that was previously
unknown. The ``iperf`` directory contains files specifically designed to interact with an inbound
*iperf* module.

.. epigraph::

    *"iPerf3 is a tool used for actively measuring the maximum achievable bandwidth on IP networks."*

    -- iPerf3 (`source <https://iperf.fr/>`_)

Regarding the ``FwImage`` directory, it is highly likely to contain a firmware image, and that assumption
is indeed correct. Typically, the file stored in this directory is the latest firmware image for the
built-in Wi-Fi chip.
