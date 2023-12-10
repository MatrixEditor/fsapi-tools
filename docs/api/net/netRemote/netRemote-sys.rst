.. THIS FILE WAS GENERATED - DO NOT MODIFY
.. _net-api_netRemote_sys:

=============
netRemote.sys
=============


BaseSysAlarmConfig (netRemote.sys.alarm.config)
-----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.alarm.config``
      - ``LIST_GET_NEXT``, ``SET``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.alarm.config/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAlarmConfigChanged (netRemote.sys.alarm.configChanged)
-------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.alarm.configChanged``
      - ``GET``
      - :class:`NodeS8`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.alarm.configChanged?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAlarmCurrent (netRemote.sys.alarm.current)
-------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.alarm.current``
      - ``GET``
      - :class:`NodeS8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.alarm.current?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAlarmDuration (netRemote.sys.alarm.duration)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.alarm.duration``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.alarm.duration?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAlarmSnooze (netRemote.sys.alarm.snooze)
-----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.alarm.snooze``
      - ``GET``, ``SET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.alarm.snooze?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAlarmSnoozing (netRemote.sys.alarm.snoozing)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.alarm.snoozing``
      - ``GET``
      - :class:`NodeU16`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.alarm.snoozing?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAlarmStatus (netRemote.sys.alarm.status)
-----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.alarm.status``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"ALARMING"*
- ``2``: *"SNOOZING"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.alarm.status?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAudioAirableQuality (netRemote.sys.audio.airableQuality)
---------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.airableQuality``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``True``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"LOW"*
- ``1``: *"NORMAL"*
- ``2``: *"HIGH"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.airableQuality?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Audio: EQ Param0 - Bass (netRemote.sys.audio.eqCustom.param0)
-----------------------------------------------------------------


The bass of the user EQ preset can be controlled with this node. The accepted
values are in the range of -14 to +14.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.eqCustom.param0``
      - ``GET``, ``SET``
      - :class:`NodeS16`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.eqCustom.param0?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Audio: EQ Param1 - Treble (netRemote.sys.audio.eqCustom.param1)
-------------------------------------------------------------------


The treble of the user EQ preset can be controlled with this node. The accepted
values are in the range of -14 to +14.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.eqCustom.param1``
      - ``GET``, ``SET``
      - :class:`NodeS16`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.eqCustom.param1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAudioEqCustomParam2 (netRemote.sys.audio.eqCustom.param2)
----------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.eqCustom.param2``
      - ``GET``, ``SET``
      - :class:`NodeS16`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.eqCustom.param2?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAudioEqCustomParam3 (netRemote.sys.audio.eqCustom.param3)
----------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.eqCustom.param3``
      - ``GET``, ``SET``
      - :class:`NodeS16`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.eqCustom.param3?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAudioEqCustomParam4 (netRemote.sys.audio.eqCustom.param4)
----------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.eqCustom.param4``
      - ``GET``, ``SET``
      - :class:`NodeS16`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.eqCustom.param4?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Audio: EQ Loudness (netRemote.sys.audio.eqLoudness)
-------------------------------------------------------


When the user-controllable EQ preset has been selected, its loudness can be
controlled by this node.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.eqLoudness``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``True``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OFF"*
- ``1``: *"ON"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.eqLoudness?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Audio: EQ Preset (netRemote.sys.audio.eqPreset)
---------------------------------------------------


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


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.eqPreset``
      - ``GET``, ``SET``
      - :class:`NodeU8`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.eqPreset?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysAudioExtStaticDelay (netRemote.sys.audio.extStaticDelay)
---------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.extStaticDelay``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.extStaticDelay?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Audio: Mute (netRemote.sys.audio.mute)
------------------------------------------


This node can be used to mute/unmute the target device.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.mute``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``True``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NOT_MUTE"*
- ``1``: *"MUTE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.mute?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Audio: Volume (netRemote.sys.audio.volume)
----------------------------------------------

Stores the current value of the valume.

    When the volume is set to the minimum value, it will activate the mute
    function. The allowed values are:

    - from ``1`` to ``32``


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.audio.volume``
      - ``GET``, ``SET``
      - :class:`NodeU8`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.audio.volume?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsClockSourceList (netRemote.sys.caps.clockSourceList)
---------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.clockSourceList``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.caps.clockSourceList/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsDabFreqList (netRemote.sys.caps.dabFreqList)
-------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.dabFreqList``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.caps.dabFreqList/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsEqBands (netRemote.sys.caps.eqBands)
-----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.eqBands``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.caps.eqBands/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Caps: EQ Presets (netRemote.sys.caps.eqPresets)
---------------------------------------------------


A list of available EQ presets can be fetched with this command.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.eqPresets``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.caps.eqPresets/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsExtStaticDelayMax (netRemote.sys.caps.extStaticDelayMax)
-------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.extStaticDelayMax``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.caps.extStaticDelayMax?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsFmFreqRangeLower (netRemote.sys.caps.fmFreqRange.lower)
------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.fmFreqRange.lower``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.caps.fmFreqRange.lower?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsFmFreqRangeStepSize (netRemote.sys.caps.fmFreqRange.stepSize)
------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.fmFreqRange.stepSize``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.caps.fmFreqRange.stepSize?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsFmFreqRangeUpper (netRemote.sys.caps.fmFreqRange.upper)
------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.fmFreqRange.upper``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.caps.fmFreqRange.upper?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsFsdca (netRemote.sys.caps.fsdca)
-------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.fsdca``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.caps.fsdca?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsUtcSettingsList (netRemote.sys.caps.utcSettingsList)
---------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.utcSettingsList``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.caps.utcSettingsList/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsValidLang (netRemote.sys.caps.validLang)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.validLang``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.caps.validLang/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsValidModes (netRemote.sys.caps.validModes)
-----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.validModes``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.caps.validModes/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCapsVolumeSteps (netRemote.sys.caps.volumeSteps)
-------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.caps.volumeSteps``
      - ``GET``
      - :class:`NodeU8`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.caps.volumeSteps?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysCfgIrAutoPlayFlag (netRemote.sys.cfg.irAutoPlayFlag)
-----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.cfg.irAutoPlayFlag``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``True``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"AUTOPLAY_ON"*
- ``1``: *"AUTOPLAY_OFF"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.cfg.irAutoPlayFlag?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysClockDateFormat (netRemote.sys.clock.dateFormat)
-------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.clock.dateFormat``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"DATE_DD_MM_YYYY"*
- ``1``: *"DATE_MM_DD_YYYY"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.clock.dateFormat?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysClockDst (netRemote.sys.clock.dst)
-----------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.clock.dst``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OFF"*
- ``1``: *"ON"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.clock.dst?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysClockLocalDate (netRemote.sys.clock.localDate)
-----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.clock.localDate``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.clock.localDate?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysClockLocalTime (netRemote.sys.clock.localTime)
-----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.clock.localTime``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.clock.localTime?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysClockMode (netRemote.sys.clock.mode)
-------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.clock.mode``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"_12_HOUR"*
- ``1``: *"_24_HOUR"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.clock.mode?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysClockSource (netRemote.sys.clock.source)
-----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.clock.source``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"MANUAL"*
- ``1``: *"DAB"*
- ``2``: *"FM"*
- ``3``: *"SNTP"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.clock.source?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysClockTimeZone (netRemote.sys.clock.timeZone)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.clock.timeZone``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.clock.timeZone?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysClockUtcOffset (netRemote.sys.clock.utcOffset)
-----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.clock.utcOffset``
      - ``GET``, ``SET``
      - :class:`NodeS32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.clock.utcOffset?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysFactoryReset (netRemote.sys.factoryReset)
