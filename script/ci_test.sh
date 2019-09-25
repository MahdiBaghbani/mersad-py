#!/usr/bin/env bash
# Usage: script/ci_test.sh
#
# run tests and coverage analysis

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# run style tests against flake8
script/test_flake8.sh
# run style tests against pylint
script/test_pylint.sh
# run static type checks
script/test_mypy.sh
# test and test coverage
script/test_unittest.sh