# mersad/test/classical/test_affine_cipher.py
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
import string
import unittest

# 3rd Party Library
from ErfanIO import ReaderIO

# Mersad Library
from mersad.classical.affine_cipher import AffineCipher


class TestShiftCipher(unittest.TestCase):
    def setUp(self) -> None:
        self.agent = AffineCipher()
        self.base_path = os.path.dirname(__file__).replace("mersad/test/classical", "mersad/test/asset/texts")
        self.plain_text = ReaderIO.read(os.path.join(self.base_path, "Long License File.txt"), "text")
        self.k125_sh0_s0 = ReaderIO.read(os.path.join(self.base_path, "AffineCipher-LLF-k125-sh0-s0.txt"), "text")
        self.k173_sh1_s0 = ReaderIO.read(os.path.join(self.base_path, "AffineCipher-LLF-k173-sh1-s0.txt"), "text")
        self.custom_alphabet = ReaderIO.read(
            os.path.join(self.base_path, "AffineCipher-LLF-alphabet-ascii-lowercase-k396-sh0-s0.txt"), "text")

    def test_encrypt_without_shuffle(self):
        self.agent.config(key=125, shuffle=False, seed=0)
        self.assertEqual(self.k125_sh0_s0, self.agent.encrypt(self.plain_text))

    def test_encrypt_with_shuffle_without_seed(self):
        self.agent.config(key=173, shuffle=True, seed=0)
        self.assertEqual(self.k173_sh1_s0, self.agent.encrypt(self.plain_text))

    def test_encrypt_with_custom_alphabet(self):
        alphabet = string.ascii_lowercase
        self.agent.config(key=396, letter_sequence=alphabet, shuffle=False, seed=0)
        self.assertEqual(self.custom_alphabet, self.agent.encrypt(self.plain_text))

    def test_decryption_without_shuffle(self):
        self.agent.config(key=125, shuffle=False, seed=0)
        self.assertEqual(self.plain_text, self.agent.decrypt(self.k125_sh0_s0))

    def test_decrypt_with_shuffle_without_seed(self):
        self.agent.config(key=173, shuffle=True, seed=0)
        self.assertEqual(self.plain_text, self.agent.decrypt(self.k173_sh1_s0))

    def test_temporary_key(self):
        # key is 173 which is stored in self.configuration dictionary
        self.agent.config(key=173, shuffle=False, seed=0)
        # use a temporary one time key (125) when encrypting/decrypting
        self.assertEqual(self.plain_text, self.agent.decrypt(self.k125_sh0_s0, key=125))
        # verify that key is still 173 in self.configuration dictionary
        self.assertEqual(173, self.agent.show_key())

    def test_temporary_key_to_permanent(self):
        # key is 173 which is stored in self.configuration dictionary
        self.agent.config(key=173, shuffle=False, seed=0)
        # use a new key (125) when encrypting/decrypting and make it permanent
        self.assertEqual(self.plain_text, self.agent.decrypt(self.k125_sh0_s0, key=125, replace_key=True))
        # verify that key is changed to 125 in self.configuration dictionary
        self.assertEqual(125, self.agent.show_key())

    def test_key_is_lower_than_alphabey_length(self):
        alphabet = string.ascii_lowercase
        self.agent.config(key=25, letter_sequence=alphabet, shuffle=False, seed=0)

        with self.assertRaises(ValueError):
            self.agent.encrypt(self.plain_text)

    def test_key_and_letter_sequence_length_not_relatively_prime(self):
        alphabet = string.ascii_lowercase
        self.agent.config(key=3456, letter_sequence=alphabet, shuffle=False, seed=0)

        with self.assertRaises(ValueError):
            self.agent.encrypt(self.plain_text)


if __name__ == '__main__':
    unittest.main()