------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.factoryReset``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NONE"*
- ``1``: *"RESET"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.factoryReset?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysInfoActiveSession (netRemote.sys.info.activeSession)
-----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.activeSession``
      - ``GET``
      - :class:`NodeE8`
      -  ``False``, ``True``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NO"*
- ``1``: *"YES"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.activeSession?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysInfoBuildVersion (netRemote.sys.info.buildVersion)
---------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.buildVersion``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.buildVersion?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysInfoControllerName (netRemote.sys.info.controllerName)
-------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.controllerName``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.controllerName?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysInfoDmruuid (netRemote.sys.info.dmruuid)
-----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.dmruuid``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.dmruuid?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Info: Friendly Name (netRemote.sys.info.friendlyName)
---------------------------------------------------------


The friendly name can be used to make it easier to identify mulitple devices
in the same network.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.friendlyName``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.friendlyName?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysInfoModelName (netRemote.sys.info.modelName)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.modelName``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.modelName?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysInfoNetRemoteVendorId (netRemote.sys.info.netRemoteVendorId)
-------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.netRemoteVendorId``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.netRemoteVendorId?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Info: RadioID (netRemote.sys.info.radioId)
----------------------------------------------

Stores the radio identifier. (MAC Address)

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.radioId``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.radioId?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


