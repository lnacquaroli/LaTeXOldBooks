# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:30:45 2020

@author: flvisa
"""

import numpy as np
import h5py
import matplotlib.pyplot as plt


def fit_line(df, a):
    x = np.linspace(df.iloc[0, 0], df.iloc[-1, 0], 100)
    y = np.exp(a*x)
    return x, y


def get_data(fn, d):
    file = h5py.File(fn, "r")
    data = np.array(file.get(d))
    return data.T


def pure_argyleelegance():
    X = np.array([[0.2471,    0.4667,    0.6039],
                 [0.7373,    0.7804,    0.6157],
                 [0.9882,    0.8824,    0.5255],
                 [0.9373,    0.7216,    0.3255],
                 [0.7020,    0.4196,    0.4275],]
    )
    return X


def tableau_colors():
    X = ["#8C564B","#E377C2", "#7F7F7F", "#BCBD22", "#17BECF"]
    return X


# https://colorpalettes.net/color-palette-4215/
def palette_4215():
    X = ["#3d677b", "#a6a7a3", "#d3c7b1", "#c28f48", "#9a4832", "#6B724E"]
    return X


def remove_spines(ax):
    for i in range(0,ax.shape[0]):
        for j in range(0,ax.shape[1]):
            plt.setp(ax[i, j].spines["top"], visible=False)
            plt.setp(ax[i, j].spines["right"], visible=False)


def remove_spines_2(ax):
    for i in range(0,ax.shape[0]):
        plt.setp(ax[i].spines["top"], visible=False)
        plt.setp(ax[i].spines["right"], visible=False)
        
