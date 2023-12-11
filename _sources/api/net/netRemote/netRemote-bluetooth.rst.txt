.. THIS FILE WAS GENERATED - DO NOT MODIFY
.. _net-api_netRemote_bluetooth:

===================
netRemote.bluetooth
===================


BaseBluetoothConnectedDevices (netRemote.bluetooth.connectedDevices)
--------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.bluetooth.connectedDevices``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.bluetooth.connectedDevices/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseBluetoothConnectedDevicesListVersion (netRemote.bluetooth.connectedDevicesListVersion)
------------------------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.bluetooth.connectedDevicesListVersion``
      - ``GET``
      - :class:`NodeU32`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.bluetooth.connectedDevicesListVersion?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseBluetoothDiscoverableState (netRemote.bluetooth.discoverableState)
----------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.bluetooth.discoverableState``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"DISCOVERABLE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.bluetooth.discoverableState?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>
