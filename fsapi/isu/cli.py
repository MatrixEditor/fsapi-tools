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

import sys
import argparse
from typing import Any
import zlib
import pathlib
import dataclasses
import json
import binascii

from colorama import Fore

from fsapi.isu.format import ISU, ISUArchiveIndexEntry, IndexEntryType
from fsapi.isu.util import DataclassPrinter

ALLOWED_SUFFIXES = ("isu.bin", "ota.bin")


class BytesJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, bytes):
            return binascii.hexlify(o).decode(errors="replace")
        return super().default(o)


def main(cmd=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", help="Path to ISU file or directory with multiple ISU files."
    )
    parser.add_argument("-o", "--output", help="Path to the output file or directory.")
    parser.add_argument(
        "--disable-color", help="Disable colorized output", action="store_true"
    )
    parser.add_argument(
        "-r",
        "--recurse",
        help="Search for *.isu.bin and *.ota.bin files in directories (recursively).",
        action="store_true",
    )
    parser.add_argument("-j", "--json", help="Saves all information as to a JSON file.")
    parser.add_argument(
        "--json-full",
        help="Saves the whole directory archive including its data section",
        action="store_true",
    )

    id_group = parser.add_argument_group("Information Dumping")
    id_group.add_argument(
        "--header", "-H", help="Prints header information.", action="store_true"
    )
    id_group.add_argument(
        "--archive",
        "-A",
        help="Dumps the whole directory archive (warning: expect long output)",
        action="store_true",
    )
    id_group.add_argument(
        "--fields",
        "-F",
        help="Prints out all identified data fields.",
        action="store_true",
    )
    id_group.add_argument(
        "--dump-all", help="Equivalent to -A -H -F all together.", action="store_true"
    )

    e_group = parser.add_argument_group("Data Extraction")
    e_group.add_argument(
        "-eA",
        "--extract-archive",
        default=None,
        metavar="PATH",
        help="Extract the directory archive (if present) to the given directory",
    )
    e_group.add_argument(
        "-eC",
        "--extract-core",
        default=None,
        metavar="PATH",
        help="Saves the compressed/encrypted core to the provided path.",
    )
    e_group.add_argument(
        "-dC",
        "--decompress-core",
        action="store_true",
        help="Decompresses the firmware core (onlay applicable with -eC).",
    )

    argv = parser.parse_args(cmd)
    pp = DataclassPrinter(colorized=not argv.disable_color)

    # some sanity checks before we can start
    if not argv.dump_all and (
        not (argv.header or argv.archive or argv.fields)
        and not (argv.extract_core or argv.extract_archive, argv.json)
    ):
        pp.print_msg(Fore.RED, "[!] -> Invalid options: nothing selected!")
        sys.exit(1)

    target_path = pathlib.Path(argv.path)

    if not target_path.is_dir():
        _run(argv, target_path, pp)
    else:
        filter_fn = target_path.glob if not argv.recurse else target_path.rglob
        out_archive_base = argv.extract_archive
        for suffix in ALLOWED_SUFFIXES:
            for path in filter_fn(f"*.{suffix}"):
                if path.is_dir():
                    continue

                if out_archive_base:
                    new_path = pathlib.Path(out_archive_base) / path.stem
                    argv.extract_archive = new_path
                try:
                    _run(argv, path, pp)
                    print()  # just for prettier output
                except Exception as err:
                    pp.print_msg(Fore.RED, f"[!] {type(err).__name__}:", str(err))


