#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 03:24:27 2018

@author: ricktjwong
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.weight"] = "light"
plt.rcParams["font.size"] = 16
plt.rcParams['lines.linewidth'] = 0.8
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default']='regular'

#df = pd.DataFrame.from_csv("../final_csv/all_csvs/all.csv")

""" 050218 """

#df = pd.DataFrame.from_csv("../final_csv/final_csv_5_filtered/run_1/run_1.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_5_filtered/run_2/run_2.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_5_filtered/run_3/run_3.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_5_filtered/all_runs/all.csv")

""" 060218 UNWIPED """

#df = pd.DataFrame.from_csv("../final_csv/final_csv_6/finals/final6_575.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_6/finals/final6_550.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_6/finals/final6_525.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_6/finals/final6_all.csv")

""" 060218 WIPED """

#df = pd.DataFrame.from_csv("../final_csv/final_csv_7/finals/finals7_575.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_7/finals/finals7_550.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_7/finals/finals7_525.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_7/finals/final7_all.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_7_filtered/final_filtered/final7_filtered.csv")

""" ALL """

#df = pd.DataFrame.from_csv("../final_csv/final_all/final_final.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_7_filtered/final_filtered/final7_filtered.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_csv_7_filtered/final_filtered/final7_filtered525550.csv")
#df = pd.DataFrame.from_csv("../final_csv/final_all/all_filtered/final_final_all.csv")


condition1 = df['n'] > 0.1
condition2 = df['v_g'] < 0
condition3 = df['v_e'] >= 0
condition4 = df['mass'] > 300
condition5 = df['ecc'] < 0.3
condition6 = df['ep'] < 0.1
condition7 = df['size'] > 2.7
condition8 = df['n'] < 10
    
#filtered = df[condition1 & condition2 & condition3 & condition4 & condition5 & condition6 & condition7]
filtered = df[condition1 & condition8 & condition2 & condition3]
#filtered.to_csv("../final_csv/final_wiped.csv")

def correctCharges(filtered):
    b = 0.862
    l = 70E-9
    filtered['Radius'] = (abs(filtered['v_g'])*9/2*1.832E-5/(871*9.807))**0.5
    filtered['Corrected_charge'] = filtered['q']*(1/(1+b*l/filtered['Radius']))**1.5
#    filtered2 = filtered[filtered['Radius'] > 4.5]
    filtered.to_csv("../final_csv/final_wiped_millikan.csv")
    plot = filtered.plot.scatter(x='Radius', y='Corrected_charge', s=0.2)
    plot.minorticks_on()
    plot.grid(linestyle='--', which='major', linewidth=1)
    plot.grid(linestyle='--', which='minor', linewidth=1)
    for i in range(7):
        plot.axhline(y=(i+1)*1.6*1E-19, linewidth=1, color='r')
    plot.set_xlim([0, 20E-7])
    plot.set_ylim([0, 10E-19])

#    plt.savefig('../Figures/final_plots/final_mass'+'.pdf', format='pdf', dpi=3000)    

def firstApprox(filtered):
    
    """ FIRST APPROXIMATION """
    
    filtered['Radius (m)'] = (abs(filtered['v_g'])*9/2*1.832E-5/(871*9.807))**0.5/1E-7
    filtered['Charge (C)'] = filtered['q']*1E19
    
#    filtered2 = filtered[filtered['Radius'] > 4.5]
    
    plot = filtered.plot.scatter(x='Radius (m)', y='Charge (C)', s=0.2, color='blue')
    plot.spines['right'].set_visible(False)
    plot.spines['top'].set_visible(False)
#    plot.set_xlabel('xlabel', fontweight='light')
#    plot.set_ylabel('ylabel')
#    plot.minorticks_on()
#    plot.grid(linestyle='--', which='major', linewidth=1)
#    plot.grid(linestyle='--', which='minor', linewidth=1)
    for i in range(7):
        plot.axhline(y=(i+1)*1.6, linewidth=0.5, color='gray', linestyle='--')
        
    #plot.set_ylim([0, 10E-19])
    #plot.set_xlim([0, 1.2E-6])
    
    plt.savefig('../Figures/final_plots/unwiped'+'.pdf', format='pdf', dpi=3000)    

def millikansCorrection():
    
    """ MILLIKAN'S CORRECTION """
    
    filtered['q_obs2/3'] = filtered['q']**(2/3)/(1E-13)
    filtered['v_g2'] = (abs(filtered['v_g']))**-0.5
        
    plot2 = filtered.plot.scatter(x='v_g2', y='q_obs2/3', s=1.0)
    plot2.minorticks_on()
    plot2.grid(linestyle='--', which='major', linewidth=1)
    plot2.grid(linestyle='--', which='minor', linewidth=1)
    #plot2.set_ylim([0, 10E-13])
    for i in range(8):
        plot2.axhline(y=(i+1)*2.947225, linewidth=1, color='r')
    
#    plt.savefig('millikans_correction'+'.pdf', format='pdf', dpi=3000)    

def histogram():    
    pd.DataFrame.hist(filtered, column='n', bins=300)
    
firstApprox(filtered)
#correctCharges(filtered)
#millikansCorrection()
#histogram()
