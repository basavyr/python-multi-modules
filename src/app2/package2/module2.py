#!/usr/bin/env python

import os
import platform
from datetime import datetime
import sys

# uses an external module, from package 1
try:
    from src.app2.package2 import module1 as m1
except ModuleNotFoundError:
    sys.path.insert(1, '')
    from src.app2.package2 import module1 as m1


class Class_Script:

    @staticmethod
    def Give_Array():
        try:
            # receive an array from module 1
            test_array = [1, 2, 'test']
            new_array = m1.Class_Script.Give_Array()
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

    @staticmethod
    def Test_Module2():
        sub_test1 = Class_Script.Give_Array()
        sub_test2 = None
        try:
            assert type(sub_test1) != type(None) and type(
                sub_test2) != type(None)
        except AssertionError:
            print('Invalid type')
        # try:
        #     assert all(sub_test1) and all(sub_test2)
        # except AssertionError as asserter:
        #     print(asserter)
        #     mseg = f'This is {os.path.basename(__file__)} inside Package-2 | ❌ Bad imports'
        # else:
        #     mseg = f'This is {os.path.basename(__file__)} inside Package-2 | ✅ Successfull imports'

        return 1


def Main():
    print(Class_Script.Test_Module2())


if __name__ == '__main__':
    Main()
