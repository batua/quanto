#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 07:11:27 2018

@author: batu
"""

import os
import pytest

_path = os.path.dirname(__file__).replace('\\', '/')

testsdir =  _path + '/tests/'

if __name__ == '__main__':
    pytest.main(['-x', testsdir])

