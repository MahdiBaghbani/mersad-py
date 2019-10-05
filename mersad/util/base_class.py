# mersad/util/base_class.py
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

mersad.util.base_class module.
==============================

The module contains base (parent) classes for
Mersad's cipher classes.

"""

# Python Standard Library
import argparse
import string
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

# Mersad Library
from mersad._version import __version__
from mersad.util import type_check


class MersadClassicalBase(object):
    """
    Base class for classical cipher algorithms objects.

    This class provides a clean interface for building other
    cipher classes with it.

    Sub-classes should override self._translator method
    with their desired algorithm to make their class work
    as they want.
    """

    def __init__(self, **kwargs: Union[int, str, bool]) -> None:
        """
        Create an instance of the class.

        Example
        ======

        >>> agent = MersadClassicalBase(key=53, letter_sequence="abcdefghrstuvwxyz")

        AffineCipher takes keyword arguments when initializing new instance.

        Valid kwargs
        ============
        key             : (optional) primary key.
        letter_sequence : (optional) alphabet for using in cipher.
        shuffle         : (optional) randomize letter sequence order.
        seed            : (optional)(requires shuffle) specifies a seed for
                          randomizing, default seed is 0.

        Agent uses predefined default values for each of above arguments if
        it isn't provided by the user, for above example the key and letter sequence
        are provided by user but not shuffle and seed, agent will use default values
        for shuffle and seed.

        Default key is set to 0.
        Default letter sequence is set to "string.printable" except \r character.
        Default shuffle is set to False.
        Default seed is set to 0.

        Each instance has it's own unique configurations saved in
        self.configuration and can work independent from other instances.

        Configurations can be changed even after initialization via
        self.config() method.

        Example
        =======

        >>> agent = MersadClassicalBase()
        >>> # override defaults
        >>> agent.config(key=3453, letter_sequence="abcdefghijklmnopqrstuvwxyz")

        Note
        ====

        This class is just a parent class and can't encrypt/decrypt anything.
        """
        # private configuration dictionary that holds default values.
        # should not be changed by anyone!
        self._defaults: Dict[str, Any] = dict(
                key=0, letter_sequence=string.printable.replace("\r", ""),
                shuffle=False, seed=0, decrypt=False
        )
        # public configuration dictionary.
        self.configuration: Dict[str, Any] = dict()
        # set self.configuration to default values (default_configuration).
        self.reset()
        # process kwargs and update self.configuration values.
        self.config(**kwargs)

    def __str__(self) -> str:
        """
        Return the objects info as string.

        :return : information such as key, letter sequence and etc.
        :rtype  : str
        """
        key: int = self.configuration["key"]
        letter_sequence: str = self.configuration["letter_sequence"]
        shuffle: bool = self.configuration["shuffle"]
        seed: int = self.configuration["seed"]
        return "{0}: {1}.\n{2}: {3}.\n{4}: {5}.\n{6}: {7}.\n{8}: {9}.".format(
                "Agent type", type(self), "key", key, "letter_sequence",
                letter_sequence, "shuffle", shuffle, "seed", seed
        )

    def encrypt(self, plain_text: str, key: Optional[int] = None,
                replace_key: bool = False) -> str:
        """
        Encrypt a string.

        This function is a wrapper for self._process function.

        :param plain_text   :   (required) the string that will be encrypted.
        :param key          :   (optional) a new key for encryption.
        :param replace_key  :   (optional) if set to True, the provided new key
                                replaces old key at self.configuration.
        :return             :   encrypted string.
        :rtype              :   str
        """
        return self._process(plain_text, key, replace_key=replace_key, decrypt=False)

    def decrypt(self, cipher_text: str, key: Optional[int] = None,
                replace_key: bool = False) -> str:
        """
        Decrypt a string.

        This function is a wrapper for self._process function.

        :param cipher_text  :   (required) the string that will be decrypted.
        :param key          :   (optional) a new key for decryption.
        :param replace_key  :   (optional) if set to True, the provided new key
                                replaces old key at self.configuration.
        :return             :   decrypted string.
        :rtype              :   str
        """
        return self._process(cipher_text, key, replace_key=replace_key, decrypt=True)

    def config(self, **kwargs: Union[int, str, bool]) -> None:
        """
        Assign values to self.configuration dictionary.

        :raise ValueError: if type of a dictionary value is wrong.
        """
        if "letter_sequence" in kwargs:
            type_check.type_guard(kwargs["letter_sequence"], str)
            self.configuration["letter_sequence"] = kwargs["letter_sequence"]

        if "key" in kwargs and kwargs["key"] is not None:
            type_check.type_guard(kwargs["key"], int)
            self.configuration["key"] = kwargs["key"]

        if "seed" in kwargs:
            type_check.type_guard(kwargs["seed"], int)
            self.configuration["seed"] = kwargs["seed"]

        if "shuffle" in kwargs:
            type_check.type_guard(kwargs["shuffle"], bool)
            self.configuration["shuffle"] = kwargs["shuffle"]

        if "decrypt" in kwargs:
            type_check.type_guard(kwargs["decrypt"], bool)
            self.configuration["decrypt"] = kwargs["decrypt"]

    def reset(self) -> None:
        """Reset all configurations to defaults."""
        # deep copy default_configuration dictionary
        # into instance variable self.configuration.
        self.configuration = {i: j for (i, j) in self._defaults.items()}

    def show_key(self) -> int:
        """
        Return the current key in self.configuration dictionary.

        :return : current key in use.
        :rtype  : int
        """
        return self.configuration["key"]

    def _process(self, text: str, key: Optional[int], replace_key: bool,
                 decrypt: bool) -> str:
        """
        Handle the process for both encryption and decryption.

        :param text         : string to be processed.
        :param key          : key for encryption/decryption.
        :param decrypt      : switch for encryption/decryption.
        :param replace_key  : replace the old key in self.configuration
                              with new one.
        :return             : encrypted/decrypted string.
        :rtype              : str
        """
        # explicitly switch mode to encryption/decryption.
        self.config(decrypt=decrypt)

        # replace the old key in self.configuration with new key
        if replace_key:
            self.config(key=key)

        if key and not replace_key:
            # deep copy self.configuration dictionary into new dictionary to be used.
            configuration = {i: j for (i, j) in self.configuration.items()}
            # check key type to be compatible.
            type_check.type_guard(key, int)
            # change the key in the copied dictionary,
            # self.configuration key will remain unchanged.
            configuration["key"] = key
        else:
            # alias self.configuration dictionary to configuration
            # in this case configuration dictionary isn't a copy
            # and is just a pointer to self.configuration
            configuration = self.configuration

        # return a call to affine_cipher_translator function with
        # string and unpacked (prepended "**" is used to unpack the dictionary)
        # configuration dictionary as arguments.
        return self._translator(text, **configuration)

    @staticmethod
    def _translator(text: str, **kwargs: Union[int, str, bool]) -> str:
        """
        Wrap the actual encryption/decryption function for class.

        This method should be implemented in sub classes.

        :param text : string to be translated.
        :return     : translated text.
        :rtype      : str
        """
        return "Not Implemented in this class!"


class MainFunctionClassical(object):
    """
    Manage classical cipher programs execution from terminal.

    This class has a parser and a process function that controls
    all thw procedures needed for running classical ciphers from terminal.
    """

    def __init__(self, args: List[Any], agent_class, description: str, epilog: str) \
            -> None:
        """ Initialize instance with needed data """
        self.args: List[Any] = args
        self.agent_class = agent_class
        self.description: str = description
        self.epilog: str = epilog

    def process(self) -> None:
        """ Process program execution based on terminal arguments """
        args: argparse.Namespace = self.parse_args()
        # load text_input from file or terminal.
        # type annotations.
        text_input: str
        if args.file:
            text_input = args.file.read()
        else:
            text_input = args.text

        # construct a shift cipher agent with parsed arguments.
        agent = self.agent_class(
                key=args.key,
                letter_sequence=args.letters,
                shuffle=args.shuffle,
                seed=args.seed
        )
        # type annotations.
        text_output: str
        if args.decrypt:
            text_output = agent.decrypt(text_input)
        else:
            text_output = agent.encrypt(text_input)

        # write output to a file or show on terminal.
        if args.output:
            args.output.write(text_output)
        else:
            print(text_output)

    def parse_args(self) -> argparse.Namespace:
        """
        Start parsing terminal arguments.

        :return: terminal argument namespace.
        :rtype: argparse.Namespace
        """
        # create a parser with given arguments
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
                parents=[self._argparse_parent()],
                description=self.description,
                epilog=self.epilog,
                formatter_class=argparse.RawDescriptionHelpFormatter
        )

        # parse args and create a dictionary like namespace object.
        return parser.parse_args(args=self.args)

    @staticmethod
    def _argparse_parent() -> argparse.ArgumentParser:
        """
        Create base parser object.

        This function creates and returns a base parser
        for all classical ciphers.

        :return: parser
        :rtype: argparse.ArgumentParser
        """
        # create the parent parser, the base parser for creating
        # various other program specific parsers at the top of it.
        parent_parser: argparse.ArgumentParser = argparse.ArgumentParser(
                add_help=False
        )

        # display version
        version: str = f"Azadeh Afzar - Mersad Cryptography Library v{__version__}"
        parent_parser.add_argument("-V", "--version", action="version",
                                   version=version)

        help_key: str = "key for encryption/decryption"
        parent_parser.add_argument("key", type=int, help=help_key)

        # create an mutually exclusive group for parser, user should either
        # provide a filename or a text for the process.
        source_type = parent_parser.add_mutually_exclusive_group(required=True)

        help_file: str = "read a file and process it"
        source_type.add_argument("-f", "--file", help=help_file,
                                 type=argparse.FileType("r", encoding="UTF-8"))

        help_text: str = "read a text from terminal and process it"
        source_type.add_argument("-t", "--text", type=str, help=help_text)

        help_output: str = "write out the result into a file"
        parent_parser.add_argument("-o", "--output", help=help_output,
                                   type=argparse.FileType("w+", encoding="UTF-8"))

        help_decrypt: str = "decryption switch"
        parent_parser.add_argument("-d", "--decrypt", action="store_true",
                                   default=False, help=help_decrypt)

        help_letters: str = "alphabet for encryption/decryption, only letters " \
                            "which are also in this alphabet will be processed " \
                            "by program"
        parent_parser.add_argument("-l", "--letters", type=str,
                                   default=string.printable, help=help_letters)

        help_shuffle: str = "shuffle alphabet letters"
        parent_parser.add_argument("-sh", "--shuffle", action="store_true",
                                   default=False, help=help_shuffle)

        help_seed: str = "specify random seed for shuffling the alphabet"
        parent_parser.add_argument("-s", "--seed", type=int, default=0,
                                   help=help_seed)

        return parent_parser
