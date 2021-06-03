#!/usr/bin/env python
import numpy as np
from inspect import getmembers, isclass, isfunction
import os
import sys

# print(f'in module 1 from package 2 {sys.path}')

try:
    from src.app2.package1 import module1
except ModuleNotFoundError:
    sys.path.insert(1, '../')
    from package1 import module1


class Class_Script:
    @staticmethod
    def Give_Array():
        try:
            new_array = np.arange(0, 101, 1)
        except Exception:
            return None
        else:
            return new_array


def Main():
    message = f'This is {os.path.basename(__file__)} script from Module-2'
    m1 = module1
    print('******* Classes *******')
    for x in getmembers(m1, isclass):
        print(f'class --> {x[0]}')
    print('******* Functions *******')
    for x in getmembers(m1,isfunction):
        print(f'function --> {x[0]}()')


if __name__ == '__main__':
    Main()
