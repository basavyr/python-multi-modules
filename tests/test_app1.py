#!/usr/bin/env python

import sys

app = 'App-1'

try:
    # print(sys.path)
    sys.path.insert(1, '')
    # print('in first import block')
    import src.app1.package1.module1 as module1
    import src.app1.package1.module2 as module2
    import src.app1.package2.module1 as module1_m2
    import src.app1.package2.module2 as module2_m2
    #print('Direct execution of the test')
except ImportError:
    # print(sys.path)
    sys.path.insert(1, '../')
    # print('in second import block')
    import src.app1.package1.module1 as module1
    import src.app1.package1.module2 as module2
    import src.app1.package2.module1 as module1_m2
    import src.app1.package2.module2 as module2_m2
    #print('Execution of the script from tests/ dir')
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')


class Test_Package1_Module1:

    @staticmethod
    def test_sayhi():
        x = module1.Class_Script.Say_Hi()
        try:
            assert x != 0
        except AssertionError:
            print(f'{module1.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{module1.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_showtime():
        x = module1.Class_Script.Show_Time('Test')
        try:
            assert x != 0
        except AssertionError:
            print(f'{module1.Class_Script.Show_Time.__name__}: Failed ❌')
        else:
            print(f'{module1.Class_Script.Show_Time.__name__}: Success ✅')

    @staticmethod
    def test_computeterms():
        # a good list with valid elements
        test_good_list = [x for x in range(1, 10)]
        # a list that contains a string will fail the procedure, since the compute function only takes numbers
        test_bad_list = [1, 2, 3, 'a']
        try:
            x = module1.Class_Script.Compute_Term(test_good_list)
            assert x != 0
        except AssertionError:
            print(f'{module1.Class_Script.Compute_Term.__name__}: Failed ❌')
        else:
            print(f'{module1.Class_Script.Compute_Term.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Package1_Module1.test_sayhi()
        Test_Package1_Module1.test_showtime()
        Test_Package1_Module1.test_computeterms()


class Test_Module1_module2:

    @staticmethod
    def test_sayhi():
        x = module2.Class_Script.Say_Hi()
        try:
            assert x != 0
        except AssertionError:
            print(f'{module2.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{module2.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_showlocation():
        x = module2.Class_Script.Show_Location('test')
        try:
            assert x != 0
        except AssertionError:
            print(f'{module2.Class_Script.Show_Location.__name__}: Failed ❌')
        else:
            print(f'{module2.Class_Script.Show_Location.__name__}: Success ✅')

    @staticmethod
    def test_showsysteminfo():
        x = module2.Class_Script.Show_System_Info('MACBOOK-PRO')
        try:
            assert x != 0
        except AssertionError:
            print(f'{module2.Class_Script.Show_System_Info.__name__}: Failed ❌')
        else:
            print(f'{module2.Class_Script.Show_System_Info.__name__}: Success ✅')

    @staticmethod
    def test_giverandomarray():
        x = module2.Class_Script.Give_Random_Array(1)
        try:
            assert len(x) > 0
        except AssertionError:
            print(f'{module2.Class_Script.Give_Random_Array.__name__}: Failed ❌')
        else:
            print(f'{module2.Class_Script.Give_Random_Array.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Module1_module2.test_sayhi()
        Test_Module1_module2.test_showlocation()
        Test_Module1_module2.test_showsysteminfo()
        Test_Module1_module2.test_giverandomarray()


class Test_Module2_module1:
    @staticmethod
    def test_sayhi():
        x = module1_m2.Class_Script.Say_Hi()
        try:
            assert x != None
        except AssertionError:
            print(f'{module1_m2.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{module1_m2.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_scriptname():
        x = module1_m2.Class_Script.Get_Script_Name()
        try:
            assert x != None
        except AssertionError:
            print(f'{module1_m2.Class_Script.Get_Script_Name.__name__}: Failed ❌')
        else:
            print(f'{module1_m2.Class_Script.Get_Script_Name.__name__}: Success ✅')

    @staticmethod
    def test_externalfunctions():
        x = module1_m2.Class_Script.Test_External_Functions(10, 10)
        try:
            assert x != None
        except AssertionError:
            print(
                f'{module1_m2.Class_Script.Test_External_Functions.__name__}: Failed ❌')
        else:
            print(
                f'{module1_m2.Class_Script.Test_External_Functions.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Module2_module1.test_sayhi()
        Test_Module2_module1.test_scriptname()
        Test_Module2_module1.test_externalfunctions()


class Test_Module2_module2:
    @staticmethod
    def test_sayhi():
        x = module2_m2.Class_Script.Say_Hi()
        try:
            assert x != None
        except AssertionError:
            print(f'{module2_m2.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{module2_m2.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_scriptname():
        x = module2_m2.Class_Script.Get_Script_Name()
        try:
            assert x != None
        except AssertionError:
            print(f'{module2_m2.Class_Script.Get_Script_Name.__name__}: Failed ❌')
        else:
            print(f'{module2_m2.Class_Script.Get_Script_Name.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Module2_module2.test_sayhi()
        Test_Module2_module2.test_scriptname()


def Main():
    print(f'********** Package-1 **********')

    print(f'\n⚙️ Testing Module-1...\n')
    Test_Module1_module1.Start_Test()

    print(f'\n⚙️ Testing Module-2...\n')
    Test_Module1_module2.Start_Test()

    print(f'\n********** Package-2 **********\n')
    print(f'\n⚙️ Testing Module-1...\n')
    Test_Module2_module1.Start_Test()

    print(f'\n⚙️ Testing Module-2...\n')
    Test_Module2_module2.Start_Test()


if __name__ == '__main__':
    Main()
