#!/usr/bin/env bash
# Usage: script/dev_tag_release.sh
#
# tags repo and pushes to master

case "$1" in
-h | --help )
  sed -ne '/^#/!q;s/.\{1,2\}//;1d;p' < "$0"
  exit 0
  ;;
esac

if git diff --quiet mersad/_version.py; then
  echo "You must bump the version first." >&2
  exit 1
fi

# run tests
script/ci_test.sh

# must be same as in
version=0.0.3

# commit release and tag it mersad/_version.py
git commit mersad/_version.py -m "mersad $version"
git tag "v${version}"
git push origin HEAD "v${version}"