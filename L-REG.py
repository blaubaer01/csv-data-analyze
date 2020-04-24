#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:34:04 2020

@author: blaubaer (Ricky Helfgen)
"""


""" ----- Lineare Regressionsanalyse ------- """
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

from sklearn import linear_model, metrics


def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier


def LREG(df):
    
    sns.set(color_codes=True)        
        
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column_y= input('y-value: \n(choose number) \n?')
    value_column_x= input('x-value: \n(choose number) \n?')
    
    y = df[list_columns_werte[int(value_column_y)]]
    
    x = df[list_columns_werte[int(value_column_x)]]
    
    yg = list_columns_werte[int(value_column_y)]
    
    xg = list_columns_werte[int(value_column_x)]
    
    x = x.reshape(-1, 1)
    
    #Einfache lineare Regressionreg
    model =linear_model.LinearRegression()
    model.fit(x,y)
    #coef = regr.coef_[0]
    
    #y = 8,96 + 7,37 * x
    
    y_value = model.intercept_
    steigung = model.coef_
    rq = model.score(x,y)
    
    print(y_value, steigung, rq)
    
    
    #sns.regplot(x=x, y=y, lowess=True, color="g");
    
    eintrag = 'rquadrat: ' + str(rq)
    
    
    
    
    
    plt.figure(figsize=(6, 4))
    plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
    sns.regplot(x=xg, y=yg, data=df);
    plt.subplot(222)
    sns.residplot(x=xg, y=yg, data=df, lowess=True, color="g"); 
    plt.subplot(223)
    plt.text(0.1,0.5,eintrag, ha='left', va='center',fontsize=12)
    plt.subplot(224)
    plt.text(0.1,0.5,eintrag, ha='left', va='center',fontsize=12)
    plt.axis('off')
    plt.show()
    
    
    
    #sns.residplot(x=x, y=y, data=df); 
    #plt.show()
    
    
    
    









plt.show()