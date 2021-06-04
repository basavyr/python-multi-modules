from datetime import datetime
import sys

app = 'App-2'


try:
    sys.path.insert(1, '')
    from src.app2.package2 import module1 as module1_p2
    from src.app2.package2 import module2 as module2_p2
    from src.app2.package1 import module1 as module1_p1
    from src.app2.package1 import module2 as module2_p1
except ModuleNotFoundError:
    sys.path.insert(1, '../')
    from src.app2.package2 import module1 as module1_p2
    from src.app2.package2 import module2 as module2_p2
    from src.app2.package1 import module1 as module1_p1
    from src.app2.package1 import module2 as module2_p1
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')


class Test_Package1_Module1:

    @staticmethod
    def test_combo():
        try:
            x = module1_p1.Class_Script.Combo_Function()
            assert x != -1
        except AssertionError:
            print(
                f'Test: {Test_Package1_Module1.test_combo.__name__} @ {datetime.utcnow()}: ❌')
        else:
            print(
                f'Test: {Test_Package1_Module1.test_combo.__name__} @ {datetime.utcnow()}: ✅')

    @staticmethod
    def Start_Test():
        Test_Package1_Module1.test_combo()


class Test_Package1_Module2:

    @staticmethod
    def test_operation():
        try:
            x = module2_p1.Plot_Maker.Operation(10)
            assert x != 0
        except AssertionError:
            print(
                f'Test: {Test_Package1_Module2.test_operation.__name__} @ {datetime.utcnow()}: ❌')
        else:
            print(
                f'Test: {Test_Package1_Module2.test_operation.__name__} @ {datetime.utcnow()}: ✅')

    @staticmethod
    def test_mathfunction():
        try:
            x = module2_p1.Plot_Maker.Math_Function([1, 2, 3])
            assert type(x) != 0
        except AssertionError:
            print(
                f'Test: {Test_Package1_Module2.test_mathfunction.__name__} @ {datetime.utcnow()}: ❌')
        else:
            print(
                f'Test: {Test_Package1_Module2.test_mathfunction.__name__} @ {datetime.utcnow()}: ✅')

    @staticmethod
    def test_createdataset():
        try:
            x = module2_p1.Plot_Maker.Create_Data_Set()
            assert type(x[0]) != None and type(x[1]) != None
        except AssertionError:
            print(
                f'Test: {Test_Package1_Module2.test_createdataset.__name__} @ {datetime.utcnow()}: ❌')
        else:
            print(
                f'Test: {Test_Package1_Module2.test_createdataset.__name__} @ {datetime.utcnow()}: ✅')

    @staticmethod
    def Start_Test():
        Test_Package1_Module2.test_operation()
        Test_Package1_Module2.test_mathfunction()
        Test_Package1_Module2.test_createdataset()


class Test_Package2_Module1:

    @staticmethod
    def test_main():
        fail_msg = f'Test: {Test_Package2_Module1.test_main.__name__} @ {datetime.utcnow()}: ❌'
        ok_msg = f'Test: {Test_Package2_Module1.test_main.__name__} @ {datetime.utcnow()}: ✅'
        try:
            x = module1_p2.Class_Script.Test()
        except Exception:
            print(fail_msg)
        else:
            print(ok_msg)

    @ staticmethod
    def test_givearray():
        try:
            x = module1_p2.Class_Script.Give_Array()
            assert type(x) != None
        except AssertionError:
            print(
                f'Test: {Test_Package2_Module1.test_givearray.__name__} @ {datetime.utcnow()}: ❌')
        else:
            print(
                f'Test: {Test_Package2_Module1.test_givearray.__name__} @ {datetime.utcnow()}: ✅')

    @ staticmethod
    def Start_Test():
        Test_Package2_Module1.test_main()
        Test_Package2_Module1.test_givearray()


class Test_Package2_Module2:

    @ staticmethod
    def test_givearray():
        try:
            x = module2_p2.Class_Script.Give_Array()
            assert type(x) != None
        except AssertionError:
            print(
                f'Test: {Test_Package2_Module2.test_givearray.__name__} @ {datetime.utcnow()}: ❌')
        else:
            print(
                f'Test: {Test_Package2_Module2.test_givearray.__name__} @ {datetime.utcnow()}: ✅')

    @ staticmethod
    def test_gettime():
        try:
            x = module2_p2.Class_Script.Get_Time()
            assert x != None
        except AssertionError:
            print(
                f'Test: {Test_Package2_Module2.test_gettime.__name__} @ {datetime.utcnow()}: ❌')
        else:
            print(
                f'Test: {Test_Package2_Module2.test_gettime.__name__} @ {datetime.utcnow()}: ✅')

    @ staticmethod
    def Start_Test():
        Test_Package2_Module2.test_givearray()
        Test_Package2_Module2.test_gettime()


def Main():

    print(f'********** Package-1 **********')
    print(f'\n⚙️ Testing Module-1...\n')
    Test_Package1_Module1.Start_Test()
    print(f'\n⚙️ Testing Module-2...\n')
    Test_Package1_Module2.Start_Test()

    print(f'\n********** Package-2 **********')
    print(f'\n⚙️ Testing Module-1...\n')
    Test_Package2_Module1.Start_Test()
    print(f'\n⚙️ Testing Module-2...\n')
    # Test_Package2_Module2.Start_Test()


if __name__ == '__main__':
    Main()
