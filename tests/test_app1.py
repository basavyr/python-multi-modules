#!/usr/bin/env python

import sys

app = 'App-1'

try:
    # print(sys.path)
    sys.path.insert(1, '')
    # print('in first import block')
    import src.app1.package1.module1 as m1_p1
    import src.app1.package1.module2 as m2_p1
    import src.app1.package2.module1 as m1_p2
    import src.app1.package2.module2 as m2_p2
    #print('Direct execution of the test')
except ImportError:
    # print(sys.path)
    sys.path.insert(1, '../')
    # print('in second import block')
    import src.app1.package1.module1 as m1_p1
    import src.app1.package1.module2 as m2_p1
    import src.app1.package2.module1 as m1_p2
    import src.app1.package2.module2 as m2_p2
    #print('Execution of the script from tests/ dir')
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')


class Test_Package1_Module1:

    @staticmethod
    def test_sayhi():
        x = m1_p1.Class_Script.Say_Hi()
        try:
            assert x != 0
        except AssertionError:
            print(f'{m1_p1.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{modm1_p1ule1.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_showtime():
        x = m1_p1.Class_Script.Show_Time('Test')
        try:
            assert x != 0
        except AssertionError:
            print(f'{m1_p1.Class_Script.Show_Time.__name__}: Failed ❌')
        else:
            print(f'{m1_p1.Class_Script.Show_Time.__name__}: Success ✅')

    @staticmethod
    def test_computeterms():
        # a good list with valid elements
        test_good_list = [x for x in range(1, 10)]
        # a list that contains a string will fail the procedure, since the compute function only takes numbers
        test_bad_list = [1, 2, 3, 'a']
        try:
            x = m1_p1.Class_Script.Compute_Term(test_good_list)
            assert x != 0
        except AssertionError:
            print(f'{m1_p1.Class_Script.Compute_Term.__name__}: Failed ❌')
        else:
            print(f'{m1_p1.Class_Script.Compute_Term.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Package1_Module1.test_sayhi()
        Test_Package1_Module1.test_showtime()
        Test_Package1_Module1.test_computeterms()


class Test_Package1_Module2:

    @staticmethod
    def test_sayhi():
        x = m2_p1.Class_Script.Say_Hi()
        try:
            assert x != 0
        except AssertionError:
            print(f'{m2_p1.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{m2_p1.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_showlocation():
        x = m2_p1.Class_Script.Show_Location('test')
        try:
            assert x != 0
        except AssertionError:
            print(f'{m2_p1.Class_Script.Show_Location.__name__}: Failed ❌')
        else:
            print(f'{m2_p1.Class_Script.Show_Location.__name__}: Success ✅')

    @staticmethod
    def test_showsysteminfo():
        x = m2_p1.Class_Script.Show_System_Info('MACBOOK-PRO')
        try:
            assert x != 0
        except AssertionError:
            print(f'{m2_p1.Class_Script.Show_System_Info.__name__}: Failed ❌')
        else:
            print(f'{m2_p1.Class_Script.Show_System_Info.__name__}: Success ✅')

    @staticmethod
    def test_giverandomarray():
        x = m2_p1.Class_Script.Give_Random_Array(1)
        try:
            assert len(x) > 0
        except AssertionError:
            print(f'{m2_p1.Class_Script.Give_Random_Array.__name__}: Failed ❌')
        else:
            print(f'{m2_p1.Class_Script.Give_Random_Array.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Package1_Module2.test_sayhi()
        Test_Package1_Module2.test_showlocation()
        Test_Package1_Module2.test_showsysteminfo()
        Test_Package1_Module2.test_giverandomarray()


class Test_Package2_Module1:
    @staticmethod
    def test_sayhi():
        x = m1_p2.Class_Script.Say_Hi()
        try:
            assert x != None
        except AssertionError:
            print(f'{m1_p2.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{m1_p2.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_scriptname():
        x = m1_p2.Class_Script.Get_Script_Name()
        try:
            assert x != None
        except AssertionError:
            print(f'{m1_p2.Class_Script.Get_Script_Name.__name__}: Failed ❌')
        else:
            print(f'{m1_p2.Class_Script.Get_Script_Name.__name__}: Success ✅')

    @staticmethod
    def test_externalfunctions():
        x = m1_p2.Class_Script.Test_External_Functions(10, 10)
        try:
            assert x != None
        except AssertionError:
            print(
                f'{m1_p2.Class_Script.Test_External_Functions.__name__}: Failed ❌')
        else:
            print(
                f'{m1_p2.Class_Script.Test_External_Functions.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Package2_Module1.test_sayhi()
        Test_Package2_Module1.test_scriptname()
        Test_Package2_Module1.test_externalfunctions()


class Test_Package2_Module2:
    @staticmethod
    def test_sayhi():
        x = m2_p2.Class_Script.Say_Hi()
        try:
            assert x != None
        except AssertionError:
            print(f'{m2_p2.Class_Script.Say_Hi.__name__}: Failed ❌')
        else:
            print(f'{m2_p2.Class_Script.Say_Hi.__name__}: Success ✅')

    @staticmethod
    def test_scriptname():
        x = m2_p2.Class_Script.Get_Script_Name()
        try:
            assert x != None
        except AssertionError:
            print(f'{m2_p2.Class_Script.Get_Script_Name.__name__}: Failed ❌')
        else:
            print(f'{m2_p2.Class_Script.Get_Script_Name.__name__}: Success ✅')

    @staticmethod
    def Start_Test():
        Test_Package2_Module2.test_sayhi()
        Test_Package2_Module2.test_scriptname()


def Main():
    print(f'********** Package-1 **********')

    print(f'\n⚙️ Testing Module-1...\n')
    Test_Package1_Module1.Start_Test()

    print(f'\n⚙️ Testing Module-2...\n')
    Test_Package1_Module2.Start_Test()

    print(f'\n********** Package-2 **********\n')
    print(f'\n⚙️ Testing Module-1...\n')
    Test_Package2_Module1.Start_Test()

    print(f'\n⚙️ Testing Module-2...\n')
    Test_Package2_Module2.Start_Test()


if __name__ == '__main__':
    Main()
