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

def gray(image):
    return image[:, :, 0]

mpl.rc('figure',  figsize=(10, 6))
mpl.rc('image', cmap='gray')
mpl.rc('font', family = "Times New Roman")

datapath = '../report_imgs'
prefix = 'frame'

#vid = pims.Video('../300118_recordings/varying_voltage/575-0_1.MOV')

frames = pims.ImageSequence(os.path.join(datapath, prefix + '*.png'), process_func=gray)
#frames = as_grey(vid)

f = tp.locate(frames[0], 11, invert=False)

plt.figure()
tp.annotate(f, frames[0]);

fig, ax = plt.subplots()
ax.hist(f['mass'], bins=100)

# Optionally, label the axes.
ax.set(xlabel='mass', ylabel='count');

f = tp.locate(frames[0], 11, invert=False, minmass=300, maxsize=3.0, threshold=3.0)

plt.figure()
tp.annotate(f, frames[0], plot_style={'markersize': 10}, color='red');
plt.savefig('marked.pdf', format='pdf', dpi=3000)
#
#plt.figure()
#tp.subpx_bias(f)
#
#plt.figure()
#tp.subpx_bias(tp.locate(frames[0], 13, invert=False, minmass=200, maxsize=3.0, threshold=3.0));

#f = tp.batch(frames[110:210], 11, invert=False, minmass=160, maxsize=3.0, engine="numba");
#
#t = tp.link_df(f, 5, memory=3)
#
#t1 = tp.filter_stubs(t, 50)
## Compare the number of particles in the unfiltered and filtered data.
#print('Before:', t['particle'].nunique())
#print('After:', t1['particle'].nunique())

#d = tp.compute_drift(t1, skip=1)
#plt.figure()
#d.plot()
#
#plt.figure()
#tp.plot_traj(t1);
#
#data = []
#for item in set(t1.particle):
#    sub = t1[t1.particle==item]
#    dvx = np.diff(sub.x)
#    dvy = np.diff(sub.y)
#    for x, y, dx, dy, frame, mass, size, ecc, signal, raw_mass, ep in \
#        zip(sub.x[:-1], sub.y[:-1], dvx, dvy, sub.frame[:-1], sub.mass[:-1], sub['size'][:-1], sub.ecc[:-1], sub.signal[:-1], sub.raw_mass[:-1], sub.ep[:-1]):
#            data.append({'dx': dx,
#                         'dy': dy,
#                         'x': x,
#                         'y': y,
#                         'frame': frame,
#                         'particle': item,
#                         'size': size,
#                         'ecc': ecc,
#                         'signal': signal,
#                         'mass': mass,
#                         'raw_mass': raw_mass,
#                         'ep': ep
#                        })
#df = pd.DataFrame(data)
    
#i = 250
#d = data[data.frame==i]
#plt.figure()
#plt.imshow(frames[i])
#plt.quiver(d.x, d.y, d.dx, -d.dy, pivot='middle', headwidth=0.1, headlength=0.1, color='yellow')
#plt.axis('off')

#df.to_csv('test.csv')