#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 07:53:05 2020

@author: blaubaer (Ricky Helfgen)
"""
from scipy.stats import shapiro
#from scipy.stats import stats
import scipy as spy
from scipy.stats import median_test
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from outliers import smirnov_grubbs as grubbs
#import statistics as stats
from mft import isfloat, clear


###############################################################################
###Statistical Tests
###############################################################################        


#######################################################################        
###test of normality
def normality_test(df):
    #clear()
    
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
        value_column= input('Which value column do you want to verify: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
        
    y = df[list_columns_werte[int(value_column)]]
    
    
    stat, p = shapiro(y)
    
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
        decision = 'Sample looks Gaussian (fail to reject H0)'
    else:
        print('Sample does not look Gaussian (reject H0)')
        decision = 'Sample does not look Gaussian (reject H0)'
    

    eintrag = 'Shapiro-Wilk - Test:' + '\nStatistics: ' + str(stat) + '\np-Value: ' + str(p) + '\ndecision: ' + decision
    
    plt.figure(figsize=(6,2))
    plt.subplot(211)
    spy.stats.probplot(y, dist="norm", plot=plt)
    
    plt.subplot(212)
    plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.show() 

#######################################################################
###correlation test
def correl(df):
    #clear()
    correlation_df = df.corr()
    print(correlation_df)
    
    
#######################################################################    
###Grubbs outlier test
def outliert(df):
    
    sns.set(color_codes=True)
    
    
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
        value_column= input('Which value column do you want to verify: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = df[list_columns_werte[int(value_column)]]
    print('Value could be outlier:',grubbs.max_test_outliers(y, alpha=0.05))
    
       
    
    eintrag = 'Grubbs-Outlier Test' + '\nValue could be outlier:' + str(grubbs.max_test_outliers(y, alpha=0.05))
    
    plt.figure(figsize=(6,2))
    plt.subplot(211)
    sns.boxplot(x=y)
    plt.subplot(212)
    plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.show()    

#######################################################################
###f-test
def f_test(df):
    clear()
    
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
    
    
    d1 = df[list_columns_werte[int(value_column_a)]]
    
    d2 = df[list_columns_werte[int(value_column_b)]]
    
    
    
    f, p = spy.stats.f_oneway(d1, d2)
    
    
    print('f-Test:')
    
    print('F-Value:' ,f)
    print('p-value:' ,p)
    
    
    
    
    alpha = 0.05
    if p > alpha:
        print('Variances should be equal (fail to reject H0)')
    else:
        print('Variances should not be equal (reject H0)')    

#######################################################################    
###one single t-test
def ttest_o_s(df, alpha=0.05, alternative='greater'):
    clear()
    
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
        value_column= input('Which value column do you want to verify: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        target_value = input('Input taget mean-value \n(choose point-comma \n?')
    
        if not isfloat(target_value):
            print("Target mean value is not a number with point-comma, please try again")
        else:
            break
    
    
    y = df[list_columns_werte[int(value_column)]]
    
    try:
        t, p = spy.stats.ttest_1samp(y, float(target_value))
    
    
        print('One sample t-Test:')
        print ('t-Value:',t)
        print ('p-Value:',p)
    
        alpha = 0.05
        if p > alpha:
            print('Means should not be different (fail to reject H0)')
        else:
            print('Means should be different (reject H0)')    
    except Exception as exception:
                print('Wrong input (choose point-comma), please try again!')
    

#######################################################################    
###two sided t-test
def ttest_t_s(df):
    #clear()
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
    
    
    
    try:
        t, p = spy.stats.ttest_rel(a,b)
    
    
        print('Two sample t-Test:')
        print ('t-Value:',t)
        print ('p-Value:',p)
    
        alpha = 0.05
        if p > alpha:
            print('Means should not be different (fail to reject H0)')
        else:
            print('Means should be different (reject H0)')    
    except Exception as exception:
                print('Wrong input (choose point-comma), please try again!')
                
    
    
#######################################################################                
###indipendent t-test
def ttest_i(df):
    #clear()
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
    
    
    try:
        t, p = spy.stats.ttest_ind(a,b, equal_var = False)
    
    
        print('Two sample t-Test (for the means of two independent samples of scores):')
        print ('t-Value:',t)
        print ('p-Value:',p)
    
        alpha = 0.05
        
        if p > alpha:
            print('Means should not be different (fail to reject H0)')
        else:
            print('Means should be different (reject H0)')    
    except Exception as exception:
                print('Wrong input, please try again!')

    


#######################################################################
###median test
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
                

#######################################################################    
###One way ANOVA    
def anova_o_w (df):
    clear()
    
    kategorie=df.select_dtypes(include=['object', 'int'])
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number=[]
    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        list_number.append(str(i))
        print(i, kategorie.columns[i])
        i+=1
    
    while True:
        groupby_column = input('Group by column: \n(choose number) \n?')
        if groupby_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    
    mod = ols(y + '~' + x,
                data=df).fit()
                
    aov_table = sm.stats.anova_lm(mod, typ=2)
    print('one way ANOVA Result:' )
    print (aov_table)
    
#######################################################################    
###Two way ANOVA    
def anova_t_w(df):
    clear()
    kategorie=df.select_dtypes(exclude=['float'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    
    while True:
        value_column= input('Which value column do you want to compare: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number=[]
    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        list_number.append(str(i))
        print(i, kategorie.columns[i])
        i+=1
    
    
    
    while True:
        faktor1 = input('Factor1: \n(choose number) \n?')
        if faktor1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        faktor2 = input('Factor2: \n(choose number) \n?')
        if faktor2 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    y = list_columns_werte[int(value_column)]
    a = list_columns_kategorie[int(faktor1)]
    b = list_columns_kategorie[int(faktor2)]
    
    mod = ols(y + '~C(' + a + ')*C(' + b +')',
                data=df).fit()

    # Seeing if the overall model is significant
    print(f"Overall mod F({mod.df_model: .0f},{mod.df_resid: .0f}) = {mod.fvalue: .3f}, p = {mod.f_pvalue: .4f}")    
    
    mod.summary()
        
    aov_table = sm.stats.anova_lm(mod, typ=2)
    print('two way ANOVA Result:' )
    print (aov_table)
        