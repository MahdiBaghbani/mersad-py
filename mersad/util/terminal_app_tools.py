# mersad/util/terminal_app_tools.py
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

mersad.util.terminal_app_tools.py module.
==============================

The module contains tools to run
Mersad programs in terminal.

"""

# Python Standard Library
import argparse
import string
from typing import Any
from typing import List
from typing import Type
from typing import TypeVar

# Mersad Library
from mersad._version import __version__
from mersad.util.base_class import MersadClassicalBase

# define a new type hint.
MCLCryptClass = TypeVar("MCLCryptClass", bound=MersadClassicalBase)


class MainFunctionClassical(object):
    """
    Manage classical cipher programs execution from terminal.

    This class has a parser and a process function that controls
    all the procedures needed for running classical ciphers from terminal.
    """

    def __init__(
        self,
        args: List[Any],
        agent_class: Type[MCLCryptClass],
        description: str,
        epilog: str,
        predefined_parser: argparse.ArgumentParser,
    ) -> None:
        """
        Initialize instance with needed data.

        :param args: terminal arguments, usually sys.argv[1:].
        :param agent_class: the cipher class without parentheses.
        :param description: a string describing program.
        :param epilog: a string to be printed at the end of help message.
        :param predefined_parser: an existing external arg parser to be used.
        """
        self.args: List[Any] = args
        self.agent_class: Type[MCLCryptClass] = agent_class
        self.description: str = description
        self.epilog: str = epilog
        self.predefined_parser: argparse.ArgumentParser = predefined_parser

    def process(self) -> None:
        """Process program execution based on terminal arguments."""
        # parse terminal arguments
        args: argparse.Namespace = self._parse_args()

        # load text_input from file or terminal.
        # type annotations.
        text_input: str
        if args.file:
            with open(args.file, "r") as file:
                text_input = file.read()
        else:
            text_input = args.text

        # construct a shift cipher agent with parsed arguments.
        agent = self.agent_class()

        # config agent.
        self._config_agent(agent, args)

        # type annotations.
        text_output: str
        if args.decrypt:
            text_output = agent.decrypt(text_input)
        else:
            text_output = agent.encrypt(text_input)

        # write output to a file or show on terminal.
        if args.output:
            with open(args.output, "w+") as file:
                file.write(text_output)
        else:
            print(text_output)

    def _config_agent(
        self, agent: Type[MCLCryptClass], args: argparse.Namespace
    ) -> None:
        """
        Config the agent parameters in process method.

        This method should be implemented in subclasses.
        """

    def _parse_args(self) -> argparse.Namespace:
        """
        Start parsing terminal arguments.

        :return: terminal argument namespace.
        :rtype: argparse.Namespace
        """
        # create parent parsers for the final parser
        # this includes the main parent and the custom
        # subclass specific arguments.
        base_parser: argparse.ArgumentParser = self._base_parser()
        custom_arguments: argparse.ArgumentParser = self._custom_arguments()

        # create a parser list.
        parent_parser_list: List[argparse.ArgumentParser] = list()
        # add parsers to parser list if they aren't None.
        if custom_arguments:
            parent_parser_list.append(custom_arguments)
        if self.predefined_parser:
            parent_parser_list.append(self.predefined_parser)
        if base_parser:
            parent_parser_list.append(base_parser)

        # create a parser with given arguments.
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
            parents=parent_parser_list,
            description=self.description,
            epilog=self.epilog,
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )

        # parse args and create a dictionary like namespace object.
        return parser.parse_args(args=self.args)

    def _custom_arguments(self) -> argparse.ArgumentParser:
        """
        Extend _base_parser method with subclass specific arguments.

        This method should return a parser with add_help=False that
        has the subclass specific arguments to extend the parent parser.

        :return: parser
        :rtype: argparse.ArgumentParser
        """

    @staticmethod
    def _base_parser() -> argparse.ArgumentParser:
        """
        Create base parser.

        This function creates and returns a base parser
        for all classical ciphers.

        :return: parser
        :rtype: argparse.ArgumentParser
        """
        # create the parent parser, the base parser for creating
        # various other program specific parsers at the top of it.
        parser: argparse.ArgumentParser = argparse.ArgumentParser(add_help=False)

        # create an mutually exclusive group for parser, user should either
        # provide a filename or a text for the process.
        source_type = parser.add_mutually_exclusive_group(required=True)

        help_file: str = "file path for reading data from it"
        source_type.add_argument("-f", "--file", type=str, help=help_file)

        help_text: str = "read data from terminal"
        source_type.add_argument("-t", "--text", type=str, help=help_text)

        help_output: str = "file path for writing the result into it"
        parser.add_argument("-o", "--output", type=str, help=help_output)

        help_decrypt: str = "decrypt data"
        parser.add_argument(
            "-d", "--decrypt", action="store_true", default=False, help=help_decrypt
        )

        # display version.
        version: str = f"Azadeh Afzar - Mersad Cryptography Library v{__version__}"
        parser.add_argument("-V", "--version", action="version", version=version)

        return parser


def monoalphabetic_common_parser() -> argparse.ArgumentParser:
    """
    Create a parser with common arguments of monoalphabetic ciphers.

    This function creates and returns a parser
    for monoalphabetic ciphers common arguments.

    :return: parser
    :rtype: argparse.ArgumentParser
    """
    # create the parent parser, the base parser for creating
    # various other program specific parsers at the top of it.
    parser: argparse.ArgumentParser = argparse.ArgumentParser(add_help=False)

    help_letters: str = "alphabet for encryption/decryption"
    parser.add_argument(
        "-l",
        "--letters",
        type=str,
        default=string.printable.replace("\r", ""),
        help=help_letters,
    )

    help_shuffle: str = "shuffle alphabet letters"
    parser.add_argument(
        "-sh", "--shuffle", action="store_true", default=False, help=help_shuffle
    )

    help_seed: str = "specify random seed for shuffling the alphabet letters"
    parser.add_argument("-s", "--seed", type=int, default=0, help=help_seed)

    return parser
