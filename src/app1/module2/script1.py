#!/usr/bin/env python

# try/except block for importing the script1
try:
    from app1.module2 import script2
except ModuleNotFoundError:
    import script2
except ImportError:
    from src.app1.module2 import script2


import os


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
            core = script2.Class_Script.Add_Numbers(num1, num2)
        except Exception:
            return None
        else:
            return core


def Main():
    print(
        f'This is the {Main.__name__}() function from {Class_Script.Get_Script_Name()}')


if __name__ == '__main__':
    Main()
