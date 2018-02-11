#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:31:01 2018

@author: ricktjwong
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience

import pims
import trackpy as tp

import os

mpl.rc('figure',  figsize=(10, 6))
mpl.rc('image', cmap='gray')

def gray(image):
    return image[:, :, 0]

datapath = '501-0_1'
prefix = 'frame'

frames = pims.ImageSequence(os.path.join(datapath, prefix + '*.png'), process_func=gray)

f = tp.locate(frames[0], 11, invert=False)

plt.figure()
tp.annotate(f, frames[0]);

fig, ax = plt.subplots()
ax.hist(f['mass'], bins=100)

# Optionally, label the axes.
ax.set(xlabel='mass', ylabel='count');

f = tp.locate(frames[0], 11, invert=False, minmass=200, maxsize = 2.6)

plt.figure()
tp.annotate(f, frames[0], plot_style={'markersize': 5});

f = tp.batch(frames[284:384], 11, invert=False, minmass=200, maxsize = 2.6, engine="numba");
#f = tp.batch(frames[:10], 11, invert=False, minmass=200, maxsize = 2.6, engine="numba");

t = tp.link_df(f, 5, memory=3)

t1 = tp.filter_stubs(t, 2)
# Compare the number of particles in the unfiltered and filtered data.
print('Before:', t['particle'].nunique())
print('After:', t1['particle'].nunique())

d = tp.compute_drift(t1, skip=1)
plt.figure()
d.plot()

plt.figure()
tp.plot_traj(t1);

data = []
for item in set(t1.particle):
    sub = t1[t1.particle==item]
    dvx = np.diff(sub.x)
    dvy = np.diff(sub.y)
    for x, y, dx, dy, frame in zip(sub.x[:-1], sub.y[:-1], dvx, dvy, sub.frame[:-1],):
        data.append({'dx': dx,
                     'dy': dy,
                     'x': x,
                     'y': y,
                     'frame': frame,
                     'particle': item
                    })
df = pd.DataFrame(data)
    
#i = 250
#d = data[data.frame==i]
#plt.figure()
#plt.imshow(frames[i])
#plt.quiver(d.x, d.y, d.dx, -d.dy, pivot='middle', headwidth=0.1, headlength=0.1, color='yellow')
#plt.axis('off')

#data.to_csv('501.csv')