#!/usr/bin/env python

import os
import numpy as np


class Class_Script:
    @staticmethod
    def Test():
        mseg = f'function {Class_Script.Test.__name__}() from  {os.path.basename(__file__)} inside Module-1'
        # print(mseg)
        return mseg

    @staticmethod
    def Extra_Text():
        x = np.arange(0, 11, 1)
        y = list(map(lambda x: x * 2, x))
        assert len(x) == len(y), 'Arrays do not have the same length'
        return x, y


def Main():
    Class_Script.Test()


if __name__ == '__main__':
    Main()
