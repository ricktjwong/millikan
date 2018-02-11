#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:10:01 2018

@author: ricktjwong
"""

import pandas as pd
import matplotlib.pyplot as plt
import trackpy as tp
import os

def plotTraj(i):
    particle = df.loc[df['particle'] == i]    
    plt.plot(particle['frame'], particle['x'])    
    turning_index = particle['y'].idxmax()    
    bef = particle[:turning_index]
    aft = particle[turning_index:]    
    print(turning_index)    
    return bef, aft
    
df = pd.DataFrame.from_csv('test_vids/test.csv')
x = tp.compute_drift(df)
x.plot()

#particles = set(df['particle'])
#
#for i in particles:
#    plotTraj(i)

def returnParticles(middle):
    filtered = []
    turning_indices = []
    for i in pivoted_y:
        turning_index = pivoted_y[i].idxmax()
        if abs(turning_index - middle) < 10:
            filtered.append(i)
            turning_indices.append(turning_index)
    return filtered, turning_indices

def filterParticles():
    turning_indices = []
    for i in pivoted_y:
        turning_index = pivoted_y[i].idxmax()
        turning_indices.append(turning_index)
    middle = int(sum(turning_indices)/len(turning_indices))
    return middle


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
                          'n': n, 
                          'size': size.sum()/len(size),
                          'ecc': ecc.sum()/len(ecc),
                          'signal': signal.sum()/len(signal),
                          'mass': mass.sum()/len(mass),
                          'ep': ep.sum()/len(ep)})
    return final

pivoted = df.pivot(index = 'frame', columns = 'particle')
pivoted_y = pivoted['y']
pivoted_dy = pivoted['dy']
pivoted_size = pivoted['size']
pivoted_ecc = pivoted['ecc']
pivoted_signal = pivoted['signal']
pivoted_mass = pivoted['mass']
pivoted_ep = pivoted['ep']

filtered_particles, turning_indices = returnParticles(184)

final = returnFinal(175)
df = pd.DataFrame(final)
df.to_csv('asdads.csv')