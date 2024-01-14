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

__all__ = [
    "IndexEntryType",
    "ISUHeader",
    "ISUDataField",
    "ISUArchiveIndexEntry",
    "ISUArchiveIndexFileEntry",
    "ISUArchiveIndexDirectoryEntry",
    "ISUArchiveIndex",
    "ISUArchive",
    "ISUDataField",
    "ISUDataSection",
    "ISU",
]

import typing as t
import io
import mmap
import enum
import construct as cs

from lzallright import LZOCompressor, LZOError, InputNotConsumed
from construct_dataclasses import dataclass_struct, csfield, tfield, subcsfield


# -- Enums -------------------------------------------------------------------
class IndexEntryType(enum.IntEnum):
    File = 0x00
    Directory = 0x01


# -- Adapters ----------------------------------------------------------------
class SpacePaddedString(cs.Adapter):
    def __init__(self, length):
        super().__init__(cs.PaddedString(length, "utf-8"))

    def _decode(self, obj: str, context, path):
        return obj.strip("\x20")

    def _build(self, obj: str, stream, context, path):
        padding = self.subcon.sizeof() - len(obj)
        self.subcon._build(obj + "\x20" * padding, stream, context, path)


class ArchiveIndexEntryAdapter(cs.Construct):
    def __init__(self):
        super().__init__()

    def _parse(self, stream, context, path):
        value = context.type
        if isinstance(value, cs.EnumIntegerString):
            value = value.intvalue

        if value == IndexEntryType.Directory:
            return ISUArchiveIndexDirectoryEntry.parser.parse_stream(stream)
        elif value == IndexEntryType.File:
            return ISUArchiveIndexFileEntry.parser.parse_stream(stream)
        else:
            raise cs.ValidationError(f"Invalid type: {value}", path)

    def _build(self, obj, stream, context, path):
        return obj.parser.build(obj)


# -- Structs -----------------------------------------------------------------
@dataclass_struct
class ISUHeader:
    magic: int = csfield(cs.Const(0x1176, cs.Int32ul))  # "76 11 00 00"
    length: int = csfield(cs.Int32ul)
    isu_version: int = csfield(cs.Int32ul)
    version: str = csfield(SpacePaddedString(32))
    customisation: str = csfield(SpacePaddedString(64))
    # We have to create a Conditional object here as these fields
    # are only present in FS2028 firmware binaries
    os_major_version: str | None = csfield(
        cs.If(cs.this.length == 0xA2, SpacePaddedString(6))
    )
    os_minor_version: str | None = csfield(
        cs.If(cs.this.length == 0xA2, SpacePaddedString(32))
    )
    uuid: bytes = csfield(cs.Bytes(16))


@dataclass_struct
class ISUDataField:
    length: int = csfield(cs.Int16ul)
    unknown_1: int = csfield(cs.Int16ul)
    name_length: int = csfield(cs.Int16ul)
    flags: int = csfield(cs.Int16ul)
    name: str = csfield(cs.PaddedString(cs.this.name_length, "utf-8"))
    unknown_2: int | None = csfield(cs.If(cs.this.length == 32, cs.Int32ul))
    value: int | None = csfield(cs.If(cs.this.length == 32, cs.Int32ul))


@dataclass_struct
class ISUArchiveIndexEntry:
    type: IndexEntryType = tfield(IndexEntryType, cs.Enum(cs.Int8ul, IndexEntryType))
    name_length: int = csfield(cs.Int8ul)
    name: str = csfield(cs.PaddedString(cs.this.name_length, "utf-8"))
    content: ISUArchiveIndexDirectoryEntry | ISUArchiveIndexFileEntry = csfield(
        ArchiveIndexEntryAdapter()
    )


@dataclass_struct
class ISUArchiveIndexFileEntry:
    size: int = csfield(cs.Int32ul)
    offset: int = csfield(cs.Int32ul)
    compressed_size: int = csfield(cs.Int32ul)

    def is_compressed(self) -> bool:
        return self.compressed_size != self.size


