#!/usr/bin/env python
import numpy as np

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
    print(message)
    with open('helper.md', 'w+') as writer:
        for function_component in dir(module1):
            writer.write(function_component)
            writer.write('\n')


if __name__ == '__main__':
    Main()
