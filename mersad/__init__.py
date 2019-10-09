# mersad/__init__.py
#
# This file is a part of:
# Azadeh Afzar - Mersad Cryptography Library in Python language (AA-MCLpy).
#
# Copyright (C) 2019 Azadeh Afzar
# Copyright (C) 2019 Mohammad Mahdi Baghbani Pourvahid
#
# GNU AFFERO GENERAL PUBLIC LICENSE
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ZLIB LICENSE
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgement in the product documentation would be
# appreciated but is not required.
#
# 2. Altered source versions must be plainly marked as such, and must not be
# misrepresented as being the original software.
#
# 3. This notice may not be removed or altered from any source distribution.
#

"""
Azadeh Afzar - Mersad Cryptography Library.

mersad package.
===============

This package contains various cryptographic algorithms,
separated into this sub groups:

- classical
- Modern

"""

# Python Standard Library
from typing import List

# Mersad Library
from mersad import _version

# AA-MCL package information
__author__: str = "Mohammad Mahdi Baghbani Pourvahid"
__description__: str = "Azadeh Afzar - Mersad Cryptographic Library"
__copyright__: str = "Copyright (C) 2019 Azadeh Afzar - Mersad Cryptography Library"
__credits__: List[str] = []
__license__: str = "AGPLv3"
__version__: str = _version.__version__
__maintainer__: str = "Mohammad Mahdi Baghbani Pourvahid"
__email__: str = "MahdiBaghbani@protonmail.com"
__status__: str = "Prototype"

# please keep alphabetical order
__all__: List[str] = [
    "classical",
    "test",
    "util",
    "_version"
]
