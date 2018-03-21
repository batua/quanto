#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:31:38 2018

@author: batu
"""
import numpy as np


def nday_return(y, nday=1, log=False):
    """
    Returns a simple or log return
    """

    if log:
        r = np.log(y).diff(nday)
    else:
        r = y.diff(nday)/y
    return r