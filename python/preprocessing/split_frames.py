#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:18:48 2018

@author: ricktjwong
"""

import cv2

vidcap = cv2.VideoCapture('../test_video/test-vid.MOV')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  cv2.imwrite("../test_images/frame%d.png" % count, image)     # save frame as JPEG file
  count += 1