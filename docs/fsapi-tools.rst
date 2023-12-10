.. _fsapi_tools:

===========
FSAPI Tools
===========

This project offers not only the :ref:`isutool <isutool>` but also two additional tools that extend
its functionality. These tools provide valuable capabilities for decompiling binary XDR files and
interacting with internet radio devices. Let's explore these tools in more detail:

XDR Decompiler
--------------

This tool is designed to decompile binary XDR (eXternal Data Representation) files used by the ScriptMonkey
Javascript Engine in version 1.8. By utilizing this tool, you can reverse engineer XDR files and extract their
contents, making them more accessible for analysis and further processing.

.. code-block:: bash
    :caption: Decompiling all files recursively

    fsapi-xdr -d -r /path/to/directory -o /path/to/target

Note that this tool is still under development and under subject to changes. The following options are
implemented:

.. code-block:: text

    positional arguments:
    path                  The target file that will be used to operate on.

    optional arguments:
    -h, --help            show this help message and exit
    -d, --decompile       Indicates that the given input file should be decompiled.
    -o OUT, --out OUT     The path were the decompiled output should be saved.

    --use-decompiler DECOMPATH  Specifies the path to the decompiler.
    -r, --recurse               Indicates that all files in the given directory should be decompiled

FS NET-API
----------

With this tool, you can seamlessly interact with internet radio devices. It provides a convenient interface to
communicate with internet radio devices, enabling you to control various aspects such as playback, volume, station
selection, and more.

Fetching a Node's value
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console
    :caption: Fetch the *friendlyName* from host at *127.0.0.1*

    fsapi-ctl get netremote.sys.info.friendlyName 127.0.0.1
    > FSResponse('netRemote.sys.info.friendlyName', <Method.GET: 'GET'>)
        - status: <Status.FS_OK: 'FS_OK'>
        - value: 'MEDION'

    fsapi-ctl list netremote.sys.caps.eqBands 127.0.0.1
    > FSResponse('netRemote.sys.caps.eqBands', <Method.LIST_GET_NEXT: 'LIST_GET_NEXT'>)
        - status: <Status.FS_OK: 'FS_OK'>
        - value:
            [0] => <class 'fsapi.net.base.NodeListItem'>
                - label: 'Bass'
                - min: -7
                - max: 7
            [1] => <class 'fsapi.net.base.NodeListItem'>
                - label: 'Höhen'
                - min: -7
                - max: 7

.. note::
    The node's value will be displayed only if the status of the response
    is set to ``FS_OK``. Otherwise, an error will be shown:

    .. code-block:: console

        > FSResponse(/error/, <Method.GET: 'GET'>)
            - status: <Status.FS_TIMEOUT: 'FS_TIMEOUT'>

Viewing a node class
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
    :caption: View properties of ``netRemote.sys.caps.eqBands``

    fsapi-ctl view netremote.sys.caps.eqBands
    > BaseSysCapsEqBands (netRemote_sys_caps_eqBands_nt):
        - path: 'netRemote.sys.caps.eqBands'
        - readonly: True
        - cacheable: True
        - notifying: False
        - type: <class 'fsapi.net.base.NodeList'>
        - prototype:
            [0] => 'key'
                - length: 1
                - type: <ArgType.ARG_TYPE_U32: 20>
            [1] => 'label'
                - length: 32
                - type: <ArgType.ARG_TYPE_C8: 16>
            [2] => 'min'
                - length: 1
                - type: <ArgType.ARG_TYPE_S16: 22>
            [3] => 'max'
                - length: 1
                - type: <ArgType.ARG_TYPE_S16: 22>

Changing a Node's value
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
    :caption: Set the *friendlyName* of *127.0.0.1* to *Hello World*

    fsapi-ctl set netremote.sys.info.friendlyName "Hello World" 127.0.0.1
    > FSResponse('netRemote.sys.info.friendlyName', <Method.SET: 'SET'>)
        - status: <Status.FS_OK: 'FS_OK'>

Generating an Update-URL
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
    :caption: Find an update

    fsapi-ctl update check 127.0.0.1
    [!] No Update available.

Most of the time, there won't be an update available, but you can try tampering
with the generated request URL. You can retrieve it by simulating the update request.

