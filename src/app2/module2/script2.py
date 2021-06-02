#!/usr/bin/env python

import os


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


def Main():
    print(Class_Script.Give_Array())


if __name__ == '__main__':
    Main()
