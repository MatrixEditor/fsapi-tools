import enum
import uuid
import pprint
import dataclasses

from colorama import Fore, init

init(autoreset=True)


def handle_magic(value, **context: dict) -> str:
    if isinstance(value, bytes):
        value = value.decode()
    elif isinstance(value, int):
        value = hex(value)

    if context.get("colorized"):
        return Fore.GREEN + str(value)
    else:
        return str(value)


def handle_uuid(value, **context) -> str:
    assert type(value) == bytes, "Expected bytes for UUID!"

    value = str(uuid.UUID(bytes=value))
    if context.get("colorized"):
        value = Fore.CYAN + value
    return value


class DataclassPrinter: # maybe add depth
    """Internal class"""

    indent: int = 0

    def __init__(self, colorized=True, out=None, default_handlers=None) -> None:
        self.colorized = colorized
        self.handlers = default_handlers or {"magic": handle_magic, "uuid": handle_uuid}
        self.out = out or print

    def print_object(self, obj, indent=None) -> None:
        indent = (indent or (self.indent-1))
        self.out(self.get_msg(Fore.LIGHTBLACK_EX, " "*indent, f"> {type(obj).__name__}:"))
        self._fprint_dataclass(obj, indent)

    def print_field(self, name: str, value) -> None:
        self._fprint(name, value, self.indent - 1)

    def _fprint(self, name: str, value, indent) -> None:
        if dataclasses.is_dataclass(value):
            self.out(self.get_name_format(name, indent))
            self._fprint_dataclass(value, indent)
            return

        value = self.get_format(name, value)
        msg = self.get_name_format(name, indent)
        if not isinstance(value, list):
            self.out(" ".join((msg, str(value))))
        else:
            self.out(msg)
            for i, element in enumerate(value):
                msg = " " * (indent + 4) + self.get_array_format(i)
                if dataclasses.is_dataclass(element):
                    self.out(msg + self.get_msg(Fore.LIGHTCYAN_EX, str(type(element))))
                    self._fprint_dataclass(element, indent + 8)
                else:
                    self.out(msg + self.get_format("", element))

    def _fprint_dataclass(self, obj, indent) -> None:
        for field in dataclasses.fields(obj):
            field_val = getattr(obj, field.name)
            self._fprint(field.name, field_val, indent=indent + 4)

    def get_msg(self, style, *msg, end="") -> str:
        if self.colorized:
            return style + " ".join(list(msg)) + end

        return " ".join(list(msg))

    def print_msg(self, style, *msg, end="") -> None:
        print(self.get_msg(style, *msg, end=end))

    def get_format(self, name: str, value) -> str:
        result = value
        result_c = value
        indent = len(name) + self.indent
        if name in self.handlers:
            return self.handlers[name](value, colorized=self.colorized, indent=indent)

        elif isinstance(value, (enum.Enum, enum.IntEnum, type)):
            result = repr(value)
            result_c = Fore.LIGHTCYAN_EX + result

        elif isinstance(value, (int, float)):
            result = str(value)
            result_c = Fore.LIGHTMAGENTA_EX + str(value)

        elif isinstance(value, str):
            result = pprint.pformat(value, indent=indent, width=125)
            result_c = Fore.YELLOW + result

        elif isinstance(value, bytes):
            try:
                result = pprint.pformat(value.decode(), indent=indent, width=125)
                result_c = Fore.YELLOW + result
            except Exception:
                result = 'b"..."'
                result_c = Fore.CYAN + "b" + Fore.YELLOW + '"..."' + Fore.RESET
                result_c += " size=" + self.get_format("", len(value))

        return result if not self.colorized else result_c

    def get_array_format(self, index):
        if self.colorized:
            return f" [{Fore.LIGHTMAGENTA_EX}{index}{Fore.RESET}] => "

        return f"[{index}] => "

    def get_name_format(self, name, indent):
        msg = f"- {name}:"
        return self.get_msg(Fore.LIGHTBLACK_EX, " " * indent, msg, end=Fore.RESET)
