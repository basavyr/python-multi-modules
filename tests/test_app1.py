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
    print(f'\nImporting modules from {app} 📚\n')


class Test_Script1:

    @staticmethod
    def test_sayhi():
        x = script1.Class_Script.Say_Hi()
        try:
            print(f'⚙️ Testing Script-1...')
            assert type(x) != 0
        except AssertionError:
            print('Script-1: Failed ❌')
        else:
            print('Script-1: Success ✅')

    @staticmethod
    def test_showtime():
        x = script1.Class_Script.Show_Time('Test')
        try:
            assert type(x) != 0
        except AssertionError:
            print('Script-1: Failed ❌')
        else:
            print('Script-1: Success ✅')

    @staticmethod
    def test_computeterms():
        test_list = [1, 2, 3, 4]
        x = script1.Class_Script.Compute_Term(test_list)
        try:
            assert x != 0
        except AssertionError:
            print('Script-1: Failed ❌')
        else:
            print('Script-1: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Script1.test_sayhi()
        Test_Script1.test_showtime()
        Test_Script1.test_computeterms()


def Main():
    Test_Script1.Start_Test()


if __name__ == '__main__':
    Main()
