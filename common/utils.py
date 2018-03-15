#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:29:38 2018

@author: batu
"""

import matplotlib.pyplot as plt


def groupby_subplot(grouped, columns, plot,
                    ncol=4, figsize=(20, 15), ticksize=(8, 8)):
    """
    Creates the subplots out of each group in the groups

    Parameters
    ----------
    grouped: Pandas groupby object
    columns: Column labels to use for resulting plot
    plot: Plot function taking pandas DataFrame as an argument
    """
    ngroups = grouped.ngroups

    xticksize = ticksize[0]
    yticksize = ticksize[1]
    with plt.rc_context({'xtick.labelsize': xticksize,
                         'ytick.labelsize': yticksize}):
        fig, axes = plt.subplots(int(ngroups/ncol) + 1
                                 * (ngroups % ncol > 0), ncol,
                                 figsize=figsize, squeeze=False)
        for (key, group), ax in zip(grouped, axes.flatten()):
            plt.sca(ax)  # sets the current axis
            plot(group[columns])
        fig.tight_layout()


def groupby_asdf(df, grouped, idx=0):
    """
    Returns pandas DataFrame as a subset from df with given index idx in
    the grouped

    Parameters
    ----------
    df: pandas DataFrame
    grouped: pandas GroupBy object based on df
    idx: group index in grouped

    Returns
    -------
    pandas DataFrame as a subset from df in the grouped with a given index idx

    """

    start = grouped.groups[idx][0]
    end = grouped.groups[idx][-1]
    return df[start:end]
