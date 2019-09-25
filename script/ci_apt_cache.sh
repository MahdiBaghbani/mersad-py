#!/usr/bin/env bash
# Usage: script/ci_apt_cache.sh
#
# Configure apt caching
# for gitlab runner

# set flag for shell execution
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# print current directory in stdout
echo $CI_PROJECT_DIR
# part 1
export APT_DIR=$CI_PROJECT_DIR/.apt
export APT_STATE_LISTS=$APT_DIR/lists
export APT_CACHE_ARCHIVES=$APT_DIR/archives
# part 2
printf "dir::state::lists    ${APT_STATE_LISTS};\ndir::cache::archives    ${APT_CACHE_ARCHIVES};\n" > /etc/apt/apt.conf
# part 3
mkdir -p "${APT_STATE_LISTS}/partial"
mkdir -p "${APT_CACHE_ARCHIVES}/partial"

