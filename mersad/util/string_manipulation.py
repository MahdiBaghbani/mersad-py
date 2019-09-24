# mersad/util/string_manipulation.py
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

mersad.util.string_manipulation module.
=======================================

This module provides functions for modifying string objects.

"""

# Python Standard Library
import random
from typing import List


def shuffle_string(text: str, seed: int) -> str:
    """
    Shuffle letters in the string with random.shuffle.

    with seed parameter in can create identical strings
    from same source in multiple calls.

    :param text : string to be shuffled.
    :param seed : number for setting seed on random library.
    :return     : the shuffled string.
    :rtype      : str
    """
    random.seed(seed)
    letter_list: List[str] = list(text)
    random.shuffle(letter_list)
    return ''.join(letter_list)


def replace_letter_by_index(text: str, letter: str, indexes: List[int]) -> str:
    """
    Replace letters in specific index of a string with another letter.

    :param text     : string to be manipulated.
    :param letter   : the new letter which will be placed instead of old letters.
    :param indexes  : a list of indexes in the string that should be replaced with
                      new letter.
    :return         : new string with replaced letters.
    :rtype          : str
    """
    letter_list: List[str] = list(text)
    for index in indexes:
        letter_list[index] = letter
    return ''.join(letter_list)
