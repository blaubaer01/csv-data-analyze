#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:34:04 2020

@author: blaubaer (Ricky Helfgen)
"""


""" ----- Lineare Regressionsanalyse ------- """
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro
import statsmodels.api as sm


def LREG(df):
    
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
        value_column_y= input('y-value: \n(choose number) \n?')
        if value_column_y not in list_number:
            print('wrong input, try again!')
        else:
            break  
    while True:
        value_column_x= input('x-value: \n(choose number) \n?')
        if value_column_x not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    y = df[list_columns_werte[int(value_column_y)]]
    
    x = df[list_columns_werte[int(value_column_x)]]
    
    yg = list_columns_werte[int(value_column_y)]
    
    xg = list_columns_werte[int(value_column_x)]
    
    x = sm.add_constant(x)

    
    model = sm.OLS(y, x)
    
    
    
    results = model.fit()

    print(results.summary())    
    
    print('coefficient of determination:', results.rsquared)
    print('adjusted coefficient of determination:', results.rsquared_adj)
    print('regression coefficients:', results.params)
    
    ols_resid = sm.OLS(y, x).fit().resid
    
    stat, p = shapiro(ols_resid)
    
    
    
    text_lreg = 'rsquared: ' + str(results.rsquared) + '\nregression coefficients: ' + str(results.params) 
    text_lres = 'Test of normality residuals' + '\np-Value: ' + str(p)
    
    
    
    plt.figure(figsize=(6, 4))
    plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
    sns.regplot(x=xg, y=yg, data=df);
    plt.subplot(222)
    sns.residplot(x=xg, y=yg, data=df, lowess=True, color="g"); 
    plt.subplot(223)
    plt.text(0.1,0.5,text_lreg, ha='left', va='center',fontsize=12)
    plt.axis('off')
    plt.subplot(224)
    plt.text(0.1,0.5,text_lres, ha='left', va='center',fontsize=12)
    plt.axis('off')
    
    plt.show()