def _run(argv, target: pathlib.Path, pp: DataclassPrinter):
    pp.print_msg(Fore.LIGHTBLACK_EX, f"[in] {target}")

    isu = ISU.parse_file(str(target))
    header = isu.header
    if argv.header or argv.dump_all:
        pp.print_object(header, indent=3)

    fields = isu.data_fields
    if argv.fields or argv.dump_all:
        if len(fields) == 0:
            pp.print_msg(Fore.YELLOW, " " * 3, "> No Data Fields")
        else:
            pp.print_msg(Fore.LIGHTBLACK_EX, " " * 3, "> Data Fields:")
            for i, data_field in enumerate(fields):
                msg = " " * 7 + pp.get_array_format(i)
                print(msg + pp.get_msg(Fore.LIGHTCYAN_EX, str(type(data_field))))

                pp.print_object(data_field, indent=11)

    archive = isu.archive
    if archive is None:
        msg = pp.get_msg(Fore.RED, "[!] Firmware does not store a directory archive!")
        print(msg)

    if (argv.archive or argv.dump_all) and archive:
        pp.print_object(archive, indent=3)

    if argv.json:
        out_path = pathlib.Path(argv.json)
        if not out_path.is_dir():
            values = {
                "header": dataclasses.asdict(header),
                "fields": [dataclasses.asdict(x) for x in fields],
                "archive": dataclasses.asdict(archive),
            }
            if not argv.json_full:
                # Don't include the data section if no explicitly activated
                values["archive"].pop("data")

            with open(str(out_path), "w", encoding="utf-8") as fp:
                json.dump(values, fp, cls=BytesJSONEncoder)
            pp.print_msg(Fore.LIGHTBLACK_EX, "[out] JSON saved to", str(out_path))
        else:
            pp.print_msg(Fore.RED, "[!] Invalid JSON output path (is a dir)")

    if argv.extract_core:
        field = fields["CompSize"]
        out_path = pathlib.Path(argv.extract_core)
        if out_path.is_dir():
            out_path = out_path / f"{header.customisation}_{header.version}.core.bin"

        decomp_size = fields["DecompSize"]
        core = isu.get_core(field.value)
        if core.has_errors:
            pp.print_msg(Fore.RED, "[!] Could not find any compressed core data!")
        else:
            with open(str(out_path), "wb") as fp:
                if argv.decompress_core:
                    msg = "[out] Saved decompressed core to"
                    data = core.decompress(decomp_size.value)
                    if core.has_errors:
                        pp_msg = pp.get_msg(
                            Fore.RED, "[!] Could not decompress core:", str(core.errors)
                        )
                        print(pp_msg)
                        return
                    fp.write(data)
                else:
                    msg = "[out] Saved core to"
                    fp.write(core.data)

            pp.print_msg(Fore.LIGHTBLACK_EX, msg, str(out_path))

    if argv.extract_archive and archive is not None:
        out_dir = pathlib.Path(argv.extract_archive)
        if not out_dir.exists():
            out_dir.mkdir(parents=True, exist_ok=True)

        if not out_dir.is_dir():
            out_dir = out_dir.parent
        pp.print_msg(Fore.LIGHTBLACK_EX, "[out] Directory Archive:", str(out_dir))
        for entry in archive.index.entries:
            save_entry(entry, out_dir, isu, archive, pp, indent=3)

    isu.stream.close()


def save_entry(
    entry: ISUArchiveIndexEntry,
    path: pathlib.Path,
    isu: ISU,
    archive,
    pp: DataclassPrinter,
    indent=0,
):
    if entry.type == IndexEntryType.File:
        msg = pp.get_msg(Fore.LIGHTBLACK_EX, " " * indent, f"- {entry.name}")
        print(msg)
        content = entry.content
        with open(str(path / entry.name), "wb") as fp:
            data = isu.get_archive_file(content, archive)
            if content.is_compressed():
                try:
                    fp.write(zlib.decompress(data))
                except zlib.error as err:
                    pp.print_msg(Fore.RED, " " * indent, f"! zlib.error: {err}")
            else:
                fp.write(data)

    else:
        msg = pp.get_msg(
            Fore.LIGHTBLACK_EX,
            " " * indent,
            f"> {entry.name}/ ({entry.content.entry_count})",
        )
        print(msg)
        path = path / entry.name
        path.mkdir(exist_ok=True)
        for dir_entry in entry.content.entries:
            save_entry(dir_entry, path, isu, archive, pp, indent + 4)


if __name__ == "__main__":
    main()