INFO: Radion PIN (netRemote.sys.info.radioPin)
----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.radioPin``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.radioPin?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysInfoRadiotest (netRemote.sys.info.radiotest)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.radiotest``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.radiotest?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


INFO: SerialNumber (netRemote.sys.info.serialNumber)
----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.serialNumber``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.serialNumber?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS-Info: Version (netRemote.sys.info.version)
----------------------------------------------


A readonly node that can be used to dump the current firmware version. More
information about the structure of a firmware version can be found in the
details section below.

*TODO: description of version*


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.info.version``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.info.version?pin=1234

    <fsapiResponse>
        <status>FS_OK</status>
        <value>
            <c8_array>ir-mmi-FS2026-0500-0549_V2.12.25c.EX72088-1A12</c8_array>
        </value>
    </fsapiResponse>

.. raw:: html

    <hr>


BaseSysIpodDockStatus (netRemote.sys.ipod.dockStatus)
-----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.ipod.dockStatus``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NOT_DOCKED"*
- ``1``: *"DOCKED_STILL_CONNECTING"*
- ``2``: *"DOCKED_ONLINE_READY"*
- ``3``: *"DOCKED_UNSUPPORTED_IPOD"*
- ``4``: *"DOCKED_UNKNOWN_DEVICE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.ipod.dockStatus?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysIsuControl (netRemote.sys.isu.control)
---------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.isu.control``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"UPDATE_FIRMWARE"*
- ``2``: *"CHECK_FOR_UPDATE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.isu.control?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysIsuMandatory (netRemote.sys.isu.mandatory)
-------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.isu.mandatory``
      - ``GET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NO"*
- ``1``: *"YES"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.isu.mandatory?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysIsuSoftwareUpdateProgress (netRemote.sys.isu.softwareUpdateProgress)
---------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.isu.softwareUpdateProgress``
      - ``GET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.isu.softwareUpdateProgress?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysIsuState (netRemote.sys.isu.state)
-----------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.isu.state``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"CHECK_IN_PROGRESS"*
- ``2``: *"UPDATE_AVAILABLE"*
- ``3``: *"UPDATE_NOT_AVAILABLE"*
- ``4``: *"CHECK_FAILED"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.isu.state?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysIsuSummary (netRemote.sys.isu.summary)
---------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.isu.summary``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.isu.summary?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysIsuVersion (netRemote.sys.isu.version)
---------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.isu.version``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.isu.version?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysLang (netRemote.sys.lang)
--------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.lang``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.lang?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS: Mode (netRemote.sys.mode)
------------------------------

The current system configuration.

    Allthough, this node has not been identified as an enum node, it can take the following
    values:

    - ``0``: *"Ethernet Radio"*
    - ``1``: *"Music Player"*
    - ``2``: *"FM Radio"*


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.mode``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.mode?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetCommitChanges (netRemote.sys.net.commitChanges)
---------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.commitChanges``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NO"*
- ``1``: *"YES"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.commitChanges?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetIpConfigAddress (netRemote.sys.net.ipConfig.address)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.ipConfig.address``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.ipConfig.address?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetIpConfigDhcp (netRemote.sys.net.ipConfig.dhcp)
--------------------------------------------------------

