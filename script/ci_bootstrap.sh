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
# install curl
apt-get install -y curl
curl --version
command -v curl
# install python 3.6
apt-get install -y python3.6