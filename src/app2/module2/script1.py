#!/usr/bin/env python
import numpy as np

import os

from src.app2.module1 import script1


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
    message = f'This is {os.path.basename(__file__)} script from Module-1'
    # print(message)
    s1.Test()


if __name__ == '__main__':
    Main()
