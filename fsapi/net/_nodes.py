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
from .base import (
    Argument,
    ArgType,
    Node,
    NodeU8,
    NodeU16,
    NodeU32,
    NodeS16,
    NodeS32,
    NodeS8,
    NodeE8,
    NodeU,
    NodeC8,
    NodeList,
    dynamic,
)

# ============================================================================
# FSAPI + DAB Nodes:
#
# This python file defines ALL discovered FSAPI and DAB nodes defined as
# simple class structures. Each class contains an inner meta class with all
# important information.
#
# Currently, this script contains 337 Web FSAPI nodes and and 315 DAB nodes.
# Nodes specified in this file follow a specific naming convention:
#
#      - <path>_nt
#
# where path specifies the node path with its dots replaced by an underscore.
#
# NOTE: Nodes that extend the NodeList class and are not readonly, can be
# modified by using the key value of an item of that list.
#
# NOTE: There are some nodes that store a "dynamic" prototype. The return
# value will be one or a list of NodeValue objects storing the type and
# de-serialized value.
#
# IMPORTANT: Most of the documentation is available online, but some comments
# can be access via <node_class>.description
# ============================================================================


class netRemote_debug_incidentReport_list_nt(NodeList):
    class Meta:
        path = "netRemote.debug.incidentReport.list"
        name = "BaseDebugIncidentReportList"
        prototype = [
            Argument(name="uuid", length=100, type=ArgType.ARG_TYPE_C8),
            Argument(name="path", length=100, type=ArgType.ARG_TYPE_C8),
            Argument(name="time", length=100, type=ArgType.ARG_TYPE_C8),
            Argument(name="key", length=100, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_debug_incidentReport_lastCreatedKey_nt(NodeU8):
    class Meta:
        path = "netRemote.debug.incidentReport.lastCreatedKey"
        name = "BaseDebugIncidentReportLastCreatedKey"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_debug_incidentReport_delete_nt(NodeU8):
    class Meta:
        path = "netRemote.debug.incidentReport.delete"
        methods = ["SET"]
        name = "BaseDebugIncidentReportDelete"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_debug_incidentReport_create_nt(NodeU8):
    class Meta:
        path = "netRemote.debug.incidentReport.create"
        name = "BaseDebugIncidentReportCreate"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


### START GENERATED CONTENT ###
class netRemote_airplay_clearPassword_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.airplay.clearPassword"
        name = "BaseAirplayClearPassword"
        defaults = {0: "CLEAR"}
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]


class netRemote_airplay_setPassword_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.airplay.setPassword"
        name = "BaseAirplaySetPassword"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_avs_alarmVolume_nt(NodeU8):
    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.avs.alarmVolume"
        name = "BaseAvsAlarmVolume"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_avs_authcode_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.avs.authcode"
        name = "BaseAvsAuthcode"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_avs_hastoken_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.avs.hastoken"
        name = "BaseAvsHastoken"
        defaults = {0: "FALSE", 1: "TRUE"}
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]


class netRemote_avs_locale_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.avs.locale"
        name = "BaseAvsLocale"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_avs_logout_nt(NodeU8):
    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.avs.logout"
        name = "BaseAvsLogout"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_avs_metadata_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.avs.metadata"
        name = "BaseAvsMetadata"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_avs_productmetadata_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.avs.productmetadata"
        name = "BaseAvsProductmetadata"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_avs_token_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.avs.token"
        name = "BaseAvsToken"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_avs_validLocales_nt(NodeList):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.avs.validLocales"
        name = "BaseAvsValidLocales"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="name", length=50, type=ArgType.ARG_TYPE_C8),
            Argument(name="code", length=20, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_bluetooth_connectedDevices_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.bluetooth.connectedDevices"
        name = "BaseBluetoothConnectedDevices"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="deviceState", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="deviceName", length=65, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_bluetooth_connectedDevicesListVersion_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.bluetooth.connectedDevicesListVersion"
        name = "BaseBluetoothConnectedDevicesListVersion"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_bluetooth_discoverableState_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.bluetooth.discoverableState"
        name = "BaseBluetoothDiscoverableState"
        defaults = {0: "IDLE", 1: "DISCOVERABLE"}
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]


class netRemote_cast_appName_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.cast.appName"
        name = "BaseCastAppName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_cast_tos_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.cast.tos"
        name = "BaseCastTos"
        defaults = {0: "INACTIVE", 1: "ACTIVE", 2: "UNSET"}
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]


class netRemote_cast_usageReport_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.cast.usageReport"
        name = "BaseCastUsageReport"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "INACTIVE", 1: "ACTIVE"}


class netRemote_cast_version_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.cast.version"
        name = "BaseCastVersion"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_fsdca_authCode_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.fsdca.authCode"
        name = "BaseFsdcaAuthCode"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_fsdca_clientId_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.fsdca.clientId"
        name = "BaseFsdcaClientId"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_fsdca_disassociate_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.fsdca.disassociate"
        name = "BaseFsdcaDisassociate"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NO_REQUEST", 1: "DISSASOCIATE"}


class netRemote_fsdca_fsdcaId_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.fsdca.fsdcaId"
        name = "BaseFsdcaFsdcaId"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_fsdca_state_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.fsdca.state"
        name = "BaseFsdcaState"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "FSDCA_STATE_INITIAL",
            1: "FSDCA_STATE_NOT_ASSOCIATED",
            2: "FSDCA_STATE_AUTH_IN_PROGRESS",
            3: "FSDCA_STATE_CONNECTING",
            4: "FSDCA_STATE_CONNECTED",
            5: "FSDCA_STATE_WAITING",
        }


class netRemote_misc_fsDebug_component_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.misc.fsDebug.component"
        name = "BaseMiscFsDebugComponent"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_misc_fsDebug_traceLevel_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.misc.fsDebug.traceLevel"
        name = "BaseMiscFsDebugTraceLevel"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_misc_nvs_data_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.misc.nvs.data"
        name = "BaseMiscNvsData"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multichannel_primary_channelmask_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multichannel.primary.channelmask"
        name = "BaseMultichannelPrimaryChannelmask"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "NONE", 1: "LEFT", 2: "RIGHT", 3: "STEREO"}


class netRemote_multichannel_secondary0_channelmask_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multichannel.secondary0.channelmask"
        name = "BaseMultichannelSecondary0Channelmask"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "NONE", 1: "LEFT", 2: "RIGHT", 3: "STEREO"}


class netRemote_multichannel_secondary0_status_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multichannel.secondary0.status"
        name = "BaseMultichannelSecondary0Status"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "SYNCHRONISING", 1: "READY", 2: "INVALID"}


class netRemote_multichannel_system_addsecondary_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multichannel.system.addsecondary"
        name = "BaseMultichannelSystemAddsecondary"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multichannel_system_compatibilityid_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.multichannel.system.compatibilityid"
        name = "BaseMultichannelSystemCompatibilityid"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multichannel_system_create_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multichannel.system.create"
        name = "BaseMultichannelSystemCreate"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multichannel_system_id_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multichannel.system.id"
        name = "BaseMultichannelSystemId"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multichannel_system_name_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.multichannel.system.name"
        name = "BaseMultichannelSystemName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multichannel_system_removesecondary_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multichannel.system.removesecondary"
        name = "BaseMultichannelSystemRemovesecondary"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multichannel_system_state_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multichannel.system.state"
        name = "BaseMultichannelSystemState"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "INDEPENDENT", 1: "PRIMARY", 2: "SECONDARY"}


class netRemote_multichannel_system_unpair_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multichannel.system.unpair"
        name = "BaseMultichannelSystemUnpair"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "UNPAIR"}


class netRemote_multiroom_caps_maxClients_nt(NodeU8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.multiroom.caps.maxClients"
        name = "BaseMultiroomCapsMaxClients"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_multiroom_caps_protocolVersion_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.multiroom.caps.protocolVersion"
        name = "BaseMultiroomCapsProtocolVersion"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_multiroom_client_mute0_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.client.mute0"
        name = "BaseMultiroomClientMute0"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NOT_MUTE", 1: "MUTE"}


class netRemote_multiroom_client_mute1_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.client.mute1"
        name = "BaseMultiroomClientMute1"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NOT_MUTE", 1: "MUTE"}


class netRemote_multiroom_client_mute2_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.client.mute2"
        name = "BaseMultiroomClientMute2"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NOT_MUTE", 1: "MUTE"}


class netRemote_multiroom_client_mute3_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.client.mute3"
        name = "BaseMultiroomClientMute3"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NOT_MUTE", 1: "MUTE"}


class netRemote_multiroom_client_status0_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.client.status0"
        name = "BaseMultiroomClientStatus0"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM"}


class netRemote_multiroom_client_status1_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.client.status1"
        name = "BaseMultiroomClientStatus1"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM"}


class netRemote_multiroom_client_status2_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.client.status2"
        name = "BaseMultiroomClientStatus2"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM"}


class netRemote_multiroom_client_status3_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.client.status3"
        name = "BaseMultiroomClientStatus3"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM"}


class netRemote_multiroom_client_volume0_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.client.volume0"
        name = "BaseMultiroomClientVolume0"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_multiroom_client_volume1_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.client.volume1"
        name = "BaseMultiroomClientVolume1"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_multiroom_client_volume2_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.client.volume2"
        name = "BaseMultiroomClientVolume2"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_multiroom_client_volume3_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.client.volume3"
        name = "BaseMultiroomClientVolume3"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_multiroom_device_clientIndex_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.device.clientIndex"
        name = "BaseMultiroomDeviceClientIndex"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_multiroom_device_clientStatus_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.device.clientStatus"
        name = "BaseMultiroomDeviceClientStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM"}


class netRemote_multiroom_device_listAll_nt(NodeList):
    """Lists all other multiroom devices in the local network."""

    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.multiroom.device.listAll"
        name = "Multiroom: List Devices"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="UDN", length=256, type=ArgType.ARG_TYPE_C8),
            Argument(name="FriendlyName", length=256, type=ArgType.ARG_TYPE_C8),
            Argument(name="IPAddress", length=16, type=ArgType.ARG_TYPE_C8),
            Argument(name="AudioSyncVersion", length=11, type=ArgType.ARG_TYPE_C8),
            Argument(name="GroupId", length=37, type=ArgType.ARG_TYPE_C8),
            Argument(name="GroupName", length=256, type=ArgType.ARG_TYPE_C8),
            Argument(name="GroupRole", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="ClientNumber", length=1, type=ArgType.ARG_TYPE_U8),
            Argument(name="SystemId", length=37, type=ArgType.ARG_TYPE_C8),
            Argument(name="SystemRole", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="SystemName", length=256, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_multiroom_device_listAllVersion_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.device.listAllVersion"
        name = "BaseMultiroomDeviceListAllVersion"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_multiroom_device_serverStatus_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.device.serverStatus"
        name = "BaseMultiroomDeviceServerStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "STREAM_STARTING",
            1: "STREAM_PRESENTABLE",
            2: "STREAM_UNPRESENTABLE",
        }


class netRemote_multiroom_device_transportOptimisation_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multiroom.device.transportOptimisation"
        name = "BaseMultiroomDeviceTransportOptimisation"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "DISABLED", 1: "ENABLED"}


class netRemote_multiroom_group_addClient_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multiroom.group.addClient"
        name = "BaseMultiroomGroupAddClient"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multiroom_group_attachedClients_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.group.attachedClients"
        name = "BaseMultiroomGroupAttachedClients"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_multiroom_group_becomeServer_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.group.becomeServer"
        name = "BaseMultiroomGroupBecomeServer"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NO_GROUP", 1: "CLIENT", 2: "SERVER"}


class netRemote_multiroom_group_create_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multiroom.group.create"
        name = "BaseMultiroomGroupCreate"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multiroom_group_destroy_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multiroom.group.destroy"
        name = "BaseMultiroomGroupDestroy"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "DESTROY"}


class netRemote_multiroom_group_id_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.group.id"
        name = "BaseMultiroomGroupId"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multiroom_group_masterVolume_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.group.masterVolume"
        name = "BaseMultiroomGroupMasterVolume"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_multiroom_group_name_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.group.name"
        name = "BaseMultiroomGroupName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multiroom_group_removeClient_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.multiroom.group.removeClient"
        name = "BaseMultiroomGroupRemoveClient"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_multiroom_group_state_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.group.state"
        name = "BaseMultiroomGroupState"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NO_GROUP", 1: "CLIENT", 2: "SERVER"}


class netRemote_multiroom_group_streamable_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.multiroom.group.streamable"
        name = "BaseMultiroomGroupStreamable"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "FALSE", 1: "TRUE"}


class netRemote_multiroom_singlegroup_state_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.multiroom.singlegroup.state"
        name = "BaseMultiroomSinglegroupState"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "SINGLE", 1: "MULTIROOM"}


class netRemote_nav_action_context_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.action.context"
        name = "BaseNavActionContext"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_action_dabPrune_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.action.dabPrune"
        name = "BaseNavActionDabPrune"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "PRUNE"}


class netRemote_nav_action_dabScan_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.nav.action.dabScan"
        name = "BaseNavActionDabScan"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "SCAN"}


class netRemote_nav_action_navigate_nt(NodeU32):
    """
    Use this node to navigate through the internal directory structure of an
    attached storage. The maximum value will move the pointer to the next upper
    level.

    .. warning:: NAV state must be enabled to use this node.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        methods = ["SET"]
        path = "netRemote.nav.action.navigate"
        name = "NAV-Action: Navigate"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_action_selectItem_nt(NodeU32):
    """
    Open/ Select a file in the current directory. The selected value will
    open the item with the same item key.

    .. note::
        This command can't be used to move through map levels. It will only
        open the selected item if the item type is not a directory.

    .. warning:: NAV state must be enabled to use this node.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        methods = ["SET"]
        path = "netRemote.nav.action.selectItem"
        name = "BaseNavActionSelectItem"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_action_selectPreset_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.action.selectPreset"
        name = "BaseNavActionSelectPreset"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_amazonMpGetRating_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.nav.amazonMpGetRating"
        name = "BaseNavAmazonMpGetRating"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_nav_amazonMpLoginComplete_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.amazonMpLoginComplete"
        name = "BaseNavAmazonMpLoginComplete"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "FALSE", 1: "TRUE"}


class netRemote_nav_amazonMpLoginUrl_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.nav.amazonMpLoginUrl"
        name = "BaseNavAmazonMpLoginUrl"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_amazonMpSetRating_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.amazonMpSetRating"
        name = "BaseNavAmazonMpSetRating"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "POSITIVE", 1: "NEGATIVE"}


