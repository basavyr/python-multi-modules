#!/usr/bin/env python

import sys


try:
    sys.path.append('../')
    import src.app1.module1.script1 as script1
except ImportError:
    sys.path.append('src/')
    import app1.module1.script1 as script1
finally:
    print('Finish importing...')
