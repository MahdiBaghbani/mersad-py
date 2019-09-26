# Python Standard Library
import re

# 3rd Party Library
from setuptools import find_packages
from setuptools import setup

# load version
VERSION_FILE = "mersad/_version.py"
VERSION_STRING = open(VERSION_FILE, "r").read()
REGEX_PATTERN = r"^__version__: str =  ['\"]([^'\"]*)['\"]"

re_search = re.search(REGEX_PATTERN, VERSION_STRING, re.M)

if re_search:
    version = re_search.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSION_FILE}.")

# general information about package
name = "mersad"
url = "https://gitlab.com/Azadeh-Afzar/Cryptography/Mersad-Cryptography-Library"
license_name = "AGPLv3"
author = "Mohammad Mahdi Baghbani Pourvahid"
author_email = "MahdiBaghbani@protonmail.com"
description = """Azadeh Afzar - mersad Cryptographic Library"""
classifiers = [
    "Development Status :: 1 - Planning",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Affero General Public License v3",
    "License :: OSI Approved :: zlib/libpng License",
    "Topic :: Software Development",
    "Topic :: Utilities",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7"
]

# filter test directory from packages
packages = {package for package in find_packages() if "test" not in package}

# add stub files to package data
package_data = {
    "mersad": [
        "py.typed", "__init__.pyi"
    ],
    "mersad.classical": [
        "__init__.pyi", "affine_cipher.pyi", "shift_cipher.pyi"
    ],
    "mersad.util": [
        "__init__.pyi", "base_class.pyi", "crypto_math.pyi",
        "string_analyzer.pyi", "string_manipulation.pyi",
        "type_check.pyi"
    ]
}

# dependencies
install_requires = ["ErfanIO"]

setup(
        name=name,
        version=version,
        packages=packages,
        package_data=package_data,
        url=url,
        license=license_name,
        author=author,
        author_email=author_email,
        description=description,
        classifiers=classifiers,
        install_requires=install_requires
)
