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
__doc__ = '''
Products with the `Venice 8` module have a different directory archive structure
compared to the common modules `Venice 6` or `Venice X`. Notably, the stored files
in `Venice 8` modules primarily consist of graphical resources and script files
written in `ECMAScript`, also known as `ecma`.

To extract and uncompress the stored files, you can utilize the `ISUTool` tool or
directly execute the ``fsapi.isu`` module. The files that can be used within this
module have the `.es.bin` suffix, where `es` refers to ECMAScript.

Although there is no available binary structure definition for ECMAScript files,
this module attempts to read and extract data from the input files. Decompilation
of `.es.bin` files back to ECMAScript code might be considered as a potential feature
for future releases.
'''

from .esbin import (
    is_valid_ext,
    ES_BIN_SUFFIX,
    ES_BIN_MAGIC,
    ES_BIN_HEADER_LEN,
    Decompiler
)
from .opcode import (
    OPCODES,
    ECMASCRIPT_HDR_LEN,
    ECMASCRIPT_MAGIC_BYTES
)
