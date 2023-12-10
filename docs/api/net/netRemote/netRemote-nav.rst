.. THIS FILE WAS GENERATED - DO NOT MODIFY
.. _net-api_netRemote_nav:

=============
netRemote.nav
=============


BaseNavActionContext (netRemote.nav.action.context)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.action.context``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.action.context?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavActionDabPrune (netRemote.nav.action.dabPrune)
-----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.action.dabPrune``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"PRUNE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.action.dabPrune?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavActionDabScan (netRemote.nav.action.dabScan)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.action.dabScan``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"IDLE"*
- ``1``: *"SCAN"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.action.dabScan?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


NAV-Action: Navigate (netRemote.nav.action.navigate)
----------------------------------------------------


Use this node to navigate through the internal directory structure of an
attached storage. The maximum value will move the pointer to the next upper
level.

.. warning:: NAV state must be enabled to use this node.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.action.navigate``
      - ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.action.navigate?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavActionSelectItem (netRemote.nav.action.selectItem)
---------------------------------------------------------


Open/ Select a file in the current directory. The selected value will
open the item with the same item key.

.. note::
    This command can't be used to move through map levels. It will only
    open the selected item if the item type is not a directory.

.. warning:: NAV state must be enabled to use this node.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.action.selectItem``
      - ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.action.selectItem?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavActionSelectPreset (netRemote.nav.action.selectPreset)
-------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.action.selectPreset``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.action.selectPreset?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavAmazonMpGetRating (netRemote.nav.amazonMpGetRating)
----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.amazonMpGetRating``
      - ``GET``
      - :class:`NodeU8`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.amazonMpGetRating?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavAmazonMpLoginComplete (netRemote.nav.amazonMpLoginComplete)
------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.amazonMpLoginComplete``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"FALSE"*
- ``1``: *"TRUE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.amazonMpLoginComplete?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavAmazonMpLoginUrl (netRemote.nav.amazonMpLoginUrl)
--------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.amazonMpLoginUrl``
      - ``GET``
      - :class:`NodeC8`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.amazonMpLoginUrl?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavAmazonMpSetRating (netRemote.nav.amazonMpSetRating)
----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.amazonMpSetRating``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"POSITIVE"*
- ``1``: *"NEGATIVE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.amazonMpSetRating?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavBrowseMode (netRemote.nav.browseMode)
--------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.browseMode``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``True``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.browseMode?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavCaps (netRemote.nav.caps)
--------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.caps``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.caps?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextDepth (netRemote.nav.context.depth)
-------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.depth``
      - ``GET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.context.depth?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextErrorStr (netRemote.nav.context.errorStr)
-------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.errorStr``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.context.errorStr?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextFormData (netRemote.nav.context.formData)
-------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.formData``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.context.formData?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextFormItem (netRemote.nav.context.form.item)
--------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.form.item``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.nav.context.form.item/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextFormOption (netRemote.nav.context.form.option)
------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.form.option``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.nav.context.form.option/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextList (netRemote.nav.context.list)
-----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.list``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.nav.context.list/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextNavigate (netRemote.nav.context.navigate)
-------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.navigate``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.context.navigate?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextNumItems (netRemote.nav.context.numItems)
-------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.numItems``
      - ``GET``
      - :class:`NodeS32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.context.numItems?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextRefresh (netRemote.nav.context.refresh)
-----------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.refresh``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"FALSE"*
- ``1``: *"TRUE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.context.refresh?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavContextStatus (netRemote.nav.context.status)
---------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.context.status``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"WAITING"*
- ``1``: *"READY"*
- ``2``: *"FAIL"*
- ``3``: *"FATAL_ERR"*
- ``4``: *"READY_ROOT"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.context.status?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavCurrentTitle (netRemote.nav.currentTitle)
------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.currentTitle``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.currentTitle?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavDabScanUpdate (netRemote.nav.dabScanUpdate)
--------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.dabScanUpdate``
      - ``GET``
      - :class:`NodeU32`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.dabScanUpdate?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavDepth (netRemote.nav.depth)
----------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.depth``
      - ``GET``
      - :class:`NodeU8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.depth?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavDescription (netRemote.nav.description)
----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.description``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.description?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavEncFormData (netRemote.nav.encFormData)
----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.encFormData``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.encFormData?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavErrorStr (netRemote.nav.errorStr)
----------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.errorStr``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.errorStr?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavFormButton (netRemote.nav.form.button)
---------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.form.button``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.nav.form.button/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavFormData (netRemote.nav.formData)
----------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.formData``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.formData?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavFormItem (netRemote.nav.form.item)
-----------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.form.item``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.nav.form.item/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavFormOption (netRemote.nav.form.option)
---------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.form.option``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.nav.form.option/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