Enum node that tells you whether the device is using a DHCP server to retrieve its IP address.

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.ipConfig.dhcp``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NO"*
- ``1``: *"YES"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.ipConfig.dhcp?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetIpConfigDnsPrimary (netRemote.sys.net.ipConfig.dnsPrimary)
--------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.ipConfig.dnsPrimary``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.ipConfig.dnsPrimary?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetIpConfigDnsSecondary (netRemote.sys.net.ipConfig.dnsSecondary)
------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.ipConfig.dnsSecondary``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.ipConfig.dnsSecondary?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetIpConfigGateway (netRemote.sys.net.ipConfig.gateway)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.ipConfig.gateway``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.ipConfig.gateway?pin=1234

    <fsapiResponse>
    <status>FS_OK</status>
    <value><u32>3232243908</u32></value>
    </fsapiResponse>


.. raw:: html

    <hr>


BaseSysNetIpConfigSubnetMask (netRemote.sys.net.ipConfig.subnetMask)
--------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.ipConfig.subnetMask``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.ipConfig.subnetMask?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetKeepConnected (netRemote.sys.net.keepConnected)
---------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.keepConnected``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NO"*
- ``1``: *"YES"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.keepConnected?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetUapInterfaceEnable (netRemote.sys.net.uap.interfaceEnable)
--------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.uap.interfaceEnable``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"INTERFACE_DISABLE"*
- ``1``: *"INTERFACE_ENABLE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.uap.interfaceEnable?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWiredInterfaceEnable (netRemote.sys.net.wired.interfaceEnable)
------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wired.interfaceEnable``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"INTERFACE_DISABLE"*
- ``1``: *"INTERFACE_ENABLE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wired.interfaceEnable?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWiredMacAddress (netRemote.sys.net.wired.macAddress)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wired.macAddress``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wired.macAddress?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanActivateProfile (netRemote.sys.net.wlan.activateProfile)
----------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.activateProfile``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.activateProfile?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanConnectedSSID (netRemote.sys.net.wlan.connectedSSID)
------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.connectedSSID``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.connectedSSID?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanDeactivateProfile (netRemote.sys.net.wlan.deactivateProfile)
--------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.deactivateProfile``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.deactivateProfile?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanInterfaceEnable (netRemote.sys.net.wlan.interfaceEnable)
----------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.interfaceEnable``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"INTERFACE_DISABLE"*
- ``1``: *"INTERFACE_ENABLE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.interfaceEnable?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanMacAddress (netRemote.sys.net.wlan.macAddress)
------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.macAddress``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.macAddress?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanPerformFCC (netRemote.sys.net.wlan.performFCC)
------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.performFCC``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"TEST_STOP"*
- ``1``: *"TEST_START"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.performFCC?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanPerformWPS (netRemote.sys.net.wlan.performWPS)
------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.performWPS``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"WPS_IDLE"*
- ``1``: *"WPS_PBC"*
- ``2``: *"WPS_PIN"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.performWPS?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanProfiles (netRemote.sys.net.wlan.profiles)
--------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.profiles``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.net.wlan.profiles/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanRegion (netRemote.sys.net.wlan.region)
----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.region``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"INVALID"*
- ``1``: *"USA"*
- ``2``: *"CANADA"*
- ``3``: *"EUROPE"*
- ``4``: *"SPAIN"*
- ``5``: *"FRANCE"*
- ``6``: *"JAPAN"*
- ``7``: *"AUSTRALIA"*
- ``8``: *"Reserved8"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.region?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanRegionFcc (netRemote.sys.net.wlan.regionFcc)
----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.regionFcc``
      - ``GET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NOT_ACTIVE"*
