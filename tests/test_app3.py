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


class X_2_Class:
    """initialize a class that takes other two classes as arguments

    If the objects which are given as arguments are not initialized classes of Test_Class1 and Test_Class2 type, then the return object will be an array of None items.

    """

    def __init__(self, cls_1, cls_2):
        class_containers = [cls_1, cls_2]
        try:
            self.combo = [
                class_container.main_object for class_container in class_containers]
        except AttributeError:
            self.combo = [None for _ in class_containers]

    def Check_Container_Integrity(self):
        if(all(self.combo)):
            print('Passed')
        else:
            print('Failed')

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


class Combo_Class:
    def __init__(self, class_container):
        self.container = []
        for class_component in class_container:
            try:
                # non-initialized class
                self.container.append(class_component.main_object)
                # print(f'{class_component.main_object}')
                # return f'{class_component.main_object}'
            except AttributeError:
                # class instance
                self.container.append(class_component().main_object)
                # print(f'{class_component().main_object}')
                # return f'{class_component().main_object}'

    def Show_Container(self):
        return self.container


class_getter = lambda obj: m1.Export_Object.Get_Classes(obj)
function_getter = lambda obj: m1.Export_Object.Get_Functions(obj)


def Main():
    try:
        functions = function_getter(Test_Class_2())
        assert len(functions) == 4
    except AssertionError:
        print('App-3 failed ❌')
    else:
        print('App-3 works ✅')
    # print(f'Functions in {Test_Class_2.__name__}')
    # for fct in functions:
    #     print(fct[0])


if __name__ == '__main__':
    print(f'********** Package-1 **********')
    print(f'\n⚙️ Testing Module-1...\n')
    Main()
