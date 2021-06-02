import sys

app = 'App-2'


try:
    sys.path.insert(1, '')
    from src.app2.module2 import script1
    from src.app2.module2 import script2
except ModuleNotFoundError:
    sys.path.insert(1, '../')
    from src.app2.module2 import script1
    from src.app2.module2 import script2


class Test_Module2_Script1:

    @staticmethod
    def test_main():
        try:
            x = script1.Main()
            print(x)
        except Exception:
            print('Test failed ❌')
        else:
            print('Test passed ✅')


def Main():
    print('Main works')


if __name__ == '__main__':
    Main()