.. code-block:: bash

    fsapi-ctl -X update check 127.0.0.1
    > URL: 'https://update.wifiradiofrontier.com/FindUpdate.aspx?mac=************&customisation=ir-mmi-FS2026-0500-0549&version=2.12.25c.EX72088-1A12'

The URL for the current firmware can be generated using the following command:

.. code-block:: bash

    fsapi-ctl -X update fetch 127.0.0.1 ./
    > URL: 'https://update.wifiradiofrontier.com/Update.aspx?f=/updates/ir-mmi-FS2026-0500-0549.2.12.25c.EX72088-1A12.isu.bin'

Download Firmware Updates
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
    :caption: Fetching one or multiple firmware binaries

    # fetching the current firmware of a device
    fsapi-ctl update fetch 127.0.0.1 /path/to/file
    # download all binaries from version numbers in a file
    fsapi-ctl update fetch -f updates.txt /path/to/directory/


Common Options
--------------

Here are some common options available in this tool:

.. code-block:: text

    usage: fsapi-ctl [-h] [-C] [-X] [-F] [--raw] {view,get,list,set,get-notifies,update,scan} ...

    options:
    -h, --help            show this help message and exit
    -C, --disable-color   Disables colorized output
    -X, --simulate        Simulates the request and prints the used URL.
    -F, --force-session   Creates a new session before running the command.
    --raw                 Prints XML output instead of pretty print.

    subcommands:
    Commands of this tool.

    {view,get,list,set,get-notifies,update,scan}
        view                Views properties of a node class
        get                 Fetches the value for the given nodes.
        list                Fetches values from a list node
        set                 Tries to apply a new value to a given node.
        get-notifies        Queries all notifies of the target device
        update              Firmware update related context.
        scan                Scans for known nodes on a device.


.. code-block:: text
    :caption: Common options for the *view* context are as follows:

    usage: fsapi-ctl view [-h] [-S] value

    positional arguments:
        value         The node path or search value

    options:
        -h, --help    show this help message and exit
        -S, --search  Searches for nodes with the provided base path.

.. code-block:: text
    :caption: Common options for the *get* context

    usage: fsapi-ctl get [-h] [--pin PIN] nodes [nodes ...] host

    positional arguments:
        nodes       The node paths to query.
        host        The target host's ip address or domain name.

    options:
        -h, --help  show this help message and exit
        --pin PIN   The device's PIN.


.. code-block:: text
    :caption: Common options for the *set* context

    usage: fsapi-ctl set [-h] [--pin PIN] node value host

    positional arguments:
        node        The node path (e.g. netRemote.sys.info.friendlyName).
        value       The new value to apply.
        host        The target host's ip address or domain name.

    options:
        -h, --help  show this help message and exit
        --pin PIN   The device's PIN.

.. code-block:: text
    :caption: Common options for the *list* context

    usage: fsapi-ctl list [-h] [--pin PIN] [--pos POS] [-N MAX_ITEMS] node host

    positional arguments:
        node                  The node path (unique identifier).
        host                  The target host's ip address or domain name.

    options:
        -h, --help                              Show this help message and exit
        --pin PIN                               The device's PIN.
        --pos POS                               Specifies the starting index position.
        -N MAX_ITEMS, --max-items MAX_ITEMS     The number of items to return.

.. code-block:: text
    :caption: Common options for the *update* context

    usage: fsapi-ctl update [-h] {check,fetch} ...

    positional arguments:
    {check,fetch}
        check        Queries for an update.
        fetch        Download of firmware binaries

    options:
    -h, --help     show this help message and exit

.. code-block:: text
    :caption: Common options for the *update check* context

    usage: fsapi-ctl update check [-h] [--pin PIN] target

    positional arguments:
        target      IP address or device version.

    options:
        -h, --help  show this help message and exit
        --pin PIN   The device's PIN.

.. code-block:: text
    :caption: Common options for the *update fetch* context

    usage: fsapi-ctl update fetch [-h] [-f] [--pin PIN] target dest

    positional arguments:
        target      The target IP address of input file.
        dest        The destination file or directory.

    options:
        -h, --help  show this help message and exit
        -f, --file  Specifies that an input file should be used.
        --pin PIN   The device's PIN.