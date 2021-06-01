#!/usr/bin/env bash
system=$(uname -a)

echo 'Running the test script on:'
echo $system
python tests/test_app1.py