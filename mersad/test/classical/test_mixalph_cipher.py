# mersad/test/classical/test_mixalph_cipher.py
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
import os
import unittest

# 3rd Party Library
from ErfanIO import ReaderIO

# Mersad Library
from mersad.classical.mixalph_cipher import MixalphCipher
from mersad.classical.mixalph_cipher import main as mixalph_main


class TestShiftCipher(unittest.TestCase):
    def setUp(self) -> None:
        # setup path
        classical_path = os.path.abspath(os.path.dirname(__file__))
        test_path = os.path.abspath(os.path.dirname(classical_path))
        self.base_path = os.path.join(test_path, "asset", "texts")
        # create a cipher agent
        self.agent = MixalphCipher()
        self.plain_text = ReaderIO.read(
            os.path.join(self.base_path, "Long License File.txt"), "text"
        )
        self.sh0_s0 = ReaderIO.read(
            os.path.join(self.base_path, "MixalphCipher-LLF-sh0-s0.txt"), "text"
        )
        self.sh1_s0 = ReaderIO.read(
            os.path.join(self.base_path, "MixalphCipher-LLF-sh1-s0.txt"), "text"
        )
        self.custom_sort_key = ReaderIO.read(
            os.path.join(
                self.base_path,
                "MixalphCipher-LLF-sortkey-plmnkoijbhuygvcftrdxzsewaq-sh0-s0.txt",
            ),
            "text",
        )

    def test_encrypt_without_shuffle(self):
        self.agent.config(key="zxcvbnmlkjhgfdsaqwertyuiop", shuffle=False, seed=0)
        self.assertEqual(self.sh0_s0, self.agent.encrypt(self.plain_text))

    def test_encrypt_with_shuffle_without_seed(self):
        self.agent.config(key="zxcvbnmlkjhgfdsaqwertyuiop", shuffle=True, seed=0)
        self.assertEqual(self.sh1_s0, self.agent.encrypt(self.plain_text))

    def test_encrypt_with_custom_sort_key(self):
        self.agent.config(
            key="zxcvbnmlkjhgfdsaqwertyuiop",
            sort_key="plmnkoijbhuygvcftrdxzsewaq",
            shuffle=False,
            seed=0,
        )
        self.assertEqual(self.custom_sort_key, self.agent.encrypt(self.plain_text))

    def test_decryption_without_shuffle(self):
        self.agent.config(key="zxcvbnmlkjhgfdsaqwertyuiop", shuffle=False, seed=0)
        self.assertEqual(self.plain_text, self.agent.decrypt(self.sh0_s0))

    def test_decrypt_with_shuffle_without_seed(self):
        self.agent.config(key="zxcvbnmlkjhgfdsaqwertyuiop", shuffle=True, seed=0)
        self.assertEqual(self.plain_text, self.agent.decrypt(self.sh1_s0))

    def test_decrypt_with_custom_alphabet(self):
        self.agent.config(
            key="zxcvbnmlkjhgfdsaqwertyuiop",
            sort_key="plmnkoijbhuygvcftrdxzsewaq",
            shuffle=False,
            seed=0,
        )
        self.assertEqual(self.plain_text, self.agent.decrypt(self.custom_sort_key))

    def test_show_sort_key(self):
        sort_key = "plmnkoijbhuygvcftrdxzsewaq"
        self.agent.config(
            key="zxcvbnmlkjhgfdsaqwertyuiop",
            sort_key=sort_key,
            shuffle=False,
            seed=0,
        )
        self.assertEqual(sort_key, self.agent.show_sort_key())

    def test_none_key(self):
        self.agent.config(shuffle=False, seed=0)
        with self.assertRaises(ValueError):
            self.agent.encrypt(self.plain_text)

    def test_sort_key_doesnt_have_all_key_letters(self):
        self.agent.config(
            key="zxcvbnmlkjhgfdsaqwertyuiop",
            sort_key="plmnkoijb",
            shuffle=False,
            seed=0,
        )
        with self.assertRaises(ValueError):
            self.agent.encrypt(self.plain_text)

    def test_sort_key_have_more_letters_than_key(self):
        self.agent.config(
            key="zxcvbnmlkjhgfdsaqwertyuiop",
            sort_key="plmnkoijbhuygvcftrdxzsewaqABCDEFGHIJKLMNOP",
            shuffle=False,
            seed=0,
        )
        self.assertEqual(self.plain_text, self.agent.decrypt(self.custom_sort_key))

    def test_terminal_application(self):
        # mock up terminal arguments
        args = [
            "--file",
            "{}".format(os.path.join(self.base_path, "Long License File.txt")),
            "--output",
            "{}".format(os.path.join(self.base_path, "Test Mixalph Terminal.txt")),
            "--key",
            "zxcvbnmlkjhgfdsaqwertyuiop",
        ]

        # run main function
        mixalph_main(tuple(args))

        # test if it's ok
        result = ReaderIO.read(
            os.path.join(self.base_path, "MixalphCipher-LLF-sh0-s0.txt"), "text"
        )
        self.assertEqual(self.sh0_s0, result)


if __name__ == "__main__":
    unittest.main()
