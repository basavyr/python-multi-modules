#!/usr/bin/env python

import os
import platform
from datetime import datetime


class Class_Script:
    @staticmethod
    def Give_Array():
        try:
            new_array = [os.path.relpath(__file__)]
            new_array.append(os.path.basename(__file__))
        except Exception:
            return None
        else:
            return new_array

    @staticmethod
    def Get_Time():
        try:
            message = f'{datetime.utcnow()} -> {platform.os.uname()}'
        except Exception:
            return None
        else:
            return message


def Main():
    print(Class_Script.Give_Array())
    print(Class_Script.Get_Time())


if __name__ == '__main__':
    Main()
