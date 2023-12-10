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
__doc__ = """
In order to store and identify each part of the firmware-version and -customisation
string, the classes ``FSCustomisation`` and ``FSVersion`` were created. Additionally,
there are two RegEx-strings that are used to verify the given verison or customisation
string::

  # e.g. ir-mmi-FS2026-0500-0015
  RE_CUSTOMISATION = r"^\w*-\w*-(FS\d{4})-\d{4}-\d{4}"

  # e.g. 2.6.17c4.EX53330-V1.08
  RE_VERSION = r"^\d*([.][\d]*\w*\d*){2}[.].*-.*"

Both classes mentioned above can be created with and without their attributes. To load
a verison or customisation string, you can use the ``loads()`` method in both classes.
"""

__all__ = [
    "FSCustomisation",
    "FSVersion",
    "RE_CUSTOMISATION",
    "RE_VERSION",
    "FSVERSION_MODULE_TYPES",
]

# Structure of each customisation: The following BNF-declarations should
# cover all firmware customisations that were found and downloadable. At
# fist, the <device_type> has to be specified as it defines the first
# section of the customisation string:
#
# <device_type>       := <type> '-' <interface>
# <type>              := 'ir' | 'ns' | 'dab'
# <interface>         := <interface_name> [ '-' <sub_type> ]
# <interface_name>    := 'mmi' | 'cui' | 'ser' | 'fsccp'
# <sub_type>          := 'scb' | '16m'
#
# The next section covers the used module version and model:
#
# <module>         := <module_type> '-' <module_version> '-' <product> [ '_' <spec> ]
# <module_type>    := 'FS' NUMBER{4}
# <module_version> := NUMBER{4}
# <product>        := NUMBER{4}
# <spec>           := ( CHAR* | NUMBER* )*
# @PendingDeprecationWarning
RE_CUSTOMISATION = r"^\w*-\w*-(FS\d{4})-\d{4}-\d{4}(_\w*)*"

# Structure of each version: The following BNF-declarations should
# cover all firmware versions:
#
# <version> := <release> '.' <feature> '.' <patch> '.' <revision> [ '-' <branch> ]
# <release  := NUMBER{1}
# <feature> := NUMBER{1, 2}
# <patch> := NUMBER{1, 2} [ CHAR{1} [ NUMBER{1, 2} ] ]
# <revision> := [ 'EX' ] NUMBER{5}
# <branch> := ( 'V' NUMBER{1, 2} '.' NUMBER{1, 2} | NUMBER{1} [ CHAR{1} ]
#                NUMBER{1, 2} [ CHAR{1} ] ) [ '-' <branch> ]
RE_VERSION = r"^\d*([.][\d]*\w*\d*){2}[.].*-.*"

# Each datasheet can be downloaded from the following URL:
# https://www.electronicsdatasheets.com/manufacturers/frontier-silicon/parts/
FSVERSION_MODULE_TYPES = {
    "FS1230": "Chorus 3",
    "FS1235": "Kino",
    "FS2025": "Venice 5",
    "FS2026": "Venice 6",
    "FS2027": "Venice 7",
    "FS2028": "Venice 8",
    "FS2029": "Venice 9",
    "FS2052": "Verona",
    "FS2230": "Tuscany",
    "FS2240": "Roma",
    "FS2340": "Venice X",
    "FS2445": "Verona 2",
    "FS4052": "Venus",
    "FS4053": "Venus 2I-L",
    "FS4230": "Neptune",
    "FS4240": "Ceres",
    "FS4255": "Venus-H2",
    "FS5332": "Minuet",
}


class FSCustomisation:
    """Customisation for Frontier-Smart products."""

    def __init__(self) -> None:
        self.device_type: str = ""
        self.type_spec: str = ""
        self.interface: str = ""
        self.interface_sub_types: list = []
        self.module_type: str = ""
        self.module_version: str = ""
        self.product: str = ""
        self.spec: str = ""
        self.string: str = ""
        self.module_name: str = ""

    def loads(self, buffer: str):
        """Tries to parse the given string

        :param buffer: the input to parse
        :type buffer: str
        """
        if not buffer:
            return

        content = buffer.split("-")
        self.string = buffer
        self.type_spec = content[0]
        self.interface = content[1]

        idx = 2
        while "FS" not in content[idx]:
            self.interface_sub_types.append(content[idx])
            idx += 1

        self.device_type = "-".join(
            [self.type_spec, self.interface] + self.interface_sub_types
        )
        self.module_type = content[idx]
        self.module_version = content[idx + 1]
        self.product = content[idx + 2]

        if "_" in self.product:
            values = self.product.split("_")
            self.product = values[0]
            self.spec = values[1]

        if self.module_type in FSVERSION_MODULE_TYPES:
            self.module_name = FSVERSION_MODULE_TYPES[self.module_type]

    def get_module_name(self) -> str:
        """Returns the printable module name of this customisation.

        :return: the module name
        :rtype: str
        """
        return self.module_name

    def __str__(self) -> str:
        if not self.string:
            # Try to build the representation string
            self.string = (
                f"{self.device_type}-{self.module_type}-{self.module_version}"
                f"-{self.product}_{self.spec}"
            )
        return self.string


class FSVersion:
    """Frontier-Smart version representation."""

    def __init__(
        self,
        firmware_version: str = None,
        sdk_version: str = None,
        revision: str = None,
        branch: str = None,
    ) -> None:
        self.firmware_version = firmware_version
        self.string = None
        self.sdk_version = sdk_version
        self.revision = revision
        self.branch = branch

    def loads(self, buffer: str):
        """Parses the given input.

        :param buffer: the full version representation
        :type buffer: str
        """
        # TODO: error handling
        index = buffer.rindex(".")
        self.firmware_version = buffer[:index]
        self.sdk_version = "IR" + self.firmware_version + " SDK"
        temp = buffer[index + 1 :]
        self.revision = temp[2:7]
        self.string = buffer

    def __str__(self) -> str:
        return self.string
