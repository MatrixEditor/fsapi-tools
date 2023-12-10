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
from __future__ import annotations

__doc__ = """
The backend used to find and download updates is located at ``update.wifiradiofrontier.com.``
To interact with the underlaying API, the isudata-module comes with three main-methods:

* ``url_get_update``,
* ``find_update`` and
* ``get_update``.

"""

import urllib3
import re
import dataclasses
import enum
import xml.etree.ElementTree as xmltree

from typing import Optional, Union
from fsapi.netconfig import FSNetConfiguration
from .product import RE_CUSTOMISATION, RE_VERSION

__all__ = [
    "ISU_FILE_PROVIDER_HOST",
    "ISUSoftwareElement",
    "UpdateError",
    "MalformedMACError",
    "CustomisationError",
    "VersionError",
    "UpdateStatus",
    "UpdateRequest",
    "url_find_update",
    "find_update",
    "get_update",
    "url_get_update",
]

###############################################################################
# Constants
###############################################################################
ISU_FILE_PROVIDER_HOST = "update.wifiradiofrontier.com"
ISU_EDGE_PROVIDER_HOST = "nuv-isu-cdn.azureedge.net"
ISU_REQUEST_HEADERS = {"User-Agent": "FSL IR/0.1", "Connection": "Close"}

# MAC-Address structure for internet radios:
# '002261' + 6 characters from hex-alphabet
RE_FSIR_MAC_ADDR = r"^(002261)[\w]{6}$"


###############################################################################
# Classes
###############################################################################
@dataclasses.dataclass
class ISUSoftwareElement:
    """This class contains all information needed to distinguish an update entry.

    Use the ``loadxml`` function to import data from an XML-Element.

    :param customisaton: The customisation string for this element.
    :param version: The version string for this element.
    :param download_url: The URL where the firmware binary is located
    :param mandatory: Indicates whether this update is mandatory
    :param md5hash: The calculated md5Hash for the firmware binary
    :param product: The product's name
    :param vendor: usually Frontier Silicon
    :param size: the file's size
    """

    customisation: Optional[str] = None
    version: Optional[str] = None
    download_url: Optional[str] = None
    mandatory: bool = False
    md5hash: Optional[str] = None
    product: Optional[str] = None
    size: int = 0
    vendor: str = "Frontier Silicon"
    summary: Optional[str] = None

    def loadxml(self, element: xmltree.Element):
        """Imports data from the given XML-Element."""
        if element is None:
            return
        self.customisation = element.get("customisation")
        self.version = element.get("version")
        self.download_url = element.find("download").text
        self.mandatory = element.find("mandatory").text == "True"
        self.product = element.find("product").text
        self.size = int(element.find("size").text)
        self.md5hash = element.find("md5").text
        self.summary = element.find("summary").text
        self.vendor = element.find("vendor").text


class UpdateError(Exception):
    """Base class for general update related errors."""
    pass


class MalformedMACError(UpdateError):
    """Raised if an invalid MAC address is passed."""


class CustomisationError(UpdateError):
    """Raised if an invalid customisation is passed."""
    pass


class VersionError(UpdateError):
    """Raised if an invalid version is passed."""
    pass


class UpdateStatus(enum.IntEnum):
    """Update status of an UpdateRequest."""

    NOT_FOUND = 404
    NOT_AVAILABLE = 304
    FOUND = 200
    ERROR = -1


@dataclasses.dataclass
class UpdateRequest:
    """Small storage class for update requests.

    Objects of this class can be utilized as follows:

    >>> request = find_update(...)
    >>> if request.has_update:
    ...     updates = request.updates
    ...
    """

    status: Union[UpdateStatus, int] = UpdateStatus.ERROR
    updates: list[ISUSoftwareElement] = dataclasses.field(default_factory=list)
    error: Optional[Exception] = None

    @property
    def has_update(self) -> bool:
        """Returns whether the request stores an actual :class:`ISUSoftwareElement`.

        :return: whether the status is set to ``FOUND`` and there is no error
        :rtype: bool
        """
        return self.status == UpdateStatus.FOUND and self.error is None


###############################################################################
# Functions
###############################################################################
def _url_find_update_add_parameters(url: str, parameters: dict) -> str:
    uri = "/FindUpdate.aspx?"
    return (
        url + uri + "&".join(["%s=%s" % (key, parameters[key]) for key in parameters])
    )


def url_find_update(mac, customisation, version) -> str:
    """Generates a new URL that can be used to query for newer software packages.

    :param mac: the MAC address
    :type mac: str
    :param customisation: the device's customisation
    :type customisation: str
    :param version: the current firmware version
    :type version: str
    :return: the created URL
    :rtype: str
    """
    return _url_find_update_add_parameters(
        "https://" + ISU_FILE_PROVIDER_HOST,
        {"mac": mac, "customisation": customisation, "version": version},
    )


