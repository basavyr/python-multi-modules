#!/usr/bin/env python

import os

import sys
# print(f'module1/package2 -> {sys.path}')


try:
    from src.app1.package2 import module2
except ModuleNotFoundError:
    import module2


# try/except block for importing the script1
# try:
#     from src.app1.module2 import script2
# except ModuleNotFoundError:
#     import script2
# except ImportError:
#     from app1.module2 import script2


class Class_Script:
    @staticmethod
    def Get_Script_Name():
        return os.path.basename(__file__)

    @staticmethod
    def Say_Hi():
        try:
            message = f'Hi from {Class_Script.Say_Hi.__name__} from {Class_Script.__name__} within {Class_Script.Get_Script_Name()}'
        except Exception:
            return None
        else:
            return message

    @staticmethod
    def Test_External_Functions(num1, num2):
        try:
            core = module2.Class_Script.Add_Numbers(num1, num2)
        except Exception:
            return None
        else:
            return core


def Main():
    print(
        f'This is the {Main.__name__}() function from {Class_Script.Get_Script_Name()}')


if __name__ == '__main__':
    Main()
