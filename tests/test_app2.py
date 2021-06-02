import sys

try:
    sys.path.insert(1, '')
    from src.app2.module2 import script1
    from src.app2.module2 import script2
except ModuleNotFoundError:
    sys.path.insert(1, '../')
    from src.app2.module2 import script1
    from src.app2.module2 import script2

script1.Main()
