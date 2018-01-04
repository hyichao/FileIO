#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Read Image by OpenCV
Personal used for daily Deep Learning
Yichao Huang
2017.11
'''

import os
import cv2
import numpy
from multiprocessing import Pool

def read_image(path, exp_height=None, exp_width=None, exp_ratio=None):
    ''' read image into numpy, check if in valid range '''
    if not os.path.exists(path):
        print '[image_io]', 'Image not found. '+path
        return None
    src = cv2.imread(path)
    if src is None:
        print '[image_io]', 'Empty Image.'
        return None
    is_color = True if len(src.shape) == 3 else False
    if is_color:
        height, width, channel = src.shape
    else:
        height, width = src.shape
        channel = 1
    
    # check height
    if exp_height is not None:
        if height<exp_height[0]:
            print '[image_io]', 'Image height too small'
            return None
        if height>exp_height[1]:
            print '[image_io]', 'Image height too large'
            return None   
    # check width
    if exp_width is not None:
        if height<exp_width[0]:
            print '[image_io]', 'Image width too small'
            return None
        if height>exp_width[1]:
            print '[image_io]', 'Image width too large'
            return None   
    # check ratio               
    if exp_ratio is not None:
        if 1.0*height/width<exp_ratio[0]:
            print '[image_io]', 'Image ratio too small'
            return None
        if 1.0*height/width>exp_ratio[1]:
            print '[image_io]', 'Image ratio too large'
            return None  
 
    return src

def get_image_size(path):
    src = read_image(path)
    if src is None:
        return None
    return src.shape

def do_statistic(paths):
    pool = Pool()
    sizes = pool.map(get_image_size, paths)
    pool.close()
    pool.join()
    sizes = [size for size in sizes if size is not None]
    
    avg_height = avg_width = 0
    for height,width in sizes:
        avg_height += height
        avg_width += width
    avg_height /= len(sizes)
    avg_width /= len(sizes)
    print '[image_io]', avg_height, avg_width