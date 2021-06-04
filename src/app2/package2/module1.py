#!/usr/bin/env python

import numpy as np

import os
import sys


# uses an external module, from package 1
try:
    from src.app2.package1 import module2 as m2_p1
    from src.app3.package1 import module1 as m1_app3
except ModuleNotFoundError:
    sys.path.insert(1, '')
    from src.app2.package1 import module2 as m2_p1
    from src.app3.package1 import module1 as m1_app3


class Class_Script:

    @staticmethod
    def Test():
        mseg = f'function {Class_Script.Test.__name__}() from  {os.path.basename(__file__)} inside Package-1'
        return mseg

    @staticmethod
    def Give_Array():
        try:
            new_array = np.arange(0, 101, 1)
        except Exception:
            return None
        else:
            return new_array


def Main():
    message = f'This is {os.path.basename(__file__)} script from Package-2'
    print(message)


if __name__ == '__main__':
    Main()
