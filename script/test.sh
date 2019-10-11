#!/usr/bin/env bash
# Usage: script/ci_test.sh
#
# run style and unittest tests and coverage analysis

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# run style tests against flake8
script/test_style.sh
# test and test coverage
script/test_unittest.sh