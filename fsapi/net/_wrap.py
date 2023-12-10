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

import typing as t

from .base import NodePath, NodeListItem, IntEnumValue
from .device import FSDevice, Status


def wrap(device: FSDevice) -> _Wrapper:
    """Creates a new API wrapper for the given device.

    With the returned wrapper object, the most important nodes can be accessed
    using simple attribute syntax:

    >>> device = FSDevice("127.0.0.1")
    >>> api = wrap(device)
    >>> name: str = api.friendly_name

    Note that every access will fire an HTTP request to the desired target device.
    It is also possible to use this method as a decorator (property is optionall):

    >>> class Foo:
    ...    @wrap
    ...    @property
    ...    def api(self):
    ...        return self.device
    ...

    :param device: the controller implementing the FSAPI
    :type device: FSDevice
    :return: a new API wrapper
    :rtype: _Wrapper
    """
    return _Wrapper(device)


# Internal type variable to enable static type checking
_T = t.TypeVar("_T")


class APICall(t.Generic[_T]):
    """Generic API call using simple node definitions.

    This class will enable checks during runtime that prevents changing immutable
    values.

    **Important:** This class is strongly typed. In order to enable static type checking
    this class is annotated with a type variable.

    >>> class Foo:
    ...     value: APICall[int] = APICall("foo.bar")
    ...
    >>> foo = Foo()
    >>> foo.value
    5

    :param node_path: the node's path
    :type node_path: str
    """

    def __init__(self, node_path: str) -> None:
        self.node_path = NodePath(node_path)

    def __get__(self, __instance: t.Any, __owner: type | None = None) -> _T:
        return self.get(__instance)

    def __set__(self, __instance: t.Any, __value: _T) -> None:
        self.put(__instance, __value)

    def get(self, wrapper: _Wrapper) -> _T | None:
        """Returns the value for the linked node.

        :param wrapper: the API wrapper instance
        :type wrapper: _Wrapper
        :return: the fetched value or None if an error occurred
        :rtype: _T | None
        """
        response = wrapper.device.get(self.node_path)
        if response.status == Status.FS_OK:
            return response.node.value
        # REVISIT: maybe raise an exception
        return None

    def put(self, wrapper: _Wrapper, value: _T) -> None:
        """Sets a new value for the linked node.

        :param wrapper: the API wrapper instance
        :type wrapper: _Wrapper
        :param value: the new value to be applied
        :type value: _T
        :raises AttributeError: if the linked node is readonly
        """
        cls = self.node_path.get_node_type()
        if cls.readonly:
            # REVISIT: maybe don't throw an exception here
            raise AttributeError(f"Node '{cls.path}' is immutable!")

        wrapper.device.put(self.node_path, value=value)