- ``1``: *"ACTIVE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.regionFcc?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanRemoveProfile (netRemote.sys.net.wlan.removeProfile)
------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.removeProfile``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.removeProfile?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanRssi (netRemote.sys.net.wlan.rssi)
------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.rssi``
      - ``GET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.rssi?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanScan (netRemote.sys.net.wlan.scan)
------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.scan``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"SCAN"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.scan?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanScanList (netRemote.sys.net.wlan.scanList)
--------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.scanList``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.sys.net.wlan.scanList/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSelectAP (netRemote.sys.net.wlan.selectAP)
--------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.selectAP``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.selectAP?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSelectProfile (netRemote.sys.net.wlan.selectProfile)
------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.selectProfile``
      - ``GET``, ``SET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.selectProfile?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSetAuthType (netRemote.sys.net.wlan.setAuthType)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setAuthType``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OPEN"*
- ``1``: *"PSK"*
- ``2``: *"WPA"*
- ``3``: *"WPA2"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setAuthType?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSetEncType (netRemote.sys.net.wlan.setEncType)
------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setEncType``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NONE"*
- ``1``: *"WEP"*
- ``2``: *"TKIP"*
- ``3``: *"AES"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setEncType?pin=1234

    <fsapiResponse>
    <status>FS_OK</status>
    <value><u8>3</u8></value>
    </fsapiResponse>


.. raw:: html

    <hr>


BaseSysNetWlanSetFccTestChanNum (netRemote.sys.net.wlan.setFccTestChanNum)
--------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setFccTestChanNum``
      - ``GET``, ``SET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setFccTestChanNum?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSetFccTestDataRate (netRemote.sys.net.wlan.setFccTestDataRate)
----------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setFccTestDataRate``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"_1M"*
- ``1``: *"_2M"*
- ``2``: *"_5_5M"*
- ``3``: *"_11M"*
- ``4``: *"_22M"*
- ``5``: *"_6M"*
- ``6``: *"_9M"*
- ``7``: *"_12M"*
- ``8``: *"_18M"*
- ``9``: *"_24M"*
- ``10``: *"_36M"*
- ``11``: *"_48M"*
- ``12``: *"_54M"*
- ``13``: *"_72M"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setFccTestDataRate?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSetFccTestTxDataPattern (netRemote.sys.net.wlan.setFccTestTxDataPattern)
--------------------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setFccTestTxDataPattern``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setFccTestTxDataPattern?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSetFccTestTxPower (netRemote.sys.net.wlan.setFccTestTxPower)
--------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setFccTestTxPower``
      - ``GET``, ``SET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setFccTestTxPower?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSetFccTxOff (netRemote.sys.net.wlan.setFccTxOff)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setFccTxOff``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"TX_ON"*
- ``1``: *"TX_OFF"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setFccTxOff?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSetPassphrase (netRemote.sys.net.wlan.setPassphrase)
------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setPassphrase``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setPassphrase?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanSetSSID (netRemote.sys.net.wlan.setSSID)
------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.setSSID``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.setSSID?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysNetWlanWpsPinRead (netRemote.sys.net.wlan.wpsPinRead)
------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.net.wlan.wpsPinRead``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.net.wlan.wpsPinRead?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


SYS: Power (netRemote.sys.power)
--------------------------------


With this node the user is able to activate / deactivate the standby function of the
device. "Standby" refers to a special mode where the output will be muted and the display
deactivated.

.. note::
    The ethernet or FM radio will select the last configuret item and automatically start
    playing


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.power``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``True``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OFF"*
- ``1``: *"ON"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.power?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysRsaPublicKey (netRemote.sys.rsa.publicKey)
-------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.rsa.publicKey``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.rsa.publicKey?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysRsaStatus (netRemote.sys.rsa.status)
-------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.rsa.status``
      - ``GET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"GENERATION_IN_PROGRESS"*
- ``1``: *"KEY_AVAILABLE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.rsa.status?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysSleep (netRemote.sys.sleep)
----------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.sleep``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.sleep?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseSysState (netRemote.sys.state)
----------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.sys.state``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NORMAL_MODE"*
- ``1``: *"SAPU_MODE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.sys.state?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>
