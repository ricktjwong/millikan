# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:56:16 2018

@author: Danielsrq
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.weight"] = "light"
plt.rcParams["font.size"] = 16
plt.rcParams['lines.linewidth'] = 2
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default']='regular'

x = np.arange(800) * 0.01

def gauss(x, sigma, mu):
    return (1/(sigma * np.sqrt(2*np.pi)) ) * np.exp(-0.5 * ((x-mu)/sigma)**2 )

sigma_res = 0.2900482
sigma1, sigma2, sigma3 = 0.67703/2, 0.7609/2, 3.16059/2
mu1, mu2, mu3 = 1.6752, 3.23668, 4.71988
A1, A2, A3 = 139.1548, 31.80335, 31.51135

sigma1_d, sigma2_d, sigma3_d = (sigma1**2-sigma_res**2)**0.5, (sigma2**2-sigma_res**2)**0.5, (sigma3**2-sigma_res**2)**0.5

q1 = A1 * gauss(x, sigma1, mu1)
q2 = A2 * gauss(x, sigma2, mu2)
q3 = A3 * gauss(x, sigma3, mu3)
q1_d = A1 * gauss(x , sigma1_d, mu1)
q2_d = A2 * gauss(x, sigma2_d, mu2)
q3_d = A3 * gauss(x, sigma3_d, mu3)

print("Band 1: " + str(mu1) + " +/- " + str(sigma1_d))
print("Band 2: " + str(mu2) + " +/- " + str(sigma2_d))
print("Band 3: " + str(mu3) + " +/- " + str(sigma3_d))

plt.figure()
plt.plot(x , q1, 'r')
plt.plot(x , q2, 'b')
plt.plot(x , q3, 'g')
plt.plot(x , q1_d, 'r', linestyle='--')
plt.plot(x , q2_d, 'b', linestyle='--')
plt.plot(x , q3_d, 'g', linestyle='--')
plt.ylabel("Count")
plt.xlabel("Charge (C)")
plt.show()

plt.savefig('../Figures/final_plots/deconv_unwiped2'+'.pdf', format='pdf', dpi=3000)    