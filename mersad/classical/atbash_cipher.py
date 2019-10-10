#!/usr/bin/env python3

# mersad/classical/atbash_cipher.py
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

mersad.classical.atbash_cipher module.
=====================================

The Atbash cipher is a particular type
of mono alphabetic cipher formed by taking
the alphabet (or abjad, syllabary, etc.)
and mapping it to its reverse, so that
the first letter becomes the last letter,
the second letter becomes the second to
last letter, and so on.

"""

# Python Standard Library
import sys
from typing import Dict
from typing import Union

# Mersad Library
from mersad.util import string_manipulation
from mersad.util.base_class import MainFunctionClassical
from mersad.util.base_class import MersadClassicalBase


def main() -> None:
    """Execute program in terminal (cli application)."""
    # module descriptions.
    description: str = "Azadeh Afzar - Mersad Atbash Cipher\n" \
                       + "Encrypt/Decrypt data with Atbash algorithm"
    epilog: str = "Many pig organs can be temporarily or sometimes permanently " \
                  "transplanted into humans."

    # create a parser and parse command line arguments.
    program = MainFunctionClassical(sys.argv[1:], AtbashCipher, description, epilog)
    program.process()


class AtbashCipher(MersadClassicalBase):
    r"""
    Atbash cipher algorithm class.

    Create an instance like every other python class.

    Atbash is key-less cipher so if you provide it with key,
    key won't affect the result.

    Example:
    ==================================

    >>> agent = AtbashCipher(letter_sequence="abcdefghijklmnopqrstuvwxyz")
    >>> # encrypt a string
    >>> agent.encrypt("Hail Julius Caesar.")
    "Hzro Jforfh Czvhzi."

    ==================================

    ShiftCipher takes keyword arguments when initializing new instance.

    Valid kwargs keys are listed in below:
        - letter_sequence : (optional) alphabet for using in cipher.
        - shuffle         : (optional) randomize letter sequence order.
        - seed            : (optional)(requires shuffle) specifies a seed
                            for randomizing, default seed is 0.

    Agent uses predefined default values for each of above arguments if
    it isn't provided by the user, for above example the letter sequence
    is provided by user but not shuffle and seed, agent will use default values
    for shuffle and seed.

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
    >>> agent = AtbashCipher()
    >>> # override defaults.
    >>> agent.config(letter_sequence="abcdefghijklmnopqrstuvwxyz")
    >>> # encrypt a string
    >>> agent.encrypt("Hail Julius Caesar.")
    "Hzro Jforfh Czvhzi."

    ==================================
    """

    @staticmethod
    def _translator(text: str, **kwargs: Union[int, str, bool]) -> str:
        """
        Wrap the actual encryption/decryption function for class.

        :param text : string to be translated.
        :return     : translated text
        :rtype      : str
        """
        return atbash_cipher_translator(text, **kwargs)


def atbash_cipher_translator(text: str, **kwargs: Union[int, str, bool]) -> str:
    """
    Translate a string with Atbash cipher algorithm.

    The Atbash cipher is a particular type of mono alphabetic cipher
    formed by taking the alphabet (or abjad, syllabary, etc.) and
    mapping it to its reverse, so that the first letter becomes the last
    letter, the second letter becomes the second to last letter, and so on.

    :param text                             : string to be translated.
    :param kwargs:
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
    # get length of letter sequence, minus 1 to be start from 0
    sequence_length: int = len(sequence) - 1
    # default shuffle to False if no shuffle is defined in kwargs.
    shuffle: bool = kwargs["shuffle"] if "shuffle" in kwargs else False
    # default seed to 0 if no seed is defined in kwargs.
    seed: int = kwargs["seed"] if "seed" in kwargs else 0

    # type annotations
    translated_sequence: Dict[str, str]
    # blank string.
    translated: str = ""

    # shuffle letter sequence with respect to seed if shuffle is set to True.
    if shuffle:
        # shuffle sequence.
        sequence = string_manipulation.shuffle_string(sequence, seed)

    # create a table mapping that maps every letter in sequence to
    # it's equivalent new letter with respect to the key and size of sequence.
    translated_sequence = {
        i: sequence[sequence_length - sequence.index(i)] for i in sequence
    }

    # type annotations
    translated_letter: str

    # select each letter in the text and only if it is also provided in sequence
    # from user and replace it with new letter .
    for letter in text:
        if letter in sequence:
            # get the translated letter for this letter from mapping
            translated_letter = translated_sequence[letter]
        else:
            # if the letter in the text isn't in sequence, it remains unchanged.
            translated_letter = letter
        # add new letter to translated string.
        translated += translated_letter

    return translated
