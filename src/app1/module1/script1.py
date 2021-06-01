#!/usr/bin/env python


class Script1:
    @staticmethod
    def Say_Hi():
        print(f'Hi from {__name__}')


def Main():
    print(f'This is the main function from script 1')


if __name__ == '__main__':
    Main()
