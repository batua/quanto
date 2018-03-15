#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:44:43 2018

@author: batu
"""
import numpy as np


def select_n_components(X, mixture, maxcomp):
    """
    Returns the optimal number of components in
    the mixture based on AIC and BIC
    """

    n_components = np.arange(1, maxcomp + 1)
    models = [mixture(n_components=n).fit(X) for n in n_components]

    m_bic = [m.bic(X) for m in models]
    m_aic = [m.aic(X) for m in models]

    n_components_bic = m_bic.index(min(m_bic)) + 1   # index starts with 0
    n_components_aic = m_aic.index(min(m_aic)) + 1

    return (n_components_bic, n_components_aic, m_bic, m_aic)


def quantile_eq(f, alpha):
    def g(x):
        return f(x) - alpha
    return g