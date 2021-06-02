#!/usr/bin/env python

import sys

app = 'App-1'

try:
    sys.path.insert(1, '')
    import src.app1.module1.script1 as script1
    import src.app1.module1.script2 as script2
    import src.app1.module2.script1 as script1_m2
    import src.app1.module2.script2 as script2_m2
    #print('Direct execution of the test')
except ImportError:
    sys.path.insert(1, '../')
    import src.app1.module1.script1 as script1
    import src.app1.module1.script2 as script2
    import src.app1.module2.script1 as script1_m2
    import src.app1.module2.script2 as script2_m2
    #print('Execution of the script from tests/ dir')
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')


class Test_Module1_Script1:

    @staticmethod
    def test_sayhi():
        x = script1.Class_Script.Say_Hi()
        try:
            assert x != 0
        except AssertionError:
            print(f'{script1.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{script1.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_showtime():
        x = script1.Class_Script.Show_Time('Test')
        try:
            assert x != 0
        except AssertionError:
            print(f'{script1.Class_Script.Show_Time.__name__}: Failed ❌')
        else:
            print(f'{script1.Class_Script.Show_Time.__name__}: Success ✅')

    @staticmethod
    def test_computeterms():
        # a good list with valid elements
        test_good_list = [x for x in range(1, 10)]
        # a list that contains a string will fail the procedure, since the compute function only takes numbers
        test_bad_list = [1, 2, 3, 'a']
        try:
            x = script1.Class_Script.Compute_Term(test_good_list)
            assert x != 0
        except AssertionError:
            print(f'{script1.Class_Script.Compute_Term.__name__}: Failed ❌')
        else:
            print(f'{script1.Class_Script.Compute_Term.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Module1_Script1.test_sayhi()
        Test_Module1_Script1.test_showtime()
        Test_Module1_Script1.test_computeterms()


class Test_Module1_Script2:

    @staticmethod
    def test_sayhi():
        x = script2.Class_Script.Say_Hi()
        try:
            assert x != 0
        except AssertionError:
            print(f'{script2.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{script2.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_showlocation():
        x = script2.Class_Script.Show_Location('test')
        try:
            assert x != 0
        except AssertionError:
            print(f'{script2.Class_Script.Show_Location.__name__}: Failed ❌')
        else:
            print(f'{script2.Class_Script.Show_Location.__name__}: Success ✅')

    @staticmethod
    def test_showsysteminfo():
        x = script2.Class_Script.Show_System_Info('MACBOOK-PRO')
        try:
            assert x != 0
        except AssertionError:
            print(f'{script2.Class_Script.Show_System_Info.__name__}: Failed ❌')
        else:
            print(f'{script2.Class_Script.Show_System_Info.__name__}: Success ✅')

    @staticmethod
    def test_giverandomarray():
        x = script2.Class_Script.Give_Random_Array(1)
        try:
            assert len(x) > 0
        except AssertionError:
            print(f'{script2.Class_Script.Give_Random_Array.__name__}: Failed ❌')
        else:
            print(f'{script2.Class_Script.Give_Random_Array.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Module1_Script2.test_sayhi()
        Test_Module1_Script2.test_showlocation()
        Test_Module1_Script2.test_showsysteminfo()
        Test_Module1_Script2.test_giverandomarray()


class Test_Module2_Script1:
    @staticmethod
    def test_sayhi():
        x = script1_m2.Class_Script.Say_Hi()
        try:
            assert x != None
        except AssertionError:
            print(f'{script1_m2.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{script1_m2.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_scriptname():
        x = script1_m2.Class_Script.Get_Script_Name()
        try:
            assert x != None
        except AssertionError:
            print(f'{script1_m2.Class_Script.Get_Script_Name.__name__}: Failed ❌')
        else:
            print(f'{script1_m2.Class_Script.Get_Script_Name.__name__}: Success ✅')

    @staticmethod
    def test_externalfunctions():
        x = script1_m2.Class_Script.Test_External_Functions(10, 10)
        try:
            assert x != None
        except AssertionError:
            print(
                f'{script1_m2.Class_Script.Test_External_Functions.__name__}: Failed ❌')
        else:
            print(
                f'{script1_m2.Class_Script.Test_External_Functions.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Module2_Script1.test_sayhi()
        Test_Module2_Script1.test_scriptname()
        Test_Module2_Script1.test_externalfunctions()


class Test_Module2_Script2:
    @staticmethod
    def test_sayhi():
        x = script2_m2.Class_Script.Say_Hi()
        try:
            assert x != None
        except AssertionError:
            print(f'{script2_m2.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{script2_m2.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_scriptname():
        x = script2_m2.Class_Script.Get_Script_Name()
        try:
            assert x != None
        except AssertionError:
            print(f'{script2_m2.Class_Script.Get_Script_Name.__name__}: Failed ❌')
        else:
            print(f'{script2_m2.Class_Script.Get_Script_Name.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Module2_Script2.test_sayhi()
        Test_Module2_Script2.test_scriptname()


def Main():
    print(f'********** MODULE 1 **********')

    print(f'\n⚙️ Testing Script-1...\n')
    Test_Module1_Script1.Start_Test()

    print(f'\n⚙️ Testing Script-2...\n')
    Test_Module1_Script2.Start_Test()

    print(f'\n********** MODULE 2 **********\n')
    print(f'\n⚙️ Testing Script-1...\n')
    Test_Module2_Script1.Start_Test()

    print(f'\n⚙️ Testing Script-2...\n')
    Test_Module2_Script2.Start_Test()


if __name__ == '__main__':
    Main()
