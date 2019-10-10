#!/usr/bin/env python3

# mersad/classical/affine_cipher.py
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

mersad.classical.affine_cipher module.
======================================

The affine is a type of mono alphabetical substitution
cipher, wherein each letter in an alphabet is mapped to
its numeric equivalent, encrypted using a single mathematical
function, and converted back to a letter.

"""

# Python Standard Library
import sys
from math import gcd
from typing import Dict
from typing import Union

# Mersad Library
from mersad.util import crypto_math
from mersad.util import string_manipulation
from mersad.util import type_check
from mersad.util.base_class import MainFunctionClassical
from mersad.util.base_class import MersadClassicalBase


def main() -> None:
    """Execute program in terminal (cli application)."""
    # module descriptions.
    description: str = "Azadeh Afzar - Mersad Affine Cipher\n" \
                       + "Encrypt/Decrypt data with Affine"
    epilog: str = "CIA can still read your messages ..."

    # create a parser and parse command line arguments.
    program = MainFunctionClassical(sys.argv[1:], AffineCipher, description, epilog)
    program.process()


class AffineCipher(MersadClassicalBase):
    r"""
    Affine cipher algorithm class.

    Create an instance like every other python class.

    Example:
    ==================================

    >>> agent = AffineCipher(key=235, letter_sequence="abcdefghijklmnopqrstuvwxyz")
    >>> # encrypt a string
    >>> agent.encrypt("Is this really more secure than shift cipher?")
    'Ih qmvh ylbwwj fxyl hltzyl qmbo hmvuq tvgmly?'

    ==================================

    AffineCipher takes keyword arguments when initializing new instance.

    Valid kwargs keys are listed in below:
        - key             : (optional) primary key.
        - letter_sequence : (optional) alphabet for using in cipher.
        - shuffle         : (optional) randomize letter sequence order.
        - seed            : (optional)(requires shuffle) specifies a seed
                            for randomizing, default seed is 0.

    Agent uses predefined default values for each of above arguments if
    it isn't provided by the user, for above example the key and letter sequence
    are provided by user but not shuffle and seed, agent will use default values
    for shuffle and seed.

    Default key is set to 0.
    Default letter sequence is set to "string.printable" except "\r".
    Default shuffle is set to False.
    Default seed is set to 0.

    Each instance has it's own unique configurations saved in
    self.configuration and can work independent from other instances.

    Configurations can be changed even after initialization via
    self.config() method.

    Example:
    ==================================

    >>> # create object without any keyword arguments so agent will use
    >>> # default values for all the settings.
    >>> agent = AffineCipher()
    >>> # override defaults.
    >>> agent.config(key=135)
    >>> # encrypt a string
    >>> agent.encrypt("Is this really more secure than shift cipher?")
    '<"t#QR"t!NJUU(tVX!Nt"NL$!Nt#QJWt"QRO#tLRYQN!h'

    ==================================
    """

    def _config_subroutines(self, **kwargs: Union[int, str, bool]) -> None:
        """
        Assign values to self.configuration dictionary.

        :raise ValueError: if type of a dictionary value is wrong.
        """
        if "key" in kwargs and kwargs["key"] is not None:
            type_check.type_guard(kwargs["key"], int)
            self.configuration["key"] = kwargs["key"]

    @staticmethod
    def _translator(text: str, **kwargs: Union[int, str, bool]) -> str:
        """
        Wrap the actual encryption/decryption function for class.

        :param text : string to be translated.
        :return     : translated text
        :rtype      : str
        """
        return affine_cipher_translator(text, **kwargs)


def affine_cipher_translator(text: str, **kwargs: Union[int, str, bool]) -> str:
    """
    Translate a string with Affine cipher algorithm.

    :param text                             : string to be translated.
    :param kwargs:
        key                                 : key for encrypt/decrypt.
        letter_sequence                     : alphabet for encryption/decryption.
        shuffle (optional)(default = False) : randomize letter sequence order.
        seed (optional)(requires shuffle)   : specify a seed for randomizing,
                                              default seed is 0.
        decrypt (optional)(default = False) : switch for encryption/decryption mode.
    :return                                 : translated text
    :rtype                                  : str
    """
    # for sake of readability and prettifying below code
    # I will assign aliases for key, values inside kwargs.
    sequence: str = kwargs["letter_sequence"]
    # length of sequence is needed for mathematical calculations.
    sequence_length: int = len(sequence)
    # key alias.
    key: int = kwargs["key"]
    # check key is not None
    if key is None:
        raise ValueError("ERROR: key isn't found, use config method to define a key")
    # type annotations
    key_a: int
    key_b: int
    # generate partial keys.
    key_a, key_b = divmod(key, sequence_length)
    # validate keys.
    _check_keys(key_a, key_b, sequence_length)
    # default shuffle to False if no shuffle is defined in kwargs.
    shuffle: bool = kwargs["shuffle"] if "shuffle" in kwargs else False
    # default seed to 0 if no seed is defined in kwargs.
    seed: int = kwargs["seed"] if "seed" in kwargs else 0
    # default decrypt to False if no decrypt is defined in kwargs.
    decrypt: bool = kwargs["decrypt"] if "decrypt" in kwargs else False

    # type annotations
    translated_sequence: Dict[str, str]
    # blank string.
    translated: str = ""

    # shuffle letter sequence with respect to seed if shuffle is set to True.
    if shuffle:
        # shuffle sequence
        sequence = string_manipulation.shuffle_string(sequence, seed)

    # create a table mapping that maps every letter in sequence to
    # it's equivalent new letter with respect to the key and size of sequence.
    if decrypt:
        # find mode inverse of key a.
        key_a_mode_inverse = crypto_math.mod_inverse(key_a, sequence_length)
        # generate decryption letter sequence map.
        translated_sequence = {
            i: sequence[
                ((sequence.index(i) - key_b) * key_a_mode_inverse) % sequence_length
                ]
            for i in sequence
        }
    else:
        # generate encryption letter sequence map.
        translated_sequence = {
            i: sequence[(sequence.index(i) * key_a + key_b) % sequence_length]
            for i in sequence
        }

    # select each letter in the text and only if it is also provided in sequence
    # from user and replace it with new letter.
    for letter in text:
        if letter in sequence:
            # get the translated letter for this letter from mapping.
            translated_letter = translated_sequence[letter]
        else:
            # if the letter in the text isn't in sequence, it remains unchanged.
            translated_letter = letter
        # add new letter to translated string.
        translated += translated_letter

    return translated


def _check_keys(key_a: int, key_b: int, sequence_length: int) -> None:
    """
    Check if keys are in correct range.

    :param key_a            : first key.
    :param key_b            : second key.
    :param sequence_length  : length of letter sequence.
    :raise ValueError       : if keys are incorrect.
    """
    # test for invalid key range
    if key_a <= 0:
        raise ValueError(
                "The affine cipher's 'key a' must be greater than 0. "
                + "Change your key."
        )

    if not (0 <= key_b <= sequence_length - 1):
        raise ValueError(
                "The affine cipher's 'key b' must be in this range: "
                + "0 <= 'key b' <= length of letter sequence - 1. "
                + "Change your key."
        )

    if gcd(key_a, sequence_length) != 1:
        raise ValueError(
                "The affine cipher's 'key a' and length of 'letter "
                + "sequence' are not relatively prime. Change your key."
        )