class netRemote_nav_browseMode_nt(NodeU32):
    class Meta:
        cacheable = True
        notifying = False
        readonly = False
        path = "netRemote.nav.browseMode"
        name = "BaseNavBrowseMode"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_caps_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.caps"
        name = "BaseNavCaps"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_context_depth_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.context.depth"
        name = "BaseNavContextDepth"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_nav_context_errorStr_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.context.errorStr"
        name = "BaseNavContextErrorStr"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_context_formData_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.context.formData"
        name = "BaseNavContextFormData"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_context_form_item_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.context.form.item"
        name = "BaseNavContextFormItem"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="formItemType", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="id", length=32, type=ArgType.ARG_TYPE_C8),
            Argument(name="label", length=32, type=ArgType.ARG_TYPE_C8),
            Argument(name="description", length=256, type=ArgType.ARG_TYPE_C8),
            Argument(name="optionsCount", length=1, type=ArgType.ARG_TYPE_U16),
        ]


class netRemote_nav_context_form_option_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.context.form.option"
        name = "BaseNavContextFormOption"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="name", length=32, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_nav_context_list_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.context.list"
        name = "BaseNavContextList"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="name", length=766, type=ArgType.ARG_TYPE_C8),
            Argument(name="type", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="subType", length=1, type=ArgType.ARG_TYPE_E8),
        ]


class netRemote_nav_context_navigate_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.context.navigate"
        name = "BaseNavContextNavigate"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_context_numItems_nt(NodeS32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.context.numItems"
        name = "BaseNavContextNumItems"
        prototype = [Argument(type=ArgType.ARG_TYPE_S32)]


class netRemote_nav_context_refresh_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.context.refresh"
        name = "BaseNavContextRefresh"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "FALSE", 1: "TRUE"}


class netRemote_nav_context_status_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.nav.context.status"
        name = "BaseNavContextStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "WAITING",
            1: "READY",
            2: "FAIL",
            3: "FATAL_ERR",
            4: "READY_ROOT",
        }


class netRemote_nav_currentTitle_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.currentTitle"
        name = "BaseNavCurrentTitle"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_dabScanUpdate_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.nav.dabScanUpdate"
        name = "BaseNavDabScanUpdate"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_depth_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.depth"
        name = "BaseNavDepth"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_nav_description_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.description"
        name = "BaseNavDescription"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_encFormData_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.encFormData"
        name = "BaseNavEncFormData"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_errorStr_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.errorStr"
        name = "BaseNavErrorStr"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_form_button_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.form.button"
        name = "BaseNavFormButton"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="name", length=32, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_nav_formData_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.formData"
        name = "BaseNavFormData"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_form_item_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.form.item"
        name = "BaseNavFormItem"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="formItemType", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="id", length=32, type=ArgType.ARG_TYPE_C8),
            Argument(name="label", length=32, type=ArgType.ARG_TYPE_C8),
            Argument(name="description", length=256, type=ArgType.ARG_TYPE_C8),
            Argument(name="optionsCount", length=1, type=ArgType.ARG_TYPE_U16),
        ]


class netRemote_nav_form_option_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.form.option"
        name = "BaseNavFormOption"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="name", length=32, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_nav_list_nt(NodeList):
    """
    This node returns the list of available items in the attached storage.

    .. warning:: NAV state must be enabled to use this node.

    There are three enums linked to the returned item structure, so we have to
    define them first:

    - ``type``: This field specifies the general file type.
        It is an enum field and accepts the following values:
        - ``0``: *"Directory"*
        - ``1``: *"PlayableItem"*
        - ``2``: *"SearchDirectory"*
        - ``3``: *"Unknown"*
        - ``4``: *"FormItem"*
        - ``5``: *"MessageItem"*
        - ``6``: *"AmazonLogin"*
        - ``7``: *"FetchErrItem"*

    - ``subtype``:
        This field is also an enum field:
        - ``0``: *"None"*
        - ``1``: *"Station"*
        - ``2``: *"Podcast"*
        - ``3``: *"Track"*
        - ``4``: *"Text"*
        - ``5``: *"Password"*
        - ``6``: *"Options"*
        - ``7``: *"Submit"*
        - ``8``: *"Button"*
        - ``9``: *"Disabled"*

    - ``graphicUri``: *TODO*
    - ``name``: the name of this item
    - ``artist``: *TODO*
    - ``contextMenu``: maybe whether the file is displayed in the context menu
        Also an enum definition:
        - ``0``: *"False"*
        - ``1``: *"True"*
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.list"
        name = "NAV: List"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="name", length=766, type=ArgType.ARG_TYPE_C8),
            Argument(name="type", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="subType", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="graphicUri", length=766, type=ArgType.ARG_TYPE_C8),
            Argument(name="artist", length=766, type=ArgType.ARG_TYPE_C8),
            Argument(name="contextMenu", length=1, type=ArgType.ARG_TYPE_E8),
        ]


class netRemote_nav_numItems_nt(NodeS32):
    """
    Returns the amount of items in the current folder of the attached
    storage device.

    .. warning:: NAV state must be enabled to use this node.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.numItems"
        name = "NAV: NumItems"
        prototype = [Argument(type=ArgType.ARG_TYPE_S32)]


class netRemote_nav_preset_currentPreset_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.nav.preset.currentPreset"
        name = "BaseNavPresetCurrentPreset"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_preset_delete_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.delete"
        name = "BaseNavPresetDelete"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_preset_download_artworkUrl_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.preset.download.artworkUrl"
        name = "BaseNavPresetDownloadArtworkUrl"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_preset_download_blob_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.preset.download.blob"
        name = "BaseNavPresetDownloadBlob"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_preset_download_download_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.download.download"
        name = "BaseNavPresetDownloadDownload"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_preset_download_name_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.preset.download.name"
        name = "BaseNavPresetDownloadName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_preset_download_type_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.preset.download.type"
        name = "BaseNavPresetDownloadType"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_preset_listversion_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.nav.preset.listversion"
        name = "BaseNavPresetListversion"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_presets_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.presets"
        name = "BaseNavPresets"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="name", length=65, type=ArgType.ARG_TYPE_C8),
            Argument(name="type", length=32, type=ArgType.ARG_TYPE_C8),
            Argument(name="uniqid", length=32, type=ArgType.ARG_TYPE_C8),
            Argument(name="blob", length=2064, type=ArgType.ARG_TYPE_C8),
            Argument(name="artworkUrl", length=512, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_nav_preset_swap_index1_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.swap.index1"
        name = "BaseNavPresetSwapIndex1"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_preset_swap_index2_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.swap.index2"
        name = "BaseNavPresetSwapIndex2"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_preset_swap_swap_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.swap.swap"
        name = "BaseNavPresetSwapSwap"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_preset_upload_artworkUrl_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.upload.artworkUrl"
        name = "BaseNavPresetUploadArtworkUrl"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_preset_upload_blob_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.upload.blob"
        name = "BaseNavPresetUploadBlob"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_preset_upload_name_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.upload.name"
        name = "BaseNavPresetUploadName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_preset_upload_type_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.upload.type"
        name = "BaseNavPresetUploadType"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_preset_upload_upload_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.preset.upload.upload"
        name = "BaseNavPresetUploadUpload"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_refresh_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.refresh"
        name = "BaseNavRefresh"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "FALSE", 1: "TRUE"}


class netRemote_nav_releaseDate_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.nav.releaseDate"
        name = "BaseNavReleaseDate"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_nav_searchTerm_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.searchTerm"
        name = "BaseNavSearchTerm"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_nav_state_nt(NodeE8):
    """
    Enables or diables the navigation state. To enable other nav commands, the
    ``nav.state`` needs to be set to one.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.nav.state"
        name = "NAV: State"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "OFF", 1: "ON"}


class netRemote_nav_status_nt(NodeE8):
    """
    When the unit is still loading, it's not possible to read the data. To prevent
    errors or invalid answers it's recommended to always check the status after
    changing the system.mode before sending new commands.
    """

    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.nav.status"
        name = "NAV: Status"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "WAITING",
            1: "READY",
            2: "FAIL",
            3: "FATAL_ERR",
            4: "READY_ROOT",
        }


class netRemote_platform_OEM_colorProduct_nt(NodeC8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.platform.OEM.colorProduct"
        name = "BasePlatformOEMColorProduct"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_platform_OEM_ledIntensity_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.platform.OEM.ledIntensity"
        name = "BasePlatformOEMLedIntensity"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_platform_OEM_ledIntensitySteps_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.platform.OEM.ledIntensitySteps"
        name = "BasePlatformOEMLedIntensitySteps"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_platform_softApUpdate_updateModeRequest_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.platform.softApUpdate.updateModeRequest"
        name = "BasePlatformSoftApUpdateUpdateModeRequest"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "START"}


class netRemote_platform_softApUpdate_updateModeStatus_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.platform.softApUpdate.updateModeStatus"
        name = "BasePlatformSoftApUpdateUpdateModeStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "STARTED"}


class netRemote_play_addPreset_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.play.addPreset"
        name = "BasePlayAddPreset"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_play_addPresetStatus_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.play.addPresetStatus"
        name = "BasePlayAddPresetStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "PRESET_STORRED", 1: "PRESET_NOT_STORRED"}


class netRemote_play_alerttone_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.play.alerttone"
        name = "BasePlayAlerttone"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "PLAY"}


class netRemote_play_caps_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.caps"
        name = "BasePlayCaps"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_play_ConcurencyResponse_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.play.ConcurencyResponse"
        name = "BasePlayConcurencyResponse"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "FALSE", 1: "TRUE"}


class netRemote_play_ConcurencyStr_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.ConcurencyStr"
        name = "BasePlayConcurencyStr"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_control_nt(NodeE8):
    """
    This node allows control over the current track. Please note the differencies
    of different unit states:

    - ``NEXT``:
        When used on "Media Player" mode, the next track will be selected and start
        playing. On "Radio" mode, the next higher frequency will be scanned for signals.

    - ``PREV``:
        The "Media Player" mode selects the next track and "Radio" mode scans for lower
        frequency signals.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.play.control"
        name = "Play: Control"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "STOP", 1: "PLAY", 2: "PAUSE", 3: "NEXT", 4: "PREVIOUS"}


class netRemote_play_errorStr_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.errorStr"
        name = "BasePlayErrorStr"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_feedback_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.play.feedback"
        name = "BasePlayFeedback"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "IDLE", 1: "POSITIVE", 2: "NEGATIVE"}


class netRemote_play_frequency_nt(NodeU32):
    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.play.frequency"
        name = "BasePlayFrequency"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_play_info_album_nt(NodeC8):
    """The name of the album of the current selected or playing track."""

    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.album"
        name = "Play-Info: Album"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_albumDescription_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.albumDescription"
        name = "BasePlayInfoAlbumDescription"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_artist_nt(NodeC8):
    """The name of the artist of the current selected or playing track."""

    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.artist"
        name = "Play-Info: Artist"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_artistDescription_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.artistDescription"
        name = "BasePlayInfoArtistDescription"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_description_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.description"
        name = "BasePlayInfoDescription"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_duration_nt(NodeU32):
    """
    The specific duration of the current selected or playing track can be retrieved with
    this command. This is helpful when the user is going to jump to a specific part of
    the track and doesn't want to send an invalid command.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.duration"
        name = "Play-Info: Duration"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_play_info_graphicUri_nt(NodeC8):
    """
    The device will automatically check if the current selected radio has a logo in the
    database and if possible returns the location.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.graphicUri"
        name = "Play-Info: Graphic URI"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_name_nt(NodeC8):
    """The name of the current selected or playing track."""

    class Meta:
        cacheable = True
        notifying = True
        readonly = True
        path = "netRemote.play.info.name"
        name = "Play-Info: Name"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_providerLogoUri_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.providerLogoUri"
        name = "BasePlayInfoProviderLogoUri"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_providerName_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.info.providerName"
        name = "BasePlayInfoProviderName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_info_text_nt(NodeC8):
    """
    The user can retrieve extra information of the track with this command
    or when the Ethernet radio is active, this command will retrieve the
    data that is showed on the display.
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = True
        path = "netRemote.play.info.text"
        name = "Play-Info: Text"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_NotificationMessage_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.play.NotificationMessage"
        name = "BasePlayNotificationMessage"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_play_position_nt(NodeU32):
    """
    In order to jump to a specific position within a playing track, this node can
    be utilized. Therefore, the range of this value is different for every track.

    .. note::
        The range of the value has no solid value, because the number of samples
        is different in every played track.

    .. hint::
        The maximum range of a track can be retrieved by using ``netRemote.play.duration``.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.play.position"
        name = "Play: Position"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_play_rate_nt(NodeS8):
    """
    With this node the user can control how the current track gets played. The possible
    range of the value this node accepts is from ``-127`` to ``127`` (signed Int8).

    - ``-127`` to ``-1``:
        When a negative value is provided, the music player will rewind the track. The
        rewind speed depends on the provided value. (-15 is faster than -3)

    - ``0``:
        This value stops the current track.

    - ``1``:
        The track will be resumed/ played with normal speed

    - ``2`` to ``127``:
        The track will be fast forwarded, where the speed also depends on the provided
        value.

    .. note::
        REWIND or FAST FORWARD is only activated for 1 track. When the track reaches the
        end, the music player will pause. The rate value has to be changed to 1 to either
        play the next track after FAST FORWARD or replay the same after REWIND. If you
        start the next or previous track via another command, the music player automatically
        sets the value to 1.
    """

    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.play.rate"
        name = "Play: Rate"
        prototype = [Argument(type=ArgType.ARG_TYPE_S8)]


class netRemote_play_rating_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.play.rating"
        name = "BasePlayRating"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "NEUTRAL", 1: "POSITIVE", 2: "NEGATIVE"}


class netRemote_play_repeat_nt(NodeE8):
    """
    This nodes controls the repeat mode of the target device. The "repeat" mode
    can take up to three states. The different values are listed below."""

    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.play.repeat"
        name = "Play: Repeat"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "OFF", 1: "REPEAT_ALL", 2: "REPEAT_ONE"}


class netRemote_play_scrobble_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.play.scrobble"
        name = "BasePlayScrobble"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "OFF", 1: "ON"}


class netRemote_play_serviceIds_dabEnsembleId_nt(NodeU16):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.play.serviceIds.dabEnsembleId"
        name = "BasePlayServiceIdsDabEnsembleId"
        prototype = [Argument(type=ArgType.ARG_TYPE_U16)]


