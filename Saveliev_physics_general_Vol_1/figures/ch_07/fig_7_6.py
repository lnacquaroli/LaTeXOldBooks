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
k = 1
A = 1
E = 1
t = np.arange(0, 1.65, 0.01)
omega_0 = 0.1
alpha = 0
x = A*np.cos(np.rad2deg(omega_0*t + alpha))
Ep = k*x**2/2
Ek = E*np.sin(np.rad2deg(omega_0*t + alpha))**2

# Plot
fig, ax = plt.subplots(3,1)

ax[0].spines["left"].set_position("zero")
ax[0].spines["bottom"].set_position("zero")
ax[0].plot(t, x, c=c[0], lw=lw, ls="solid")
#ax[0].set_xlabel(R"$t$", fontsize=fs)#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax[0].xaxis.set_label_coords(1.03,0.65)
#ax[0].set_ylabel(R"$x$", fontsize=fs, rotation=0, color=c[0])#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax[0].yaxis.set_label_coords(0.05,1.1)
#ax[0].text(-0.1, 0.92, r"$+A$", fontsize=fs)
#ax[0].text(-0.1, -0.92, r"$-A$", fontsize=fs)
#ax[0].grid(True, axis="both", visible=True)

ax[1].spines["bottom"].set_position("zero")
ax[1].plot(t, Ek, c=c[1], lw=lw, ls="solid")
ax[1].spines["left"].set_position("zero")
#ax[1].set_xlabel(R"$t$", fontsize=fs)#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax[1].xaxis.set_label_coords(1.03,0.65)
#ax[1].set_ylabel(R"$Ek$", fontsize=fs, rotation=0, color=c[1])#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax[1].yaxis.set_label_coords(0.05,1.1)
#ax[1].text(-0.1, 0.92, r"$+A$", fontsize=fs)
#ax[1].text(-0.1, -0.92, r"$-A$", fontsize=fs)

ax[2].spines["bottom"].set_position("zero")
ax[2].plot(t, Ep, c=c[3], lw=lw, ls="solid")
ax[2].spines["left"].set_position("zero")
#ax[2].set_xlabel(R"$t$", fontsize=fs)#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax[2].xaxis.set_label_coords(1.03,0.65)
#ax[2].set_ylabel(R"$Ep$", fontsize=fs, rotation=0, color=c[3])#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax[2].yaxis.set_label_coords(0.05,1.1)
#ax[2].text(-0.1, 0.92, r"$+A$", fontsize=fs)
#ax[2].text(-0.1, -0.92, r"$-A$", fontsize=fs)

utils.remove_all(ax)

#ax1.set_xlabel(R"$x$", fontsize=fs)#"Fluence, $\si{\milli\joule\per\square\centi\meter}$", fontsize=fs)
#ax1.xaxis.set_label_coords(1,-0.005)
##ax1.set(xlim=(-5,5))
#ax1.set_xticks([])#np.arange(-6,6,250))
#ax1.set_xticklabels([])
#ax1.set_ylabel(r"$E_{\text{p}}$", fontsize=fs, rotation=0)
#ax1.yaxis.set_label_coords(0.45,0.9)
#ax1.set_yticks([])#[round(i,2) for i in np.arange(0,1.1,0.25)])
#ax1.set_yticklabels([])#[round(i,2) for i in np.arange(0,1.1,0.25)], fontsize=fs)
## ax1.set_yticklabels([round(i,2) for i in np.arange(0,1.1,0.25)], fontsize=fs)
##ax1.set(ylim=(0.00,1.1))
#
#ax1.text(-4.6, -3, "Compression", fontsize=fs)
#ax1.text(-4, -5, r"$(x<0)$", fontsize=fs)
#ax1.text(1.75, -3, "Stretching", fontsize=fs)
#ax1.text(2, -5, r"$(x>0)$", fontsize=fs)
#ax1.text(-0.15, -3, r"$0$", fontsize=fs)
#
##ax1.legend(bbox_to_anchor=(1.05, 0.75), loc=2)
##ax1.legend(bbox_to_anchor=(0.5, 1.05), loc=2)
#
plt.savefig(path + r"\fig_7_6_.pdf", bbox_inches="tight")