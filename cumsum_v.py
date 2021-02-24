#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 06:56:09 2021

@author: blaubaer
"""

import numpy as np


def moving_average(x, w=8):
    return np.convolve(x, np.ones(w), 'valid') / w


a = np.arange(20)
#a = input('a=')
print(a)
b = moving_average(a)
print(b)
