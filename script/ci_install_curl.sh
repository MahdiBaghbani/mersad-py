#!/usr/bin/env bash
# Usage: script/ci_install_curl.sh
#
# installs curl

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# update apt
apt-get update -y
# install curl
apt-get install -y curl
# verify installation
curl --version
command -v curl