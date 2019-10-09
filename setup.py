#!/usr/bin/env python3

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

# 3rd Party Library
from setuptools import find_packages
from setuptools import setup

# get path to this file's directory
base_path = os.path.abspath(os.path.dirname(__file__))

# open _version file
with open(os.path.join(base_path, "mersad", "_version.py")) as file:
    version_file = file.readlines()

# set version to None, so if we didn't find
# a version in _version.py, we can throw an error
version = None

# find version
for line in version_file:
    if "__version_info__: Tuple[int, int, int] = " in line:
        # find tuple inside _version.py and reformat it to
        # standard x.y.z version format
        tuple_left = line.index("(")
        tuple_right = line.index(")")
        version = line[tuple_left + 1:tuple_right].replace(",", ".").replace(" ", "")

# throe error if version not found
if not version:
    raise ValueError("ERROR: version not found at _version.py.")

# open mersad/__init__.py to retrieve package info
with open(os.path.join(base_path, "mersad", "__init__.py"), "r") as file:
    info_file = file.readlines()


# define extractor function
def extract_info(source, name):
    for line in source:
        # find the metadata
        if "__{name}__: str =".format(name=name) in line:
            # strip from left until ", " is also excluded
            line = line[line.index('"') + 1:]
            # return string until "
            return line[:line.index('"')]


# general information about package
name = "mersad"
url = "https://gitlab.com/Azadeh-Afzar/Cryptography/Mersad-Cryptography-Library"
author = extract_info(info_file, "author")
author_email = extract_info(info_file, "email")
license_name = extract_info(info_file, "license")
description = extract_info(info_file, "description")
long_description = open("README.md", "r", encoding="utf-8").read()
classifiers = [
    "Development Status :: 1 - Planning",
    "License :: OSI Approved :: GNU Affero General Public License v3",
    "License :: OSI Approved :: zlib/libpng License",
    "Operating System :: Unix",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS :: MacOS X",
    "Environment :: Console",
    "Topic :: Security :: Cryptography",
    "Topic :: Software Development",
    "Topic :: Utilities",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
]

# dictionary of packages
packages = find_packages()

# add stub files to package data
package_data = {
    "mersad": [
        "py.typed", "*.pyi"
    ],
    "mersad.classical": [
        "*.pyi"
    ],
    "mersad.test": [
        "*.pyi"
    ],
    "mersad.test.asset": [
        "*.pyi"
    ],
    "mersad.test.asset.texts": [
        "*.pyi"
    ],
    "mersad.test.classical": [
        "*.pyi"
    ],
    "mersad.test.util": [
        "*.pyi"
    ],
    "mersad.util": [
        "*.pyi"
    ]
}

# dependencies
install_requires = ["ErfanIO"]

# command line programs
entry_points = {
    "console_scripts": [
        "mclAffine = mersad.classical.affine_cipher:main",
        "mclAtbash = mersad.classical.atbash_cipher:main",
        "mclShift = mersad.classical.shift_cipher:main"
    ]
}

setup(
        name=name,
        version=version,
        packages=packages,
        package_data=package_data,
        entry_points=entry_points,
        url=url,
        license=license_name,
        author=author,
        author_email=author_email,
        description=description,
        long_description=long_description,
        long_description_content_type="text/markdown",
        platforms="Posix; Windows; MacOS X",
        classifiers=classifiers,
        python_requires=">=3.6",
        install_requires=install_requires
)
