# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:16:13 2021

@author: Z173728
"""



import matplotlib.pyplot as plt


from mft import clear
#import pandas as pd
import statistics
import numpy as np
import math

F1 = '\U0001f522 ?'
F2 = '\U0001f521 ?' 


def p_chart(df):
    clear()
    print('p-chart')
    
    werte = df.select_dtypes(include=['int', 'int64'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number = []
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    
    while True:
        value_column= input('Column with count issues: \n(choose number)\n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    while True:
        sgroup_column= input('Column with subgroup size: \n(choose number)\n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
      
    
    y = list_columns_werte[int(value_column)]
    z = list_columns_werte[int(sgroup_column)]
    
    
    # Add 'p' column to data frame
    df['p'] = df[y]/df[z]
    
    
    
    # Plot p-chart
    xquer=df['p'].mean()
    ymax =df['p'].max()
    ylimmax = ymax + ((ymax-xquer) / 6)
    # Plot p-chart
    #plt.figure(figsize=(15,7.5))
    plt.plot(df['p'], linestyle='-', marker='o', color='black')
    
    
    
    #plt.step(x=range(0,len(df['p'])), y=df['p'].mean()+3*(np.sqrt((df['p'].mean()*(1-df['p'].mean()))/df[z])), color='red', linestyle='dashed')
    
    plt.step(x=range(0,len(df['p'])), y=xquer+3*(np.sqrt((xquer*(1-xquer))/df[z])), color='red', linestyle='dashed')    
    plt.step(x=range(0,len(df['p'])), y=xquer-3*(np.sqrt((xquer*(1-xquer))/df[z])), color='red', linestyle='dashed')        
    #plt.step(x=range(0,len(df['p'])), y=df['p'].mean()-3*(np.sqrt((df['p'].mean()*(1-df['p'].mean()))/df[z])), color='red', linestyle='dashed')
    
    
    
    plt.axhline(xquer,linewidth=2, color='green')
    #plt.axhline(statistics.mean(df['p']), color='blue')
    plt.ylim(bottom=0, top=ylimmax)
    plt.title('p Chart')
    plt.xlabel('Group')
    plt.ylabel('Fraction Defective')
    plt.show()
    