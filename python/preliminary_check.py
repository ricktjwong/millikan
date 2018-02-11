#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:48:15 2018

@author: ricktjwong
"""

import pandas as pd
import matplotlib.pyplot as plt
import trackpy as tp
import os

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['lines.linewidth'] = 0.8
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default']='regular'


def generateDriftPlots():
    
    directory = os.fsencode("../csv_raw/csv_raw_4")
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"): 
            df = pd.DataFrame.from_csv("../csv_raw/csv_raw_4/"+str(filename))
            x = tp.compute_drift(df)
            plt.figure()
            filename = filename.split('.')[0]
            plt.title(str(filename))
            plt.xlabel('Frame Number')
            plt.ylabel('Pixels')
            plt.plot(x)
#            plt.savefig('../Figures/drift_plots_2/'+filename+'.pdf', format='pdf', dpi=3000)    

def generateBandPlots():
    
    directory = os.fsencode("../final_csv/final_csv_7")
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"): 
            df = pd.DataFrame.from_csv("../final_csv/final_csv_7/" + filename)
            
            condition1 = df['n'] > 0.0
            
            filtered = df[condition1]
            #filtered.to_csv("final_csv2/merged2.csv")
            
            firstApprox(filename, filtered)

def firstApprox(filename, filtered):
    
    """ FIRST APPROXIMATION """
    
    filtered['Radius'] = (abs(filtered['v_g'])*9/2*1.832E-5/(871*9.807))**0.5/1E-7
    
    filename = filename.split('.')[0]
    plot = filtered.plot.scatter(x='Radius', y='n', s=5.0)
    plot.minorticks_on()
    plot.grid(linestyle='--', which='major', linewidth=1)
    plot.grid(linestyle='--', which='minor', linewidth=1)
    plot.set_title(str(filename))
    for i in range(7):
        plot.axhline(y=(i+1)*1.00, linewidth=1, color='r')
    
    plt.savefig('../Figures/indiv_plots_4/'+filename+'.pdf', format='pdf', dpi=3000)  
        
#generateDriftPlots()
generateBandPlots()