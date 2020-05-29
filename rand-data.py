#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:51:59 2020

@author: blaubaer (Ricky Helfgen)
"""

import pandas as pd
import numpy as np
import os


df = pd.DataFrame()
####create random data

#######################################################################
###test input about float
def isfloat(x):
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True
#######################################################################
###set decimals
def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    
#######################################################################
### define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 



def seq_numbers(df):
    
    
    seq_nr_from = input('Number from: ?')
    seq_often = input('Count of data: ?')
    seq_int = input('Sequence interval: ?')
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = range(seq_nr_from, seq_often + seq_int)
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      
 




def menu_rd(df):
    clear()
    
    
    print('Create random data with "numpy" and "pandas"')
    rand_liste = ['sequence number']
    for i in range(len(rand_liste)):
        print(i, rand_liste[i])
        i+=1
    rd = input('Which kind of numbers do you would like to create: \n(choose a number) \n?')
    
    
    if rd == '0' :
        