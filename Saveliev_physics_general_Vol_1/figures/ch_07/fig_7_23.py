# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:30:03 2020

@author: lnacquaroli
"""

#!/home/leniac/anaconda3/bin/python

import numpy as np
#import h5py
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
#from scipy.optimize import curve_fit
import plot_utils as utils 

##

# Font size
fs = 10
factor = 1.0
width_fig = 3.4*factor  # inch

rcParams["font.family"] = "serif"
rcParams["figure.figsize"] = [width_fig, width_fig/1.333333333333333/factor]
rcParams["legend.handletextpad"] = 0.01

rc("text", usetex=True)
rc("font", size=fs)          # controls default text sizes
rc("legend", fontsize=fs-1)    # legend fontsize
rc("text.latex", preamble=[r"\usepackage[utf8]{inputenc}",
   r"\usepackage[english]{babel}",
   r"\usepackage[p,osf,swashQ,sups]{cochineal}",
   r"\usepackage[varqu,varl,var0]{inconsolata}",
   r"\usepackage[scale=.95,type1]{cabin}",
   r"\usepackage[cochineal,vvarbb,slantedGreek]{newtxmath}",
   r"\usepackage[cal=boondoxo]{mathalfa}",
   r"\usepackage{amsmath}",
   r"\usepackage{siunitx}",],
)

##

plt.close("all")

# file name
#path = "/home/leniac/Flavia/phd/tesis/2019_tesis/Imagen_GraficosMios/"
path = r"C:\Users\flvisa\Desktop\lna\latexify_books\physics_general_course_1_saveliev\figures\cap_07"
#filename = path + r"\fig3_data.h5"

c = utils.palette_4215()
lw = 1.5

# Data
A0 = 1.0
omega = 70.0
beta = 8.0
alpha = np.pi/2.0
phi = np.pi/2.0
t = np.arange(0, 1.025, 0.001)
A2 = 1.0
A = A0*np.exp(-beta*t)
x112 = A*np.cos(omega*t + alpha)
x119 = A2*np.cos(omega*t - phi)

# Plot
#fig, ax = plt.subplots(2,1)
fig, ax = plt.subplots()

ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.plot(t, x112+x119, c=c[0], lw=lw, ls="solid")
ax.plot(t, A-1.0, c=c[2], lw=lw, ls="dashed")
ax.plot(t, 1.0-A, c=c[2], lw=lw, ls="dashed")
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])

#ax[0].set_xlabel(R"$t$", fontsize=fs)#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax[0].xaxis.set_label_coords(1.03,0.65)
#ax[0].set_ylabel(R"$x$", fontsize=fs, rotation=0, color=c[0])#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax[0].yaxis.set_label_coords(0.05,1.1)
#ax[0].text(-0.1, 0.92, r"$+A$", fontsize=fs)
#ax[0].text(-0.1, -0.92, r"$-A$", fontsize=fs)
#ax[0].grid(True, axis="both", visible=True)

#ax[1].spines["bottom"].set_position("zero")
#ax[1].plot(phi, np.abs(np.cos(phi)), c=c[3], lw=lw, ls="solid")
#ax[1].spines["left"].set_position("zero")

plt.setp(ax.spines["top"], visible=False)
plt.setp(ax.spines["right"], visible=False)
#plt.setp(ax.spines["bottom"], visible=False)
#plt.setp(ax.spines["left"], visible=False)
#

#
##ax1.legend(bbox_to_anchor=(1.05, 0.75), loc=2)
##ax1.legend(bbox_to_anchor=(0.5, 1.05), loc=2)
#
plt.savefig(path + r"\fig_7_23_.pdf", bbox_inches="tight")