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


def compute_phi(beta, omega_0, omega_i, omega_f):
    phia = np.rad2deg(np.arctan((2.0*beta*omega_i)/(omega_0**2 - omega_i**2)))
    phib = np.rad2deg(np.arctan((2.0*beta*omega_f)/(omega_0**2 - omega_f**2)))
    phi= np.concatenate([phia, phib - np.min(phib) + np.max(phia)])
    return phi


plt.close("all")

# file name
#path = "/home/leniac/Flavia/phd/tesis/2019_tesis/Imagen_GraficosMios/"
path = r"C:\Users\flvisa\Desktop\lna\latexify_books\physics_general_course_1_saveliev\figures\cap_07"
#filename = path + r"\fig3_data.h5"

c = utils.palette_4215()
lw = 1.5

# Data
omega_0 = 1.0
omega_i = np.arange(0, 0.9999, 0.0001)
omega_f = np.arange(1.0001, 1.999999, 0.0001)
omega = np.concatenate([omega_i, omega_f])
beta3 = 0.3
beta2 = 0.14
beta1 = 0.05

phi1 = compute_phi(beta1, omega_0, omega_i, omega_f)
phi2 = compute_phi(beta2, omega_0, omega_i, omega_f)
phi3 = compute_phi(beta3, omega_0, omega_i, omega_f)

# Plot
#fig, ax = plt.subplots(2,1)
fig, ax = plt.subplots()

#ax.spines["left"].set_position("zero")
#ax.spines["bottom"].set_position("zero")
ax.plot(omega, phi1, c=c[0], lw=lw, ls="solid")
ax.plot(omega, phi2, c=c[3], lw=lw, ls="solid")
ax.plot(omega, phi3, c=c[4], lw=lw, ls="solid")
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])
#plt.ylim([0, 180])

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
plt.savefig(path + r"\fig_7_25_.pdf", bbox_inches="tight")