#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 07:21:05 2018

@author: batu
"""
import numpy as np
import pandas as pd


from analytics.financials import utils


def test_log_nday_return():
    df = pd.DataFrame([112.5, 110.5, 110.9, 113.9], columns=['price'])
    expected_log_rtn_1 = np.array([np.nan, -0.017937700686667318,
                                   0.0036133733985138313, 0.026691976096815107])
    expected_log_rtn_3 = np.array([np.nan, np.nan,
                                   np.nan, 0.012367648808661669])

    df_log_rtn_1 = utils.nday_return(df, nday=1, log=True)
    df_log_rtn_3 = utils.nday_return(df, nday=3, log=True)

    np.testing.assert_array_equal(df_log_rtn_1.values[:,0],
                                  expected_log_rtn_1)
    np.testing.assert_array_equal(df_log_rtn_3.values[:,0],
                                  expected_log_rtn_3)

