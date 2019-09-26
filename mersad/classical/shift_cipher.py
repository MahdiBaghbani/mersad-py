#!/usr/bin/env python3

# mersad/classical/shift_cipher.py
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

mersad.classical.shift_cipher module.
=====================================

The shift (also knows as caesar cipher) is a type
of mono alphabetical substitution cipher, in which
each letter in alphabet is replaced by a letter some
fixed number of positions down the alphabet.

"""

# Python Standard Library
from typing import Any
from typing import Dict
from typing import Union

# Mersad Library
from mersad.util import string_manipulation
from mersad.util.base_class import MersadClassicalBase


class ShiftCipher(MersadClassicalBase):
    """
    Shift cipher algorithm class.

    Create an instance like every other python class.

    Example:
    ==================================

    >>> agent = ShiftCipher(key=3453, letter_sequence="abcdefghijklmnopqrstuvwxyz")
    >>> # encrypt a string
    >>> agent.encrypt("Hail Julius Caesar.")
    'Hvdg Jpgdpn Cvznvm.'

    ==================================

    ShiftCipher takes keyword arguments when initializing new instance.

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
    Default letter sequence is set to "string.printable" .
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
    >>> agent = ShiftCipher()
    >>> # override defaults.
    >>> agent.config(key=3453, letter_sequence="abcdefghijklmnopqrstuvwxyz")
    >>> # encrypt a string
    >>> agent.encrypt("Hail Julius Caesar.")
    'Hvdg Jpgdpn Cvznvm.'

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
        return shift_cipher_translator(text, **kwargs)


def shift_cipher_translator(text: str, **kwargs: Any) -> str:
    """
    Translate a string with Shift cipher algorithm.

    Shift encryption/decryption algorithm:
    1. choose a sequence of letters.
    2. calculate its length.
    3. select letters of a string one by one.
    4. if the selected letter is also in the sequence.
    - 4.1. if selected letter isn't in sequence, it remains unchanged.
    5. find the letter index in the sequence.
    6. add key to index (if decrypting: subtract key from index).
    7. find the reminder of dividing the number you have obtained from step #6
       to sequence length.
    8. find new letter in the sequence at index of the number you have obtained
       from step #7.
    9. replace old letter with new letter.

    :param text                             : string to be translated.
    :param kwargs:
        key                                 : key for encrypt/decrypt.
        letter_sequence                     : the letter sequence which will be
                                              used for shifting letters.
        shuffle (optional)                  : randomize letter sequence order.
        seed (optional)(requires shuffle)   : specify a seed for randomizing,
                                              default seed is 0.
    :return                                 : translated text
    :rtype                                  : str
    """
    # for sake of readability and prettifying below code
    # I will assign aliases for kwargs["letter_sequence"]
    # and kwargs["key"], which is not necessary.
    sequence: str = kwargs["letter_sequence"]
    key: int = kwargs["key"]
    # length of sequence is needed for mathematical calculations.
    key_size: int = len(sequence)

    # type annotations
    translated_sequence: Dict[str, str]
    # blank string.
    translated: str = ""

    # shuffle letter sequence with respect to seed if shuffle is set to True.
    if kwargs["shuffle"]:
        # default seed to 0 if no seed is defined in kwargs.
        seed: int = kwargs["seed"] if "seed" in kwargs else 0
        # shuffle sequence.
        sequence = string_manipulation.shuffle_string(sequence, seed)

    # reverse key for decryption.
    if kwargs["decrypt"]:
        key *= -1

    # create a table mapping that maps every letter in sequence to
    # it's equivalent new letter with respect to the key and size of sequence.
    translated_sequence = {
        i: sequence[(sequence.index(i) + key) % key_size] for i in sequence
    }

    # select each letter in the text and only if it is also provided in sequence
    # from user and replace it with new letter selected by shift method.
    for letter in text:
        if letter in sequence:
            # below code is steps 6 to 8 all together which is actually executed
            # in initializing the translated_sequence dictionary.
            # get the translated letter for this letter from mapping
            translated_letter = translated_sequence[letter]
        else:
            # if the letter in the text isn't in sequence, it remains unchanged.
            translated_letter = letter
        # step 9
        # add new letter to translated string.
        translated += translated_letter

    return translated
