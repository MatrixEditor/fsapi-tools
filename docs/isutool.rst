.. _isutool:

=======
ISUTool
=======

This document offers a brief overview of the command line integration of
``fsapi.isu``. Once you have installed *fsapi-tools*, you can run this
tool either by referencing the Python module or by executing it directly.

.. code-block:: bash

    python3 -m fsapi.isu --help
    # or directly
    isutool --help


Displaying ISU Header
~~~~~~~~~~~~~~~~~~~~~

You have the option to either dump the header of a single file or list all
headers of firmware files within the specified directory.

.. code-block:: bash
    :caption: Dumping the ISUHeader

    # headers of all firmware files (optional: recursively)
    isutool -H [-r] /path/to/directory
    # Or just one file header
    isutool -H ./firmware.isu.bin
    [in] ./firmware.isu.bin
        > ISUHeader:
            - magic: 0x1176
            - length: 124
            - isu_version: 1
            - version: '2.5.15.EX51267-1BS8'
            - customisation: 'ir-mmi-FS2026-0500-0034'
            - os_major_version: None
            - os_minor_version: None
            - uuid: ae8ee1b1-75d5-c2f4-c401-b6c95cdf2379


Displaying DataFields
~~~~~~~~~~~~~~~~~~~~~

The *isutool* also provides an option to display all data fields defined
in an ISU file.

.. code-block:: bash
    :caption: Dumping all DataFields

    isutool -F firmware.isu.bin
    [in] firmware.isu.bin
        > Data Fields:
            [0] => <class 'fsapi.isu.format.ISUDataField'>
                > ISUDataField:
                    - length: 32
                    - unknown_1: 21248
                    - name_length: 13
                    - flags: 4
                    - name: 'DecompBuffer'
                    - value: 2958237696
                    - unknown_2: 0
            # ...


Displaying the Directory Archive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the previously mentioned options, you have the ability to print
and inspect the entire directory archive.

.. warning::
    The output can potentially be too large to handle directly. Therefore, it is
    recommended to save the archive in JSON format and inspect it at a later time.

.. code-block:: bash
    :caption: Duming a directory archive

    isutool -A firmware.isu.bin
    [in] firmware.isu.bin
        > ISUArchive:
            - magic: FSH1
            - size: 246669
            - unknown_1: 10539
            - index_size: 537
            - index:
                - length: 1
                - name: '\x00' # Root index entry
                - entry_count: 3
                - entries:
                    [0] => <class 'fsapi.isu.format.ISUArchiveIndexEntry'>
                            - type: IndexEntryType.Directory
                            - name_length: 3
                            - name: 'web'
                            - content:
                                - entry_count: 7
                                - entries:
            # ...


.. hint::
    If you wish to display the header, all fields, and the directory archive simultaneously,
    you have two options. You can either use all the presented options together or simply
    utilize the ``--dump-all`` option.


Export to JSON
~~~~~~~~~~~~~~

This tool also supports JSON format, allowing you to easily utilize the extracted data in your
own tools. The exported schema is equivalent to the defined structures in the firmware structure
document, providing compatibility and ease of integration.

.. code-block:: bash
    :caption: Exporting all data to JSON

    isutool firmware.isu.bin --json ./data.json
    [in] firmware.isu.bin
    [out] JSON saved to ./data.json


.. hint::
    To include the data section of a directory archive, you can use an additional option named ``--json-full``.
    When this option is enabled, the tool will include the data section in the JSON output as a string.


Extraction of Compressed/Encrypted Core-Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since the core data block of Frontier Smart's firmware binaries is not fully understood, it is
recommended to solely extract the block without attempting reverse engineering. Reverse engineering
can be performed using other specialized tools designed for that purpose. You have the flexibility
to either specify the output destination or provide a directory, and the tool will generate an
appropriate file accordingly.

.. code-block:: bash
    :caption: Extract compressed/encrypted data block

    isutool firmware.isu.bin --extract-core /path/to/directory/
    [in] firmware.isu.bin
    [out] Saved core to /path/to/directory/ir-mmi-FS2026-0500-0034_2.5.15.EX51267-1BS8.core.bin


.. hint::
    You can also try to decompress the core of a firmware file using ``--decompress-core`` or shortly
    ``-dC``:

    .. code-block:: bash

        isutool firmware.isu.bin --decompress-core --extract-code /path/to/directorty
        [in] firmware.isu.bin
        [out] Saved core to /path/to/directory/ir-mmi-FS2026-0500-0034_2.5.15.EX51267-1BS8.core.bin


Extraction of Directory Archive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tool also supports the extraction of directory archives. If the stored files within the archive
are marked as compressed, the tool will automatically decompress them during the extraction process.
This simplifies the extraction procedure and ensures that the extracted files are in their
uncompressed form.

.. code-block:: bash
    :caption: Extract directory archive

    isutool firmware.isu.bin --extract-archive ./rootfs
    [in] firmware.isu.bin
    [out] Directory Archive:
        > web/ (7)
            > css/ (1)
                > base/ (3)
                    > images/ (1)
                        - header_bg.png
                    - style-handheld.css
                    - style-screen.css
            > images/ (2)
                - company_logo.png


General Options
~~~~~~~~~~~~~~~

.. code-block:: bash

    isutool --help

    positional arguments:
    path                  Path to ISU file or directory with multiple ISU files.

    optional arguments:
    -h, --help                  show this help message and exit
    -o OUTPUT, --output OUTPUT  Path to the output file or directory.
    --disable-color             Disable colorized output
    -r, --recurse               Search for *.isu.bin and *.ota.bin files in directories (recursively).
    -j JSON, --json JSON        Saves all information as to a JSON file.
    --json-full                 Saves the whole directory archive including its data section

    Information Dumping:
    --header, -H          Prints header information.
    --archive, -A         Dumps the whole directory archive (warning: expect long output)
    --fields, -F          Prints out all identified data fields.
    --dump-all            Equivalent to -A -H -F all together.

    Data Extraction:
    -eA PATH, --extract-archive PATH    Extract the directory archive (if present) to the given directory
    -eC PATH, --extract-core PATH       Saves the compressed/encrypted core to the provided path.
    -dC, --decompress-core              Decompresses the firmware core (onlay applicable with -eC).
