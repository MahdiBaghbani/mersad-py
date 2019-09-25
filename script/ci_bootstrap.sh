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
# set alias for python3.6 > python3
alias python3='/usr/bin/python3.6'
# verify python3 command works, and version of python is 3.6
python3 -V
command -v curl