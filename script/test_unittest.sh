#!/usr/bin/env bash
# Usage: script/test_unittest.sh
#
# run tests and coverage analysis

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

pipenv run coverage run --source mersad -m  unittest discover -s mersad -p 'test_*.py'
pipenv run coverage report
pipenv run coverage xml