#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:31:38 2018

@author: batu
"""
import numpy as np


def nday_return(df, nday=1, log=False):
    """
    Returns a simple or log return
    """
    gross_rtn = df/df.shift(periods=nday)
    if log:
        r = np.log(gross_rtn)
    else:
        r = gross_rtn - 1
    return r