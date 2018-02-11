#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 21:09:54 2018

@author: ricktjwong
"""

import pandas as pd
import operator
import os
import numpy as np

def returnParticles(middle):
    filtered = []
    turning_indices = []
    for i in pivoted_y:
        turning_index = pivoted_y[i].idxmax()
        if abs(turning_index - middle) < 20:
            filtered.append(i)
            turning_indices.append(turning_index)
    return filtered, turning_indices

def getIndices():
    turning_indices = []
    for i in pivoted_y:
        turning_index = pivoted_y[i].idxmax()
        turning_indices.append(turning_index)
    return turning_indices

def returnFinal(voltage):
    final = []
    for i,j in zip(filtered_particles, turning_indices):
        particle = pivoted_dy[i][pd.Series.notnull(pivoted_dy[i])]
        size = pivoted_size[i][pd.Series.notnull(pivoted_size[i])]
        ecc = pivoted_ecc[i][pd.Series.notnull(pivoted_ecc[i])]
        signal = pivoted_signal[i][pd.Series.notnull(pivoted_signal[i])]
        mass = pivoted_mass[i][pd.Series.notnull(pivoted_mass[i])]
        ep = pivoted_ep[i][pd.Series.notnull(pivoted_ep[i])]
        bef = particle[:j-particle.index[0]]
        aft = particle[j-particle.index[0]:]
        if len(bef) > 0 and len(aft) > 0:
            v_e = bef.sum()/len(bef) 
            v_g = aft.sum()/len(aft)
            ve_si = v_e*30/8*0.05E-03
            vg_si = v_g*30/8*0.05E-03
            k = 3.39249E-08
            charge = k*abs(vg_si)**0.5*(abs(vg_si)+abs(ve_si))/(voltage/0.006)
            n = (charge/(1.60217662E-19))
            final.append({'particle': i, 
                          'turning_point': j, 
                          'v_e': ve_si, 
                          'v_g': vg_si, 
                          'q': charge,
                          'n': n, 
                          'size': size.sum()/len(size),
                          'ecc': ecc.sum()/len(ecc),
                          'signal': signal.sum()/len(signal),
                          'mass': mass.sum()/len(mass),
                          'ep': ep.sum()/len(ep)})
    return final

def highestNumber(start, end, number, all_middle):

    turning_dict = dict()
    intervals = np.linspace(start, end, number)
    step = (end-start)/number
    for i in intervals:
        N = len([x for x in all_middle if x > i and x < i+step])
        mean = int(i + step/2)
        turning_dict[str(mean)] = N
    key = int(max(turning_dict.items(), key=operator.itemgetter(1))[0])
    return key

directory = os.fsencode("../csv_raw/csv_raw_7/525_wiped")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"): 
        df = pd.DataFrame.from_csv("../csv_raw/csv_raw_7/525_wiped/"+str(filename))
        pivoted = df.pivot(index = "frame", columns = "particle")
        pivoted_y = pivoted['y']
        pivoted_dy = pivoted['dy']
        pivoted_size = pivoted['size']
        pivoted_ecc = pivoted['ecc']
        pivoted_signal = pivoted['signal']
        pivoted_mass = pivoted['mass']
        pivoted_ep = pivoted['ep']
        turningIndices = getIndices()
        middle = highestNumber(pivoted_dy.index[0], pivoted_dy.index[-1], 50, turningIndices)
        filtered_particles, turning_indices = returnParticles(middle)
        final = returnFinal(int(filename.split('-')[0]))
        data_final = pd.DataFrame(final)
        data_final.to_csv("../final_csv/final_csv_7/final_"+str(filename))