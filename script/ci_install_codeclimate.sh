#!/usr/bin/env bash
# Usage: script/ci_install_codeclimate.sh
#
# installs code climate test coverage reporter

curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
# chmod +x ./cc-test-reporter
./cc-test-reporter before-build