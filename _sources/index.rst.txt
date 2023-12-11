.. frontier-smart-api documentation master file, created by
   sphinx-quickstart on Mon Oct  3 08:55:07 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to fsapi-tools' documentation!
==============================================

This project comprises various tools written in Ppython3` that are designed to analyze properties of
firmware binaries provided by Frontier Smart (formerly Frontier Silicon - FS) and interact with the
inbuilt API.

Although there are other repositories that focus on the specific API, the implementation provided here
includes **ALL** available nodes that were invented/developed by Frontier Smart.

Features:

- ISUTool: An inspector for Frontier Smart firmware binaries.
- Pattern Specification: Designed for ISU binaries to be used in ImHex.
- Python3 FSAPI implementation.
- XDR-Decompiler: For decompiling binary packed JavaScript files.
- FSAPI-NET Tool: Enables interaction with Frontier Smart IoT devices.

.. code-block:: bash
   :caption: Installation via pip

   pip install fsapi-tools

.. note::
   Please make sure to install all necessary dependencies before using this project.

.. raw:: html

   <hr>


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   firmware-analysis
   firmware-structure
   isutool
   fsapi-tools
   api-examples

.. toctree::
   :maxdepth: 1
   :caption: Reference

   api/net/nodes


.. raw:: html

   <hr>

Basic usage
-----------

.. code-block:: python
   :linenos:
   :caption: ISU API

   from fsapi.isu import ISU
   from fsapi.isu.util import DataclassPrinter

   isu = ISU << "firmware.isu.bin"
   # load an ISUHeader object and print the loaded data
   pp = DataclassPrinter()
   pp.print_object(isu.header)


.. code-block:: python
   :linenos:
   :caption: FSAPI

   from fsapi.net import FSDevice, wrap

   # First, create the device:
   device = FSDevice("127.0.0.1")

   # Create an API wrapper
   api = wrap(device)

   # Fetch and change the friendly name of a device
   name = api.friendly_name
   api.fiendly_name = "FooBar"

   # Query an enum value. The value's name is bound to the returned value
   state = api.nav_state
   name = state.stringvalue

   # Iterate over a list of items
   for item in api.ls_nav_list(_pos=-1, max_items=10): # -1 for all (optional)
      key = item["key"]
      item_name = iem["name"]
      # attriutes can be accessed directly with .attrib

   # Select an item in a list
   api.ls_nav_list = 2


.. code-block:: python
   :linenos:
   :caption: Software update URL

   from fsapi.netconfig import FSNetConfiguration
   from fsapi.isu import isu_find_update, isu_new_url, isu_get_update

   # 1.Find and download updates
   # without custom netconfig -> HTTPS traffic
   response = isu_find_update('$MAC', '$CUSTOM', '$VERSION')

   # with custom config -> force HTTP traffic
   config = FSNetConfiguration(http_pool=urllib3.HTTPConnectionPool('$HOST'))
   response = isu_find_update('$MAC', '$CUSTOM', '$VERSION', netconfig=config)

   # without custom netconfig -> HTTPS traffic
   response = isu_find_update('$MAC', '$CUSTOM', '$VERSION')
   for _software in response['updates']:
      isu_get_update('$FILE_PATH', software=_software)


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Developer Reference

   api/isu_format
   api/isu_product
   api/isu_update
   api/net/index
   api/ecmascript/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
