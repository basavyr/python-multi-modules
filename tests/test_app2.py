from datetime import datetime
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
finally:
    print(f'\nImporting modules from {app} -> OK ✅\n')


class Test_Module2_Script1:

    @staticmethod
    def test_main():
        ok_msg = f'Test @ {datetime.utcnow()}: ✅'
        fail_msg = f'Test @ {datetime.utcnow()}: ❌'
        try:
            x = script1.Main()
        except Exception:
            print(fail_msg)
        else:
            print(ok_msg)

    @staticmethod
    def Start_Test():
        Test_Module2_Script1.test_main()


def Main():
    Test_Module2_Script1.Start_Test()


if __name__ == '__main__':
    Main()
