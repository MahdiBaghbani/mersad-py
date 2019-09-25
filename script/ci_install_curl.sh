#!/usr/bin/env bash
# Usage: script/ci_apt_cache.sh
#
# installs curl

# update apt
apt-get update -y
# install curl
apt-get install -y curl
# verify installation
curl --version
command -v curl