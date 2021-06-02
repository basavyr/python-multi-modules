#!/usr/bin/env python
import numpy as np


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
    message = f'This is {__file__} script from Module-1'
    print(message)


if __name__ == '__main__':
    Main()
