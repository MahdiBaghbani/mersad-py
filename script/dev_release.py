import os
import subprocess

# get full path to _version.py.
VERSION_FILE_NAME = "mersad/_version.py"
NORM_PATH = os.path.normpath(__file__)
BASE_PATH = os.path.abspath(__file__).replace(NORM_PATH, "")
VERSION_FILE_PATH = os.path.join(BASE_PATH, VERSION_FILE_NAME)

# hack (really doesn't like thus way):
# run version file to  get variables in here.
# variables __version__ and __version_info__ will  be loaded.
exec(open(VERSION_FILE_PATH, "r").read())

print("This program will tag a new release of mersad\n"
      + "and it will push to gitlab and github for building,\n"
      + "gitlab will push to pypi.\n\n"
      + f"current version is {__version__}\n\n")

# read and convert to integer.
new_major = int(input("Enter version major number:\n"))
new_minor = int(input("Enter version minor  number:\n"))
new_patch = int(input("Enter version patch number:\n"))

new_version = ".".join(map(str, [new_major, new_minor, new_patch]))

# check version to be bigger than last version.
if new_version == __version__:
    raise ValueError("Version can't be same as current version!")

if new_major < __version_info__[0]:
    raise ValueError("Major version can't be less than current version!")
elif new_minor < __version_info__[1]:
    raise ValueError("Minor version can't be less than current version!")
elif new_patch < __version_info__[2]:
    raise ValueError("Patch version can't be less than current version!")

# write new __version_info__ and _version.py.
version_info = f"__version_info__: Tuple[int, int, int] = ({new_major}, " \
               f"{new_minor}, {new_patch})\n"
new_version_py = list()

print("Writing new version. \n\n")

# read current _version.py, update __version_info__ .
with open(VERSION_FILE_PATH, "r") as file:
    lines = file.readlines()
    for line in lines:
        if "__version_info__: Tuple[int, int, int]" in line:
            new_version_py.append(version_info)
        else:
            new_version_py.append(line)

# write updated content back into _version.py
with open(VERSION_FILE_PATH, "w+") as file:
    file.writelines(new_version_py)

print("Commit and Tag and Push to upstream. \n\n")
# do git commit and tag and push to upstreams
subprocess.call(f"git commit {VERSION_FILE_NAME} -m \"mersad v{new_version}\"", shell=True)
subprocess.call(f"git tag \"v{new_version}\"", shell=True)
subprocess.call(f"git push origin HEAD \"v{new_version}\"", shell=True)
subprocess.call(f"git push github HEAD \"v{new_version}\"", shell=True)
