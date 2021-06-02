#!/usr/bin/env python

import os

def Test():
    return f'function {Test.__name__}() from  {os.path.basename(__file__)} inside Module-1'