@dataclass_struct
class ISUArchiveIndexDirectoryEntry:
    entry_count: int = csfield(cs.Int8ul)
    entries: t.List[ISUArchiveIndexEntry] = subcsfield(
        ISUArchiveIndexEntry, cs.Array(cs.this.entry_count, ISUArchiveIndexEntry.struct)
    )


@dataclass_struct
class ISUArchiveIndex:
    length: int = csfield(cs.Int8ul)
    name: bytes = csfield(cs.Bytes(cs.this.length))  # always 0
    entry_count: int = csfield(cs.Int8ul)
    entries: t.List[ISUArchiveIndexEntry] = subcsfield(
        ISUArchiveIndexEntry, cs.Array(cs.this.entry_count, ISUArchiveIndexEntry.struct)
    )


@dataclass_struct
class ISUArchive:
    magic: bytes = csfield(cs.Const(b"FSH1"))
    size: int = csfield(cs.Int32ul)
    unknown_1: int = csfield(cs.Int16ul)
    index_size: int = csfield(cs.Int32ul)
    index: ISUArchiveIndex = csfield(ISUArchiveIndex)
    data: bytes = csfield(cs.Bytes(cs.this.size - cs.this.index_size - 4))


@dataclass_struct
class ISUDataSection:
    magic: int = csfield(cs.Int8ul)
    length: int = csfield(cs.Int8ul)
    data: bytes = csfield(cs.Bytes(cs.this.length))


# -- Core Classes ------------------------------------------------------------
class isu_t(type):
    def __lshift__(cls, path: str) -> ISU:
        return ISU.parse_file(path)


