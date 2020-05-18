#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 07:53:05 2020

@author: blaubaer
"""
from scipy.stats import shapiro
from scipy.stats import stats
import scipy as spy
from scipy.stats import median_test



def mediantest(df):
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number =[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    while True:
        value_column_a= input('a-value: \n(choose number) \n?')
        if value_column_a not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        value_column_b= input('b-value: \n(choose number) \n?')
        if value_column_b not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    a = df[list_columns_werte[int(value_column_a)]]
    b = df[list_columns_werte[int(value_column_b)]]
    
    med1=a.median()
    med2=b.median()
    
    diff = abs(med1-med2)
    
    print('Median Group a: ', med1)
    print('Median Group b: ', med2)
    print('Differences :', diff)
    
    
    
    try:
        
        stat, p, med, tbl = median_test(a, b)
    
    
        print('Median-Test:')
        print ('stat-Value:',stat)
        print ('p-Value:',p)
    
        alpha = 0.05
        if p > alpha:
            print('Medians should not be different (fail to reject H0)')
        else:
            print('Medians should be different (reject H0)')    
    except Exception as exception:
                print('Wrong input (choose point-comma), please try again!')
                
    
    