# mersad/util/string_analyzer.py
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

mersad.util.string_analyzer module.
===================================

This module provides functions to extract data
about a string.

"""

# Python Standard Library
from typing import Dict
from typing import List
from typing import Set

# Mersad Library
from mersad.util import type_check


def find_unique_letters(text: str) -> Set[str]:
    """
    Create a set of all letters in a string.

    :param text: string source.
    :return: a set of all unique letters in the string
    :rtype: set
    """
    # check types
    type_check.type_guard(text, str)
    # create and return set
    return set(text)


def find_letter_indexes(text: str, letter: str) -> List[int]:
    """
    List indexes of a letter in a string.

    This function returns a list of index of every occurrence
    of a letter in a string.

    :param text: string source
    :param letter: the letter to find all of its  occurrence indexes
    :return: list containing letters occurrence indexes
    :rtype: list
    """
    # check types
    type_check.type_guard(text, str)
    type_check.type_guard(letter, str)
    # return index list
    return [
        index for index, character in enumerate(text) if character == letter
    ]


def map_letters_to_indexes(text: str) -> Dict[str, List[int]]:
    """
    Create an index  mapping dictionary.

    Dictionary holds that maps every letter
    to a list of indexes of its occurrence in a given string

    :param text: string source for finding indexes letters in it.
    :return: a dictionary with letter as key and a list of indexes as value.
    :rtype: dict
    """
    # check types
    type_check.type_guard(text, str)

    # return a dictionary with letter as key and a list of indexes as value
    return {
        letter: find_letter_indexes(text, letter)
        for letter in find_unique_letters(text)
    }
