#!/usr/bin/env bash
# Usage: script/test_flake8.sh
#
# run codestyle, docstyle and mccabe tests

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

pipenv run flake8