#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:10:01 2018

@author: ricktjwong
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame.from_csv('501_2.csv')

def plotTraj(i):
    
    particle = df.loc[df['particle'] == i]
    
    plt.figure()
    plt.plot(particle['frame'], particle['x'])
    
    turning_index = particle['x'].idxmax()
    
    bef = particle[:turning_index]
    aft = particle[turning_index:]
    
    print(turning_index)
    
    return bef, aft

#bef, aft = plotTraj(6)
    
pivoted = df.pivot(index = 'frame', columns = 'particle')
pivoted_x = pivoted['x']
pivoted_dx = pivoted['dx']

def returnParticles(middle):
    filtered = []
    turning_indices = []
    for i in pivoted_x:
        turning_index = pivoted_x[i].idxmax()
        if abs(turning_index - middle) < 10:
            filtered.append(i)
            turning_indices.append(turning_index)
    return filtered, turning_indices

filtered_particles, turning_indices = returnParticles(334)

def returnFinal():
    final = []
    for i,j in zip(filtered_particles, turning_indices):
        particle = pivoted_dx[i]
        bef = particle[:j-pivoted_dx.index[0]]
        aft = particle[j-pivoted_dx.index[0]:]
        v_e = bef.sum()/len(bef)
        v_g = aft.sum()/len(aft)
        final.append({'particle': i, 'turning_point': j, 'v_e': v_e, 'v_g': v_g})

returnFinal()

#particles = set(df['particle'])

#for i in particles:
#    plotTraj(i)