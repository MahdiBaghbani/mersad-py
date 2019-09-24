#!/usr/bin/env bash

# re-generate all stub files
script/dev_stubgen.sh
# sort import statements
script/dev_isort.sh
# run style tests against flake8
script/test_flake8.sh
# run style tests against pylint
script/test_pylint.sh
# run static type checks
script/test_mypy.sh