NAV: List (netRemote.nav.list)
------------------------------


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


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.list``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.nav.list/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


NAV: NumItems (netRemote.nav.numItems)
--------------------------------------


Returns the amount of items in the current folder of the attached
storage device.

.. warning:: NAV state must be enabled to use this node.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.numItems``
      - ``GET``
      - :class:`NodeS32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.numItems?pin=1234

    <?xml version="1.0"?>
    <fsapiresponse>
        <status>FS_OK</status>
        <value>
            <s32>2</s32>
        </value>
    </fsapiresponse>

.. raw:: html

    <hr>


BaseNavPresetCurrentPreset (netRemote.nav.preset.currentPreset)
---------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.currentPreset``
      - ``GET``
      - :class:`NodeU32`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.currentPreset?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetDelete (netRemote.nav.preset.delete)
-------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.delete``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.delete?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetDownloadArtworkUrl (netRemote.nav.preset.download.artworkUrl)
--------------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.download.artworkUrl``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.download.artworkUrl?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetDownloadBlob (netRemote.nav.preset.download.blob)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.download.blob``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.download.blob?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetDownloadDownload (netRemote.nav.preset.download.download)
----------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.download.download``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.download.download?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetDownloadName (netRemote.nav.preset.download.name)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.download.name``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.download.name?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetDownloadType (netRemote.nav.preset.download.type)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.download.type``
      - ``GET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.download.type?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetListversion (netRemote.nav.preset.listversion)
-----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.listversion``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``True``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.listversion?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresets (netRemote.nav.presets)
--------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.presets``
      - ``LIST_GET_NEXT``
      - :class:`NodeList`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/LIST_GET_NEXT/netRemote.nav.presets/-1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetSwapIndex1 (netRemote.nav.preset.swap.index1)
----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.swap.index1``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.swap.index1?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetSwapIndex2 (netRemote.nav.preset.swap.index2)
----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.swap.index2``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.swap.index2?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetSwapSwap (netRemote.nav.preset.swap.swap)
------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.swap.swap``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.swap.swap?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetUploadArtworkUrl (netRemote.nav.preset.upload.artworkUrl)
----------------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.upload.artworkUrl``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.upload.artworkUrl?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetUploadBlob (netRemote.nav.preset.upload.blob)
----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.upload.blob``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.upload.blob?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetUploadName (netRemote.nav.preset.upload.name)
----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.upload.name``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.upload.name?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetUploadType (netRemote.nav.preset.upload.type)
----------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.upload.type``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.upload.type?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavPresetUploadUpload (netRemote.nav.preset.upload.upload)
--------------------------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.preset.upload.upload``
      - ``GET``, ``SET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.preset.upload.upload?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavRefresh (netRemote.nav.refresh)
--------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.refresh``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"FALSE"*
- ``1``: *"TRUE"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.refresh?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavReleaseDate (netRemote.nav.releaseDate)
----------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.releaseDate``
      - ``GET``
      - :class:`NodeU32`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.releaseDate?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


BaseNavSearchTerm (netRemote.nav.searchTerm)
--------------------------------------------

*TODO*

.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.searchTerm``
      - ``GET``, ``SET``
      - :class:`NodeC8`
      -  ``False``, ``False``


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.searchTerm?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>


NAV: State (netRemote.nav.state)
--------------------------------


Enables or diables the navigation state. To enable other nav commands, the
``nav.state`` needs to be set to one.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.state``
      - ``GET``, ``SET``
      - :class:`NodeE8`
      -  ``False``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"OFF"*
- ``1``: *"ON"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.state?pin=1234

    <fsapiResponse>
        <status>FS_OK</status>
        <value>
            <u8>0</u8>
        </value>
    </fsapiResponse>

.. raw:: html

    <hr>


NAV: Status (netRemote.nav.status)
----------------------------------


When the unit is still loading, it's not possible to read the data. To prevent
errors or invalid answers it's recommended to always check the status after
changing the system.mode before sending new commands.


.. list-table::
    :header-rows: 1
    :widths: 20, 20, 20, 20

    * - Node Path
      - Methods
      - Type
      - Notifying, Cacheable
    * - ``netRemote.nav.status``
      - ``GET``
      - :class:`NodeE8`
      -  ``True``, ``False``


As this node is of an enum type, you can utilize the following constants in
its usage:

- ``0``: *"WAITING"*
- ``1``: *"READY"*
- ``2``: *"FAIL"*
- ``3``: *"FATAL_ERR"*
- ``4``: *"READY_ROOT"*


.. code-block:: xml
    :linenos:
    :caption: Example: /fsapi/GET/netRemote.nav.status?pin=1234

    <!-- TBD --!>

.. raw:: html

    <hr>
