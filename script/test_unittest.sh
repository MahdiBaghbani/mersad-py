#!/usr/bin/env bash

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

coverage run --source mersad -m  unittest discover -s mersad -p 'test_*.py'
coverage report
coverage xml