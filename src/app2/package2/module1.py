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
    def Give_Array():
        try:
            new_array = np.arange(0, 101, 1)
        except Exception:
            return None
        else:
            return new_array


def Main():
    message = f'This is {os.path.basename(__file__)} script from Package-2'
    print(f'Successfully imported module -> {dir(m2_p1)}')
    print(message)
    try:
        x = m1_app3.Export_Object.Get_Classes(m2_p1)
        y = m1_app3.Export_Object.Get_Functions(m2_p1.Plot_Maker)
    except Exception:
        print(-1)
    else:
        print(f'x -> {x}')
        print(f'x -> {y}')


if __name__ == '__main__':
    Main()
    branch_name = 'test-apps'
    print(f'From brach -> {branch_name}')
