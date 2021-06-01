#!/usr/bin/env python

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


def Main():
    print(
        f'This is the {Main.__name__}() function from {Class_Script.Get_Script_Name()}')


if __name__ == '__main__':
    Main()
