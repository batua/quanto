#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:53:08 2018

@author: batu
"""

import os
import sys

_path = os.path.dirname(__file__).replace('\\', '/')

WORK_DIR = _path[:_path.rfind('/')+1]
os.environ['WORK_DIR'] = WORK_DIR

if WORK_DIR not in sys.path:
    sys.path.append(WORK_DIR)
    
    if 'PYTHONPATH' in os.environ:
        os.environ['PYTHONPATH'] = WORK_DIR + ':' + os.environ['PYTHONPATH']
    else:
        os.environ['PYTHONPATH'] = WORK_DIR



