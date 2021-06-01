#!/usr/bin/env python

import sys


try:
    sys.path.append('../')
    import src.app1.module1.script1 as m1
except ImportError:
    sys.path.append('src/')
    import app1.module1.script1 as m1

m1.Script1.Say_Hi()
