import sys

try:
    sys.path.insert(1, '')
    from src.app2.module2 import script1
    from src.app2.module2 import script2
except ModuleNotFoundError:
    print(1)
except ImportError:
    print(0)

script1.Main()