def find_update(
    mac: str,
    customisation: str,
    version: str,
    netconfig: FSNetConfiguration = None,
) -> UpdateRequest:
    """Tries to find updates for the given version and customisation.

    :param mac: The MAC-Address string of a frontier silicon device in the following
                format: ``002261xxxxxx``. This string must start with ``002261``.
    :param customisation: Information about the used interface, module and version
                            number.
    :param version: As the name already states, the full version string.
    :param netconfig: if a custom configuration like a proxy should be used, this
                        object can be passed as a parameter

    :returns: a new instance of an :class:`UpdateRequest` that stores any occurred errors.
    """

    result = UpdateRequest()
    if not re.match(RE_FSIR_MAC_ADDR, mac):
        result.error = MalformedMACError(f"'{mac}' is not a valid FS MAC address.")
        return result

    if not re.match(RE_CUSTOMISATION, customisation):
        result.error = CustomisationError(
            f"Malformed customisation: '{customisation}' does not match r'{RE_CUSTOMISATION}'"
        )
        return result

    if not re.match(RE_VERSION, version):
        result.error = VersionError(
            f"Malformed version string: '{version}' does not match r'{RE_VERSION}'"
        )
        return result

    url = url_find_update(mac, customisation, version)
    try:
        if netconfig:
            response = netconfig.delegate_request("GET", url, ISU_REQUEST_HEADERS)
        else:
            pool = urllib3.HTTPSConnectionPool(
                host=ISU_FILE_PROVIDER_HOST, headers=ISU_REQUEST_HEADERS
            )
            response = pool.request("GET", url)
            pool.close()
    except urllib3.exceptions.PoolError as err:
        result.error = err
        return result

    if response.status == 404:
        result.status = UpdateStatus.NOT_FOUND
        return result
    elif response.status == 304:
        result.status = UpdateStatus.NOT_AVAILABLE
        return result

    if response.status != 200:
        result.status = UpdateStatus.ERROR
        return result
    else:
        result.status = UpdateStatus.FOUND
        try:
            content = str(response.data, "utf-8")
            # NOTE: The returned content is a HTML page with embedded
            # XML data.
            pos = content.find("<?xml")
            if pos == -1:
                result.status = UpdateStatus.ERROR
                result.error = UpdateError("Could not find XML document!")
                return result
            else:
                content = content[pos : pos + content.find("</updates>", pos) + 9]
                root = xmltree.fromstring(content)
                updates = []
                for software in root:
                    s = ISUSoftwareElement()
                    s.loadxml(software)
                    updates.append(s)

                result.updates.extend(updates)
        except Exception as err:
            result.error = err

        return result


def get_update(
    path: str,
    url: str = None,
    software: ISUSoftwareElement = None,
    netconfig: FSNetConfiguration = None,
):
    """Tries to download and save the firmware binary located at the given URL.

    :param path: an absolute or relative path to the output file
    :param url: optional the direct download link - if not set, the software parameter
                must be defined
    :param software: the software object containing the relevant data for downloading
                    the update file
    :param netconfig: if a custom configuration like a proxy should be used, this object
                        can be passed as a parameter
    """
    if not url and (not software or not software.download_url):
        raise UpdateError(
            "Invalid choice of parameters: either url or software has to be non null"
        )

    url = url if url else software.download_url
    try:
        if netconfig:
            response = netconfig.delegate_request(
                "GET", url, ISU_REQUEST_HEADERS, preload_content=False
            )
        else:
            if "https" not in url:
                url = url.replace("http", "https")
            pool = urllib3.HTTPSConnectionPool(
                host=url.split("/")[2], headers=ISU_REQUEST_HEADERS, timeout=5
            )
            response = pool.request("GET", url, preload_content=False)
    except urllib3.exceptions.PoolError as err:
        raise UpdateError from err

    if response.status != 200:
        raise UpdateError(f"Unexpected result code: {response.status}")
    else:
        try:
            with open(path, "wb") as _res:
                for chunk in response.stream(4096 * 16):
                    if chunk:
                        _res.write(chunk)
        except urllib3.exceptions.PoolError as err:
            raise UpdateError from err
    response.release_conn()


def url_get_update(name: str) -> str:
    """An URL generator for the given product descriptor.

    :param name: the customisation and version put toghether wither with a '`_V`'.
    :returns: the newly generated url where the firmware can be downloaded
    """
    parts = name.split("-")
    fs_part = None
    url = None

    # NOTE: Some firmware binaries contain different sub-interfaces, so
    # the FSXXXX module definition will be shifted to the right.
    for f in filter(lambda x: "FS" in x, parts):
        fs_part = f
        break

    if fs_part is None:
        # Venice 6 module will be inferred
        fs_part = "FS2026"

    if fs_part is not None:
        if fs_part == "FS2340":
            customisation = name.split("_V")[0]
            url = "https://%s/srupdates/srupdates/%s/%s.isu.bin" % (
                ISU_EDGE_PROVIDER_HOST,
                customisation,
                name,
            )
        elif fs_part == "FS5332":
            customisation = name.split("_")[0]
            url = "https://%s/nsupdates/nsupdates/%s/%s.ota.bin" % (
                ISU_EDGE_PROVIDER_HOST,
                customisation,
                name,
            )
        else:
            url = "https://%s/Update.aspx?f=/updates/%s.isu.bin" % (
                ISU_FILE_PROVIDER_HOST,
                name.replace("_V", "."),
            )

    return url
