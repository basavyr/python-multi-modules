#!/usr/bin/env python

import sys
import os

# print(f'module2/package2 -> {sys.path}')


try:
    from src.app1.package2 import module1
except ModuleNotFoundError:
    import module1

# try/except block for importing the module1
# try:
#     from src.app1.module2 import module1
# except ModuleNotFoundError:
#     from app1.module2 import module1
# except ImportError:
#     import module1


class Class_Script:
    @staticmethod
    def Get_Script_Name():
        try:
            script_name = os.path.basename(__file__)
        except Exception:
            return None
        else:
            return script_name

    @staticmethod
    def Say_Hi():
        try:
            message = f'Hi from {Class_Script.Say_Hi.__name__} from {Class_Script.__name__}'
        except Exception:
            return None
        else:
            return message

    @staticmethod
    def Add_Numbers(num1, num2):
        try:
            x = [num1 for _ in range(10)]
            y = [num2 for _ in range(10)]
        except Exception:
            return None
        else:
            return x, y


def Main():
    print(
        f'This is the {Main.__name__}() function from {Class_Script.Get_Script_Name()}')
    print(f'This is called from -> {module1.Class_Script.Get_Script_Name()}')
    print(f'{module1.Class_Script.Say_Hi()} | This is called from -> {module1.Class_Script.Get_Script_Name()}')


if __name__ == '__main__':
    Main()
