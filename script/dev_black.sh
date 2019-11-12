#!/usr/bin/env bash

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

black --target-version py36 --line-length 85 mersad