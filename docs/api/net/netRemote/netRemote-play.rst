.. THIS FILE WAS GENERATED - DO NOT MODIFY
.. _net-api_netRemote_play:

==============
netRemote.play
==============


BasePlayAddPreset (netRemote.play.addPreset)
--------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.addPreset``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.addPreset?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayAddPresetStatus (netRemote.play.addPresetStatus)
--------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.addPresetStatus``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"PRESET_STORRED"*
- ``1``: *"PRESET_NOT_STORRED"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.addPresetStatus?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayAlerttone (netRemote.play.alerttone)
--------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.alerttone``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"PLAY"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.alerttone?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayCaps (netRemote.play.caps)
----------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.caps``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.caps?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayConcurencyResponse (netRemote.play.ConcurencyResponse)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.ConcurencyResponse``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"FALSE"*
- ``1``: *"TRUE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.ConcurencyResponse?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayConcurencyStr (netRemote.play.ConcurencyStr)
----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.ConcurencyStr``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.ConcurencyStr?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play: Control (netRemote.play.control)
--------------------------------------


This node allows control over the current track. Please note the differencies
of different unit states:

- ``NEXT``:
    When used on "Media Player" mode, the next track will be selected and start
    playing. On "Radio" mode, the next higher frequency will be scanned for signals.

- ``PREV``:
    The "Media Player" mode selects the next track and "Radio" mode scans for lower
    frequency signals.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.control``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"STOP"*
- ``1``: *"PLAY"*
- ``2``: *"PAUSE"*
- ``3``: *"NEXT"*
- ``4``: *"PREVIOUS"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.control?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayErrorStr (netRemote.play.errorStr)
------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.errorStr``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.errorStr?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayFeedback (netRemote.play.feedback)
------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.feedback``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"POSITIVE"*
- ``2``: *"NEGATIVE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.feedback?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayFrequency (netRemote.play.frequency)
--------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.frequency``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.frequency?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play-Info: Album (netRemote.play.info.album)
--------------------------------------------

The name of the album of the current selected or playing track.

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.album``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.album?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayInfoAlbumDescription (netRemote.play.info.albumDescription)
-------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.albumDescription``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.albumDescription?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play-Info: Artist (netRemote.play.info.artist)
----------------------------------------------

The name of the artist of the current selected or playing track.

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.artist``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.artist?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayInfoArtistDescription (netRemote.play.info.artistDescription)
---------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.artistDescription``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.artistDescription?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayInfoDescription (netRemote.play.info.description)
---------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.description``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.description?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play-Info: Duration (netRemote.play.info.duration)
--------------------------------------------------


The specific duration of the current selected or playing track can be retrieved with
this command. This is helpful when the user is going to jump to a specific part of
the track and doesn't want to send an invalid command.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.duration``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.duration?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play-Info: Graphic URI (netRemote.play.info.graphicUri)
-------------------------------------------------------


The device will automatically check if the current selected radio has a logo in the
database and if possible returns the location.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.graphicUri``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.graphicUri?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play-Info: Name (netRemote.play.info.name)
------------------------------------------

The name of the current selected or playing track.

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.name``
      - ``GET``
      - :class:`NodeC8`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.name?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayInfoProviderLogoUri (netRemote.play.info.providerLogoUri)
-----------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.providerLogoUri``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.providerLogoUri?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayInfoProviderName (netRemote.play.info.providerName)
-----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.providerName``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.providerName?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play-Info: Text (netRemote.play.info.text)
------------------------------------------


The user can retrieve extra information of the track with this command
or when the Ethernet radio is active, this command will retrieve the
data that is showed on the display.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.info.text``
      - ``GET``
      - :class:`NodeC8`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.info.text?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayNotificationMessage (netRemote.play.NotificationMessage)
----------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.NotificationMessage``
      - ``GET``
      - :class:`NodeC8`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.NotificationMessage?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play: Position (netRemote.play.position)
----------------------------------------


In order to jump to a specific position within a playing track, this node can
be utilized. Therefore, the range of this value is different for every track.

.. note::
    The range of the value has no solid value, because the number of samples
    is different in every played track.

.. hint::
    The maximum range of a track can be retrieved by using ``netRemote.play.duration``.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.position``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.position?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play: Rate (netRemote.play.rate)
--------------------------------


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


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.rate``
      - ``GET``, ``SET``
      - :class:`NodeS8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.rate?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayRating (netRemote.play.rating)
--------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.rating``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NEUTRAL"*
- ``1``: *"POSITIVE"*
- ``2``: *"NEGATIVE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.rating?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play: Repeat (netRemote.play.repeat)
------------------------------------


This nodes controls the repeat mode of the target device. The "repeat" mode
can take up to three states. The different values are listed below.

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.repeat``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OFF"*
- ``1``: *"REPEAT_ALL"*
- ``2``: *"REPEAT_ONE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.repeat?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayScrobble (netRemote.play.scrobble)
------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.scrobble``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OFF"*
- ``1``: *"ON"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.scrobble?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayServiceIdsDabEnsembleId (netRemote.play.serviceIds.dabEnsembleId)
-------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.serviceIds.dabEnsembleId``
      - ``GET``
      - :class:`NodeU16`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.serviceIds.dabEnsembleId?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayServiceIdsDabScids (netRemote.play.serviceIds.dabScids)
---------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.serviceIds.dabScids``
      - ``GET``
      - :class:`NodeU8`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.serviceIds.dabScids?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayServiceIdsDabServiceId (netRemote.play.serviceIds.dabServiceId)
-----------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.serviceIds.dabServiceId``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.serviceIds.dabServiceId?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayServiceIdsEcc (netRemote.play.serviceIds.ecc)
-----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.serviceIds.ecc``
      - ``GET``
      - :class:`NodeU8`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.serviceIds.ecc?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayServiceIdsFmRdsPi (netRemote.play.serviceIds.fmRdsPi)
-------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.serviceIds.fmRdsPi``
      - ``GET``
      - :class:`NodeU16`
      -  ``True``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.serviceIds.fmRdsPi?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play: Shuffle (netRemote.play.shuffle)
--------------------------------------


This node controls the status of the music player shuffle mode. It can be
activated (``1``) / deactivated (``0``).


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.shuffle``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OFF"*
- ``1``: *"ON"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.shuffle?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlayShuffleStatus (netRemote.play.shuffleStatus)
----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.shuffleStatus``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OK"*
- ``1``: *"SHUFFLING"*
- ``2``: *"TOO_MANY_ITEMS"*
- ``3``: *"UNSUPPORTED"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.shuffleStatus?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BasePlaySignalStrength (netRemote.play.signalStrength)
------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.signalStrength``
      - ``GET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.signalStrength?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


Play: Status (netRemote.play.status)
------------------------------------


This node is readonly and returns the current status of the media player.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.play.status``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``True``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"BUFFERING"*
- ``2``: *"PLAYING"*
- ``3``: *"PAUSED"*
- ``4``: *"REBUFFERING"*
- ``5``: *"ERROR"*
- ``6``: *"STOPPED"*
- ``7``: *"ERROR_POPUP"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.play.status?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>