class netRemote_play_serviceIds_dabScids_nt(NodeU8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.play.serviceIds.dabScids"
        name = "BasePlayServiceIdsDabScids"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_play_serviceIds_dabServiceId_nt(NodeU32):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.play.serviceIds.dabServiceId"
        name = "BasePlayServiceIdsDabServiceId"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_play_serviceIds_ecc_nt(NodeU8):
    class Meta:
        cacheable = True
        notifying = True
        readonly = True
        path = "netRemote.play.serviceIds.ecc"
        name = "BasePlayServiceIdsEcc"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_play_serviceIds_fmRdsPi_nt(NodeU16):
    class Meta:
        cacheable = True
        notifying = True
        readonly = True
        path = "netRemote.play.serviceIds.fmRdsPi"
        name = "BasePlayServiceIdsFmRdsPi"
        prototype = [Argument(type=ArgType.ARG_TYPE_U16)]


class netRemote_play_shuffle_nt(NodeE8):
    """
    This node controls the status of the music player shuffle mode. It can be
    activated (``1``) / deactivated (``0``).
    """

    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.play.shuffle"
        name = "Play: Shuffle"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "OFF", 1: "ON"}


class netRemote_play_shuffleStatus_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.play.shuffleStatus"
        name = "BasePlayShuffleStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "OK", 1: "SHUFFLING", 2: "TOO_MANY_ITEMS", 3: "UNSUPPORTED"}


class netRemote_play_signalStrength_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.play.signalStrength"
        name = "BasePlaySignalStrength"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_play_status_nt(NodeE8):
    """
    This node is readonly and returns the current status of the media player.
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = True
        path = "netRemote.play.status"
        name = "Play: Status"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "IDLE",
            1: "BUFFERING",
            2: "PLAYING",
            3: "PAUSED",
            4: "REBUFFERING",
            5: "ERROR",
            6: "STOPPED",
            7: "ERROR_POPUP",
        }


class netRemote_spotify_bitRate_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.spotify.bitRate"
        name = "BaseSpotifyBitRate"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_spotify_lastError_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.spotify.lastError"
        name = "BaseSpotifyLastError"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_spotify_loggedInState_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.spotify.loggedInState"
        name = "BaseSpotifyLoggedInState"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NOT_LOGGED_IN", 1: "LOGGED_IN"}


class netRemote_spotify_loginUsingOauthToken_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.spotify.loginUsingOauthToken"
        name = "BaseSpotifyLoginUsingOauthToken"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_spotify_playlist_name_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.spotify.playlist.name"
        name = "BaseSpotifyPlaylistName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_spotify_playlist_uri_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.spotify.playlist.uri"
        name = "BaseSpotifyPlaylistUri"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_spotify_status_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.spotify.status"
        name = "BaseSpotifyStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_spotify_username_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.spotify.username"
        name = "BaseSpotifyUsername"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_alarm_config_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.alarm.config"
        name = "BaseSysAlarmConfig"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="on", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="time", length=7, type=ArgType.ARG_TYPE_C8),
            Argument(name="duration", length=1, type=ArgType.ARG_TYPE_U8),
            Argument(name="source", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="preset", length=1, type=ArgType.ARG_TYPE_U8),
            Argument(name="repeat", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="date", length=9, type=ArgType.ARG_TYPE_C8),
            Argument(name="volume", length=1, type=ArgType.ARG_TYPE_U8),
        ]


class netRemote_sys_alarm_configChanged_nt(NodeS8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.sys.alarm.configChanged"
        name = "BaseSysAlarmConfigChanged"
        prototype = [Argument(type=ArgType.ARG_TYPE_S8)]


class netRemote_sys_alarm_current_nt(NodeS8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.alarm.current"
        name = "BaseSysAlarmCurrent"
        prototype = [Argument(type=ArgType.ARG_TYPE_S8)]


class netRemote_sys_alarm_duration_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.alarm.duration"
        name = "BaseSysAlarmDuration"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_alarm_snooze_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.alarm.snooze"
        name = "BaseSysAlarmSnooze"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_alarm_snoozing_nt(NodeU16):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.alarm.snoozing"
        name = "BaseSysAlarmSnoozing"
        prototype = [Argument(type=ArgType.ARG_TYPE_U16)]


class netRemote_sys_alarm_status_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.sys.alarm.status"
        name = "BaseSysAlarmStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "IDLE", 1: "ALARMING", 2: "SNOOZING"}


class netRemote_sys_audio_airableQuality_nt(NodeE8):
    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.airableQuality"
        name = "BaseSysAudioAirableQuality"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "LOW", 1: "NORMAL", 2: "HIGH"}


class netRemote_sys_audio_eqCustom_param0_nt(NodeS16):
    """
    The bass of the user EQ preset can be controlled with this node. The accepted
    values are in the range of -14 to +14.
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.eqCustom.param0"
        name = "SYS-Audio: EQ Param0 - Bass"
        prototype = [Argument(type=ArgType.ARG_TYPE_S16)]


class netRemote_sys_audio_eqCustom_param1_nt(NodeS16):
    """
    The treble of the user EQ preset can be controlled with this node. The accepted
    values are in the range of -14 to +14.
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.eqCustom.param1"
        name = "SYS-Audio: EQ Param1 - Treble"
        prototype = [Argument(type=ArgType.ARG_TYPE_S16)]


class netRemote_sys_audio_eqCustom_param2_nt(NodeS16):
    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.eqCustom.param2"
        name = "BaseSysAudioEqCustomParam2"
        prototype = [Argument(type=ArgType.ARG_TYPE_S16)]


class netRemote_sys_audio_eqCustom_param3_nt(NodeS16):
    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.eqCustom.param3"
        name = "BaseSysAudioEqCustomParam3"
        prototype = [Argument(type=ArgType.ARG_TYPE_S16)]


class netRemote_sys_audio_eqCustom_param4_nt(NodeS16):
    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.eqCustom.param4"
        name = "BaseSysAudioEqCustomParam4"
        prototype = [Argument(type=ArgType.ARG_TYPE_S16)]


class netRemote_sys_audio_eqLoudness_nt(NodeE8):
    """
    When the user-controllable EQ preset has been selected, its loudness can be
    controlled by this node.
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.eqLoudness"
        name = "SYS-Audio: EQ Loudness"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "OFF", 1: "ON"}


class netRemote_sys_audio_eqPreset_nt(NodeU8):
    """
    This node stores the currently selected EQ present. There are two different types
    of preset configurations.

    - ``My EQ`` at 0: individual user-configurable preset
    - ``Pre-Configured EQ`` from 1 to 8: the user can choose between preconfigured EQ presets

    However, below are all values known so far.:

    - ``0``: *"My EQ"*
    - ``1``: *"Normal"*
    - ``2``: *"Flat"*
    - ``3``: *"Jazz"*
    - ``4``: *"Rock"*
    - ``5``: *"Movie"*
    - ``6``: *"Classic"*
    - ``7``: *"Pop"*
    - ``8``: *"News"*
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.eqPreset"
        name = "SYS-Audio: EQ Preset"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_audio_extStaticDelay_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.audio.extStaticDelay"
        name = "BaseSysAudioExtStaticDelay"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_audio_mute_nt(NodeE8):
    """
    This node can be used to mute/unmute the target device.
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.mute"
        name = "SYS-Audio: Mute"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NOT_MUTE", 1: "MUTE"}


class netRemote_sys_audio_volume_nt(NodeU8):
    """Stores the current value of the valume.

    When the volume is set to the minimum value, it will activate the mute
    function. The allowed values are:

    - from ``1`` to ``32``
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.audio.volume"
        name = "SYS-Audio: Volume"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_caps_clockSourceList_nt(NodeList):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.clockSourceList"
        name = "BaseSysCapsClockSourceList"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="source", length=10, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_sys_caps_dabFreqList_nt(NodeList):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.dabFreqList"
        name = "BaseSysCapsDabFreqList"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="freq", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="label", length=8, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_sys_caps_eqBands_nt(NodeList):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.eqBands"
        name = "BaseSysCapsEqBands"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="label", length=32, type=ArgType.ARG_TYPE_C8),
            Argument(name="min", length=1, type=ArgType.ARG_TYPE_S16),
            Argument(name="max", length=1, type=ArgType.ARG_TYPE_S16),
        ]


class netRemote_sys_caps_eqPresets_nt(NodeList):
    """
    A list of available EQ presets can be fetched with this command.
    """

    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.eqPresets"
        name = "SYS-Caps: EQ Presets"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="label", length=32, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_sys_caps_extStaticDelayMax_nt(NodeU32):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.extStaticDelayMax"
        name = "BaseSysCapsExtStaticDelayMax"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_caps_fmFreqRange_lower_nt(NodeU32):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.fmFreqRange.lower"
        name = "BaseSysCapsFmFreqRangeLower"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_caps_fmFreqRange_stepSize_nt(NodeU32):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.fmFreqRange.stepSize"
        name = "BaseSysCapsFmFreqRangeStepSize"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_caps_fmFreqRange_upper_nt(NodeU32):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.fmFreqRange.upper"
        name = "BaseSysCapsFmFreqRangeUpper"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_caps_fsdca_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.fsdca"
        name = "BaseSysCapsFsdca"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_caps_utcSettingsList_nt(NodeList):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.utcSettingsList"
        name = "BaseSysCapsUtcSettingsList"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="time", length=1, type=ArgType.ARG_TYPE_S32),
            Argument(name="region", length=32, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_sys_caps_validLang_nt(NodeList):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.validLang"
        name = "BaseSysCapsValidLang"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="langLabel", length=32, type=ArgType.ARG_TYPE_C8),
        ]


class netRemote_sys_caps_validModes_nt(NodeList):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.validModes"
        name = "BaseSysCapsValidModes"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="id", length=8, type=ArgType.ARG_TYPE_C8),
            Argument(name="selectable", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="label", length=32, type=ArgType.ARG_TYPE_C8),
            Argument(name="streamable", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="modeType", length=1, type=ArgType.ARG_TYPE_E8),
        ]


class netRemote_sys_caps_volumeSteps_nt(NodeU8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.caps.volumeSteps"
        name = "BaseSysCapsVolumeSteps"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_cfg_irAutoPlayFlag_nt(NodeE8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = False
        path = "netRemote.sys.cfg.irAutoPlayFlag"
        name = "BaseSysCfgIrAutoPlayFlag"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "AUTOPLAY_ON", 1: "AUTOPLAY_OFF"}


class netRemote_sys_clock_dateFormat_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.clock.dateFormat"
        name = "BaseSysClockDateFormat"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "DATE_DD_MM_YYYY", 1: "DATE_MM_DD_YYYY"}


class netRemote_sys_clock_dst_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.clock.dst"
        name = "BaseSysClockDst"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "OFF", 1: "ON"}


class netRemote_sys_clock_localDate_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.sys.clock.localDate"
        name = "BaseSysClockLocalDate"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_clock_localTime_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.sys.clock.localTime"
        name = "BaseSysClockLocalTime"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_clock_mode_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.clock.mode"
        name = "BaseSysClockMode"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "_12_HOUR", 1: "_24_HOUR"}


class netRemote_sys_clock_source_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.clock.source"
        name = "BaseSysClockSource"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "MANUAL", 1: "DAB", 2: "FM", 3: "SNTP"}


class netRemote_sys_clock_timeZone_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.clock.timeZone"
        name = "BaseSysClockTimeZone"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_clock_utcOffset_nt(NodeS32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.clock.utcOffset"
        name = "BaseSysClockUtcOffset"
        prototype = [Argument(type=ArgType.ARG_TYPE_S32)]


class netRemote_sys_factoryReset_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.factoryReset"
        name = "BaseSysFactoryReset"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NONE", 1: "RESET"}


class netRemote_sys_info_activeSession_nt(NodeE8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.info.activeSession"
        name = "BaseSysInfoActiveSession"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NO", 1: "YES"}


class netRemote_sys_info_buildVersion_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.info.buildVersion"
        name = "BaseSysInfoBuildVersion"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_controllerName_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.info.controllerName"
        name = "BaseSysInfoControllerName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_dmruuid_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.info.dmruuid"
        name = "BaseSysInfoDmruuid"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_friendlyName_nt(NodeC8):
    """
    The friendly name can be used to make it easier to identify mulitple devices
    in the same network.
    """

    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.sys.info.friendlyName"
        name = "SYS-Info: Friendly Name"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_modelName_nt(NodeC8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.info.modelName"
        name = "BaseSysInfoModelName"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_netRemoteVendorId_nt(NodeC8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.info.netRemoteVendorId"
        name = "BaseSysInfoNetRemoteVendorId"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_radioId_nt(NodeC8):
    """Stores the radio identifier. (MAC Address)"""

    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.info.radioId"
        name = "SYS-Info: RadioID"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_radioPin_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.info.radioPin"
        name = "INFO: Radion PIN"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_radiotest_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.info.radiotest"
        name = "BaseSysInfoRadiotest"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_serialNumber_nt(NodeC8):
    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.info.serialNumber"
        name = "INFO: SerialNumber"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_info_version_nt(NodeC8):
    """
    A readonly node that can be used to dump the current firmware version. More
    information about the structure of a firmware version can be found in the
    details section below.

    *TODO: description of version*
    """

    class Meta:
        cacheable = True
        notifying = False
        readonly = True
        path = "netRemote.sys.info.version"
        name = "SYS-Info: Version"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_ipod_dockStatus_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.sys.ipod.dockStatus"
        name = "BaseSysIpodDockStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "NOT_DOCKED",
            1: "DOCKED_STILL_CONNECTING",
            2: "DOCKED_ONLINE_READY",
            3: "DOCKED_UNSUPPORTED_IPOD",
            4: "DOCKED_UNKNOWN_DEVICE",
        }


class netRemote_sys_isu_control_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.isu.control"
        name = "BaseSysIsuControl"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "UPDATE_FIRMWARE", 2: "CHECK_FOR_UPDATE"}


class netRemote_sys_isu_mandatory_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.isu.mandatory"
        name = "BaseSysIsuMandatory"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NO", 1: "YES"}


class netRemote_sys_isu_softwareUpdateProgress_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.isu.softwareUpdateProgress"
        name = "BaseSysIsuSoftwareUpdateProgress"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_isu_state_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = True
        path = "netRemote.sys.isu.state"
        name = "BaseSysIsuState"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "IDLE",
            1: "CHECK_IN_PROGRESS",
            2: "UPDATE_AVAILABLE",
            3: "UPDATE_NOT_AVAILABLE",
            4: "CHECK_FAILED",
        }


class netRemote_sys_isu_summary_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.isu.summary"
        name = "BaseSysIsuSummary"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_isu_version_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.isu.version"
        name = "BaseSysIsuVersion"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_lang_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.lang"
        name = "BaseSysLang"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_mode_nt(NodeU32):
    """The current system configuration.

    Allthough, this node has not been identified as an enum node, it can take the following
    values:

    - ``0``: *"Ethernet Radio"*
    - ``1``: *"Music Player"*
    - ``2``: *"FM Radio"*
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.mode"
        name = "SYS: Mode"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_net_commitChanges_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.commitChanges"
        name = "BaseSysNetCommitChanges"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NO", 1: "YES"}


