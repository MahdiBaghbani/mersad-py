#!/usr/bin/env bash
# Usage: script/ci_bootstrap
#
# Installs required modules
# in docker container

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# update apt
apt-get update -y
# install python 3.6
apt-get install -y python3.6
# verify installation path
whereis python3
# create a symlink for python3.6 > python3
# -s, --symbolic make symbolic links instead of hard links
# -f, --force remove existing destination files
ln -sf /usr/bin/python3.6 /usr/bin/python3
# verify python3 command works, and version of python is 3.6
python3 -V
