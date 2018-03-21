#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:24:01 2018

@author: batu
"""
import os
import startup

wdir = os.environ['WORK_DIR']
os.chdir(wdir + '/notebooks/')
os.system('jupyter notebook')
