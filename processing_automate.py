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
        particle = pivoted_dy[i]
        bef = particle[:j-pivoted_dy.index[0]]
        aft = particle[j-pivoted_dy.index[0]:]
        if len(bef) > 0 and len(aft) > 0:
            v_e = bef.sum()/len(bef) 
            v_g = aft.sum()/len(aft)
        else:
            v_e = 0
            v_g = 0
        ve_si = v_e*30/8*0.05E-03
        vg_si = v_g*30/8*0.05E-03
        k = 3.39249E-08
        charge = k*abs(vg_si)**0.5*(abs(vg_si)+abs(ve_si))/(voltage/0.006)
        n = (charge/(1.60217662E-19))
        final.append({'particle': i, 'turning_point': j, 'v_e': v_e, 'v_g': v_g, 'n': n})
    return final

def highestNumber(start, end, number, all_angles):

    turning_dict = dict()
    intervals = np.linspace(start, end, number)
    step = (end-start)/number
    for i in intervals:
        N = len([x for x in all_angles if x > i and x < i+step])
        mean = int(i + step/2)
        turning_dict[str(mean)] = N
    key = int(max(turning_dict.items(), key=operator.itemgetter(1))[0])
    return key

directory = os.fsencode("csv")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    df = pd.DataFrame.from_csv("csv/"+str(filename))
    pivoted = df.pivot(index = 'frame', columns = 'particle')
    pivoted_y = pivoted['y']
    pivoted_dy = pivoted['dy']
    turningIndices = getIndices()
    middle = highestNumber(pivoted_dy.index[0], pivoted_dy.index[-1], 50, turningIndices)
    filtered_particles, turning_indices = returnParticles(middle)
    final = returnFinal(int(filename.split('-')[0]))
    data_final = pd.DataFrame(final)
    data_final.to_csv("final_csv/final_"+str(filename))