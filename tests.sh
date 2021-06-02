#!/usr/bin/env bash
system=$(uname -a)

echo 'Running the test script on:'
echo $system
echo 'App-1 🚀'
python tests/test_app1.py
echo 'App-2 🚀'
python tests/test_app2.py