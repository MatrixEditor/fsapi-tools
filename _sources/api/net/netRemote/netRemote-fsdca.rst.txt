.. THIS FILE WAS GENERATED - DO NOT MODIFY
.. _net-api_netRemote_fsdca:

===============
netRemote.fsdca
===============


BaseFsdcaAuthCode (netRemote.fsdca.authCode)
--------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.fsdca.authCode``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.fsdca.authCode?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseFsdcaClientId (netRemote.fsdca.clientId)
--------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.fsdca.clientId``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.fsdca.clientId?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseFsdcaDisassociate (netRemote.fsdca.disassociate)
----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.fsdca.disassociate``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"NO_REQUEST"*
- ``1``: *"DISSASOCIATE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.fsdca.disassociate?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseFsdcaFsdcaId (netRemote.fsdca.fsdcaId)
------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.fsdca.fsdcaId``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.fsdca.fsdcaId?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseFsdcaState (netRemote.fsdca.state)
--------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.fsdca.state``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"FSDCA_STATE_INITIAL"*
- ``1``: *"FSDCA_STATE_NOT_ASSOCIATED"*
- ``2``: *"FSDCA_STATE_AUTH_IN_PROGRESS"*
- ``3``: *"FSDCA_STATE_CONNECTING"*
- ``4``: *"FSDCA_STATE_CONNECTED"*
- ``5``: *"FSDCA_STATE_WAITING"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.fsdca.state?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>
