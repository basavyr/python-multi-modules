import inspect
import sys
import os


class Export_Object:
    """A class which offers a set of implementations that extract information from objects, such as classes, functions, methods, attributes and many more.
    By default, all the information will be stored into an output file.
    """

    object_info_file = 'object_info.md'

    @staticmethod
    def Import_Object(obj):
        try:
            assert obj != None
        except AssertionError:
            return None
        else:
            return obj

    @staticmethod
    def Get_Classes(obj):
        try:
            assert obj != None
        except AssertionError:
            return None
        class_members = inspect.getmembers(obj, inspect.isclass)
        return class_members

    @staticmethod
    def Get_Functions(obj):
        try:
            assert obj != None
        except AssertionError:
            return None
        function_members = inspect.getmembers(obj, inspect.isfunction)
        return function_members


def Main():
    test_object = ['a string', f'a number -> {4}']
    fake_test = None
    try:
        x = Export_Object.Import_Object(test_object)
        y = Export_Object.Get_Classes(test_object)
        z = Export_Object.Get_Functions(test_object)
        assert x != None and y != None and z != None, "Invalid results for x,y,z"
    except AssertionError:
        print(f'Failed running {os.path.basename(__file__)} ❌')
    else:
        print(f'Running {os.path.basename(__file__)} successfully ✅')


if __name__ == '__main__':
    Main()
