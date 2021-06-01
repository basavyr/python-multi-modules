#!/usr/bin/env python


class Class_Script:
    @staticmethod
    def Say_Hi():
        try:
            print(f'Hi from {__name__}')
        except Exception:
            return 0
        else:
            return 1
