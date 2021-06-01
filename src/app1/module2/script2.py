#!/usr/bin/env python

# try/except block for importing the script1
try:
    from app1.module2 import script1
except ModuleNotFoundError:
    import script1
except ImportError:
    from src.app1.module2 import script1


import os


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
    print(f'This is called from -> {script1.Class_Script.Get_Script_Name()}')
    print(f'{script1.Class_Script.Say_Hi()} | This is called from -> {script1.Class_Script.Get_Script_Name()}')


if __name__ == '__main__':
    Main()
