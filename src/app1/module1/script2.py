#!/usr/bin/env python


class Class_Script:
    @staticmethod
    def Say_Hi():
        try:
            message = f'Hi from {Class_Script.Say_Hi.__name__} in {Class_Script.__name__}'
            return message
        except Exception:
            return 0
        else:
            return 1


def Main():
    print(f'This is the {Main.__name__}() function from Script-2')


if __name__ == '__main__':
    Class_Script.Say_Hi()
    Main()
