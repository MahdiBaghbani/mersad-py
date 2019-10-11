#!/usr/bin/env python3

# mersad/classical/mixalph_cipher.py
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

mersad.classical.mixalph_cipher module.
=====================================

The mixed alphabet cipher is a mono alphabetical
substitution cipher, it substitutes letters from
alphabet with letters from a cipher alphabet.

"""

# Python Standard Library
import argparse
import string
import sys
from typing import Dict
from typing import Tuple
from typing import Union

# Mersad Library
from mersad.util import string_manipulation
from mersad.util import type_check
from mersad.util.base_class import MersadClassicalBase
from mersad.util.terminal_app_tools import MainFunctionClassical
from mersad.util.terminal_app_tools import monoalphabetic_common_parser


def main(argv: Tuple[str] = tuple(sys.argv[1:])) -> None:
    """Execute program in terminal (cli application)."""
    # module descriptions.
    description: str = "Azadeh Afzar - Mersad Mixed Alphabet Cipher\n" \
                       + "Encrypt/Decrypt data with Atbash algorithm"
    epilog: str = "American Airlines saved $40,000 in 1987 when they eliminated" \
                  + "one olive from each salad served in first class."

    # create a parser and parse command line arguments.
    program = MixalphCipherMainFunction(list(argv), MixalphCipher, description,
                                        epilog, monoalphabetic_common_parser())
    program.process()


class MixalphCipher(MersadClassicalBase):
    r"""
    Mixed Alphabet cipher algorithm class.

    Create an instance like every other python class.

    Example:
    ==================================

    >>> agent = MixalphCipher(key="zxcvbnmlkjhgfdsaqwertyuiop")
    >>> # encrypt a string
    >>> agent.encrypt("Hail Julius Caesar.")
    "Hzkg Jtgkte Czbezw."

    ==================================

    ShiftCipher takes keyword arguments when initializing new instance.

    Valid kwargs keys are listed in below:
        - letter_sequence : (optional) alphabet for using in cipher.
        - sort_key        : (optional) a key for sorting alphabet.
        - shuffle         : (optional) randomize letter sequence order.
        - seed            : (optional)(requires shuffle) specifies a seed
                            for randomizing, default seed is 0.

    Agent uses predefined default values for each of above arguments if
    it isn't provided by the user, for above example the letter sequence
    is provided by user but not shuffle and seed, agent will use default values
    for shuffle and seed.

    Default letter sequence is set to "string.printable" except "\r".
    Default sort key is set to "string.printable" except "\r".
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
    >>> agent = MixalphCipher()
    >>> # override defaults.
    >>> agent.config(key="zxcvbnmlkjhgfdsaqwertyuiop")
    >>> # encrypt a string
    >>> agent.encrypt("Hail Julius Caesar.")
    "Hzkg Jtgkte Czbezw."

    ==================================
    """

    def show_sort_key(self) -> int:
        """
        Return the current sort key in self.configuration dictionary.

        :return : current sort key in use.
        :rtype  : int
        """
        return self.configuration["sort_key"]

    def _init_subroutines(self) -> None:
        """Extend _defaults dictionary with default value for sort_key."""
        self._defaults["sort_key"] = string.printable.replace("\r", "")

    def _config_subroutines(self, **kwargs: Union[int, str, bool]) -> None:
        """
        Assign values to self.configuration dictionary.

        :raise ValueError: if type of a dictionary value is wrong.
        """
        if "key" in kwargs and kwargs["key"] is not None:
            type_check.type_guard(kwargs["key"], str)
            self.configuration["key"] = kwargs["key"]

        if "sort_key" in kwargs:
            type_check.type_guard(kwargs["sort_key"], str)
            self.configuration["sort_key"] = kwargs["sort_key"]

    @staticmethod
    def _translator(text: str, **kwargs: Union[int, str, bool]) -> str:
        """
        Wrap the actual encryption/decryption function for class.

        :param text : string to be translated.
        :return     : translated text
        :rtype      : str
        """
        return mixalph_cipher_translator(text, **kwargs)


def mixalph_cipher_translator(text: str, **kwargs: Union[int, str, bool]) -> str:
    """
    Translate a string with Mixed Alphabet cipher algorithm.

    This cipher uses a key sequence for encryption, this key can be in any order
    for example plmkoijnbhuygvtfcrdxeszwaq and cipher encrypts message by
    simple substitution of this key with the ordered string from the letter of
    this key, the default ordered string from the letters of this key will be
    abcdefghijklmnopqrstuvwxyz and the mixedalph will replace letter like this:
    a -> p, b -> l, c -> m ...

    The final mapping is like:
    abcdefghijklmnopqrstuvwxyz (ordered string from letters of key)
    TO
    plmkoijnbhuygvtfcrdxeszwaq (key)

    You can also use a custom ordering apart of default one by giving the sort_key
    argument to the function, example:

    sort_key="mnopqrstuvwxyzabcdefghijkl"

    In this case mapping will be like:
    mnopqrstuvwxyzabcdefghijkl (custom order key)
    TO
    plmkoijnbhuygvtfcrdxeszwaq (key)

    Note: sort_key must contain ALL of letters which are in key, if it doesn't the
    program :raises ValueError:

    :param text                             : string to be translated.
    :param kwargs:
        key_sequence                        : the letter sequence for substitution.
        sort_key (optional)                 : a key for sorting alphabet.
        shuffle (optional)(default = False) : randomize letter sequence order.
        seed (optional)(requires shuffle)   : specify a seed for randomizing,
                                              default seed is 0.
        decrypt (optional)(default = False) : switch for encryption/decryption mode.
    :return                                 : translated text
    :rtype                                  : str
    """
    # for sake of readability and prettifying below code
    # I will assign aliases for key, values inside kwargs.
    key_sequence: str = kwargs["key"]
    if key_sequence is None:
        raise ValueError("ERROR: key isn't found, use config method to define a key")
    # default sort key to "string.printable" except "\r".
    default_sort_key: str = string.printable.replace("\r", "")
    sort_key: str = kwargs["sort_key"] if "sort_key" in kwargs else default_sort_key
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

    # shuffle  key sequence with respect to seed if shuffle is set to True.
    if shuffle:
        # shuffle sequence.
        key_sequence = string_manipulation.shuffle_string(key_sequence, seed)

    # create sorted cipher alphabet from letter sequence
    # first: check if every letter in key sequence is also in sort key
    for letter in key_sequence:
        if letter not in sort_key:
            raise ValueError("ERROR: sort key must contain all the letters in key.")

    # second: define the sorting function
    def _sort_key(x: str) -> int:
        """Sort key function."""
        # returns the index of a letter in sort_key string,
        # letters with lower indexes come closer to the left of final sorted string.
        return sort_key.index(x)

    # third: sort sequence with the sorted() builtin function
    # and custom _sort_key function
    plain_alphabet: str = "".join(sorted(key_sequence, key=_sort_key))

    # create a table mapping that maps every letter in sequence to
    # it's equivalent new letter.
    if decrypt:
        # when decrypting map sequence letters to key plain alphabet
        translated_sequence = {
            i: plain_alphabet[key_sequence.index(i)] for i in key_sequence
        }
    else:
        # when encrypting map plain alphabet letters to key sequence letters
        translated_sequence = {
            i: key_sequence[plain_alphabet.index(i)] for i in plain_alphabet
        }

    # type annotations
    translated_letter: str

    # select each letter in the text and only if it is also provided in sequence
    # from user and replace it with new letter.
    for letter in text:
        if letter in key_sequence:
            # get the translated letter for this letter from mapping
            translated_letter = translated_sequence[letter]
        else:
            # if the letter in the text isn't in sequence, it remains unchanged.
            translated_letter = letter
        # add new letter to translated string.
        translated += translated_letter

    return translated


class MixalphCipherMainFunction(MainFunctionClassical):
    """Manage Mixalph cipher programs execution from terminal."""

    def _config_agent(self, agent, args: argparse.Namespace) -> None:
        """Config the agent parameters in process method."""
        agent.config(
                key=args.key,
                sort_key=args.sort_key,
                shuffle=args.shuffle,
                seed=args.seed
        )

    def _custom_arguments(self) -> argparse.ArgumentParser:
        """
        Extend _base_parser method with subclass specific arguments.

        :return: parser
        :rtype: argparse.ArgumentParser
        """
        # create the parser.
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
                add_help=False
        )

        help_key: str = "key sequence for encryption/decryption"
        parser.add_argument("-k", "--key", type=str, required=True, help=help_key)

        help_sorted_key: str = "alphabet sort order"
        parser.add_argument("-so", "--sort_key", type=str,
                            default=string.printable.replace("\r", ""),
                            help=help_sorted_key)

        return parser