class netRemote_sys_net_ipConfig_address_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.ipConfig.address"
        name = "BaseSysNetIpConfigAddress"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_net_ipConfig_dhcp_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.ipConfig.dhcp"
        name = "BaseSysNetIpConfigDhcp"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        __doc__ = "Enum node that tells you whether the device is using a DHCP server to retrieve its IP address."
        defaults = {0: "NO", 1: "YES"}


class netRemote_sys_net_ipConfig_dnsPrimary_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.ipConfig.dnsPrimary"
        name = "BaseSysNetIpConfigDnsPrimary"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_net_ipConfig_dnsSecondary_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.ipConfig.dnsSecondary"
        name = "BaseSysNetIpConfigDnsSecondary"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_net_ipConfig_gateway_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.ipConfig.gateway"
        name = "BaseSysNetIpConfigGateway"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_net_ipConfig_subnetMask_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.ipConfig.subnetMask"
        name = "BaseSysNetIpConfigSubnetMask"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_net_keepConnected_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.keepConnected"
        name = "BaseSysNetKeepConnected"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NO", 1: "YES"}


class netRemote_sys_net_uap_interfaceEnable_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.sys.net.uap.interfaceEnable"
        name = "BaseSysNetUapInterfaceEnable"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "INTERFACE_DISABLE", 1: "INTERFACE_ENABLE"}


class netRemote_sys_net_wired_interfaceEnable_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wired.interfaceEnable"
        name = "BaseSysNetWiredInterfaceEnable"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "INTERFACE_DISABLE", 1: "INTERFACE_ENABLE"}


class netRemote_sys_net_wired_macAddress_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.net.wired.macAddress"
        name = "BaseSysNetWiredMacAddress"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_net_wlan_activateProfile_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.activateProfile"
        name = "BaseSysNetWlanActivateProfile"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_net_wlan_connectedSSID_nt(NodeU):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.net.wlan.connectedSSID"
        name = "BaseSysNetWlanConnectedSSID"
        prototype = [Argument(type=ArgType.ARG_TYPE_U)]


class netRemote_sys_net_wlan_deactivateProfile_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.deactivateProfile"
        name = "BaseSysNetWlanDeactivateProfile"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_net_wlan_interfaceEnable_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.interfaceEnable"
        name = "BaseSysNetWlanInterfaceEnable"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "INTERFACE_DISABLE", 1: "INTERFACE_ENABLE"}


class netRemote_sys_net_wlan_macAddress_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.net.wlan.macAddress"
        name = "BaseSysNetWlanMacAddress"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_net_wlan_performFCC_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.performFCC"
        name = "BaseSysNetWlanPerformFCC"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "TEST_STOP", 1: "TEST_START"}


class netRemote_sys_net_wlan_performWPS_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.sys.net.wlan.performWPS"
        name = "BaseSysNetWlanPerformWPS"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "WPS_IDLE", 1: "WPS_PBC", 2: "WPS_PIN"}


class netRemote_sys_net_wlan_profiles_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.net.wlan.profiles"
        name = "BaseSysNetWlanProfiles"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="ssid", length=32, type=ArgType.ARG_TYPE_U8),
        ]


class netRemote_sys_net_wlan_region_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.region"
        name = "BaseSysNetWlanRegion"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "INVALID",
            1: "USA",
            2: "CANADA",
            3: "EUROPE",
            4: "SPAIN",
            5: "FRANCE",
            6: "JAPAN",
            7: "AUSTRALIA",
            8: "Reserved8",
        }


class netRemote_sys_net_wlan_regionFcc_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.net.wlan.regionFcc"
        name = "BaseSysNetWlanRegionFcc"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NOT_ACTIVE", 1: "ACTIVE"}


class netRemote_sys_net_wlan_removeProfile_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.removeProfile"
        name = "BaseSysNetWlanRemoveProfile"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_net_wlan_rssi_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.net.wlan.rssi"
        name = "BaseSysNetWlanRssi"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_net_wlan_scan_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.sys.net.wlan.scan"
        name = "BaseSysNetWlanScan"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "IDLE", 1: "SCAN"}


class netRemote_sys_net_wlan_scanList_nt(NodeList):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.net.wlan.scanList"
        name = "BaseSysNetWlanScanList"
        prototype = [
            Argument(name="key", length=1, type=ArgType.ARG_TYPE_U32),
            Argument(name="ssid", length=32, type=ArgType.ARG_TYPE_U8),
            Argument(name="privacy", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="wpsCapability", length=1, type=ArgType.ARG_TYPE_E8),
            Argument(name="rssi", length=1, type=ArgType.ARG_TYPE_U8),
        ]


class netRemote_sys_net_wlan_selectAP_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.selectAP"
        name = "BaseSysNetWlanSelectAP"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_net_wlan_selectProfile_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.selectProfile"
        name = "BaseSysNetWlanSelectProfile"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_net_wlan_setAuthType_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setAuthType"
        name = "BaseSysNetWlanSetAuthType"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "OPEN", 1: "PSK", 2: "WPA", 3: "WPA2"}


class netRemote_sys_net_wlan_setEncType_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setEncType"
        name = "BaseSysNetWlanSetEncType"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "NONE", 1: "WEP", 2: "TKIP", 3: "AES"}


class netRemote_sys_net_wlan_setFccTestChanNum_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setFccTestChanNum"
        name = "BaseSysNetWlanSetFccTestChanNum"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_net_wlan_setFccTestDataRate_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setFccTestDataRate"
        name = "BaseSysNetWlanSetFccTestDataRate"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {
            0: "_1M",
            1: "_2M",
            2: "_5_5M",
            3: "_11M",
            4: "_22M",
            5: "_6M",
            6: "_9M",
            7: "_12M",
            8: "_18M",
            9: "_24M",
            10: "_36M",
            11: "_48M",
            12: "_54M",
            13: "_72M",
        }


class netRemote_sys_net_wlan_setFccTestTxDataPattern_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setFccTestTxDataPattern"
        name = "BaseSysNetWlanSetFccTestTxDataPattern"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_net_wlan_setFccTestTxPower_nt(NodeU8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setFccTestTxPower"
        name = "BaseSysNetWlanSetFccTestTxPower"
        prototype = [Argument(type=ArgType.ARG_TYPE_U8)]


class netRemote_sys_net_wlan_setFccTxOff_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setFccTxOff"
        name = "BaseSysNetWlanSetFccTxOff"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "TX_ON", 1: "TX_OFF"}


class netRemote_sys_net_wlan_setPassphrase_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setPassphrase"
        name = "BaseSysNetWlanSetPassphrase"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_net_wlan_setSSID_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.net.wlan.setSSID"
        name = "BaseSysNetWlanSetSSID"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_net_wlan_wpsPinRead_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.net.wlan.wpsPinRead"
        name = "BaseSysNetWlanWpsPinRead"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_power_nt(NodeE8):
    """
    With this node the user is able to activate / deactivate the standby function of the
    device. "Standby" refers to a special mode where the output will be muted and the display
    deactivated.

    .. note::
        The ethernet or FM radio will select the last configuret item and automatically start
        playing
    """

    class Meta:
        cacheable = True
        notifying = True
        readonly = False
        path = "netRemote.sys.power"
        name = "SYS: Power"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "OFF", 1: "ON"}


class netRemote_sys_rsa_publicKey_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.rsa.publicKey"
        name = "BaseSysRsaPublicKey"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_sys_rsa_status_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = True
        path = "netRemote.sys.rsa.status"
        name = "BaseSysRsaStatus"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]

        defaults = {0: "GENERATION_IN_PROGRESS", 1: "KEY_AVAILABLE"}


class netRemote_sys_sleep_nt(NodeU32):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.sys.sleep"
        name = "BaseSysSleep"
        prototype = [Argument(type=ArgType.ARG_TYPE_U32)]


class netRemote_sys_state_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = True
        readonly = False
        path = "netRemote.sys.state"
        name = "BaseSysState"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "NORMAL_MODE", 1: "SAPU_MODE"}


