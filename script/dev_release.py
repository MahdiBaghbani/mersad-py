#!/usr/bin/env python3

# Python Standard Library
import os
import subprocess

# get path to this file's directory, then go one directory up
file_path = os.path.abspath(os.path.dirname(__file__))
base_path = os.path.abspath(os.path.dirname(file_path))
version_file_path = os.path.join(base_path, "mersad", "_version.py")

# open _version file
with open(version_file_path) as file:
    version_file = file.readlines()

# set version and version_info to None, so if we didn't find
# a version in _version.py, we can throw an error
version = None
version_info = None

# find version
for line in version_file:
    if "__version_info__: Tuple[int, int, int] = " in line:
        # find tuple inside _version.py and reformat it to
        # standard x.y.z version format
        tuple_left = line.index("(")
        tuple_right = line.index(")")
        version = line[tuple_left + 1:tuple_right].replace(",", ".").replace(" ", "")
        # creat a list from x.y.z string which has [x, y, z]
        # notice that x, y , z must be converted to integer
        version_info = [int(number) for number in version.split(".")]

# throe error if version not found
if not version or not version_info:
    raise ValueError("ERROR: version not found at _version.py.")

print("This program will tag a new release of mersad\n"
      + "and it will push to gitlab and github for building,\n"
      + "gitlab will push to pypi.\n\n"
      + f"current version is {version}\n\n")

# read and convert to integer.
print("Version is in X.Y.Z form\n"
      "X is version major, Y is version minor, Z id version minor.\n\n")
new_major = int(input("Enter version major number:\n"))
new_minor = int(input("Enter version minor  number:\n"))
new_patch = int(input("Enter version patch number:\n"))

new_version = ".".join(map(str, [new_major, new_minor, new_patch]))

# check version to be bigger than last version.
if new_version == version:
    raise ValueError("Version can't be same as current version!")

if new_major < version_info[0]:
    raise ValueError("Major version can't be less than current version!")
elif new_minor < version_info[1]:
    raise ValueError("Minor version can't be less than current version!")
elif new_patch < version_info[2]:
    raise ValueError("Patch version can't be less than current version!")


# creat an empty list for new _version.py file
print("Writing new version. \n\n")

new_version_py = list()

# write new version_info and in _version.py.
new_version_info = f"__version_info__: Tuple[int, int, int] = ({new_major}, " \
               f"{new_minor}, {new_patch})\n"

# read current _version.py, and update __version_info__
# then append to new_version_py list.
with open(version_file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        if "__version_info__: Tuple[int, int, int]" in line:
            new_version_py.append(new_version_info)
        else:
            new_version_py.append(line)

# write updated content from new_version_py
# back into _version.py file
with open(version_file_path, "w+") as file:
    file.writelines(new_version_py)

# do git commit and tag and push to upstreams
print("Commit and Tag and Push to upstream. \n\n")

subprocess.call(f"git commit {version_file_path} -m \"version: mersad v{new_version}\"", shell=True)
subprocess.call(f"git tag \"v{new_version}\"", shell=True)
subprocess.call(f"git push origin HEAD \"v{new_version}\"", shell=True)
subprocess.call(f"git push github HEAD \"v{new_version}\"", shell=True)
