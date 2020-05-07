#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:41:21 2020

@author: blaubaer(Ricky Helfgen)
"""

import pandas as pd
import seaborn as sns
from scipy.stats import shapiro
import matplotlib.pyplot as plt
import scipy as spy

def isfloat(x):
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True
    
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

###MSA-V1

def msa_v1(df):
    
    df['nr'] = range(1, len(df) + 1)
    
    nr = df['nr']
    ###get datas
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number) \n?')
    
    y = df[list_columns_werte[int(value_column)]]
    
    ###get target value
    while True:
            tv = input('reference target value: \n(choose point-comma) \n?')
    
            if not isfloat(tv):
                print("target mean value is not a number with point-comma, please try again")
            else:
                break
        
        
    tv = float(tv)
    offset = abs(y.mean()-tv)
    mean_y = y.mean()
    std_y = y.std()
    toff = truncate(offset, 6)
    ####test auf normalv + t-test
    ####berechnung Offset
    ####toleranz eins/zweis, berechnung Cg,Cgk
    ###daten anzeigen in diagramm
    ###tolerance
    
    ###toleranzen
    one_two_sided = input('Tolerance: \n0: no tolerance \n1: both side tolerance \n2: one side ut \n3: one side lt \n(choose number) \n?')
    
    notol = '0'
    ###both side tolerance
    if one_two_sided == '1':
        
        while True:
            tol = input('upper tolerance , lower tolerance \n(choose point-comma / seperate with float-comma, example:2.2 , 1.9) \n?')
            if ',' in tol:
                try:
                    ut, lt = tol.split(',')
                    ut = float(ut)
                    lt = float(lt)
                    if lt > ut:
                        print('ut<lt, wrong input!')
                    else:                    
                        break
                except Exception as exception:
                    print('Wrong input, try again!')
            else:
                print('wrong input, separator is missing!, please try again!')
        
        print(ut,lt)
        
        Cg = (0.2 * (ut-lt))/(6*std_y)
        Cgk = ((0.1* (ut-lt)-offset))/(3*std_y)	
        print ('Cg, Cgk:', Cg, Cgk)
        utdiagram = tv + ((ut-lt)*0.1)
        ltdiagram = tv - ((ut-lt)*0.1)
        tCg = truncate(Cg,2)
        tCgk = truncate(Cgk, 2)
        tutd = truncate(utdiagram, 3)
        tltd = truncate(ltdiagram, 3)
        
    ###one side tolerance ut
    elif one_two_sided =='2':
        
        
        while True:
            ut = input('Upper tolerance: \n(choose point-comma) \n?')
            ut = float(ut)
            if not isfloat(ut):
                print("target mean value is not a number with point-comma, please try again")
            else:
                lt = 'none'
                break
        tCg ='none'
        Cgk = Cgk = ((0.1* (ut-(mean_y-(3*std_y)))-offset))/(3*std_y)
        tCgk = truncate(Cgk, 2)
        utdiagram = tv + ((ut-(mean_y-(3*std_y)))*0.1)
        ltdiagram = tv - ((ut-(mean_y-(3*std_y)))*0.1)
        tutd = truncate(utdiagram, 3)
        tltd = truncate(ltdiagram, 3)
        
    
    ###one side tolerance lt
    elif one_two_sided =='3':
        
        while True:
            lt = input('Lower tolerance: \n(choose point-comma) \n?')
            lt = float(lt)
            if not isfloat(lt):
                print("target mean value is not a number with point-comma, please try again")
            else:
                ut = 'none'
                break
        tCg ='none'
        Cgk = ((0.1* ((mean_y + (3*std_y))-lt)-offset))/(3*std_y)
        tCgk = truncate(Cgk, 2)
        utdiagram = tv + (((mean_y + (3*std_y))-lt)*0.1)
        ltdiagram = tv - (((mean_y + (3*std_y))-lt)*0.1)
        tutd = truncate(utdiagram, 3)
        tltd = truncate(ltdiagram, 3)
                
                
    else:
        notol = '1'
        tCg = 'none'
        tCgk = 'none'
        utdiagram = tv
        ltdiagram = tv
        tutd = 'none'
        tltd = 'none'
    
    
    
    
    
    ###normality test
    stat, p = shapiro(y)
    
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')  
    
    ###offset target-mean(y)
    
    
    
    
    
    print('There is an Offset of: ', offset)
    
    
    ###one sample t-test
    if p >0.5:
        
        t, p = spy.stats.ttest_1samp(y, float(tv))
    
    
        print('One sample t-Test:')
        print ('t-Value:',t)
        
        print ('p-Value:',p)
        tp = truncate(t, 5)
        tt = truncate(p, 5)
    
    
        alpha = 0.05
        if p > alpha:
            print('Means should not be different (fail to reject H0)')
            mess = 'Means should not be different (fail to reject H0)'
            
        else:
            print('Means should be different (reject H0)')
            mess = 'Means should be different (reject H0)'
    else:
        print('no t-test possible, data looks not Gaussian')
        mess = 'no t-test possible, data looks not Gaussian'
        t='none'
        p='none'
    
    
    
    eintrag = 'MSA_V1' + '\nOffset: ' + str(toff) + '\nCg: ' + str(tCg) + ' Cgk: ' + str(tCgk) + '\none single t-Test: ' + mess + ' t: ' + str(tt) + ' p: ' + str(tp) + '\ntol(10%): ' + 'UT: ' + str(tutd) + ' LT: ' + str(tltd)
    
    
    
    
    
    #eintrag = 'Grubbs-Outlier Test' + '\nValue could be outlier:' + str(grubbs.max_test_outliers(y, alpha=0.05))
    
    plt.figure(figsize=(6,2))
    plt.subplot(211)
    sns.lineplot(x=nr, y=y, estimator=None, lw=1, data=df)
    plt.axhline(y=mean_y,linewidth=2, color='g')
    plt.axhline(y=utdiagram,linewidth=2, color='orange')
    plt.axhline(y=ltdiagram,linewidth=2, color='orange')
    plt.axhline(y=tv,linewidth=2, color='violet')
    
    plt.subplot(212)
    plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.show() 
    
    
