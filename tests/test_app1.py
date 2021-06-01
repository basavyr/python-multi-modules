#!/usr/bin/env python

import sys

app = 'App-1'

try:
    sys.path.append('../')
    import src.app1.module1.script1 as script1
except ImportError:
    sys.path.append('src/')
    import app1.module1.script1 as script1
finally:
    print(f'Finish importing modules from {app}')


def test_script1():
    x = script1.Class_Script.Say_Hi()
    try:
        print(f'Testing Script-1')
        assert type(x) == str
    except AssertionError:
        print('Script-1: Failed ❌')
    else:
        print('Script-1: Success ✅')

# def test_script1():
#     x = script1.Class_Script.Say_Hi()
#     try:
#         assert type(x) == str
#     except AssertionError:
#         print('NOT GOOD')
#     else:
#         print('GOOD')


def Main():
    test_script1()


if __name__ == '__main__':
    Main()
