#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:06:39 2020

@author: blaubaer
"""

import os
import pandas as pd
import numpy as np
from tabulate import tabulate

F1 = '\U0001f522 ?'
F2 = '\U0001f521 ?' 

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
    
########################################################################
###save dataframe to CSV-File
def save_CSV_new(df):
    clear()
    speichern_ja = input('Save the modified dataframe: y/n \n' + F2)
    if speichern_ja.lower() =='y':
        csvfilename = input('Input only Filename ([filename].csv will save automaticly) \n' + F2)
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)
        

########################################################################
###save dataframe to CSV-File
def save_CSV(fn, df):
    clear()
    speichern_ja = input('Save the modified dataframe: y/n \n? ')
    if speichern_ja.lower() =='y':
        print('save file ...', fn)
        df.to_csv(fn, sep=';', decimal=',', header =True, index=False)
        
        
#########################################################################
###calc cumsum
#def moving_average(a, n=3) :
#    ret = np.cumsum(a, dtype=float)
#    ret[n:] = ret[n:] - ret[:-n]
#    return ret[n - 1:] / n

def moving_average(x, w=8):
    return np.convolve(x, np.ones(w), 'valid') / w



def print_table(df):
    
    count_column = len(df.columns)
    print('columns', count_column)
    if count_column > 13:
        print(df)
    else:
        print(tabulate(df, headers='keys', tablefmt='psql'))
        