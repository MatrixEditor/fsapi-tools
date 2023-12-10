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
__doc__ = """
+--------+---------------------------------------------------------------------------------+
|  Name  | Description                                                                     |
+========+=================================================================================+
| ir/mmi | Basic ISU inspectors for most of the firmware binaries. All standard operations |
|        | are supported by the returned instance. (header, fields, archive)               |
+--------+---------------------------------------------------------------------------------+
| ir/cui | Inspectors written to handle files from devices with the CUI module type. Only  |
|        | the ``header`` method will work here.                                           |
+--------+---------------------------------------------------------------------------------+
| ns/mmi | These special inspectors will inspect ``ota.bin`` files from devices with the   |
|        | Minuet module. Only the ``header()`` can be called.                             |
+--------+---------------------------------------------------------------------------------+
"""

from .product import (
    FSCustomisation,
    FSVersion,
    RE_CUSTOMISATION,
    RE_VERSION,
    FSVERSION_MODULE_TYPES
)
from .update import (
    find_update,
    url_find_update,
    UpdateError,
    UpdateRequest,
    UpdateStatus,
    get_update,
    url_get_update,
    ISU_EDGE_PROVIDER_HOST,
    ISU_FILE_PROVIDER_HOST,
    ISUSoftwareElement
)
from .format import (
    ISU,
    ISUHeader,
    ISUArchive,
    ISUArchiveIndex,
    ISUArchiveIndexEntry,
    ISUArchiveIndexFileEntry,
    ISUArchiveIndexDirectoryEntry,
    ISUDataSection,
    ISUDataField,
    IndexEntryType,
)