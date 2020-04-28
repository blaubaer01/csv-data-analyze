#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:20:56 2020

@author: blaubaer
"""

import numpy
import pyspc
import pandas as pd
fake_data = numpy.random.randn(30, 5) + 100

print(fake_data)
a = spc(fake_data) + xbar_rbar() + rbar() + rules()
print(a)