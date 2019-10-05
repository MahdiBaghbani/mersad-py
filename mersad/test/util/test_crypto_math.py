# mersad/test/util/test_crypto_math.py
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
from mersad.util.crypto_math import extended_gcd
from mersad.util.crypto_math import mod_inverse


class TestCryptoMath(unittest.TestCase):
    def test_extended_gcd(self):
        test_extended_gcd_1 = extended_gcd(12134, 15)
        expected_result_1 = (1, -1, 809)
        self.assertEqual(expected_result_1, test_extended_gcd_1)
        test_extended_gcd_2 = extended_gcd(80, 1234)
        expected_result_2 = (2, 108, -7)
        self.assertEqual(expected_result_2, test_extended_gcd_2)

    def test_mod_inverse(self):
        test_mod_inverse_1 = mod_inverse(3, 26)
        expected_result_1 = 9
        self.assertEqual(expected_result_1, test_mod_inverse_1)
        test_mod_inverse_2 = mod_inverse(15413, 26)
        expected_result_2 = 5
        self.assertEqual(expected_result_2, test_mod_inverse_2)


if __name__ == '__main__':
    unittest.main()
