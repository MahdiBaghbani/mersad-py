#!/usr/bin/env bash
# Usage: script/ci_.sh
#
# run tests and coverage analysis

# run style tests against flake8
script/test_flake8.sh
# run style tests against pylint
script/test_pylint.sh
# run static type checks
script/test_mypy.sh