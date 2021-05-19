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

from datetime import date


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
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Input only Filename ([filename].csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)
    else:
        fn = 'none'
    
    ################################################################################
    ###Log-file
    fname = 'save new file'
    fvalue = 'File Name: ' + fn
    
    
    
    log = fname + '\n' + fvalue + '\n' 
    session_write(log)

        

########################################################################
###save dataframe to CSV-File
def save_CSV(fn, df):
    clear()
    speichern_ja = input('Save the modified dataframe: y/n \n? ')
    if speichern_ja.lower() =='y':
        print('save file ...', fn)
        df.to_csv(fn, sep=';', decimal=',', header =True, index=False)
        
    ################################################################################
    ###Log-file
    fname = 'save file'
    fvalue = 'File Name: ' + fn
    
    
    
    log = fname + '\n' + fvalue + '\n' 
    session_write(log)


    
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
    count_rows = len(df.index)
    print('columns', count_column)
    print('rows: ', count_rows)
    if count_column > 10 or count_rows > 1000:
        print(df)
    else:
        print(tabulate(df, headers='keys', tablefmt='psql'))
        
        
def session_doc_anlegen(fn):
    
    
       
    fn = 'session.txt'
    
    datum = date.today()
    open(fn,'w').close()
    
    file = open(fn, "w", errors='ignore')
    
    
    file.write(str(datum) + '\n')
    
    file.close()

def session_write(log):
    
    fn = 'session.txt'
    
    f = open(fn, "a", errors='ignore')
    
    btw = ('#'*50)
    
    f.write( btw + '\n' + log + "\n" )
    f.close()
    
    
def session_save_by_name(fn):

    fn = 'session.txt'
    
    sessionsaveyes = input('Would you like to save session-file of this session y/n \n?')    
    
    if sessionsaveyes == 'y':
        sessionfilename = input('Input Session-file-name ([filename].txt will save automaticly): \n?')
        
        os.rename(fn, sessionfilename)
        
        