class ISU(metaclass=isu_t):
    """Class to interact with binary ISU files.

    You can use this class to conveniently inspect ISU files. Regardless of the
    underlying file, the following attributes can be parsed:

    - header (:class:`ISUHeader`): the header of the parsed file
    - archive (:class:`ISUArchive`): if present, the stored directory archive
    - data_fields (list of :class:`ISUDataField`): A list of data fields that store various attributes

    :param stream: The memory map that stores the internal file data or an IOBase
                   object that supports the following modes: ``r+b`` and ``fileno()``.
    :type stream: IOBase or mmap

    Parse ISU Headers
    ~~~~~~~~~~~~~~~~~

    Note that each time you access the *header* attribute of an :class:`ISU` object,
    the header will be parsed again.

    >>> header = isu.header
    >>> header.customisation
    'ir-mmi-FS2026-0500-0795'

    Parse Directory Archives
    ~~~~~~~~~~~~~~~~~~~~~~~~

    As described in the :ref:`isu_firmware_structure` document, sometimes there is a
    directory archive that contains compressed and uncompressed files.

    >>> archive = isu.archive
    >>> for entry in archive.index.entries:
    ...     ... # inspect attributes here

    Parse Data Fields
    ~~~~~~~~~~~~~~~~~

    Data fields can be quite useful as they may define the size of the compressed/encrypted
    data block present in all ISU files. You can retrieve them using a property.

    >>> fields = isu.data_fields
    >>> if len(fields) > 0:
    ...     field = fields[0]
    ...     ... # inspect attributes here

    Extract Firmware Core
    ~~~~~~~~~~~~~~~~~~~~~

    The core of an firmware file is often compressed using the LZO algorithm. You can
    decompress it with two functions.

    >>> comp_size, decomp_size = fields["CompSize"], fields["DecompSize"]
    >>> core = isu.get_core(comp_size.value)
    >>> decomp_data = core.decompress(decomp_size.value, verify=True)
    """

    def __init__(self, stream: t.Union[io.IOBase, mmap.mmap]) -> None:
        if isinstance(stream, io.IOBase):
            self.stream = mmap.mmap(stream.fileno(), 0)
        elif isinstance(stream, mmap.mmap):
            self.stream = stream
        else:
            raise TypeError(f"Expected mmap or IOBase - got {type(stream)}")

    @staticmethod
    def parse_file(name: str) -> ISU:
        """Opens the given file and prepares it for parsing.

        :param name: the path to an ISU file
        :type name: str
        :return: the created ISU instance
        :rtype: ISU
        """
        with open(name, "r+b") as fp:
            stream = mmap.mmap(fp.fileno(), 0)

        return ISU(stream)

    @property
    def header(self) -> ISUHeader:
        """Parses the header of an ISU file

        :return: the parsed header instance.
        :rtype: ISUHeader
        """
        return self._create(ISUHeader)

    @property
    def archive(self) -> ISUArchive | None:
        """Parses a stored directory archive if present.

        :return: the parsed archive; None otherwise
        :rtype: ISUArchive | None
        """
        index = self.stream.rfind(b"FSH1")
        if index == -1:
            return None

        return self._create(ISUArchive, index)

    @property
    def data_fields(self) -> it_data_fields:
        """Returns all data fields defined in the underlying ISU file.

        :return: an object storing all data fields.
        :rtype: it_data_fields
        """
        return it_data_fields(self)

    def get_core(self, comp_size: int) -> isu_core_t:
        """Extracts the core of an update binary.

        :param comp_size: the compressed section size
        :type comp_size: int
        :return: the core data
        :rtype: isu_core_t
        """
        # we use this as identifier for now
        index = self.stream.find(b"\x1B\x00\x55\xAA", 0)
        if index == -1:
            return isu_core_t(self, None, BufferError("Pattern not found!"))

        # REVISIT: maybe stream that data
        return isu_core_t(self, self.stream[index : index + comp_size])

    def get_data_section(self, index: int) -> ISUDataSection:
        """Parses a data section starting at the given index.

        :param index: the starting position (absolute)
        :type index: int
        :return: the parsed data section
        :rtype: ISUDataSection
        """
        return self._create(ISUDataSection, index)

    def get_archive_file(
        self, entry: ISUArchiveIndexFileEntry, archive: ISUArchive
    ) -> bytes:
        """Returns the file entry's data within the directory archive.

        :param entry: the data of a file entry
        :type entry: ISUArchiveIndexFileEntry
        :param archive: the directory archive instance
        :type archive: ISUArchive
        :return: the file's data (may be compressed)
        :rtype: bytes
        """
        if isinstance(entry, ISUArchiveIndexEntry):
            assert entry.type == IndexEntryType.File, "File entry required!"
            entry = entry.content

        # NOTE: The offset position is relative to the start of the archive header
        # without the magic bytes. So we have to remove the index size and additional
        # four bytes for the directory archive size field.
        offset = entry.offset - archive.index_size - 4
        size = entry.size
        if size != entry.is_compressed():
            # File is compressed
            size = entry.compressed_size

        return archive.data[offset : offset + size]

    # internal
    def _create(self, __class: t.Type[t._T], index=0) -> t._T:
        self.stream.seek(index, 0)
        return __class.parser.parse_stream(self.stream)


