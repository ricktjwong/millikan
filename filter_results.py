#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 03:24:27 2018

@author: ricktjwong
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame.from_csv("csv_good/merged.csv")

condition = df['n'] > 0.8
filtered = df[condition]
filtered['v_g2'] = abs(filtered['v_g'])**0.5

plot = filtered.plot.scatter(x='v_g2', y='q')
plot.set_ylim([0, 10E-19])