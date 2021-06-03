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


class Test_Class_1:

    def __init__(self):
        self.main_object = 'Object->Test_Class1'

    @staticmethod
    def Test1():
        print(
            f'This is {Test_Class_1.Test1.__name__} from {Test_Class_1.__name__}')

    @staticmethod
    def Test2():
        print(
            f'This is {Test_Class_1.Test2.__name__} from {Test_Class_1.__name__}')

    @staticmethod
    def Test3():
        print(
            f'This is {Test_Class_1.Test3.__name__} from {Test_Class_1.__name__}')

    @staticmethod
    def Test4():
        print(
            f'This is {Test_Class_1.Test4.__name__} from {Test_Class_1.__name__}')


class Test_Class_2:

    def __init__(self):
        self.main_object = 'Object->Test_Class2'

    @staticmethod
    def Test1():
        print(
            f'This is {Test_Class_2.Test1.__name__} from {Test_Class_2.__name__}')

    @staticmethod
    def Test2():
        print(
            f'This is {Test_Class_2.Test2.__name__} from {Test_Class_2.__name__}')

    @staticmethod
    def Test3():
        print(
            f'This is {Test_Class_2.Test3.__name__} from {Test_Class_2.__name__}')

    @staticmethod
    def Test4():
        print(
            f'This is {Test_Class_2.Test4.__name__} from {Test_Class_2.__name__}')


class Combo_Class:
    def __init__(self, cls_1, cls_2):
        class_containers = [cls_1, cls_2]
        try:
            self.combo = [
                class_container.main_object for class_container in class_containers]
        except AttributeError:
            self.combo = [None for _ in class_containers]

    def Show_Container_Class(self):
        container_class = self.combo
        id = 0
        for component in container_class:
            id += 1
            try:
                mseg = f'comp-{id} -> {component}'
                print(mseg)
            except Exception:
                print('NULL')


Y_1 = Test_Class_1()
Y_2 = Test_Class_2()

Y = Combo_Class(Test_Class_1, Test_Class_2)
print(Y.combo)