#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:21:09 2018

@author: ricktjwong
"""

from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage import exposure
import numpy as np

import pandas as pd

import pims
import trackpy as tp
import os

import matplotlib.pyplot as plt

datapath = 'test'
prefix = 'frame'

id_example = 0
rawframes = pims.ImageSequence(os.path.join(datapath, prefix + '*.jpg'), process_func=None)
plt.imshow(rawframes[id_example])

img_example = rawframes[id_example]

features = pd.DataFrame()
for num, img in enumerate(rawframes):
#    image = skimage.io.imread(img, True)
    image_gray = rgb2gray(img)
    
    blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.08)
    
    # Compute radii in the 3rd column.
    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
    for blob in blobs_log:
        # Store features which survived to the criterions
        features = features.append([{'y': blob[0],
                                     'x': blob[1],
                                     'frame': num,
                                     },])

tp.annotate(features[features.frame==id_example], img_example, plot_style={'markersize': 1})

search_range = 11
t = tp.link_df(features, search_range, memory=1)
plt.imshow(img)
tp.plot_traj(t)

unstacked = t.set_index(['frame', 'particle']).unstack()

data = pd.DataFrame()
for item in set(t.particle):
    sub = t[t.particle==item]
    dvx = np.diff(sub.x)
    dvy = np.diff(sub.y)
    for x, y, dx, dy, frame in zip(sub.x[:-1], sub.y[:-1], dvx, dvy, sub.frame[:-1],):
        data = data.append([{'dx': dx,
                             'dy': dy,
                             'x': x,
                             'y': y,
                             'frame': frame,
                             'particle': item,
                            }])
    
i = 0
d = data[data.frame==i]
plt.imshow(rawframes[i])
plt.quiver(d.x, d.y, d.dx, -d.dy, pivot='middle', headwidth=0.5, headlength=0.1, color='yellow')
plt.axis('off')
##fig.savefig('image_edited.pdf', format='pdf', dpi=3000)