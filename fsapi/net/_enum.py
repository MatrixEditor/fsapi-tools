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

import inspect
import sys
import enum

from typing import Optional

class FSAlarmSource(enum.IntEnum):
    BUZZER = 0
    DAB = enum.auto()
    FM = enum.auto()
    IPOD = enum.auto()


class FSDeviceState(enum.IntEnum):
    DISCONNECTED = enum.auto()
    CONNECTED = enum.auto()
    PAIRED = enum.auto()


class FSContextMenu(enum.IntEnum):
    FALSE = enum.auto()
    TRUE = enum.auto()


class FSGroupRole(enum.IntEnum):
    NO_GROUP = enum.auto()
    CLIENT = enum.auto()
    SERVER = enum.auto()


class FSRepeat(enum.IntEnum):
    EMPTY = enum.auto()
    EVERYDAY = enum.auto()
    ONCE = enum.auto()
    WEEKEND = enum.auto()
    WEEKDAY = enum.auto()


class FSSource(enum.IntEnum):
    MANUAL = enum.auto()
    DAB = enum.auto()
    FM = enum.auto()
    SNTP = enum.auto()


class FSSubType(enum.IntEnum):
    NONE = enum.auto()
    STATION = enum.auto()
    PODCAST = enum.auto()
    TRACK = enum.auto()
    TEXT = enum.auto()
    PASSWORD = enum.auto()
    OPTIONS = enum.auto()
    SUBMIT = enum.auto()
    BUTTON = enum.auto()
    DISABLED = enum.auto()


class FSType(enum.IntEnum):
    DIRECTORY = enum.auto()
    PLAYABLEITEM = enum.auto()
    SEARCHDIRECTORY = enum.auto()
    UNKNOWN = enum.auto()
    FORMITEM = enum.auto()
    MESSAGEITEM = enum.auto()
    AMAZONLOGIN = enum.auto()
    FETCHERRITEM = enum.auto()


class FSFormItemType(enum.IntEnum):
    STRING = enum.auto()
    PASSWORD = enum.auto()
    COMBOBOX = enum.auto()
    BUTTON = enum.auto()
    DESCRIPTION = enum.auto()


class FSModeType(enum.IntEnum):
    GENERIC = enum.auto()
    MODESPECIFIC = enum.auto()


class FSSystemRole(enum.IntEnum):
    INDEPENDENT = enum.auto()
    PRIMARY = enum.auto()
    SECONDARY = enum.auto()


# Not really en enum
class FSEQPreset(enum.IntEnum):
    MY_EQ = 0
    NORMAL = enum.auto()
    FLAT = enum.auto()
    JAZZ = enum.auto()
    ROCK = enum.auto()
    MOVIE = enum.auto()
    CLASSIC = enum.auto()
    POP = enum.auto()
    NEWS = enum.auto()


def enum_value_name(value: int, enum_: str) -> Optional[str]:
    member = get_enum(enum_)
    if member is None:
        return None

    return getattr(member, "_value2member_map_")[value]


def get_enum(field_name: str, path: str = None) -> Optional[type]:
    module = sys.modules[__name__]
    internal_name = f"FS_{field_name.upper()}"

    if path and field_name == "source" and path == "netRemote.sys.alarm.config":
        # Unfortunately, the field for this enum is also named "source"
        return FSAlarmSource

    for name, member in inspect.getmembers(module):
        if name == internal_name:
            return member

    return None
