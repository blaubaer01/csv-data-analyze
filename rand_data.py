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
###test input about integer
def isinteger(x):
    try:
        int(x)
    except ValueError:
        return False
    else:
        return True
    
    
    
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
    
    
    print('Create sequence number')
    
    while True:
        seq_nr_from = input('Number from:(input integer) ?')
        if not isinteger(seq_nr_from):
            print("'Number from' is not an integer, please try again")
        else:
            break
    
    while True:
        seq_often = input('Count of data: ?')
        if not isinteger(seq_often):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    
    seq_nr_from = int(seq_nr_from)
    seq_often = int(seq_often)
       
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = range(seq_nr_from, seq_often +1 + seq_nr_from)
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      
 

def nd_data(df):
    clear()
    
    print('Create normal distributions data')
    
    while True:
        mean_df = input('Mean (choose point-comma): ?')
    
        if not isfloat(mean_df):
            print("mean is not a number with point-comma, please try again")
        else:
            break
    while True:
        std_df = input('Deviation (choose point-comma)?')
    
        if not isfloat(std_df):
            print("Deviation is not a number with point-comma, please try again")
        else:
            break
    
    while True:
        seq_often = input('Count of data: ?')
        if not isinteger(seq_often):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    mean_df = float(mean_df)
    std_df = float(std_df)
    seq_often = int(seq_often)
    
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = np.random.normal(mean_df, std_df, seq_often)
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)    
    
def bd_data(df):
    clear()
    
    print('Create binomial distributions data')
    
        
    
    
    while True:
        p_df = input('p (0-1) (choose point-comma): ?')
        if not isfloat(p_df):
            print("p is not a number with point-comma, please try again")
        else:
            break
    
    
    while True:
        n_df = input('n : ?')
        if not isinteger(n_df):
            print("'n' is not an integer, please try again")
        else:
            break

    
    
    while True:
        seq_often = input('Count of data: ?')
        if not isinteger(seq_often):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    p_df = float(p_df)
    n_df = int(n_df)
    seq_often = int(seq_often)
    
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = np.random.binomial(n_df, p_df, seq_often)
    
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
    rand_liste = ['sequence number', 'normal distribution data', 'binomial distributions data', 'poisson distribution data', 'logistic distribution data']
    for i in range(len(rand_liste)):
        print(i, rand_liste[i])
        i+=1
    rd = input('Which kind of numbers do you would like to create: \n(choose a number) \n?')
    
    
    if rd == '0' :
        seq_numbers(df)
    elif rd == '1' :
        nd_data(df)
    elif rd == '2' :
        bd_data(df)
    elif rd == '3' :
        print('not available yet!')
    elif rd == '4' :
        print('not available yet')
    
    else:
        print('wrong input!')
        