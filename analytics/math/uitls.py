#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 00:09:54 2018

@author: batu
"""


def weighted_funcs(ws, fs):
    def f(x):
        r = 0
        for w_, f_ in zip(ws, fs):
            r += w_ * f_(x)
        return r
    return f
