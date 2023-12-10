.. _isu_firmware:

====================
FS Firmware Analysis
====================

This document offers general information on analyzing downloaded firmware binaries. Since
each product series by Frontier Smart includes distinct update binaries, each structure is
explained in a separate document (:ref:`Firmware Structure <isu_firmware_structure>`).


Understanding the firmware files becomes more challenging due to the utilization of a custom
OS by both Frontier Smart devices and the examined MEDION device. According to the Wi-Fi
certificate available at the internet archive `here <https://web.archive.org/web/20180210192501/https://certifications.prod.wi-fi.org/pdf/certificate/public/download?cid=WFA55569>`_,
the Frontier-Smart's Venice 6.5 module employs MeOS version 5.2 (source).

    The MEOS (MIPS Embedded Operating System) provides a framework that allows systems programmers
    to design systems as loosely coupled collections of tasks and device driver modules, with the
    details of scheduling, synchronisation and communication being handled by a standardised and
    well tested environment.

This brings us back to the beginning, as this embedded OS serves as a framework that can be
utilized for developing the operating system.

Binary Analysis
---------------

There are multiple methods available to determine the filetype. In this case, the following tools are
utilized: *file*, *binwalk*, *dd*, *vbindiff*, and the hex-editor `ImHex`_ for viewing the
binary data.

Let's start with the file utility:

.. code-block:: bash

    $ file ./ir-mmi-FS2026-0500-0549_V2.12.25c.EX72088-1A12.isu.bin
    ir-mmi-FS2026-0500-0549_V2.12.25c.EX72088-1A12: *data*

Now, let's examine the same file using binwalk::

    $ binwalk -B -A -t ir-mmi-FS2026.isu.bin

    DECIMAL       HEXADECIMAL     DESCRIPTION
    ------------------------------------------------------------------------------------
    1399391       0x155A5F        AES Inverse S-Box
    1400762       0x155FBA        SHA256 hash constants, little endian
    2032581       0x1F03C5        SHA256 hash constants, little endian
    2039377       0x1F1E51        AES Inverse S-Box
    2622703       0x2804EF        Zlib compressed data, best compression
    2635012       0x283504        PNG image, 120 x 120, 8-bit/color RGBA, non-interlaced
    2635097       0x283559        Zlib compressed data, best compression
    2637769       0x283FC9        Zlib compressed data, best compression
    [...]

Indeed, the *binwalk* analysis provides a more detailed breakdown of the contents stored in the
firmware file. It's worth noting that the offset indicating the beginning of the compressed data
is ``0x2804EF`` (~2.6 MB). This information is crucial because the data section before that offset
is not considered in the *binwalk* analysis.

Extracting Files
~~~~~~~~~~~~~~~~

To accurately view the contents stored in the directory archive, the ``fsapi.isu`` module (stored in
this repository) can be utilized. Use the following command to list all stored files and write their
basic information into a JSON file:


.. code-block:: bash

    $ python3 fsapi.isu firmware.isu.bin --json ./data.json


This command will retrieve an accurate view of the stored data and generate a JSON file that stores
all data fields, including the header data and optionally the directory archive's data. The output
will be saved to a file named ``data.json``, and a file entry could be represented as follows:

.. code-block:: json

    {
        "type": 0,
        "name_length": 10,
        "name": "index.html",
        "content": {
            "size": 132,
            "offset": 116935,
            "compressed_size": 94
        }
    },


This example showcases a file named *"index.html"* with a type of ``0`` (which indicates that this entry is a
file entry). It has a size of ``132`` bytes and starts at offset ``116935`` based on the starting offset of
the archive header. The file is marked as compressed, with a compression size of ``94`` bytes.

To extract the *"index.html"* file using the command line utility ``dd``, you can use the following command:

.. code-block:: bash

    $ dd if="path/to/file" of="index.html.zlib" bs=1 skip=2731787 count=762

The *bs* argument sets the block size to 1 byte, and the *skip* argument specifies the number of bytes to skip
(``2731787`` in this case). The *count* argument determines the number of bytes to copy (``132`` in this case).

Since the file is compressed, you can use the ``zlib-flate`` utility to decompress it. Here's an example command
for decompressing the extracted file:

.. code-block:: bash

    $ zlib-flate -uncompress < index.html.zlib > index.html

.. hint::
    Alternatively, *binwalk* can also extract the contents, but unfortunately, these results are named by their
    offset position, e.g. the ``2804EF`` file stores image-data. To solve this problem, use ``fsapi.isu`` with
    the *-e* flag to automatically extract (**and uncompress**) archive files.

If a web interface is available, the files stored in the directory archive can be accessed by the user through
a web browser using the following URL format::

    http://<IP-Address>:<Port>/<path/to/file>.<Extension>

.. _ImHex: https://github.com/WerWolv/ImHex


The CORE
--------

All update files contain either a compressed data block and a directory archive or only the compressed core.
Upon analysis, it has been revealed that this core block is compressed using the LZO algorithm.

.. note::
    LZO compression is only applied on Venice 6 - 6.5 modules.

The data block can be decompressed using the ``isutool``:

.. code-block:: bash

    isutool firmware.isu.bin -dC -eC firmware.core.bin

