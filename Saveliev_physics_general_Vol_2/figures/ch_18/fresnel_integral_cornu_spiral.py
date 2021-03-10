# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:14:30 2021

@author: flvisa
"""

import scipy.special as sc
import numpy as np
from matplotlib import pyplot as plt


z = np.arange(0.0, 7.0, 0.01)

S, C = sc.fresnel(z)


plt.plot(C, S)
plt.plot(-C, -S)