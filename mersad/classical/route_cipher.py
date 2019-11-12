#!/usr/bin/env python3

# mersad/classical/route_cipher.py
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

mersad.classical.route_cipher module.
======================================

The route is a transposition cipher where the key
is which route to follow when reading the cipher
text from the block created with the plaintext.

The plaintext is written in a grid and then
read off following the route chosen.

"""

# Python Standard Library
import argparse
import sys
from typing import Dict
from typing import List
from typing import Tuple

# Mersad Library
from mersad.util import type_check
from mersad.util.base_class import KWARGS_TYPE
from mersad.util.base_class import MersadClassicalBase
from mersad.util.terminal_app_tools import MainFunctionClassical
from mersad.util.terminal_app_tools import monoalphabetic_common_parser


def main(argv: Tuple[str] = tuple(sys.argv[1:])) -> None:
    """Execute program in terminal (cli application)."""
    # module descriptions.
    description: str = "Azadeh Afzar - Mersad Route Cipher\n" \
                       + "Encrypt/Decrypt data with Route algorithm."
    epilog: str = "This one is really a funny one! very good cipher. NOT SAFE!"

    # create a parser and parse command line arguments.
    program = RouteCipherMainFunction(list(argv), RouteCipher, description, epilog,
                                      monoalphabetic_common_parser())
    program.process()


class RouteCipher(MersadClassicalBase):
    r"""
    Route cipher algorithm class.

    Create an instance like every other python class.

    Example:
    ==================================

    >>> agent = RouteCipher(key=4)
    >>> route = [3, 2, 1, 0, 4, 8, 12, 13, 14, 15, 11, 7, 6, 5, 9, 10]
    >>> # encrypt a string (WE ARE DISCOVERED).
    >>> agent.encrypt("WEAREDISCOVERED", route=route)
    'RAEWECREDXESIDOV'

    ==================================

    RouteCipher takes keyword arguments when initializing new instance.

    Valid kwargs keys are listed in below:
        - key             : (optional) key for setting up a grid.
        - fill            : (optional) letter to fill empty spaces in grid.
        - route           : (optional) the list of indexes for routing through
                            the plain text or cipher text.

    Default key is set to None. it will cause error on encrypt/decrypt
    if you don't config it via config() method.
    Default fill is set to "X".
    Default route is set to None. it will cause error on encrypt/decrypt
    if you don't config it via config() method.

    Each instance has it's own unique configurations saved in
    self.configuration and can work independent from other instances.

    Configurations can be changed even after initialization via
    self.config() method.

    Example:
    ==================================

    >>> # create object without any keyword arguments so agent will use
    >>> # default values for all the settings.
    >>> agent = RouteCipher()
    >>> # override defaults.
    >>> agent.config(key=4, route=[3, 2, 1, 0, 4, 8, 12, 13,
    >>>                            14, 15, 11, 7, 6, 5, 9, 10])
    >>> # encrypt a string (WE ARE DISCOVERED).
    >>> agent.encrypt("WEAREDISCOVERED")
    'RAEWECREDXESIDOV'

    ==================================
    """

    def _init_subroutines(self) -> None:
        """Extend _defaults dictionary with default value for fill."""
        self._defaults["fill"] = "X"

    def _config_subroutines(self, **kwargs: KWARGS_TYPE) -> None:
        """
        Assign values to self.configuration dictionary.

        :raise ValueError: if type of a dictionary value is wrong.
        """
        if "key" in kwargs and kwargs["key"] is not None:
            type_check.type_guard(kwargs["key"], int)
            self.configuration["key"] = kwargs["key"]
        if "fill" in kwargs:
            type_check.type_guard(kwargs["fill"], str)
            self.configuration["fill"] = kwargs["fill"]
        if "route" in kwargs:
            type_check.type_guard(kwargs["route"], list)
            self.configuration["route"] = kwargs["route"]

    def _process_subroutines(self, configurations: Dict[str, KWARGS_TYPE],
                             **kwargs: KWARGS_TYPE) -> Dict[str, KWARGS_TYPE]:
        """
        Extend functionality of encrypt and decrypt to accept route lists.

        :raise ValueError: if type of a dictionary value is wrong.
        """
        # flags are all set to False.
        flag_route: bool = False
        flag_replace_route: bool = False

        # get route from kwargs if provided.
        if "route" in kwargs:
            route: List[int] = kwargs["route"]
            type_check.type_guard(route, list)
            flag_route = True

        # get replace route bool from kwargs if provided.
        if "replace_route" in kwargs:
            replace_route: bool = kwargs["replace_route"]
            type_check.type_guard(replace_route, bool)
            flag_replace_route = True

        # if there is a route list, proceed to next steps.
        if flag_route:
            if flag_replace_route:
                # save given route list in configuration dict.
                self.config(route=route)
            # replace route in configurations.
            configurations["route"] = route

        return configurations

    @staticmethod
    def _translator(text: str, **kwargs: KWARGS_TYPE) -> str:
        """
        Wrap the actual encryption/decryption function for class.

        :param text : string to be translated.
        :return     : translated text
        :rtype      : str
        """
        return route_cipher_translator(text, **kwargs)


def route_cipher_translator(text: str, **kwargs: KWARGS_TYPE) -> str:
    """
    Translate a string with Route cipher algorithm.

    :param text                             : string to be translated.
    :param kwargs:
        key                                 : key for encrypt/decrypt, it defines
                                              number of columns.
        fill:                               : character to fill empty spaces in grid.
                                              default is "X".
        route:                              : route to read from.
                                              a list with indexes of grid, ordered
                                              with desired route path, index starts
                                              from 0 from top left square and from
                                              left cell of grid in each new row.

                                              example of indexing grids:
                                              -------------------------------------
                                              |  0  |  1  |  2  |  3  |  4  |  5  |
                                              -------------------------------------
                                              |  6  |  7  |  8  |  9  |  10 |  11 |
                                              -------------------------------------

                                              for encrypting the message:
                                              "go for the left"
                                              with route [0, 6, 7, 1, 2, 8, 9, 3, 4,
                                              10, 5, 11]

                                              -------------------------------------
                                              |  g  |  o  |  f  |  o  |  r  |  t  |
                                              -------------------------------------
                                              |  h  |  e  |  l  |  e  |  f  |  t  |
                                              -------------------------------------

                                              we get: gheofleofrtt as cipher text.

                                              "note that in this example spaces
                                              were removed but this isn't the case in
                                              actual algorithm and all characters
                                              will be preserved."
                                              length of rout list must be equal to
                                              key * quotient(string length / key).
                                              if the above division has reminder,
                                              add 1 to quotient and then multiply.

        decrypt (optional)(default = False) : switch for encryption/decryption mode.
    :return                                 : translated text
    :rtype                                  : str
    """
    # for sake of readability and prettifying below code
    # I will assign aliases for key, values inside kwargs.
    key: int = kwargs["key"]
    if key is None:
        raise ValueError("ERROR: key not found, use config method to define a key.")
    # fill character.
    fill: str = kwargs["fill"] if "fill" in kwargs and kwargs["fill"] else "X"
    if key is None:
        raise ValueError("ERROR: key not found, use config method to define a key.")
    # route path indexes.
    route: List[int] = kwargs["route"]
    # check rout indexes to be unique by comparing its length to set length.
    if len(route) != len(set(route)):
        raise ValueError("ERROR: route indexes must be unique.")
    # default decrypt to False if no decrypt is defined in kwargs.
    decrypt: bool = kwargs["decrypt"] if "decrypt" in kwargs else False

    # store length of string.
    # length of string is needed for mathematical calculations.
    string_length: int = len(text)
    # get quotient and remainder of string length to key.
    quotient, remainder = divmod(string_length, key)

    # rout length must be equal to number of cells in a 2D grid of quotient x key.
    # if remainder is not zero, the grid becomes (quotient + 1) x key.
    quotient: int = quotient if remainder == 0 else quotient + 1
    if len(route) != (quotient * key):
        raise ValueError("ERROR: rout length is wrong.")

    if decrypt:
        # create a 2D grid of size quotient x key [note that quotient may have been
        # modified in last block of code, here we use the modified one].
        grid: List[str] = ["" for i in range(quotient * key)]
        # place string letters in grid with respect of route index.
        for i, j in enumerate(route):
            grid[j] = text[i]
        translated: str = "".join(grid)
    else:
        # if remainder  is not zero, add fill characters to the end of string
        # so that the remainder become zero.
        if remainder != 0:
            # turn string into list of letters.
            lst: List[str] = list(text)
            # add enough fill characters to end of list.
            lst.extend([fill] * (key - remainder))
            # create new string.
            text = "".join(lst)
        # encrypt based on the route.
        translated: str = "".join([text[index] for index in route])

    return translated


class RouteCipherMainFunction(MainFunctionClassical):
    """Manage Route cipher programs execution from terminal."""

    def _config_agent(self, agent, args: argparse.Namespace) -> None:
        """Config the agent parameters in process method."""
        agent.config(
            key=args.key,
            fill=args.fill,
            route=args.route,
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
        # add command line options.
        help_key: str = "key for encryption/decryption"
        parser.add_argument("-k", "--key", type=int, required=True, help=help_key)

        help_fill: str = "custom fill letter to fill empty cells on the grid"
        parser.add_argument("-fi", "--fill", type=str, default="X", help=help_fill)

        help_route: str = "route for encryption/decryption"
        parser.add_argument("-r", "--route", nargs="+", type=int, required=True,
                            help=help_route)

        return parser
