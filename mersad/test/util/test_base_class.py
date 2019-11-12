# mersad/test/util/test_base_class.py
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
import string
import unittest

# Mersad Library
from mersad.util.base_class import MersadClassicalBase


class TestMersadClassicalBase(unittest.TestCase):
    def setUp(self) -> None:
        self.BaseClass = MersadClassicalBase()

    def test_config(self):
        self.BaseClass.config(shuffle=True, seed=23, decrypt=True)
        self.assertEqual(None, self.BaseClass.configuration["key"])
        self.assertEqual(
            string.printable.replace("\r", ""),
            self.BaseClass.configuration["letter_sequence"],
        )
        self.assertEqual(23, self.BaseClass.configuration["seed"])
        self.assertEqual(True, self.BaseClass.configuration["shuffle"])
        self.assertEqual(True, self.BaseClass.configuration["decrypt"])

    def test_config_reset(self):
        self.BaseClass.config(shuffle=True, seed=23, decrypt=True)
        self.BaseClass.reset()
        self.assertEqual(None, self.BaseClass.configuration["key"])
        self.assertEqual(
            string.printable.replace("\r", ""),
            self.BaseClass.configuration["letter_sequence"],
        )
        self.assertEqual(False, self.BaseClass.configuration["shuffle"])
        self.assertEqual(0, self.BaseClass.configuration["seed"])
        self.assertEqual(False, self.BaseClass.configuration["decrypt"])

    def test_print_instance(self):
        self.BaseClass.config(
            letter_sequence="abc", shuffle=True, seed=23, decrypt=True
        )
        expected = "{0}: {1}.\n{2}: {3}.\n{4}: {5}.\n{6}: {7}.".format(
            "key", None, "letter_sequence", "abc", "shuffle", True, "seed", 23
        )
        self.assertEqual(expected, self.BaseClass.__str__())

    def test_config_bad_type(self):
        with self.assertRaises(TypeError):
            self.BaseClass.config(letter_sequence=12)

        with self.assertRaises(TypeError):
            self.BaseClass.config(seed=True)

        with self.assertRaises(TypeError):
            self.BaseClass.config(shuffle=2)

        with self.assertRaises(TypeError):
            self.BaseClass.config(decrypt="False")


if __name__ == "__main__":
    unittest.main()
