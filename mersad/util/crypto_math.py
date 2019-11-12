# mersad/util/crypto_math.py
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

mersad.util.crypto_math module.
===============================

This module provides mathematical functions for
evaluating cipher algorithms.

"""

# Python Standard Library
from typing import Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Implement extended Euclidean algorithm for gcd.

    in arithmetic and computer programming, the
    extended Euclidean algorithm is an extension
    to the Euclidean algorithm, and computes, in
    addition to the greatest common divisor of
    integers a and b, also the coefficients of
    Bezout's identity, which are integers x and y
    such that ax+by=gcd(a,b).

    :param a: first number.
    :param b: second number.
    :return: (g, x, y) such that a*x + b*y = g = gcd(a, b)
    :rtype: tuple
    """
    # assign variables
    last_x: int = 0
    last_y: int = 1
    x: int = 1
    y: int = 0
    last_remainder: int = abs(b)
    remainder: int = abs(a)

    while remainder:
        last_remainder, (quotient, remainder) = (
            remainder,
            divmod(last_remainder, remainder),
        )
        x, last_x = last_x - quotient * x, x
        y, last_y = last_y - quotient * y, y

    # fix signs
    last_x *= -1 if a < 0 else 1
    last_y *= -1 if b < 0 else 1

    # return (g, x, y) such that a*x + b*y = g = gcd(a, b)
    return last_remainder, last_x, last_y


def mod_inverse(a: int, b: int) -> int:
    """
    Find mod inverse of a mod b.

    :raise ValueError: if a and b are not co-prime.

    :param a: number that we want to find its mod inverse.
    :param b: number which is the mod.
    :return: mod inverse of a mod b
    :rtype: int
    """
    # calculate extended gcd and get (g, x, y) such that a*x + b*y = g = gcd(a, b)
    results: Tuple[int, int, int] = extended_gcd(a, b)
    # unpack g and x
    g: int = results[0]
    x: int = results[1]
    if g != 1:
        raise ValueError("mersad.util.crypto_math Error: a and b must be co-prime.")
    return x % b
