#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:20:56 2020

@author: blaubaer
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns ; sns.set()
from scipy.stats import shapiro
import os




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
    

### define our clear function 
#############################################################################
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 






def x_bar():
    auswahl_datei = 'production.csv'
    sns.set(style="darkgrid")
    
    
    trennzeichen =';'
    dezimalzeichen =','
    kopfz = 0
    
    df=pd.read_csv(auswahl_datei, sep=trennzeichen , decimal=dezimalzeichen, header=kopfz)
    #print(df)
    
    #df2 = df.groupby('Stichprobe').agg({'Istwert':['mean', 'std'].reset_index()})
    #print(df2)
    df2 = pd.DataFrame()
    
    #df2['mean_istwert'] = df.groupby('Stichprobe')['Istwert'].describe()
    df2 = df.groupby('Stichprobe')['Istwert'].describe()
    
    fn = 'describe.csv'
    df2.to_csv(fn, sep=';', decimal=',', header =True)
    auswahl_datei = 'describe.csv'
    df2=pd.read_csv(auswahl_datei, sep=trennzeichen , decimal=dezimalzeichen, header=kopfz)
    #df2=df.groupby(['Stichprobe'])[['mean']].mean().reset_index()
    print (df2)
    
    #df2['Stichprobe'] = df2['Stichprobe'].astype(str)
    
    print(df2)
    
    print(df2.dtypes)
    
    x = 'Stichprobe'
    y = 'mean'
    s = 'std'
    
    mean_mean = df2['mean'].mean()
    mean_std = df2['std'].mean()
    
    df2.plot(x, y)
    plt.axhline(y=mean_mean,linewidth=2, color='g')
    
    df2.plot(x, s)
    
    
    plt.show()



def x_chart(df):
    
    df['nummer'] = range(1, len(df) + 1)
    
    
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
    
    print(list_columns_werte[int(value_column)])    
    y = list_columns_werte[int(value_column)]
    
    x = 'nummer'
    
    yt = df[list_columns_werte[int(value_column)]]
    
    mean_y = yt.mean()
    std_y = yt.std()
    plus3s = mean_y + 3*std_y
    minus3s = mean_y -3*std_y
    median = yt.quantile(0.5)
    upper_q_y = yt.quantile(0.99869)
    lower_q_y = yt.quantile(0.00135)
    
    ###toleranzen
    one_two_sided = input('Tolerance: \n1: both side tolerance \n2: one side ut \n3: one side lt \n(choose number) \n?')
    
    
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
            
                
                
    
    
    
    
    
    
    stat, p = shapiro(df[y])
    
    if p < 0.5:
        mittelwert = median
        ut3s = upper_q_y
        lt3s = lower_q_y
    else:
        mittelwert = mean_y
        ut3s = plus3s
        lt3s = minus3s
    
    
    
    if lt =='none':
          
        df.plot(x, y)
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        plt.axhline(y=ut,linewidth=2, color='red')
        
        
        plt.show()
        
    elif ut=='none':
        
        df.plot(x, y)
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        plt.axhline(y=lt,linewidth=2, color='red')
        plt.show()
    
    else:
    
        df.plot(x, y)
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        plt.axhline(y=ut,linewidth=2, color='red')
        plt.axhline(y=lt,linewidth=2, color='red')
        
        plt.show()
        
    