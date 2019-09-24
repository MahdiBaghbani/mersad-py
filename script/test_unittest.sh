#!/usr/bin/env bash
coverage run --source mersad -m  unittest discover -s mersad -p 'test_*.py'
coverage report