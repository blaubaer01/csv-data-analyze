#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:06:39 2020

@author: blaubaer
"""

import os



##############################################################################
###Main function tools
##############################################################################
#############################################################################
###main functions
#############################################################################

            
######################################################################        
###check float
def isfloat(x):
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True

#######################################################################
### define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

#######################################################################
####truncate values
def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    
#######################################################################
###test input about integer
def isinteger(x):
    try:
        int(x)
    except ValueError:
        return False
    else:
        return True
    
