.. _ecmascript:

==========================
ECMAScript-Language module
==========================

Note that this module is still under development, so there is no gurantee that methods
will work without any errors.

.. automodule:: fsapi.ecmascript

.. toctree::
  :caption: Module Contents:
  :maxdepth: 1

  esbin

Basic usage (>=0.3.0)
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

  from fsapi import ecmascript

  # decompile the byte code from the given file
  decompiler_path = 'decompiler/ecma-decompiler'
  with ecmascript.Decompiler(decompiler_path, '<file>') as dc:
    # retrieve the source code as a string with
    code = str(dc)
    # or directly with
    code = dc.code

.. _ecma: https://www.ecma-international.org/publications-and-standards/standards/ecma-262/