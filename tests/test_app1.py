#!/usr/bin/env python

import sys

app = 'App-1'

try:
    sys.path.append('../')
    import src.app1.module1.script1 as script1
    import src.app1.module1.script2 as script2
except ImportError:
    sys.path.append('src/')
    import app1.module1.script1 as script1
    import app1.module1.script2 as script2
finally:
    print(f'\nImporting modules from {app} 📚\n')


class Test_Script1:

    @staticmethod
    def test_sayhi():
        x = script1.Class_Script.Say_Hi()
        try:
            assert x != 0
        except AssertionError:
            print('Script-1: Failed ❌')
        else:
            print('Script-1: Success ✅')

    @staticmethod
    def test_showtime():
        x = script1.Class_Script.Show_Time('Test')
        try:
            assert x != 0
        except AssertionError:
            print('Script-1: Failed ❌')
        else:
            print('Script-1: Success ✅')

    @staticmethod
    def test_computeterms():
        test_good_list = [x for x in range(1, 10)]
        test_bad_list = [1, 2, 3, 'a']
        try:
            x = script1.Class_Script.Compute_Term(test_good_list)
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


class Test_Script2:

    @staticmethod
    def test_sayhi():
        x = script2.Class_Script.Say_Hi()
        try:
            assert x != 0
        except AssertionError:
            print('Script-2: Failed ❌')
        else:
            print('Script-2: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Script2.test_sayhi()


def Main():
    print(f'\n⚙️ Testing Script-1...\n')
    Test_Script1.Start_Test()
    
    print(f'\n⚙️ Testing Script-2...\n')
    Test_Script2.Start_Test()


if __name__ == '__main__':
    Main()