class netRemote_test_iperf_commandLine_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.test.iperf.commandLine"
        name = "BaseTestIperfCommandLine"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_test_iperf_console_nt(NodeC8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.test.iperf.console"
        name = "BaseTestIperfConsole"
        prototype = [Argument(type=ArgType.ARG_TYPE_C8)]


class netRemote_test_iperf_execute_nt(NodeE8):
    class Meta:
        cacheable = False
        notifying = False
        readonly = False
        path = "netRemote.test.iperf.execute"
        name = "BaseTestIperfExecute"
        prototype = [Argument(type=ArgType.ARG_TYPE_E8)]
        defaults = {0: "STOP", 1: "START"}


class netremote_debug_astclient_debugstats_numduppkts_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numduppkts"
        name = "netremote.debug.astclient.debugstats.numduppkts"
        prototype = dynamic


class netremote_debug_astclient_debugstats_numextrarepeatrequests_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numextrarepeatrequests"
        name = "netremote.debug.astclient.debugstats.numextrarepeatrequests"
        prototype = dynamic


class netremote_debug_astclient_debugstats_numflush_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numflush"
        name = "netremote.debug.astclient.debugstats.numflush"
        prototype = dynamic


class netremote_debug_astclient_debugstats_numflushau_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numflushau"
        name = "netremote.debug.astclient.debugstats.numflushau"
        prototype = dynamic


class netremote_debug_astclient_debugstats_numlostpkts_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numlostpkts"
        name = "netremote.debug.astclient.debugstats.numlostpkts"
        prototype = dynamic


class netremote_debug_astclient_debugstats_numpktssentup_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numpktssentup"
        name = "netremote.debug.astclient.debugstats.numpktssentup"
        prototype = dynamic


class netremote_debug_astclient_debugstats_numrepeatrequests_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numrepeatrequests"
        name = "netremote.debug.astclient.debugstats.numrepeatrequests"
        prototype = dynamic


class netremote_debug_astclient_debugstats_numrxerrors_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numrxerrors"
        name = "netremote.debug.astclient.debugstats.numrxerrors"
        prototype = dynamic


class netremote_debug_astclient_debugstats_numrxok_nt(Node):
    class Meta:
        path = "netremote.debug.astclient.debugstats.numrxok"
        name = "netremote.debug.astclient.debugstats.numrxok"
        prototype = dynamic


class netremote_debug_astserver_debugstats_numcmdspropagated_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.debugstats.numcmdspropagated"
        name = "netremote.debug.astserver.debugstats.numcmdspropagated"
        prototype = dynamic


class netremote_debug_astserver_debugstats_numfsbscheduled_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.debugstats.numfsbscheduled"
        name = "netremote.debug.astserver.debugstats.numfsbscheduled"
        prototype = dynamic


class netremote_debug_astserver_debugstats_numfsbsunpresentable_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.debugstats.numfsbsunpresentable"
        name = "netremote.debug.astserver.debugstats.numfsbsunpresentable"
        prototype = dynamic


class netremote_debug_astserver_debugstats_numptsresets_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.debugstats.numptsresets"
        name = "netremote.debug.astserver.debugstats.numptsresets"
        prototype = dynamic


class netremote_debug_astserver_debugstats_numrepeatsfailed_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.debugstats.numrepeatsfailed"
        name = "netremote.debug.astserver.debugstats.numrepeatsfailed"
        prototype = dynamic


class netremote_debug_astserver_debugstats_numrepeatsqueued_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.debugstats.numrepeatsqueued"
        name = "netremote.debug.astserver.debugstats.numrepeatsqueued"
        prototype = dynamic


class netremote_debug_astserver_txdebugstats_numbufsqueuednormal_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.txdebugstats.numbufsqueuednormal"
        name = "netremote.debug.astserver.txdebugstats.numbufsqueuednormal"
        prototype = dynamic


class netremote_debug_astserver_txdebugstats_numbufsqueuedpriority_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.txdebugstats.numbufsqueuedpriority"
        name = "netremote.debug.astserver.txdebugstats.numbufsqueuedpriority"
        prototype = dynamic


class netremote_debug_astserver_txdebugstats_numbufssent_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.txdebugstats.numbufssent"
        name = "netremote.debug.astserver.txdebugstats.numbufssent"
        prototype = dynamic


class netremote_debug_astserver_txdebugstats_numflush_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.txdebugstats.numflush"
        name = "netremote.debug.astserver.txdebugstats.numflush"
        prototype = dynamic


class netremote_debug_astserver_txdebugstats_numpretxdelays_nt(Node):
    class Meta:
        path = "netremote.debug.astserver.txdebugstats.numpretxdelays"
        name = "netremote.debug.astserver.txdebugstats.numpretxdelays"
        prototype = dynamic


class netremote_debug_datarate_rxkbps_nt(Node):
    class Meta:
        path = "netremote.debug.datarate.rxkbps"
        name = "netremote.debug.datarate.rxkbps"
        prototype = dynamic


class netremote_debug_datarate_status_nt(Node):
    class Meta:
        path = "netremote.debug.datarate.status"
        name = "netremote.debug.datarate.status"
        prototype = dynamic


class netremote_debug_datarate_txkbps_nt(Node):
    class Meta:
        path = "netremote.debug.datarate.txkbps"
        name = "netremote.debug.datarate.txkbps"
        prototype = dynamic


class netremote_debug_debugdata_d0_nt(Node):
    class Meta:
        path = "netremote.debug.debugdata.d0"
        name = "netremote.debug.debugdata.d0"
        prototype = dynamic


class netremote_debug_debugdata_d1_nt(Node):
    class Meta:
        path = "netremote.debug.debugdata.d1"
        name = "netremote.debug.debugdata.d1"
        prototype = dynamic


class netremote_debug_debugdata_d2_nt(Node):
    class Meta:
        path = "netremote.debug.debugdata.d2"
        name = "netremote.debug.debugdata.d2"
        prototype = dynamic


class netremote_debug_debugdata_d3_nt(Node):
    class Meta:
        path = "netremote.debug.debugdata.d3"
        name = "netremote.debug.debugdata.d3"
        prototype = dynamic


class netremote_debug_debugdata_d4_nt(Node):
    class Meta:
        path = "netremote.debug.debugdata.d4"
        name = "netremote.debug.debugdata.d4"
        prototype = dynamic


class netremote_debug_debugdata_d5_nt(Node):
    class Meta:
        path = "netremote.debug.debugdata.d5"
        name = "netremote.debug.debugdata.d5"
        prototype = dynamic


class netremote_debug_debugdata_d6_nt(Node):
    class Meta:
        path = "netremote.debug.debugdata.d6"
        name = "netremote.debug.debugdata.d6"
        prototype = dynamic


class netremote_debug_debugdata_d7_nt(Node):
    class Meta:
        path = "netremote.debug.debugdata.d7"
        name = "netremote.debug.debugdata.d7"
        prototype = dynamic


class netremote_debug_freesocketnumber_nt(Node):
    class Meta:
        path = "netremote.debug.freesocketnumber"
        name = "netremote.debug.freesocketnumber"
        prototype = dynamic


class netremote_debug_fsdebugcompentries_nt(Node):
    class Meta:
        path = "netremote.debug.fsdebugcompentries"
        name = "netremote.debug.fsdebugcompentries"
        prototype = dynamic


class netremote_debug_fsdebugcompentriescomponent_nt(Node):
    class Meta:
        path = "netremote.debug.fsdebugcompentriescomponent"
        name = "netremote.debug.fsdebugcompentriescomponent"
        prototype = dynamic


class netremote_debug_fsdebugcompentriesinfoflags_nt(Node):
    class Meta:
        path = "netremote.debug.fsdebugcompentriesinfoflags"
        name = "netremote.debug.fsdebugcompentriesinfoflags"
        prototype = dynamic


class netremote_debug_fsdebugcompentriestracelevel_nt(Node):
    class Meta:
        path = "netremote.debug.fsdebugcompentriestracelevel"
        name = "netremote.debug.fsdebugcompentriestracelevel"
        prototype = dynamic


class netremote_debug_multichannel_mode_nt(Node):
    class Meta:
        path = "netremote.debug.multichannel.mode"
        name = "netremote.debug.multichannel.mode"
        prototype = dynamic


class netremote_debug_sntpclient_adjustlocaltime_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.adjustlocaltime"
        name = "netremote.debug.sntpclient.adjustlocaltime"
        prototype = dynamic


class netremote_debug_sntpclient_burstlength_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.burstlength"
        name = "netremote.debug.sntpclient.burstlength"
        prototype = dynamic


class netremote_debug_sntpclient_currentslewrate_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.currentslewrate"
        name = "netremote.debug.sntpclient.currentslewrate"
        prototype = dynamic


class netremote_debug_sntpclient_lastbestmeasurement_delta_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.lastbestmeasurement.delta"
        name = "netremote.debug.sntpclient.lastbestmeasurement.delta"
        prototype = dynamic


class netremote_debug_sntpclient_lastbestmeasurement_t_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.lastbestmeasurement.t"
        name = "netremote.debug.sntpclient.lastbestmeasurement.t"
        prototype = dynamic


class netremote_debug_sntpclient_lastbestmeasurement_theta_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.lastbestmeasurement.theta"
        name = "netremote.debug.sntpclient.lastbestmeasurement.theta"
        prototype = dynamic


class netremote_debug_sntpclient_measurements_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.measurements"
        name = "netremote.debug.sntpclient.measurements"
        prototype = dynamic


class netremote_debug_sntpclient_normalqueryperiod_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.normalqueryperiod"
        name = "netremote.debug.sntpclient.normalqueryperiod"
        prototype = dynamic


class netremote_debug_sntpclient_nummeasurements_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.nummeasurements"
        name = "netremote.debug.sntpclient.nummeasurements"
        prototype = dynamic


class netremote_debug_sntpclient_offsetjitter_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.offsetjitter"
        name = "netremote.debug.sntpclient.offsetjitter"
        prototype = dynamic


class netremote_debug_sntpclient_quickqueryperiod_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.quickqueryperiod"
        name = "netremote.debug.sntpclient.quickqueryperiod"
        prototype = dynamic


class netremote_debug_sntpclient_resyncclocks_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.resyncclocks"
        name = "netremote.debug.sntpclient.resyncclocks"
        prototype = dynamic


class netremote_debug_sntpclient_synchronisedwithmaster_nt(Node):
    class Meta:
        path = "netremote.debug.sntpclient.synchronisedwithmaster"
        name = "netremote.debug.sntpclient.synchronisedwithmaster"
        prototype = dynamic


class netremote_debug_sys_numi2sptsdisconts_nt(Node):
    class Meta:
        path = "netremote.debug.sys.numi2sptsdisconts"
        name = "netremote.debug.sys.numi2sptsdisconts"
        prototype = dynamic


class netremote_debug_sys_uptime_nt(Node):
    class Meta:
        path = "netremote.debug.sys.uptime"
        name = "netremote.debug.sys.uptime"
        prototype = dynamic


class netremote_misc_preset_dab_nt(Node):
    class Meta:
        path = "netremote.misc.preset.dab"
        name = "netremote.misc.preset.dab"
        prototype = dynamic


class netremote_misc_preset_fm_nt(Node):
    class Meta:
        path = "netremote.misc.preset.fm"
        name = "netremote.misc.preset.fm"
        prototype = dynamic


class netremote_spotify_latesterror_nt(Node):
    class Meta:
        path = "netremote.spotify.latesterror"
        name = "netremote.spotify.latesterror"
        prototype = dynamic


class netremote_spotify_password_nt(Node):
    class Meta:
        path = "netremote.spotify.password"
        name = "netremote.spotify.password"
        prototype = dynamic


### DAB NODES ###
class media_dmr_upnpfriendlyname_nt(Node):
    class Meta:
        path = "media.dmr.upnpfriendlyname"
        name = "media.dmr.upnpfriendlyname"
        prototype = dynamic


class media_dmr_transportstate_nt(Node):
    class Meta:
        path = "media.dmr.transportstate"
        name = "media.dmr.transportstate"
        prototype = dynamic


class media_dmr_seek_nt(Node):
    class Meta:
        path = "media.dmr.seek"
        name = "media.dmr.seek"
        prototype = dynamic


class media_dmr_uristate_nt(Node):
    class Meta:
        path = "media.dmr.uristate"
        name = "media.dmr.uristate"
        prototype = dynamic


class media_dmr_action_nt(Node):
    class Meta:
        path = "media.dmr.action"
        name = "media.dmr.action"
        prototype = dynamic


class media_dmr_state_nt(Node):
    class Meta:
        path = "media.dmr.state"
        name = "media.dmr.state"
        prototype = dynamic


class dev_data_data_nt(Node):
    class Meta:
        path = "dev.data.data"
        name = "dev.data.data"
        prototype = dynamic


class dev_data_addr_nt(Node):
    class Meta:
        path = "dev.data.addr"
        name = "dev.data.addr"
        prototype = dynamic


class dev_dab_slideshow_imagestore_nt(Node):
    class Meta:
        path = "dev.dab.slideshow.imagestore"
        name = "dev.dab.slideshow.imagestore"
        prototype = dynamic


class dev_dab_slideshow_source_nt(Node):
    class Meta:
        path = "dev.dab.slideshow.source"
        name = "dev.dab.slideshow.source"
        prototype = dynamic


class dev_fs_dirlist_nt(Node):
    class Meta:
        path = "dev.fs.dirlist"
        name = "dev.fs.dirlist"
        prototype = dynamic


class dev_fs_dirname_nt(Node):
    class Meta:
        path = "dev.fs.dirname"
        name = "dev.fs.dirname"
        prototype = dynamic


class dev_fs_state_nt(Node):
    class Meta:
        path = "dev.fs.state"
        name = "dev.fs.state"
        prototype = dynamic


class dev_kybrd_event_nt(Node):
    class Meta:
        path = "dev.kybrd.event"
        name = "dev.kybrd.event"
        prototype = dynamic


class dev_kybrd_state_nt(Node):
    class Meta:
        path = "dev.kybrd.state"
        name = "dev.kybrd.state"
        prototype = dynamic


class dev_tsc_consoleio_nt(Node):
    class Meta:
        path = "dev.tsc.consoleio"
        name = "dev.tsc.consoleio"
        prototype = dynamic


class dev_tsc_state_nt(Node):
    class Meta:
        path = "dev.tsc.state"
        name = "dev.tsc.state"
        prototype = dynamic


class dev_tft_pattern_nt(Node):
    class Meta:
        path = "dev.tft.pattern"
        name = "dev.tft.pattern"
        prototype = dynamic


class dev_tft_state_nt(Node):
    class Meta:
        path = "dev.tft.state"
        name = "dev.tft.state"
        prototype = dynamic


class dev_httpcache_cache_nt(Node):
    class Meta:
        path = "dev.httpcache.cache"
        name = "dev.httpcache.cache"
        prototype = dynamic


class dev_httpcache_request_nt(Node):
    class Meta:
        path = "dev.httpcache.request"
        name = "dev.httpcache.request"
        prototype = dynamic


class dev_iperf_consoleio_nt(Node):
    class Meta:
        path = "dev.iperf.consoleio"
        name = "dev.iperf.consoleio"
        prototype = dynamic


class dev_iperf_execute_nt(Node):
    class Meta:
        path = "dev.iperf.execute"
        name = "dev.iperf.execute"
        prototype = dynamic


class dev_iperf_cmdline_nt(Node):
    class Meta:
        path = "dev.iperf.cmdline"
        name = "dev.iperf.cmdline"
        prototype = dynamic


class dev_ping_consoleio_nt(Node):
    class Meta:
        path = "dev.ping.consoleio"
        name = "dev.ping.consoleio"
        prototype = dynamic


class dev_ping_execute_nt(Node):
    class Meta:
        path = "dev.ping.execute"
        name = "dev.ping.execute"
        prototype = dynamic


class dev_ping_cmdline_nt(Node):
    class Meta:
        path = "dev.ping.cmdline"
        name = "dev.ping.cmdline"
        prototype = dynamic


class dev_svg_eval_nt(Node):
    class Meta:
        path = "dev.svg.eval"
        name = "dev.svg.eval"
        prototype = dynamic


class dev_svg_callback_nt(Node):
    class Meta:
        path = "dev.svg.callback"
        name = "dev.svg.callback"
        prototype = dynamic


class dev_svg_debug_nt(Node):
    class Meta:
        path = "dev.svg.debug"
        name = "dev.svg.debug"
        prototype = dynamic


class dev_svg_url_nt(Node):
    class Meta:
        path = "dev.svg.url"
        name = "dev.svg.url"
        prototype = dynamic


class dev_svg_base_nt(Node):
    class Meta:
        path = "dev.svg.base"
        name = "dev.svg.base"
        prototype = dynamic


class dev_rf_controlch3_nt(Node):
    class Meta:
        path = "dev.rf.controlch3"
        name = "dev.rf.controlch3"
        prototype = dynamic


class dev_rf_register_nt(Node):
    class Meta:
        path = "dev.rf.register"
        name = "dev.rf.register"
        prototype = dynamic


class dev_fm_ifagc_nt(Node):
    class Meta:
        path = "dev.fm.ifagc"
        name = "dev.fm.ifagc"
        prototype = dynamic


class ipod_contextbutton_action_softtouch_nt(Node):
    class Meta:
        path = "ipod.contextbutton.action.softtouch"
        name = "ipod.contextbutton.action.softtouch"
        prototype = dynamic


class ipod_contextbutton_action_clear_nt(Node):
    class Meta:
        path = "ipod.contextbutton.action.clear"
        name = "ipod.contextbutton.action.clear"
        prototype = dynamic


class ipod_contextbutton_action_set_nt(Node):
    class Meta:
        path = "ipod.contextbutton.action.set"
        name = "ipod.contextbutton.action.set"
        prototype = dynamic


class ipod_metadata_playstatus_nt(Node):
    class Meta:
        path = "ipod.metadata.playstatus"
        name = "ipod.metadata.playstatus"
        prototype = dynamic


class ipod_metadata_album_nt(Node):
    class Meta:
        path = "ipod.metadata.album"
        name = "ipod.metadata.album"
        prototype = dynamic


class ipod_metadata_artist_nt(Node):
    class Meta:
        path = "ipod.metadata.artist"
        name = "ipod.metadata.artist"
        prototype = dynamic


class ipod_metadata_trackname_nt(Node):
    class Meta:
        path = "ipod.metadata.trackname"
        name = "ipod.metadata.trackname"
        prototype = dynamic


class ipod_metadata_trackpos_nt(Node):
    class Meta:
        path = "ipod.metadata.trackpos"
        name = "ipod.metadata.trackpos"
        prototype = dynamic


class ipod_metadata_tracklen_nt(Node):
    class Meta:
        path = "ipod.metadata.tracklen"
        name = "ipod.metadata.tracklen"
        prototype = dynamic


class ipod_modelnumber_nt(Node):
    class Meta:
        path = "ipod.modelnumber"
        name = "ipod.modelnumber"
        prototype = dynamic


class ipod_authstatus_nt(Node):
    class Meta:
        path = "ipod.authstatus"
        name = "ipod.authstatus"
        prototype = dynamic


class ipod_state_nt(Node):
    class Meta:
        path = "ipod.state"
        name = "ipod.state"
        prototype = dynamic


class debug_health_reset_nt(Node):
    class Meta:
        path = "debug.health.reset"
        name = "debug.health.reset"
        prototype = dynamic


class debug_health_stats_nt(Node):
    class Meta:
        path = "debug.health.stats"
        name = "debug.health.stats"
        prototype = dynamic


class io_keys_vol_nt(Node):
    class Meta:
        path = "io.keys.vol"
        name = "io.keys.vol"
        prototype = dynamic


class io_display_passivebacklight_nt(Node):
    class Meta:
        path = "io.display.passivebacklight"
        name = "io.display.passivebacklight"
        prototype = dynamic


class io_display_backlight_nt(Node):
    class Meta:
        path = "io.display.backlight"
        name = "io.display.backlight"
        prototype = dynamic


class io_display_screen_nt(Node):
    class Meta:
        path = "io.display.screen"
        name = "io.display.screen"
        prototype = dynamic


class io_adc_ch3_nt(Node):
    class Meta:
        path = "io.adc.ch3"
        name = "io.adc.ch3"
        prototype = dynamic


class io_adc_ch2_nt(Node):
    class Meta:
        path = "io.adc.ch2"
        name = "io.adc.ch2"
        prototype = dynamic


class io_adc_ch1_nt(Node):
    class Meta:
        path = "io.adc.ch1"
        name = "io.adc.ch1"
        prototype = dynamic


class io_adc_ch0_nt(Node):
    class Meta:
        path = "io.adc.ch0"
        name = "io.adc.ch0"
        prototype = dynamic


class media_direct_pandora_lastlistenacctsrcstation_nt(Node):
    class Meta:
        path = "media.direct.pandora.lastlistenacctsrcstation"
        name = "media.direct.pandora.lastlistenacctsrcstation"
        prototype = dynamic


class media_direct_lastfm_lastlistensrcurl_nt(Node):
    class Meta:
        path = "media.direct.lastfm.lastlistensrcurl"
        name = "media.direct.lastfm.lastlistensrcurl"
        prototype = dynamic


class media_direct_vtuner_uid_nt(Node):
    class Meta:
        path = "media.direct.vtuner.uid"
        name = "media.direct.vtuner.uid"
        prototype = dynamic


class media_direct_vtuner_subtype_nt(Node):
    class Meta:
        path = "media.direct.vtuner.subtype"
        name = "media.direct.vtuner.subtype"
        prototype = dynamic


class media_dpq_state_nt(Node):
    class Meta:
        path = "media.dpq.state"
        name = "media.dpq.state"
        prototype = dynamic


class media_dpq_action_play_nt(Node):
    class Meta:
        path = "media.dpq.action.play"
        name = "media.dpq.action.play"
        prototype = dynamic


class media_dpq_action_dpqremove_nt(Node):
    class Meta:
        path = "media.dpq.action.dpqremove"
        name = "media.dpq.action.dpqremove"
        prototype = dynamic


class media_dpq_list_nt(Node):
    class Meta:
        path = "media.dpq.list"
        name = "media.dpq.list"
        prototype = dynamic


class media_play_metadata_nt(Node):
    class Meta:
        path = "media.play.metadata"
        name = "media.play.metadata"
        prototype = dynamic


class media_play_lastfm_errorstate_nt(Node):
    class Meta:
        path = "media.play.lastfm.errorstate"
        name = "media.play.lastfm.errorstate"
        prototype = dynamic


class media_play_pandora_errorstate_nt(Node):
    class Meta:
        path = "media.play.pandora.errorstate"
        name = "media.play.pandora.errorstate"
        prototype = dynamic


class media_play_pandora_deletestation_nt(Node):
    class Meta:
        path = "media.play.pandora.deletestation"
        name = "media.play.pandora.deletestation"
        prototype = dynamic


class media_play_pandora_renamestation_nt(Node):
    class Meta:
        path = "media.play.pandora.renamestation"
        name = "media.play.pandora.renamestation"
        prototype = dynamic


class media_play_repeat_nt(Node):
    class Meta:
        path = "media.play.repeat"
        name = "media.play.repeat"
        prototype = dynamic


class media_play_shuffle_nt(Node):
    class Meta:
        path = "media.play.shuffle"
        name = "media.play.shuffle"
        prototype = dynamic


class media_play_position_nt(Node):
    class Meta:
        path = "media.play.position"
        name = "media.play.position"
        prototype = dynamic


class media_play_duration_nt(Node):
    class Meta:
        path = "media.play.duration"
        name = "media.play.duration"
        prototype = dynamic


class media_play_rate_nt(Node):
    class Meta:
        path = "media.play.rate"
        name = "media.play.rate"
        prototype = dynamic


class media_play_action_dpqadd_nt(Node):
    class Meta:
        path = "media.play.action.dpqadd"
        name = "media.play.action.dpqadd"
        prototype = dynamic


class media_play_action_pandora_trackcriteria_nt(Node):
    class Meta:
        path = "media.play.action.pandora.trackcriteria"
        name = "media.play.action.pandora.trackcriteria"
        prototype = dynamic


class media_play_action_pandora_requesttrackcriteria_nt(Node):
    class Meta:
        path = "media.play.action.pandora.requesttrackcriteria"
        name = "media.play.action.pandora.requesttrackcriteria"
        prototype = dynamic


class media_play_action_pandora_trackop_nt(Node):
    class Meta:
        path = "media.play.action.pandora.trackop"
        name = "media.play.action.pandora.trackop"
        prototype = dynamic


class media_play_action_lastfm_loveban_nt(Node):
    class Meta:
        path = "media.play.action.lastfm.loveban"
        name = "media.play.action.lastfm.loveban"
        prototype = dynamic


class media_play_action_scrobble_nt(Node):
    class Meta:
        path = "media.play.action.scrobble"
        name = "media.play.action.scrobble"
        prototype = dynamic


class media_play_action_favadd_nt(Node):
    class Meta:
        path = "media.play.action.favadd"
        name = "media.play.action.favadd"
        prototype = dynamic


class media_play_list_dmr_nt(Node):
    class Meta:
        path = "media.play.list.dmr"
        name = "media.play.list.dmr"
        prototype = dynamic


class media_play_list_dpq_nt(Node):
    class Meta:
        path = "media.play.list.dpq"
        name = "media.play.list.dpq"
        prototype = dynamic


class media_play_list_pandora_nt(Node):
    class Meta:
        path = "media.play.list.pandora"
        name = "media.play.list.pandora"
        prototype = dynamic


class media_play_list_lastfm_nt(Node):
    class Meta:
        path = "media.play.list.lastfm"
        name = "media.play.list.lastfm"
        prototype = dynamic


class media_play_list_upnp_nt(Node):
    class Meta:
        path = "media.play.list.upnp"
        name = "media.play.list.upnp"
        prototype = dynamic


class media_play_list_fsfs_nt(Node):
    class Meta:
        path = "media.play.list.fsfs"
        name = "media.play.list.fsfs"
        prototype = dynamic


class media_play_list_vtuner_nt(Node):
    class Meta:
        path = "media.play.list.vtuner"
        name = "media.play.list.vtuner"
        prototype = dynamic


class media_play_error_nt(Node):
    class Meta:
        path = "media.play.error"
        name = "media.play.error"
        prototype = dynamic


class media_play_state_nt(Node):
    class Meta:
        path = "media.play.state"
        name = "media.play.state"
        prototype = dynamic


class media_play_control_nt(Node):
    class Meta:
        path = "media.play.control"
        name = "media.play.control"
        prototype = dynamic


class media_play_source_nt(Node):
    class Meta:
        path = "media.play.source"
        name = "media.play.source"
        prototype = dynamic


class media_nav_title_nt(Node):
    class Meta:
        path = "media.nav.title"
        name = "media.nav.title"
        prototype = dynamic


class media_nav_pandora_newstationindex_nt(Node):
    class Meta:
        path = "media.nav.pandora.newstationindex"
        name = "media.nav.pandora.newstationindex"
        prototype = dynamic


class media_nav_pandora_errorstate_nt(Node):
    class Meta:
        path = "media.nav.pandora.errorstate"
        name = "media.nav.pandora.errorstate"
        prototype = dynamic


class media_nav_pandora_deletestation_nt(Node):
    class Meta:
        path = "media.nav.pandora.deletestation"
        name = "media.nav.pandora.deletestation"
        prototype = dynamic


class media_nav_pandora_renamestation_nt(Node):
    class Meta:
        path = "media.nav.pandora.renamestation"
        name = "media.nav.pandora.renamestation"
        prototype = dynamic


class media_nav_action_hibernate_nt(Node):
    class Meta:
        path = "media.nav.action.hibernate"
        name = "media.nav.action.hibernate"
        prototype = dynamic


class media_nav_action_dpqadd_nt(Node):
    class Meta:
        path = "media.nav.action.dpqadd"
        name = "media.nav.action.dpqadd"
        prototype = dynamic


class media_nav_action_favrem_nt(Node):
    class Meta:
        path = "media.nav.action.favrem"
        name = "media.nav.action.favrem"
        prototype = dynamic


class media_nav_action_favadd_nt(Node):
    class Meta:
        path = "media.nav.action.favadd"
        name = "media.nav.action.favadd"
        prototype = dynamic


class media_nav_action_play_nt(Node):
    class Meta:
        path = "media.nav.action.play"
        name = "media.nav.action.play"
        prototype = dynamic


class media_nav_action_navigate_nt(Node):
    class Meta:
        path = "media.nav.action.navigate"
        name = "media.nav.action.navigate"
        prototype = dynamic


class media_nav_azsearch_cancel_nt(Node):
    class Meta:
        path = "media.nav.azsearch.cancel"
        name = "media.nav.azsearch.cancel"
        prototype = dynamic


class media_nav_azsearch_pos_nt(Node):
    class Meta:
        path = "media.nav.azsearch.pos"
        name = "media.nav.azsearch.pos"
        prototype = dynamic


class media_nav_azsearch_term_nt(Node):
    class Meta:
        path = "media.nav.azsearch.term"
        name = "media.nav.azsearch.term"
        prototype = dynamic


class media_nav_search_term_nt(Node):
    class Meta:
        path = "media.nav.search.term"
        name = "media.nav.search.term"
        prototype = dynamic


class media_nav_lasterror_nt(Node):
    class Meta:
        path = "media.nav.lasterror"
        name = "media.nav.lasterror"
        prototype = dynamic


class media_nav_state_nt(Node):
    class Meta:
        path = "media.nav.state"
        name = "media.nav.state"
        prototype = dynamic


class media_nav_numitemsoffset_nt(Node):
    class Meta:
        path = "media.nav.numitemsoffset"
        name = "media.nav.numitemsoffset"
        prototype = dynamic


class media_nav_numitemslist_nt(Node):
    class Meta:
        path = "media.nav.numitemslist"
        name = "media.nav.numitemslist"
        prototype = dynamic


class media_nav_list_dmr_nt(Node):
    class Meta:
        path = "media.nav.list.dmr"
        name = "media.nav.list.dmr"
        prototype = dynamic


class media_nav_list_pandora_nt(Node):
    class Meta:
        path = "media.nav.list.pandora"
        name = "media.nav.list.pandora"
        prototype = dynamic


class media_nav_list_lastfm_nt(Node):
    class Meta:
        path = "media.nav.list.lastfm"
        name = "media.nav.list.lastfm"
        prototype = dynamic


class media_nav_list_upnp_nt(Node):
    class Meta:
        path = "media.nav.list.upnp"
        name = "media.nav.list.upnp"
        prototype = dynamic


class media_nav_list_fsfs_nt(Node):
    class Meta:
        path = "media.nav.list.fsfs"
        name = "media.nav.list.fsfs"
        prototype = dynamic


class media_nav_list_vtuner_nt(Node):
    class Meta:
        path = "media.nav.list.vtuner"
        name = "media.nav.list.vtuner"
        prototype = dynamic


class media_nav_list_common_nt(Node):
    class Meta:
        path = "media.nav.list.common"
        name = "media.nav.list.common"
        prototype = dynamic


class media_nav_source_nt(Node):
    class Meta:
        path = "media.nav.source"
        name = "media.nav.source"
        prototype = dynamic


class media_cfg_pandora_registrationurl_nt(Node):
    class Meta:
        path = "media.cfg.pandora.registrationurl"
        name = "media.cfg.pandora.registrationurl"
        prototype = dynamic


class media_cfg_pandora_registrationkey_nt(Node):
    class Meta:
        path = "media.cfg.pandora.registrationkey"
        name = "media.cfg.pandora.registrationkey"
        prototype = dynamic


class media_cfg_pandora_createprofilestate_nt(Node):
    class Meta:
        path = "media.cfg.pandora.createprofilestate"
        name = "media.cfg.pandora.createprofilestate"
        prototype = dynamic


class media_cfg_pandora_createprofile_nt(Node):
    class Meta:
        path = "media.cfg.pandora.createprofile"
        name = "media.cfg.pandora.createprofile"
        prototype = dynamic


class media_cfg_pandora_activeprofile_nt(Node):
    class Meta:
        path = "media.cfg.pandora.activeprofile"
        name = "media.cfg.pandora.activeprofile"
        prototype = dynamic


class media_cfg_pandora_profile_nt(Node):
    class Meta:
        path = "media.cfg.pandora.profile"
        name = "media.cfg.pandora.profile"
        prototype = dynamic


class media_cfg_lastfm_activeprofile_nt(Node):
    class Meta:
        path = "media.cfg.lastfm.activeprofile"
        name = "media.cfg.lastfm.activeprofile"
        prototype = dynamic


class media_cfg_lastfm_profile_nt(Node):
    class Meta:
        path = "media.cfg.lastfm.profile"
        name = "media.cfg.lastfm.profile"
        prototype = dynamic


class media_cfg_vtuner_startpoint_nt(Node):
    class Meta:
        path = "media.cfg.vtuner.startpoint"
        name = "media.cfg.vtuner.startpoint"
        prototype = dynamic


class media_cfg_vtuner_language_nt(Node):
    class Meta:
        path = "media.cfg.vtuner.language"
        name = "media.cfg.vtuner.language"
        prototype = dynamic


class media_cfg_cifs_password_nt(Node):
    class Meta:
        path = "media.cfg.cifs.password"
        name = "media.cfg.cifs.password"
        prototype = dynamic


class media_cfg_cifs_username_nt(Node):
    class Meta:
        path = "media.cfg.cifs.username"
        name = "media.cfg.cifs.username"
        prototype = dynamic


class media_cfg_factoryreset_nt(Node):
    class Meta:
        path = "media.cfg.factoryreset"
        name = "media.cfg.factoryreset"
        prototype = dynamic


class media_state_nt(Node):
    class Meta:
        path = "media.state"
        name = "media.state"
        prototype = dynamic


class net_lastadapter_nt(Node):
    class Meta:
        path = "net.lastadapter"
        name = "net.lastadapter"
        prototype = dynamic


class net_factoryreset_nt(Node):
    class Meta:
        path = "net.factoryreset"
        name = "net.factoryreset"
        prototype = dynamic


class net_wired_status_nt(Node):
    class Meta:
        path = "net.wired.status"
        name = "net.wired.status"
        prototype = dynamic


class net_wired_state_nt(Node):
    class Meta:
        path = "net.wired.state"
        name = "net.wired.state"
        prototype = dynamic


class net_wired_ipcurrent_dns2_nt(Node):
    class Meta:
        path = "net.wired.ipcurrent.dns2"
        name = "net.wired.ipcurrent.dns2"
        prototype = dynamic


class net_wired_ipcurrent_dns1_nt(Node):
    class Meta:
        path = "net.wired.ipcurrent.dns1"
        name = "net.wired.ipcurrent.dns1"
        prototype = dynamic


class net_wired_ipcurrent_gateway_nt(Node):
    class Meta:
        path = "net.wired.ipcurrent.gateway"
        name = "net.wired.ipcurrent.gateway"
        prototype = dynamic


class net_wired_ipcurrent_subnet_nt(Node):
    class Meta:
        path = "net.wired.ipcurrent.subnet"
        name = "net.wired.ipcurrent.subnet"
        prototype = dynamic


class net_wired_ipcurrent_addr_nt(Node):
    class Meta:
        path = "net.wired.ipcurrent.addr"
        name = "net.wired.ipcurrent.addr"
        prototype = dynamic


class net_wired_ipcurrent_dhcpenabled_nt(Node):
    class Meta:
        path = "net.wired.ipcurrent.dhcpenabled"
        name = "net.wired.ipcurrent.dhcpenabled"
        prototype = dynamic


class net_wired_mac_nt(Node):
    class Meta:
        path = "net.wired.mac"
        name = "net.wired.mac"
        prototype = dynamic


class net_wired_ip_listcfg_nt(Node):
    class Meta:
        path = "net.wired.ip.listcfg"
        name = "net.wired.ip.listcfg"
        prototype = dynamic


class net_wired_ip_stats_nt(Node):
    class Meta:
        path = "net.wired.ip.stats"
        name = "net.wired.ip.stats"
        prototype = dynamic


class net_wired_ip_list_nt(Node):
    class Meta:
        path = "net.wired.ip.list"
        name = "net.wired.ip.list"
        prototype = dynamic


class net_wired_config_enable_nt(Node):
    class Meta:
        path = "net.wired.config.enable"
        name = "net.wired.config.enable"
        prototype = dynamic


class net_wlan_status_nt(Node):
    class Meta:
        path = "net.wlan.status"
        name = "net.wlan.status"
        prototype = dynamic


class net_wlan_state_nt(Node):
    class Meta:
        path = "net.wlan.state"
        name = "net.wlan.state"
        prototype = dynamic


class net_wlan_ipcurrent_dns2_nt(Node):
    class Meta:
        path = "net.wlan.ipcurrent.dns2"
        name = "net.wlan.ipcurrent.dns2"
        prototype = dynamic


class net_wlan_ipcurrent_dns1_nt(Node):
    class Meta:
        path = "net.wlan.ipcurrent.dns1"
        name = "net.wlan.ipcurrent.dns1"
        prototype = dynamic


class net_wlan_ipcurrent_gateway_nt(Node):
    class Meta:
        path = "net.wlan.ipcurrent.gateway"
        name = "net.wlan.ipcurrent.gateway"
        prototype = dynamic


class net_wlan_ipcurrent_subnet_nt(Node):
    class Meta:
        path = "net.wlan.ipcurrent.subnet"
        name = "net.wlan.ipcurrent.subnet"
        prototype = dynamic


class net_wlan_ipcurrent_addr_nt(Node):
    class Meta:
        path = "net.wlan.ipcurrent.addr"
        name = "net.wlan.ipcurrent.addr"
        prototype = dynamic


class net_wlan_ipcurrent_dhcpenabled_nt(Node):
    class Meta:
        path = "net.wlan.ipcurrent.dhcpenabled"
        name = "net.wlan.ipcurrent.dhcpenabled"
        prototype = dynamic


class net_wlan_mac_nt(Node):
    class Meta:
        path = "net.wlan.mac"
        name = "net.wlan.mac"
        prototype = dynamic


class net_wlan_rssi_nt(Node):
    class Meta:
        path = "net.wlan.rssi"
        name = "net.wlan.rssi"
        prototype = dynamic


class net_wlan_ip_listcfg_nt(Node):
    class Meta:
        path = "net.wlan.ip.listcfg"
        name = "net.wlan.ip.listcfg"
        prototype = dynamic


class net_wlan_ip_stats_nt(Node):
    class Meta:
        path = "net.wlan.ip.stats"
        name = "net.wlan.ip.stats"
        prototype = dynamic


class net_wlan_ip_list_nt(Node):
    class Meta:
        path = "net.wlan.ip.list"
        name = "net.wlan.ip.list"
        prototype = dynamic


class net_wlan_scan_list_nt(Node):
    class Meta:
        path = "net.wlan.scan.list"
        name = "net.wlan.scan.list"
        prototype = dynamic


class net_wlan_scan_state_nt(Node):
    class Meta:
        path = "net.wlan.scan.state"
        name = "net.wlan.scan.state"
        prototype = dynamic


class net_wlan_config_wpspinread_nt(Node):
    class Meta:
        path = "net.wlan.config.wpspinread"
        name = "net.wlan.config.wpspinread"
        prototype = dynamic


class net_wlan_config_listcfg_nt(Node):
    class Meta:
        path = "net.wlan.config.listcfg"
        name = "net.wlan.config.listcfg"
        prototype = dynamic


class net_wlan_config_region_nt(Node):
    class Meta:
        path = "net.wlan.config.region"
        name = "net.wlan.config.region"
        prototype = dynamic


class net_wlan_config_enable_nt(Node):
    class Meta:
        path = "net.wlan.config.enable"
        name = "net.wlan.config.enable"
        prototype = dynamic


class net_wlan_config_remove_nt(Node):
    class Meta:
        path = "net.wlan.config.remove"
        name = "net.wlan.config.remove"
        prototype = dynamic


class net_wlan_config_list_nt(Node):
    class Meta:
        path = "net.wlan.config.list"
        name = "net.wlan.config.list"
        prototype = dynamic


class net_state_nt(Node):
    class Meta:
        path = "net.state"
        name = "net.state"
        prototype = dynamic


class pt_ethernet_loopback_status_nt(Node):
    class Meta:
        path = "pt.ethernet.loopback.status"
        name = "pt.ethernet.loopback.status"
        prototype = dynamic


class pt_ethernet_loopback_execute_nt(Node):
    class Meta:
        path = "pt.ethernet.loopback.execute"
        name = "pt.ethernet.loopback.execute"
        prototype = dynamic


class pt_sdram_test_addressbus_nt(Node):
    class Meta:
        path = "pt.sdram.test.addressbus"
        name = "pt.sdram.test.addressbus"
        prototype = dynamic


class pt_sdram_test_databus_nt(Node):
    class Meta:
        path = "pt.sdram.test.databus"
        name = "pt.sdram.test.databus"
        prototype = dynamic


class pt_debug_value_nt(Node):
    class Meta:
        path = "pt.debug.value"
        name = "pt.debug.value"
        prototype = dynamic


class pt_debug_address_nt(Node):
    class Meta:
        path = "pt.debug.address"
        name = "pt.debug.address"
        prototype = dynamic


class pt_core_misc_usbtestmode_nt(Node):
    class Meta:
        path = "pt.core.misc.usbtestmode"
        name = "pt.core.misc.usbtestmode"
        prototype = dynamic


class pt_core_wifi_regbb_nt(Node):
    class Meta:
        path = "pt.core.wifi.regbb"
        name = "pt.core.wifi.regbb"
        prototype = dynamic


class pt_core_wifi_regrf_nt(Node):
    class Meta:
        path = "pt.core.wifi.regrf"
        name = "pt.core.wifi.regrf"
        prototype = dynamic


class pt_core_wifi_regmac_nt(Node):
    class Meta:
        path = "pt.core.wifi.regmac"
        name = "pt.core.wifi.regmac"
        prototype = dynamic


class pt_core_wifi_macaddr_nt(Node):
    class Meta:
        path = "pt.core.wifi.macaddr"
        name = "pt.core.wifi.macaddr"
        prototype = dynamic


class pt_core_wifi_txpower_nt(Node):
    class Meta:
        path = "pt.core.wifi.txpower"
        name = "pt.core.wifi.txpower"
        prototype = dynamic


class pt_core_wifi_txmodulation_nt(Node):
    class Meta:
        path = "pt.core.wifi.txmodulation"
        name = "pt.core.wifi.txmodulation"
        prototype = dynamic


class pt_core_wifi_txdutycycle_nt(Node):
    class Meta:
        path = "pt.core.wifi.txdutycycle"
        name = "pt.core.wifi.txdutycycle"
        prototype = dynamic


class pt_core_wifi_txpayload_nt(Node):
    class Meta:
        path = "pt.core.wifi.txpayload"
        name = "pt.core.wifi.txpayload"
        prototype = dynamic


class pt_core_wifi_txpktcount_nt(Node):
    class Meta:
        path = "pt.core.wifi.txpktcount"
        name = "pt.core.wifi.txpktcount"
        prototype = dynamic


class pt_core_wifi_txpktlength_nt(Node):
    class Meta:
        path = "pt.core.wifi.txpktlength"
        name = "pt.core.wifi.txpktlength"
        prototype = dynamic


class pt_core_wifi_txdatarate_nt(Node):
    class Meta:
        path = "pt.core.wifi.txdatarate"
        name = "pt.core.wifi.txdatarate"
        prototype = dynamic


class pt_core_wifi_channel_nt(Node):
    class Meta:
        path = "pt.core.wifi.channel"
        name = "pt.core.wifi.channel"
        prototype = dynamic


class pt_core_wifi_rxcounts_nt(Node):
    class Meta:
        path = "pt.core.wifi.rxcounts"
        name = "pt.core.wifi.rxcounts"
        prototype = dynamic


class pt_core_wifi_rssi_nt(Node):
    class Meta:
        path = "pt.core.wifi.rssi"
        name = "pt.core.wifi.rssi"
        prototype = dynamic


class pt_core_wifi_bssid_nt(Node):
    class Meta:
        path = "pt.core.wifi.bssid"
        name = "pt.core.wifi.bssid"
        prototype = dynamic


class pt_core_wifi_testmode_nt(Node):
    class Meta:
        path = "pt.core.wifi.testmode"
        name = "pt.core.wifi.testmode"
        prototype = dynamic


class pt_core_swreboot_nt(Node):
    class Meta:
        path = "pt.core.swreboot"
        name = "pt.core.swreboot"
        prototype = dynamic


class pt_core_flash_value_nt(Node):
    class Meta:
        path = "pt.core.flash.value"
        name = "pt.core.flash.value"
        prototype = dynamic


class pt_core_flash_location_nt(Node):
    class Meta:
        path = "pt.core.flash.location"
        name = "pt.core.flash.location"
        prototype = dynamic


class pt_core_memory_value_nt(Node):
    class Meta:
        path = "pt.core.memory.value"
        name = "pt.core.memory.value"
        prototype = dynamic


class pt_core_memory_location_nt(Node):
    class Meta:
        path = "pt.core.memory.location"
        name = "pt.core.memory.location"
        prototype = dynamic


class pt_core_dab_reselectionstate_nt(Node):
    class Meta:
        path = "pt.core.dab.reselectionstate"
        name = "pt.core.dab.reselectionstate"
        prototype = dynamic


class pt_core_dab_ber_nt(Node):
    class Meta:
        path = "pt.core.dab.ber"
        name = "pt.core.dab.ber"
        prototype = dynamic


class pt_core_dab_station_nt(Node):
    class Meta:
        path = "pt.core.dab.station"
        name = "pt.core.dab.station"
        prototype = dynamic


class misc_ipod_dockstatus_nt(Node):
    class Meta:
        path = "misc.ipod.dockstatus"
        name = "misc.ipod.dockstatus"
        prototype = dynamic


class misc_nvs_value_nt(Node):
    class Meta:
        path = "misc.nvs.value"
        name = "misc.nvs.value"
        prototype = dynamic


class misc_nvs_factoryreset_nt(Node):
    class Meta:
        path = "misc.nvs.factoryreset"
        name = "misc.nvs.factoryreset"
        prototype = dynamic


class misc_alarm_status_nt(Node):
    class Meta:
        path = "misc.alarm.status"
        name = "misc.alarm.status"
        prototype = dynamic


class misc_alarm_config_nt(Node):
    class Meta:
        path = "misc.alarm.config"
        name = "misc.alarm.config"
        prototype = dynamic


class misc_alarm_factoryreset_nt(Node):
    class Meta:
        path = "misc.alarm.factoryreset"
        name = "misc.alarm.factoryreset"
        prototype = dynamic


class misc_usb_status_nt(Node):
    class Meta:
        path = "misc.usb.status"
        name = "misc.usb.status"
        prototype = dynamic


class misc_usb_state_nt(Node):
    class Meta:
        path = "misc.usb.state"
        name = "misc.usb.state"
        prototype = dynamic


class misc_preset_lastlisten_nt(Node):
    class Meta:
        path = "misc.preset.lastlisten"
        name = "misc.preset.lastlisten"
        prototype = dynamic


class misc_preset_vtuner_nt(Node):
    class Meta:
        path = "misc.preset.vtuner"
        name = "misc.preset.vtuner"
        prototype = dynamic


class misc_preset_fm_nt(Node):
    class Meta:
        path = "misc.preset.fm"
        name = "misc.preset.fm"
        prototype = dynamic


class misc_preset_dab_nt(Node):
    class Meta:
        path = "misc.preset.dab"
        name = "misc.preset.dab"
        prototype = dynamic


class misc_clock_local_daylightsaving_nt(Node):
    class Meta:
        path = "misc.clock.local.daylightsaving"
        name = "misc.clock.local.daylightsaving"
        prototype = dynamic


class misc_clock_local_utcoffset_nt(Node):
    class Meta:
        path = "misc.clock.local.utcoffset"
        name = "misc.clock.local.utcoffset"
        prototype = dynamic


class misc_clock_source_nt(Node):
    class Meta:
        path = "misc.clock.source"
        name = "misc.clock.source"
        prototype = dynamic


class misc_clock_localdate_nt(Node):
    class Meta:
        path = "misc.clock.localdate"
        name = "misc.clock.localdate"
        prototype = dynamic


class misc_clock_localtime_nt(Node):
    class Meta:
        path = "misc.clock.localtime"
        name = "misc.clock.localtime"
        prototype = dynamic


class audio_auxin_state_nt(Node):
    class Meta:
        path = "audio.auxin.state"
        name = "audio.auxin.state"
        prototype = dynamic


class audio_volume_nt(Node):
    class Meta:
        path = "audio.volume"
        name = "audio.volume"
        prototype = dynamic


class audio_equalizer_nt(Node):
    class Meta:
        path = "audio.equalizer"
        name = "audio.equalizer"
        prototype = dynamic


class audio_status_nt(Node):
    class Meta:
        path = "audio.status"
        name = "audio.status"
        prototype = dynamic


class audio_loudness_nt(Node):
    class Meta:
        path = "audio.loudness"
        name = "audio.loudness"
        prototype = dynamic


class audio_bass_nt(Node):
    class Meta:
        path = "audio.bass"
        name = "audio.bass"
        prototype = dynamic


class audio_flags_nt(Node):
    class Meta:
        path = "audio.flags"
        name = "audio.flags"
        prototype = dynamic


class audio_treble_nt(Node):
    class Meta:
        path = "audio.treble"
        name = "audio.treble"
        prototype = dynamic


class audio_systemmute_nt(Node):
    class Meta:
        path = "audio.systemmute"
        name = "audio.systemmute"
        prototype = dynamic


class audio_power_nt(Node):
    class Meta:
        path = "audio.power"
        name = "audio.power"
        prototype = dynamic


class audio_buzzer_rightfrequency_nt(Node):
    class Meta:
        path = "audio.buzzer.rightfrequency"
        name = "audio.buzzer.rightfrequency"
        prototype = dynamic


class audio_buzzer_leftfrequency_nt(Node):
    class Meta:
        path = "audio.buzzer.leftfrequency"
        name = "audio.buzzer.leftfrequency"
        prototype = dynamic


class audio_buzzer_type_nt(Node):
    class Meta:
        path = "audio.buzzer.type"
        name = "audio.buzzer.type"
        prototype = dynamic


class audio_buzzer_frequency_nt(Node):
    class Meta:
        path = "audio.buzzer.frequency"
        name = "audio.buzzer.frequency"
        prototype = dynamic


class audio_buzzer_state_nt(Node):
    class Meta:
        path = "audio.buzzer.state"
        name = "audio.buzzer.state"
        prototype = dynamic


class audio_mute_nt(Node):
    class Meta:
        path = "audio.mute"
        name = "audio.mute"
        prototype = dynamic


class audio_attenuation_nt(Node):
    class Meta:
        path = "audio.attenuation"
        name = "audio.attenuation"
        prototype = dynamic


class audio_drcscale_nt(Node):
    class Meta:
        path = "audio.drcscale"
        name = "audio.drcscale"
        prototype = dynamic


class audio_drcstatus_nt(Node):
    class Meta:
        path = "audio.drcstatus"
        name = "audio.drcstatus"
        prototype = dynamic


class audio_audiostatus_nt(Node):
    class Meta:
        path = "audio.audiostatus"
        name = "audio.audiostatus"
        prototype = dynamic


class audio_codec_nt(Node):
    class Meta:
        path = "audio.codec"
        name = "audio.codec"
        prototype = dynamic


class audio_bitrate_nt(Node):
    class Meta:
        path = "audio.bitrate"
        name = "audio.bitrate"
        prototype = dynamic


class audio_samplerate_nt(Node):
    class Meta:
        path = "audio.samplerate"
        name = "audio.samplerate"
        prototype = dynamic


class audio_factoryreset_nt(Node):
    class Meta:
        path = "audio.factoryreset"
        name = "audio.factoryreset"
        prototype = dynamic


class fm_stereohysteresis_nt(Node):
    class Meta:
        path = "fm.stereohysteresis"
        name = "fm.stereohysteresis"
        prototype = dynamic


class fm_stereoturnofflevel_nt(Node):
    class Meta:
        path = "fm.stereoturnofflevel"
        name = "fm.stereoturnofflevel"
        prototype = dynamic


class fm_rds_groupdata_nt(Node):
    class Meta:
        path = "fm.rds.groupdata"
        name = "fm.rds.groupdata"
        prototype = dynamic


class fm_rds_pi_nt(Node):
    class Meta:
        path = "fm.rds.pi"
        name = "fm.rds.pi"
        prototype = dynamic


class fm_rds_ct_nt(Node):
    class Meta:
        path = "fm.rds.ct"
        name = "fm.rds.ct"
        prototype = dynamic


class fm_rds_radiotext_nt(Node):
    class Meta:
        path = "fm.rds.radiotext"
        name = "fm.rds.radiotext"
        prototype = dynamic


class fm_rds_pty_nt(Node):
    class Meta:
        path = "fm.rds.pty"
        name = "fm.rds.pty"
        prototype = dynamic


class fm_rds_ps_nt(Node):
    class Meta:
        path = "fm.rds.ps"
        name = "fm.rds.ps"
        prototype = dynamic


class fm_rds_active_nt(Node):
    class Meta:
        path = "fm.rds.active"
        name = "fm.rds.active"
        prototype = dynamic


class fm_tunestatus_nt(Node):
    class Meta:
        path = "fm.tunestatus"
        name = "fm.tunestatus"
        prototype = dynamic


class fm_forcetomono_nt(Node):
    class Meta:
        path = "fm.forcetomono"
        name = "fm.forcetomono"
        prototype = dynamic


class fm_signalstrength_nt(Node):
    class Meta:
        path = "fm.signalstrength"
        name = "fm.signalstrength"
        prototype = dynamic


class fm_searchlevel_nt(Node):
    class Meta:
        path = "fm.searchlevel"
        name = "fm.searchlevel"
        prototype = dynamic


class fm_search_nt(Node):
    class Meta:
        path = "fm.search"
        name = "fm.search"
        prototype = dynamic


class fm_frequency_nt(Node):
    class Meta:
        path = "fm.frequency"
        name = "fm.frequency"
        prototype = dynamic


class fm_factoryreset_nt(Node):
    class Meta:
        path = "fm.factoryreset"
        name = "fm.factoryreset"
        prototype = dynamic


class fm_state_nt(Node):
    class Meta:
        path = "fm.state"
        name = "fm.state"
        prototype = dynamic


class dab_sl_ucomponent_nt(Node):
    class Meta:
        path = "dab.sl.ucomponent"
        name = "dab.sl.ucomponent"
        prototype = dynamic


class dab_sl_uservice_nt(Node):
    class Meta:
        path = "dab.sl.uservice"
        name = "dab.sl.uservice"
        prototype = dynamic


class dab_sl_uensemble_nt(Node):
    class Meta:
        path = "dab.sl.uensemble"
        name = "dab.sl.uensemble"
        prototype = dynamic


class dab_sl_defaultsortorder_nt(Node):
    class Meta:
        path = "dab.sl.defaultsortorder"
        name = "dab.sl.defaultsortorder"
        prototype = dynamic


class dab_sl_dupsel_nt(Node):
    class Meta:
        path = "dab.sl.dupsel"
        name = "dab.sl.dupsel"
        prototype = dynamic


class dab_sl_duplist_nt(Node):
    class Meta:
        path = "dab.sl.duplist"
        name = "dab.sl.duplist"
        prototype = dynamic


class dab_sl_version_nt(Node):
    class Meta:
        path = "dab.sl.version"
        name = "dab.sl.version"
        prototype = dynamic


class dab_sl_prune_nt(Node):
    class Meta:
        path = "dab.sl.prune"
        name = "dab.sl.prune"
        prototype = dynamic


class dab_sl_infopty_nt(Node):
    class Meta:
        path = "dab.sl.infopty"
        name = "dab.sl.infopty"
        prototype = dynamic


class dab_sl_component_nt(Node):
    class Meta:
        path = "dab.sl.component"
        name = "dab.sl.component"
        prototype = dynamic


class dab_sl_service_nt(Node):
    class Meta:
        path = "dab.sl.service"
        name = "dab.sl.service"
        prototype = dynamic


class dab_sl_ensemble_nt(Node):
    class Meta:
        path = "dab.sl.ensemble"
        name = "dab.sl.ensemble"
        prototype = dynamic


class dab_sl_factoryreset_nt(Node):
    class Meta:
        path = "dab.sl.factoryreset"
        name = "dab.sl.factoryreset"
        prototype = dynamic


class dab_sl_station_nt(Node):
    class Meta:
        path = "dab.sl.station"
        name = "dab.sl.station"
        prototype = dynamic


class dab_fic_error_nt(Node):
    class Meta:
        path = "dab.fic.error"
        name = "dab.fic.error"
        prototype = dynamic


class dab_fic_errorframecount_nt(Node):
    class Meta:
        path = "dab.fic.errorframecount"
        name = "dab.fic.errorframecount"
        prototype = dynamic


class dab_fic_errorthreshold_nt(Node):
    class Meta:
        path = "dab.fic.errorthreshold"
        name = "dab.fic.errorthreshold"
        prototype = dynamic


class dab_slideshow_uri_nt(Node):
    class Meta:
        path = "dab.slideshow.uri"
        name = "dab.slideshow.uri"
        prototype = dynamic


class dab_slideshow_state_nt(Node):
    class Meta:
        path = "dab.slideshow.state"
        name = "dab.slideshow.state"
        prototype = dynamic


class dab_udls_nt(Node):
    class Meta:
        path = "dab.udls"
        name = "dab.udls"
        prototype = dynamic


class dab_dls_nt(Node):
    class Meta:
        path = "dab.dls"
        name = "dab.dls"
        prototype = dynamic


class dab_mscerror_nt(Node):
    class Meta:
        path = "dab.mscerror"
        name = "dab.mscerror"
        prototype = dynamic


class dab_snr_nt(Node):
    class Meta:
        path = "dab.snr"
        name = "dab.snr"
        prototype = dynamic


class dab_pty_nt(Node):
    class Meta:
        path = "dab.pty"
        name = "dab.pty"
        prototype = dynamic


class dab_scan_update_nt(Node):
    class Meta:
        path = "dab.scan.update"
        name = "dab.scan.update"
        prototype = dynamic


class dab_scan_state_nt(Node):
    class Meta:
        path = "dab.scan.state"
        name = "dab.scan.state"
        prototype = dynamic


class dab_freqlist_nt(Node):
    class Meta:
        path = "dab.freqlist"
        name = "dab.freqlist"
        prototype = dynamic


class dab_tunestatus_nt(Node):
    class Meta:
        path = "dab.tunestatus"
        name = "dab.tunestatus"
        prototype = dynamic


class dab_band_nt(Node):
    class Meta:
        path = "dab.band"
        name = "dab.band"
        prototype = dynamic


class dab_frequency_nt(Node):
    class Meta:
        path = "dab.frequency"
        name = "dab.frequency"
        prototype = dynamic


class dab_state_nt(Node):
    class Meta:
        path = "dab.state"
        name = "dab.state"
        prototype = dynamic


class radio_update_usu_updateselect_nt(Node):
    class Meta:
        path = "radio.update.usu.updateselect"
        name = "radio.update.usu.updateselect"
        prototype = dynamic


class radio_update_usu_updatelist_nt(Node):
    class Meta:
        path = "radio.update.usu.updatelist"
        name = "radio.update.usu.updatelist"
        prototype = dynamic


class radio_update_usu_version_nt(Node):
    class Meta:
        path = "radio.update.usu.version"
        name = "radio.update.usu.version"
        prototype = dynamic


class radio_update_usu_completion_nt(Node):
    class Meta:
        path = "radio.update.usu.completion"
        name = "radio.update.usu.completion"
        prototype = dynamic


class radio_update_usu_intstate_nt(Node):
    class Meta:
        path = "radio.update.usu.intstate"
        name = "radio.update.usu.intstate"
        prototype = dynamic


class radio_update_usu_control_nt(Node):
    class Meta:
        path = "radio.update.usu.control"
        name = "radio.update.usu.control"
        prototype = dynamic


class radio_update_usu_state_nt(Node):
    class Meta:
        path = "radio.update.usu.state"
        name = "radio.update.usu.state"
        prototype = dynamic


class radio_language_current_nt(Node):
    class Meta:
        path = "radio.language.current"
        name = "radio.language.current"
        prototype = dynamic


class radio_shutdown_nt(Node):
    class Meta:
        path = "radio.shutdown"
        name = "radio.shutdown"
        prototype = dynamic


class radio_update_isu_version_nt(Node):
    class Meta:
        path = "radio.update.isu.version"
        name = "radio.update.isu.version"
        prototype = dynamic


class radio_update_isu_completion_nt(Node):
    class Meta:
        path = "radio.update.isu.completion"
        name = "radio.update.isu.completion"
        prototype = dynamic


class radio_update_isu_intstate_nt(Node):
    class Meta:
        path = "radio.update.isu.intstate"
        name = "radio.update.isu.intstate"
        prototype = dynamic


class radio_update_isu_control_nt(Node):
    class Meta:
        path = "radio.update.isu.control"
        name = "radio.update.isu.control"
        prototype = dynamic


class radio_update_isu_state_nt(Node):
    class Meta:
        path = "radio.update.isu.state"
        name = "radio.update.isu.state"
        prototype = dynamic


class radio_update_fsapi_crc_nt(Node):
    class Meta:
        path = "radio.update.fsapi.crc"
        name = "radio.update.fsapi.crc"
        prototype = dynamic


class radio_update_fsapi_data_nt(Node):
    class Meta:
        path = "radio.update.fsapi.data"
        name = "radio.update.fsapi.data"
        prototype = dynamic


class radio_update_fsapi_address_nt(Node):
    class Meta:
        path = "radio.update.fsapi.address"
        name = "radio.update.fsapi.address"
        prototype = dynamic


class radio_update_fsapi_updatablesize_nt(Node):
    class Meta:
        path = "radio.update.fsapi.updatablesize"
        name = "radio.update.fsapi.updatablesize"
        prototype = dynamic


class radio_update_fsapi_blocksize_nt(Node):
    class Meta:
        path = "radio.update.fsapi.blocksize"
        name = "radio.update.fsapi.blocksize"
        prototype = dynamic


class radio_update_fsapi_version_nt(Node):
    class Meta:
        path = "radio.update.fsapi.version"
        name = "radio.update.fsapi.version"
        prototype = dynamic


class radio_update_fsapi_control_nt(Node):
    class Meta:
        path = "radio.update.fsapi.control"
        name = "radio.update.fsapi.control"
        prototype = dynamic


class radio_update_fsapi_state_nt(Node):
    class Meta:
        path = "radio.update.fsapi.state"
        name = "radio.update.fsapi.state"
        prototype = dynamic


class radio_version_nt(Node):
    class Meta:
        path = "radio.version"
        name = "radio.version"
        prototype = dynamic


class radio_factoryreset_nt(Node):
    class Meta:
        path = "radio.factoryreset"
        name = "radio.factoryreset"
        prototype = dynamic


class radio_power_nt(Node):
    class Meta:
        path = "radio.power"
        name = "radio.power"
        prototype = dynamic


### END GENERATED CONTENT ###
