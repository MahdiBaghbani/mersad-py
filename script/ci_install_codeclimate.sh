#!/usr/bin/env bash
# Usage: script/ci_install_codeclimate.sh
#
# installs code climate test coverage reporter

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# install with curl
curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
# give execution privilege
chmod +x ./cc-test-reporter
