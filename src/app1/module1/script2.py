#!/usr/bin/env python

import os
import platform


class Class_Script:
    @staticmethod
    def Say_Hi():
        try:
            message = f'Hi from {Class_Script.Say_Hi.__name__} in {Class_Script.__name__}'
            return message
        except Exception:
            return 0
        else:
            return 1

    @staticmethod
    def Show_Location(directory):
        try:
            path = os.getcwd()
            new_path = path + directory
        except Exception:
            return 0
        return new_path

    @staticmethod
    def Show_System_Info(pc_name):
        try:
            uname = platform.uname()
            full_pc_name = f'This PC -> {pc_name}\n{uname}'
        except Exception:
            return 0
        else:
            return full_pc_name


def Main():
    print(f'This is the {Main.__name__}() function from Script-2')


if __name__ == '__main__':
    Class_Script.Say_Hi()
    Main()
