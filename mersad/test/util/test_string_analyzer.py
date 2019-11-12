# mersad/test/util/test_string_analyzer.py
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

# Python Standard Library
import unittest

# Mersad Library
from mersad.util import string_analyzer


class TestFindUniqeLetters(unittest.TestCase):
    def test(self):
        unique_letters = string_analyzer.find_unique_letters(
            "Is it UniQue? Or NoT ?! huh?"
        )
        expected_result = {
            "!",
            "?",
            "t",
            "s",
            "h",
            "Q",
            "N",
            "u",
            "U",
            "O",
            "T",
            "i",
            "n",
            "e",
            "o",
            "I",
            " ",
            "r",
        }
        self.assertEqual(expected_result, unique_letters)


class TestFindLetterIndexes(unittest.TestCase):
    def test(self):
        test_index = string_analyzer.find_letter_indexes(
            "Enumerate is an amazing Python function.", "a"
        )
        expected_result = [6, 13, 16, 18]
        self.assertEqual(expected_result, test_index)


class TestMapLettersToIndexes(unittest.TestCase):
    def test(self):
        test_indexes = string_analyzer.map_letters_to_indexes(
            "Hi Martin, I think my TextAnalyzer is working!"
        )
        expected_result = {
            "!": [45],
            "z": [31],
            "o": [39],
            "h": [14],
            "y": [20, 30],
            "w": [38],
            " ": [2, 10, 12, 18, 21, 34, 37],
            "s": [36],
            "i": [1, 7, 15, 35, 42],
            "m": [19],
            "A": [26],
            "H": [0],
            "t": [6, 13, 25],
            "T": [22],
            "I": [11],
            "a": [4, 28],
            "k": [17, 41],
            "e": [23, 32],
            "n": [8, 16, 27, 43],
            "g": [44],
            "x": [24],
            "r": [5, 33, 40],
            ",": [9],
            "M": [3],
            "l": [29],
        }
        self.assertEqual(expected_result, test_indexes)


if __name__ == "__main__":
    unittest.main()
