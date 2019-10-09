#!/usr/bin/env bash
# Usage: script/dev_formatter.sh
#
# format all imports and re-generate
# stub files.

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# re-generate all stub files
script/dev_stubgen.sh
# sort import statements
script/dev_isort.sh