class it_data_fields:
    """Represents data fields in an ISU file.

    This class is used to store and manage ISUDataField objects associated with an
    ISU instance. It allows iteration over the data fields, indexing by key (either
    by name or index), and retrieving the total number of data fields.

    Examples::

        >>> fields = isu.data_fields
        >>> fields["DecompSize"]
        ISUDataField(length=32, ..., name='DecompSize', value=6718304, ...)
        >>> len(fields)
        5
        >>> fields[1]
        ISUDataField(length=32, ..., name='CompSize', value=3132978, ...)

    .. note::
        All fields will be cached when an instance of this class is created.

    :param isu: An instance of the ISU class.
    """

    def __init__(self, isu: ISU) -> None:
        self.isu = isu
        self._fields = self._parse_fields()

    def _parse_fields(self) -> t.List[ISUDataField]:
        index = self.isu.stream.find(b"DecompBuffer")
        if index == -1:
            # Rather return an empty list than raising an error
            return []

        index -= 8
        result = []
        while True:
            data_field = self.isu._create(ISUDataField, index)
            result.append(data_field)

            index += data_field.length
            # REVISIT: this is very unsafe
            if self.isu.stream[index] not in (0x20, 0x18):
                break

        return result

    def __iter__(self) -> t.Iterator[ISUDataField]:
        """Return an iterator for the data fields.

        :return: An iterator yielding ISUDataField objects.
        """
        return iter(self._fields)

    def __getitem__(self, key: int | str) -> ISUDataField:
        """Get a data field by key (either name or index).

        :param key: The name or index of the data field to retrieve.
        :return: The ISUDataField object corresponding to the key, or None if not found.
        """
        if isinstance(key, str):
            for field in self._fields:
                if field.name == key:
                    return field

        elif isinstance(key, int):
            return self._fields[key]

        return None

    def __len__(self) -> int:
        """Return the number of data fields.

        :return: The total number of data fields.
        """
        return len(self._fields)


class isu_core_t:
    """Delegate class to store firmware core data.

    This class is used to represent and manipulate firmware core data. It is primarily
    used for compression and decompression operations on that data.

    :param isu: An instance of the ISU class.
    :param data: The core data as bytes.
    :param compressed: A boolean flag indicating whether the data is already compressed
                       (default: True).
    :param errors: Optional list of error messages (default: empty list).
    """

    def __init__(self, isu: ISU, data: bytes, *errors, compressed=True) -> None:
        self.errors = list(errors)
        self.data = data
        self.isu = isu
        self.compressed = compressed

    @property
    def has_errors(self) -> bool:
        """Check if there are any errors recorded in the instance.

        :return: True if there are errors, False otherwise.
        """
        return len(self.errors) > 0

    def decompress(self, decomp_size: int, verify=False) -> bytes:
        """Decompress the core data.

        This method decompresses the core data using the LZOCompressor. If the data is
        already uncompressed, it returns the original data.

        :param decomp_size: The expected size of the decompressed data.
        :param verify: A boolean flag indicating whether to verify the decompressed
                       data size (default: False).
        :return: The decompressed data as bytes.
        :raises ValueError: If the decompressed data size does not match the expected
                            size and `verify` is True.
        """
        # Clear errors first before decompressing data
        self.errors.clear()
        if not self.compressed:
            return self.data
        try:
            decomp_buf = LZOCompressor.decompress(
                self.data, output_size_hint=decomp_size
            )
        except LZOError as err:
            if isinstance(err, InputNotConsumed):
                # decompression finished with leftover data
                _, decomp_buf = err.args
            else:
                self.errors.append(err)
                decomp_buf = bytes()  # to prevent errors

        if len(decomp_buf) != decomp_size and verify:
            raise ValueError(
                f"Expected decompSize={decomp_size}, got output_size={len(decomp_buf)}"
            )
        # Always return a bytes object
        return decomp_buf

    def compress(self, comp_size: int = -1, verify=False) -> bytes:
        """Compress the core data.

        This method compresses the core data using the LZOCompressor. If the data is
        already compressed, it returns the original data.

        :param comp_size: The expected size of the compressed data (default: -1,
                          indicating no specific size requirement).
        :param verify: A boolean flag indicating whether to verify the compressed
                       data size (default: False).
        :return: The compressed data as bytes.
        :raises ValueError: If the compressed data size does not match the expected
                            size and `verify` is True.
        """
        self.errors.clear()
        if self.compressed:
            return self.data

        try:
            comp_buf = LZOCompressor.compress(self.data)
        except LZOError as err:
            self.errors.append(err)
            comp_buf = bytes()

        if verify and len(comp_buf) != comp_size:
            raise ValueError(
                f"Expected compSize={comp_size}, got output_size={len(comp_buf)}"
            )
        return comp_buf
