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
from mersad.util.base_class import MainFunctionClassical
from mersad.util.base_class import MersadClassicalBase


class TestMersadClassicalBase(unittest.TestCase):
    def setUp(self) -> None:
        self.BaseClass = MersadClassicalBase()

    def test_config(self):
        self.BaseClass.config(key=12, shuffle=True, seed=23, decrypt=True)
        self.assertEqual(12, self.BaseClass.configuration["key"])
        self.assertEqual(string.printable.replace("\r", ""),
                         self.BaseClass.configuration["letter_sequence"])
        self.assertEqual(23, self.BaseClass.configuration["seed"])
        self.assertEqual(True, self.BaseClass.configuration["shuffle"])
        self.assertEqual(True, self.BaseClass.configuration["decrypt"])

    def test_config_reset(self):
        self.BaseClass.config(shuffle=True, seed=23, decrypt=True)
        self.BaseClass.reset()
        self.assertEqual(0, self.BaseClass.configuration["key"])
        self.assertEqual(string.printable.replace("\r", ""),
                         self.BaseClass.configuration["letter_sequence"])
        self.assertEqual(False, self.BaseClass.configuration["shuffle"])
        self.assertEqual(0, self.BaseClass.configuration["seed"])
        self.assertEqual(False, self.BaseClass.configuration["decrypt"])

    def test_process_replace_manual_key(self):
        self.BaseClass.config(key=12)
        self.BaseClass.encrypt("It's a dummy text!", key=16, replace_key=True)
        self.assertEqual(16, self.BaseClass.configuration["key"])

    def test_return_key(self):
        self.BaseClass.config(key=12)
        self.assertEqual(12, self.BaseClass.show_key())

    def test_config_bad_type(self):
        with self.assertRaises(TypeError):
            self.BaseClass.config(letter_sequence=12)

        with self.assertRaises(TypeError):
            self.BaseClass.config(key="Hello There!")

        with self.assertRaises(TypeError):
            self.BaseClass.config(seed=True)

        with self.assertRaises(TypeError):
            self.BaseClass.config(shuffle=2)

        with self.assertRaises(TypeError):
            self.BaseClass.config(decrypt="False")


class TestMainFunctionClassical(unittest.TestCase):
    def setUp(self) -> None:
        args = ["10", "--text", "Yup, not funny"]
        agent_class = MersadClassicalBase
        description = "Dummy Dummy Test."
        epilog = "Oh shit here we go again ..."
        self.main = MainFunctionClassical(args, agent_class, description, epilog)

    def test_parent_parser(self):
        args = ["--key", "23", "--text", "wow, is this a test?", "--output",
                "fail.txt", "--decrypt", "--shuffle", "--seed", "12"]
        parent = self.main._argparse_parent()
        args = parent.parse_args(args)
        self.assertEqual(23, args.key)
        self.assertEqual("wow, is this a test?", args.text)
        self.assertEqual("fail.txt", args.output)
        self.assertEqual(True, args.decrypt)
        self.assertEqual(True, args.shuffle)
        self.assertEqual(12, args.seed)


if __name__ == '__main__':
    unittest.main()