class ListAPICall(APICall["list[NodeListItem]"]):
    """Representation for a list API call.

    This class behaves differently compared to standard API call variables
    as it fetches more than one item and can take query arguments.

    >>> api = wrap(device)
    >>> api.ls_eqpresets(_pos=2, max_items=3)
    [...]

    - ``_pos``: the starting index position within the list (-1 for all items)
    - ``max_items``: the number of items that should be returned
    """

    def __init__(self, node_path: str) -> None:
        super().__init__(node_path)
        self.__instance = None

    def __get__(self, __instance: t.Any, __owner: type | None = None) -> ListAPICall:
        self.__instance = __instance
        return self

    def __call__(self, _pos=-1, max_items=0xFFFF, **argv) -> list[NodeListItem] | None:
        argv["_pos"] = _pos
        argv["maxItems"] = max_items
        return self.get(self.__instance, **argv)

    def get(self, wrapper: _Wrapper, **argv) -> list[NodeListItem] | None:
        """Returns a list of items.

        :param wrapper: the api wrapper instance
        :type wrapper: _Wrapper
        :return: the list returned by the device
        :rtype: list[NodeListItem] | None
        """
        response = wrapper.device.list_get_next(self.node_path, **argv)
        if response.status != Status.FS_OK:
            return None

        return list(response.node)

    def put(self, wrapper: _Wrapper, value: int) -> None:
        """Selects an item within the context of this list node.

        :param wrapper: the API wrapper instance
        :type wrapper: _Wrapper
        :param value: the key of an item (index position)
        :type value: int
        :raises TypeError: if the provided value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError(f"Expected int value - got {type(value)}")

        return super().put(wrapper, value)


# Internal wrapper fro api call classes
_ac = APICall
_lac = ListAPICall

# TODO: add multiroom and spotify support
class _Wrapper:
    """Web FSAPI wrapper class.

    This class stores the most common nodes to control devices using the
    FSAPI. Standard nodes can be accessed via attribute access and list
    nodes should be handled differently. List nodes start with ``ls_``.

    Instances of this class can be retrieved by calling the exported ``wrap()``
    method:

    >>> device = FSDevice("127.0.0.1")
    >>> api = wrap(device)

    Standard nodes can be accessed and controlled with ease:

    >>> api.friendly_name
    'MEDION'
    >>> api.volume
    3
    >>> api.friendly_name = "MEDION2"
    >>> api.friendly_name
    'MEDION2'

    Inaccessable nodes or blocked nodes will return a ``None`` value and immutable
    nodes will raise an AttributeError on modification. List nodes behave special:

    >>> api.ls_eqpresets(_pos=4)
    [...]
    >>> api.ls_eqpresets = 1

    Use the assignment to select an item and the function call operator to query
    a range of items.
    """

    def __init__(self, device: FSDevice) -> None:
        self.__device = device

    @property
    def device(self) -> FSDevice:
        """The linked device"""
        if isinstance(self.__device, property):
            return self.__device.fget()
        elif isinstance(self.__device, t.Callable):
            return self.__device()
        return self.__device

    def get_field(self, name: str) -> APICall | ListAPICall:
        """Returns a field of this instance named by the provided string.

        :param name: the field's name
        :type name: str
        :return: the api call wrapper instance
        :rtype: APICall | ListAPICall
        """
        return getattr(self, name)

    # Standard API nodes
    friendly_name: _ac[str]     = APICall("netRemote.sys.info.friendlyName")
    dmr_uuid: _ac[str]          = APICall("netRemote.sys.info.dmruuid")
    radio_id: _ac[str]          = APICall("netRemote.sys.info.radioId")
    radio_pin: _ac[str]         = APICall("netRemote.sys.info.radioPin")
    serial_number: _ac[str]     = APICall("netRemote.sys.info.serialNumber")
    version: _ac[str]           = APICall("netRemote.sys.info.version")
    build_version: _ac[str]     = APICall("netRemote.sys.info.buildVersion")
    model_name: _ac[str]        = APICall("netRemote.sys.info.modelName")
    mode: _ac[int]              = APICall("netRemote.sys.mode")
    commit_changes: _ac[int]    = APICall("netRemote.sys.net.commitChanges")
    lang: _ac[int]              = APICall("netRemote.sys.lang")
    volume: _ac[int]            = APICall("netRemote.sys.audio.volume")
    mute: _ac[int]              = APICall("netRemote.sys.audio.mute")
    eq_preset: _ac[int]         = APICall("netRemote.sys.audio.eqPreset")
    eq_loudness: _ac[int]       = APICall("netRemote.sys.audio.eqLoudness")
    eq_custom_bass: _ac[int]    = APICall("netRemote.sys.audio.eqCustom.param0")
    eq_custom_trible: _ac[int]  = APICall("netRemote.sys.audio.eqCustom.param1")
    nav_num_items: _ac[int]     = APICall("netRemote.nav.numItems")
    play_rate: _ac[int]         = APICall("netRemote.play.rate")
    play_position: _ac[int]     = APICall("netRemote.play.position")
    frequency: _ac[int]         = APICall("netRemote.play.frequency")
    freq_upper_bound: _ac[int]  = APICall("netRemote.sys.caps.fmFreqRange.upper")
    freq_lower_bound: _ac[int]  = APICall("netRemote.sys.caps.fmFreqRange.lower")
    active_session: _ac[int]    = APICall("netRemote.sys.info.activeSession")
    trace_level: _ac[int]       = APICall("netRemote.misc.debug.traceLevel")

    delete_incident_report: _ac[int] = APICall("netRemote.debug.incidentReport.delete")
    create_incident_report: _ac[int] = APICall("netRemote.debug.incidentReport.create")
    last_incident_report: _ac[int]   = APICall("netRemote.debug.incidentReport.lastCreatedKey")

    power: _ac[IntEnumValue] = APICall("netRemote.sys.power")
    factory_reset: _ac[IntEnumValue] = APICall("netRemote.sys.factoryReset")
    nav_state: _ac[IntEnumValue] = APICall("netRemote.nav.state")
    nav_status: _ac[IntEnumValue] = APICall("netRemote.nav.status")
    play_control: _ac[IntEnumValue] = APICall("netRemote.play.control")
    play_repeat: _ac[IntEnumValue] = APICall("netRemote.play.repeat")
    play_shuffle: _ac[IntEnumValue] = APICall("netRemote.play.shuffle")
    shuffle_status: _ac[IntEnumValue] = APICall("netRemote.play.shuffleStatus")
    play_status: _ac[IntEnumValue] = APICall("netRemote.play.status")

    # List API nodes
    ls_eqpresets: _lac = ListAPICall("netRemote.sys.caps.eqPresets")
    ls_valid_modes: _lac = ListAPICall("netRemote.sys.caps.validModes")
    ls_nav_list: _lac = ListAPICall("netRemote.nav.list")
    ls_presets: _lac = ListAPICall("netRemote.nav.presets")
    ls_dab_freqs: _lac = ListAPICall("netRemote.sys.caps.dabFreqList")
    ls_eqbands: _lac = ListAPICall("netRemote.sys.caps.eqBands")
    ls_incident_reports: _lac = ListAPICall("netRemote.debug.incidentReport.list")
    ls_clock_sources: _lac = ListAPICall("netRemote.sys.caps.clockSourceList")
    ls_languages: _lac = ListAPICall("netRemote.sys.caps.validLang")
    ls_: _lac = ListAPICall("netRemote.sys.caps.clockSourceList")