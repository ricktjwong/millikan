#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:31:01 2018

@author: ricktjwong
"""

import matplotlib as mpl

import numpy as np
import pandas as pd

import pims
import trackpy as tp
import os

from slicerator import pipeline  # or: from pims import pipeline

@pipeline
def as_grey(frame):
    red = frame[:, :, 0]
    green = frame[:, :, 1]
    blue = frame[:, :, 2]
    return 0.2125 * red + 0.7154 * green + 0.0721 * blue

mpl.rc('figure',  figsize=(10, 6))
mpl.rc('image', cmap='gray')

def compute_traj(filename):
        
#    vid = pims.Video('../060218_recordings/'+filename)
    vid = pims.Video('../test_vids/'+filename)
    frames = as_grey(vid)

    midpoint = len(frames)/2
    start = int(midpoint - 60)
    stop = int(midpoint + 60)
            
    f = tp.batch(frames[start:stop], 11, invert=False, minmass=160, maxsize=3.0, engine="numba");
    
    t = tp.link_df(f, 5, memory=3)
    
    t1 = tp.filter_stubs(t, 60)
    # Compare the number of particles in the unfiltered and filtered data.
    print('Before:', t['particle'].nunique())
    print('After:', t1['particle'].nunique())
    
    data = []
    for item in set(t1.particle):
        sub = t1[t1.particle==item]
        dvx = np.diff(sub.x)
        dvy = np.diff(sub.y)
        for x, y, dx, dy, frame, mass, size, ecc, signal, raw_mass, ep in \
        zip(sub.x[:-1], sub.y[:-1], dvx, dvy, sub.frame[:-1], sub.mass[:-1], sub['size'][:-1], sub.ecc[:-1], sub.signal[:-1], sub.raw_mass[:-1], sub.ep[:-1]):
            data.append({'dx': dx,
                         'dy': dy,
                         'x': x,
                         'y': y,
                         'frame': frame,
                         'particle': item,
                         'size': size,
                         'ecc': ecc,
                         'signal': signal,
                         'mass': mass,
                         'raw_mass': raw_mass,
                         'ep': ep
                        })
    df = pd.DataFrame(data)
    df.to_csv('../csv_raw/csv_raw_7/' + str(filename.split('.')[0]) + '.csv') 

#directory = os.fsencode("../060218_recordings/")
directory = os.fsencode("../test_vids/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".MOV"): 
        compute_traj(str(filename))