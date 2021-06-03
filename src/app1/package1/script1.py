#!/usr/bin/env python

import time


class Class_Script:
    @staticmethod
    def Say_Hi():
        try:
            message = f'Hi from {Class_Script.Say_Hi.__name__} in {Class_Script.__name__}'
        except Exception:
            return 0
        else:
            return message

    @staticmethod
    def Show_Time(name):
        try:
            now = time.time()
        except Exception:
            return 0
        else:
            return f'{name} -> {now}'

    @classmethod
    def Compute_Term(cls, elements):
        operation = lambda x: x * 2
        for element in elements:
            try:
                assert type(element) != str
            except AssertionError:
                return 0
            else:
                pass
        try:
            new_elements = list(map(operation, elements))
        except Exception:
            return 0
        return new_elements


def Main():
    print(f'This is the {Main.__name__}() function from Script-1')


if __name__ == '__main__':
    Main()
