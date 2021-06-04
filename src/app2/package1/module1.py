#!/usr/bin/env python

import os
import numpy as np


class Class_Script:

    @staticmethod
    def Test():
        mseg = f'function {Class_Script.Test.__name__}() from  {os.path.basename(__file__)} inside Package-1'
        return mseg

    @staticmethod
    def Extra_Test():
        x = np.arange(0, 11, 1)
        y = list(map(lambda x: x * 2, x))
        assert len(x) == len(y), 'Arrays do not have the same length'
        return x, y

    @staticmethod
    def Combo_Function():
        try:
            x_1 = Class_Script.Test()
            x_2 = Class_Script.Extra_Test()
        except Exception:
            return -1
        else:
            return 1


def Main():
    print(Class_Script.Test())


if __name__ == '__main__':
    Main()
