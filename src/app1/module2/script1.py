#!/usr/bin/env python


class Class_Script:
    @staticmethod
    def Say_Hi():
        try:
            message = f'Hi from {Class_Script.Say_Hi.__name__} from {Class_Script.__name__}'
        except Exception:
            return None
        else:
            return message


def Main():
    print(f'This is the {Main.__name__}() function from Script-1')
