import sys

app = 'App=3'

try:
    sys.path.insert(1, '../')
    import src.app3.package1.module1 as m1
except ModuleNotFoundError:
    sys.path.insert(1, '')
    import src.app3.package1.module1 as m1
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')


class Test_Class:
    @staticmethod
    def Test1():
        print('this is test 1')

    @staticmethod
    def Test2():
        print('this is test 1')

    @staticmethod
    def Test3():
        print('this is test 1')

    @staticmethod
    def Test4():
        print('this is test 1')

Y=Test_Class


imp_Y=m1.Export_Object.Import_Object(Y)