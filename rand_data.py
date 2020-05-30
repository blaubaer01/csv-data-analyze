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

##############################################################################
###create sequence Nr

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
 
###############################################################################
###create normal distributions data
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


###############################################################################
###create binomial data

    
def bd_data(df):
    clear()
    
    print('Create binomial distributions data')
    
        
    
    
    while True:
        p_df = input('p (0-1) (choose point-comma): ?')
        if not isfloat(p_df):
            print("p is not a number with point-comma, please try again")
        elif float(p_df) > 1:
            print('p should by between 0 and 1')
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


###############################################################################
###create poisson data
def pd_data(df):
    clear()
    
    print('Create poisson distributions data')
    
        
    
    
    while True:
        p_df = input('µ (choose point-comma): ?')
        if not isfloat(p_df):
            print("µ is not a number with point-comma, please try again")
        else:
            
            break
    
     
    
    
    while True:
        seq_often = input('Count of data: ?')
        if not isinteger(seq_often):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    p_df = float(p_df)
    
    seq_often = int(seq_often)
    
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = np.random.poisson(p_df, seq_often)
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)    
        
##############################################################################
###create logistic data
def ld_data(df):
    clear()
    
    print('Create logistic distributions data')
    
    while True:
        location_df = input('location (choose point-comma): ?')
    
        if not isfloat(location_df):
            print("location is not a number with point-comma, please try again")
        else:
            break
    while True:
        scale_df = input('scale (choose point-comma)?')
    
        if not isfloat(scale_df):
            print("scale is not a number with point-comma, please try again")
        else:
            break
    
    while True:
        seq_often = input('Count of data: ?')
        if not isinteger(seq_often):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    location_df = float(location_df)
    scale_df = float(scale_df)
    seq_often = int(seq_often)
    
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = np.random.logistic(location_df, scale_df, seq_often)
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)    

##############################################################################
###create shisquare data
def shisq_data(df):
    clear()
    
    print('Create chi square distributions data')
    
    while True:
        defr = input('df: ?')
        if not isinteger(defr):
            print("'df is not an integer, please try again")
        else:
            break
    
    
    while True:
        m_df = input('µ (choose point-comma): ?')
    
        if not isinteger(m_df):
            print("µ is not a number with point-comma, please try again")
        else:
            break
    
    while True:
        k_df = input('k (choose point-comma)?')
    
        if not isinteger(k_df):
            print("k is not an integer, please try again")
        else:
            break
    
    while True:
        n_df = input('Count of data: ?')
        if not isinteger(n_df):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    m_df = int(m_df)
    k_df = int(k_df)
    n_df = int(n_df)
    defr = int(defr)
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = np.random.chisquare(defr, size=(m_df*n_df*k_df))
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)    

###############################################################################
###create pareto distribution data

def pareto_data(df):
    clear()
    
    print('Create pareto distributions data')
    
    while True:
        a_df = input('a: ?')
        if not isinteger(a_df):
            print("'a' is not an integer, please try again")
        else:
            break
    
    
    while True:
        m_df = input('m (choose point-comma): ?')
    
        if not isinteger(m_df):
            print("m is not a number with point-comma, please try again")
        else:
            break
    
    while True:
        k_df = input('k (choose point-comma)?')
    
        if not isinteger(k_df):
            print("k is not an integer, please try again")
        else:
            break
    
    while True:
        n_df = input('Count of data: ?')
        if not isinteger(n_df):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    m_df = int(m_df)
    k_df = int(k_df)
    n_df = int(n_df)
    a_df = int(a_df)
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = np.random.pareto(a_df, size=(m_df*n_df*k_df))+m_df
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)    

###############################################################################
###create exponential distribution data

def exp_data(df):
    clear()
    
    print('Create exponential distributions data')
    
    while True:
        scale_df = input('scale: ?')
        if not isinteger(scale_df):
            print("'a' is not an integer, please try again")
        else:
            break
    
    
    while True:
        m_df = input('m (choose point-comma): ?')
    
        if not isinteger(m_df):
            print("m is not a number with point-comma, please try again")
        else:
            break
    
    while True:
        k_df = input('k (choose point-comma)?')
    
        if not isinteger(k_df):
            print("k is not an integer, please try again")
        else:
            break
    
    while True:
        n_df = input('Count of data: ?')
        if not isinteger(n_df):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    m_df = int(m_df)
    k_df = int(k_df)
    n_df = int(n_df)
    scale_df = int(scale_df)
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = np.random.exponential(scale_df, size=(m_df*n_df*k_df))
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)    

###############################################################################
###create uniform distribution data
def unif_data(df):
    clear()
    
    print('Create uniform distributions data')
    
    while True:
        high_df = input('high level (choose point-comma): ?')
    
        if not isfloat(high_df):
            print("high level is not a number with point-comma, please try again")
        else:
            break
    while True:
        low_df = input('low level (choose point-comma)?')
    
        if not isfloat(low_df):
            print("low level is not a number with point-comma, please try again")
        else:
            break
    
    while True:
        seq_often = input('Count of data: ?')
        if not isinteger(seq_often):
            print("'Count of data' is not an integer, please try again")
        else:
            break
    
    high_df = float(high_df)
    low_df = float(low_df)
    seq_often = int(seq_often)
    
    
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = np.random.uniform(high_df, low_df, seq_often)
    
    print(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)    
##############################################################################
###main menu create random data
def menu_rd(df):
    clear()
    
    
    print('Create random data with "numpy" and "pandas"')
    rand_liste = ['sequence number', 'normal distribution data', 'binomial distributions data', 'poisson distribution data', 'logistic distribution data', 'chi square distribution', 'pareto distribution', 'exponetial distribution', 'uniform distribution']
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
        pd_data(df)
    elif rd == '4' :
        ld_data(df)
    elif rd == '5' :
        shisq_data(df)
    elif rd == '6' :    
        pareto_data(df)
    elif rd == '7' :
        exp_data(df)
    elif rd == '8' :
        unif_data(df)
    else:
        print('wrong input, not available yet!')
        