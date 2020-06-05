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
import numpy as np

#Thanks to: Michal Nowikowski <godfryd@gmail.com>
###got exsamples from https://github.com/mattharrison/python-spc


###statistic variables
#########################################################################################
# n         2      3      4      5      6      7      8      9      10
A2 = [0,0, 1.880, 1.023, 0.729, 0.577, 0.483, 0.419, 0.373, 0.337, 0.308]
D3 = [0,0, 0,     0,     0,     0,     0,     0.076, 0.136, 0.184, 0.223]
D4 = [0,0, 3.267, 2.575, 2.282, 2.115, 2.004, 1.924, 1.864, 1.816, 1.777]
# n   0 1      2      3      4      5      6      7      8      9     10     11     12     13     14     15       20     25
c4 = [0,0,0.7979,0.8862,0.9213,0.9400,0.9515,0.9594,0.9650,0.9693,0.9727,0.9754,0.9776,0.9794,0.9810,0.9823]#,0.9869,0.9896]
B3 = [0,0,     0,     0,     0,     0, 0.030, 0.118, 0.185, 0.239, 0.284, 0.321, 0.354, 0.382, 0.406, 0.428]#, 0.510, 0.565]
B4 = [0,0, 3.267, 2.568, 2.266, 2.089, 1.970, 1.882, 1.815, 1.761, 1.716, 1.679, 1.646, 1.618, 1.594, 1.572]#, 1.490, 1.435]
B5 = [0,0,     0,     0,     0,     0, 0.029, 0.113, 0.179, 0.232, 0.276, 0.313, 0.346, 0.374, 0.399, 0.421]#, 0.504, 0.559]
B6 = [0,0, 2.606, 2.276, 2.088, 1.964, 1.874, 1.806, 1.751, 1.707, 1.669, 1.637, 1.610, 1.585, 1.563, 1.544]#, 1.470, 1.420]
A3 = [0,0, 2.659, 1.954, 1.628, 1.427, 1.287, 1.182, 1.099, 1.032, 0.975, 0.927, 0.886, 0.850, 0.817, 0.789]#, 0.680, 0.606]
#########################################################################################



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




###X-bar-s-Chart
###############################################################################
def x_bar_s(df):
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    
    print(list_columns_werte[int(value_column)])    
    y = list_columns_werte[int(value_column)]

    datenanz = df[list_columns_werte[int(value_column)]].count()
    
    
    teilbar_durch = []
    tb = []
    i=2
    
    for i in range(2, 11):
        teilbar = datenanz %i
        
        if teilbar == 0:
            teilbar_durch.append(i)
            tb.append(str(i))
        i +=1
        
    
    print('Possible Samplesizes are:', teilbar_durch)
    
    
    while True:
        n = input('Which Sample-Size: \n(2-10)\n?')
        if n not in tb:
            print('wrong input, try again!')
        else:
            break  
        
    
    
    
    n=int(n)
    
    fact = datenanz/n
    fact = int(fact)
    
    df['sample'] = pd.Series(range(1, fact +1)).repeat(n).tolist()
    
    
    
    
    df2 = pd.DataFrame()
    
    #df2['mean_istwert'] = df.groupby('Stichprobe')['Istwert'].describe()
    df2 = df.groupby('sample')[y].describe()
    print(df2)
    
    fn = 'describe.csv'
    df2.to_csv(fn, sep=';', decimal=',')
    
    df3 = pd.read_csv(fn, sep=';' , decimal=',', header=0)

    
    target_yes = input('Would you like target center y/n \n?')
    
    if target_yes == 'y':
        while True:
            center = input('Input center value: \n?')
            if not isfloat(center):
                    print("target mean value is not a number with point-comma, please try again")
            else:
                break
        
        
        x = 'sample'
        y = 'mean'
        s = 'std'
        center=float(center)
        
        Xbar = df3['mean'].mean()
        sbar = df3['std'].mean()
        
        xlcl = float(center) - A3[n]*sbar
        xucl = float(center) + A3[n]*sbar
        
        slcl = B3[n]*sbar
        sucl = B4[n]*sbar
        
        print('s-bar :', sbar)
        print('X-bar :',  Xbar)
        
        
        tXbar = truncate(Xbar, 5)
        tsbar = truncate(sbar, 5)
        txlcl = truncate(xlcl,5)
        txucl = truncate(xucl, 5)
        tslcl = truncate(slcl,5)
        tsucl = truncate(sucl, 5)
        tcenter = truncate(center, 5)
        
        
        
        
        eintrag_x = 'Xbar/s Chart' + '\nXbar: ' + str(tXbar) + '\nucl: ' + str(txucl) + '\nlcl: ' + str(txlcl) + '\ncenter: ' + str(tcenter)
        eintrag_s = 'sbar: ' + str(tsbar) + '\nucl: ' +str(tsucl) + '\nlcl: ' + str(tslcl)
        
        
        plt.figure(figsize=(6, 4))
        
        #df3.plot(x, y, ax=axes[0])
        plt.subplot(221)
        sns.lineplot(x=x, y=y, estimator=None, lw=1, data=df3)
        plt.axhline(y=Xbar,linewidth=2, color='g')
        plt.axhline(y=xlcl,linewidth=2, color='orange')
        plt.axhline(y=xucl,linewidth=2, color='orange')
        plt.axhline(y=center,linewidth=2, color='violet')
        
        
        #df3.plot(x, s, ax = axes[1])
        plt.subplot(222)
        sns.lineplot(x=x, y=s, estimator=None, lw=1, data=df3)
        plt.axhline(y=sbar, linewidth=2, color='g')
        plt.axhline(y=slcl,linewidth=2, color='orange')
        plt.axhline(y=sucl,linewidth=2, color='orange')
        
        plt.subplot(223)
        plt.text(0.1,0.5,eintrag_x, 
                         ha='left', va='center',
                         fontsize=12)
        plt.axis('off')
        plt.subplot(224)
        plt.text(0.1,0.5,eintrag_s, 
                         ha='left', va='center',
                         fontsize=12)
        plt.axis('off')
        
        plt.show()

    ####Chart without target center    
    else:
    
        x = 'sample'
        y = 'mean'
        s = 'std'
        
        Xbar = df3['mean'].mean()
        sbar = df3['std'].mean()
        
        xlcl = Xbar - A3[n]*sbar
        xucl = Xbar + A3[n]*sbar
        
        slcl = B3[n]*sbar
        sucl = B4[n]*sbar
        
        print('s-bar :', sbar)
        print('X-bar :',  Xbar)
        
        
        tXbar = truncate(Xbar, 5)
        tsbar = truncate(sbar, 5)
        txlcl = truncate(xlcl,5)
        txucl = truncate(xucl, 5)
        tslcl = truncate(slcl,5)
        tsucl = truncate(sucl, 5)
        
        
        
        
        
        eintrag_x = 'Xbar/s Chart' + '\nXbar: ' + str(tXbar) + '\nucl: ' + str(txucl) + '\nlcl: ' + str(txlcl)
        eintrag_s = 'sbar: ' + str(tsbar) + '\nucl: ' +str(tsucl) + '\nlcl: ' + str(tslcl)
        
        
        plt.figure(figsize=(6, 4))
        
        #df3.plot(x, y, ax=axes[0])
        plt.subplot(221)
        sns.lineplot(x=x, y=y, estimator=None, lw=1, data=df3)
        plt.axhline(y=Xbar,linewidth=2, color='g')
        plt.axhline(y=xlcl,linewidth=2, color='orange')
        plt.axhline(y=xucl,linewidth=2, color='orange')
        
        #df3.plot(x, s, ax = axes[1])
        plt.subplot(222)
        sns.lineplot(x=x, y=s, estimator=None, lw=1, data=df3)
        plt.axhline(y=sbar, linewidth=2, color='g')
        plt.axhline(y=slcl,linewidth=2, color='orange')
        plt.axhline(y=sucl,linewidth=2, color='orange')
        
        plt.subplot(223)
        plt.text(0.1,0.5,eintrag_x, 
                         ha='left', va='center',
                         fontsize=12)
        plt.axis('off')
        plt.subplot(224)
        plt.text(0.1,0.5,eintrag_s, 
                         ha='left', va='center',
                         fontsize=12)
        plt.axis('off')
        
        plt.show()
    
###x-chart
################################################################################
def x_chart(df):
    
    df['nummer'] = range(1, len(df) + 1)
    
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
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
            
                
                
    else:
        notol = '1'
    
    
    
    
    
    stat, p = shapiro(df[y])
    
    if p < 0.5:
        mittelwert = median
        ut3s = upper_q_y
        lt3s = lower_q_y
    else:
        mittelwert = mean_y
        ut3s = plus3s
        lt3s = minus3s
    
    
    if notol =='1':
        df.plot(x, y)
        plt.axhline(y=mittelwert,linewidth=2, color='g')
        
        plt.axhline(y=ut3s,linewidth=1, color='orange')
        plt.axhline(y=lt3s,linewidth=1, color='orange')
        
        plt.show()
        
    else:
        
    
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
            

def x_bar_r(df):
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    print(list_columns_werte[int(value_column)])    
    y = list_columns_werte[int(value_column)]

    datenanz = df[list_columns_werte[int(value_column)]].count()
    
    
    teilbar_durch = []
    tb = []
    i=2
    
    for i in range(2, 11):
        teilbar = datenanz %i
        
        if teilbar == 0:
            teilbar_durch.append(i)
            tb.append(str(i))
        i +=1
        
    
    print('Possible Samplesizes are:', teilbar_durch)
    
    
    while True:
        n = input('Which Sample-Size: \n(2-10)\n?')
        if n not in tb:
            print('wrong input, try again!')
        else:
            break  
    
    n=int(n)
    
    fact = datenanz/n
    fact = int(fact)
    
    df['sample'] = pd.Series(range(1, fact +1)).repeat(n).tolist()
    
    
    
    
    df2 = pd.DataFrame()
    
    #df2['mean_istwert'] = df.groupby('Stichprobe')['Istwert'].describe()
    df2 = df.groupby('sample')[y].describe()
    print(df2)
    
    fn = 'describe.csv'
    df2.to_csv(fn, sep=';', decimal=',')
    
    df3 = pd.read_csv(fn, sep=';' , decimal=',', header=0)

    
    target_yes = input('Would you like target center y/n \n?')
    
    if target_yes == 'y':
        while True:
            center = input('Input center value: \n?')
            if not isfloat(center):
                    print("target mean value is not a number with point-comma, please try again")
            else:
                break
        
        
        x = 'sample'
        y = 'mean'
        s = 'std'
        center=float(center)
        
        
        df3['R'] = df3['max']-df3['min']
        
        Rbar = df3['R'].mean()
        r = 'R'
        
        Xbar = df3['mean'].mean()
        
        xlcl = center - A2[n]*Rbar
        xucl = center + A2[n]*Rbar
        
        rlcl = D3[n]*Rbar
        rucl = D4[n]*Rbar
        
        
        print('r-bar :', Rbar)
        print('X-bar :',  Xbar)
        
        
        tXbar = truncate(Xbar, 5)
        trbar = truncate(Rbar, 5)
        txlcl = truncate(xlcl,5)
        txucl = truncate(xucl, 5)
        trlcl = truncate(rlcl,5)
        trucl = truncate(rucl, 5)
        tcenter = truncate(center, 5)
        
        
        
        
        eintrag_x = 'Xbar/R Chart' + '\nXbar: ' + str(tXbar) + '\nucl: ' + str(txucl) + '\nlcl: ' + str(txlcl) + '\ncenter: ' + str(tcenter)
        eintrag_s = 'rbar: ' + str(trbar) + '\nucl: ' +str(trucl) + '\nlcl: ' + str(trlcl)
        
        
        plt.figure(figsize=(6, 4))
        
        #df3.plot(x, y, ax=axes[0])
        plt.subplot(221)
        sns.lineplot(x=x, y=y, estimator=None, lw=1, data=df3)
        plt.axhline(y=Xbar,linewidth=2, color='g')
        plt.axhline(y=xlcl,linewidth=2, color='orange')
        plt.axhline(y=xucl,linewidth=2, color='orange')
        plt.axhline(y=center,linewidth=2, color='violet')
        
        
        #df3.plot(x, s, ax = axes[1])
        plt.subplot(222)
        sns.lineplot(x=x, y=r, estimator=None, lw=1, data=df3)
        plt.axhline(y=Rbar, linewidth=2, color='g')
        plt.axhline(y=rlcl,linewidth=2, color='orange')
        plt.axhline(y=rucl,linewidth=2, color='orange')
        
        plt.subplot(223)
        plt.text(0.1,0.5,eintrag_x, 
                         ha='left', va='center',
                         fontsize=12)
        plt.axis('off')
        plt.subplot(224)
        plt.text(0.1,0.5,eintrag_s, 
                         ha='left', va='center',
                         fontsize=12)
        plt.axis('off')
        
        plt.show()

    ####Chart without target center    
    else:
    
        x = 'sample'
        y = 'mean'
        #s = 'std'
        
        df3['R'] = df3['max']-df3['min']
        
        r ='R'
        
        Rbar = df3['R'].mean()
        
        
        Xbar = df3['mean'].mean()
        
        xlcl = Xbar - A2[n]*Rbar
        xucl = Xbar + A2[n]*Rbar
        
        rlcl = D3[n]*Rbar
        rucl = D4[n]*Rbar
        
        
        print('r-bar :', Rbar)
        print('X-bar :',  Xbar)
        
        
        tXbar = truncate(Xbar, 5)
        trbar = truncate(Rbar, 5)
        txlcl = truncate(xlcl,5)
        txucl = truncate(xucl, 5)
        trlcl = truncate(rlcl,5)
        trucl = truncate(rucl, 5)
        
        
        
        
        eintrag_x = 'Xbar/R Chart' + '\nXbar: ' + str(tXbar) + '\nucl: ' + str(txucl) + '\nlcl: ' + str(txlcl)
        eintrag_s = 'rbar: ' + str(trbar) + '\nucl: ' +str(trucl) + '\nlcl: ' + str(trlcl)
        
        
        plt.figure(figsize=(6, 4))
        
        #df3.plot(x, y, ax=axes[0])
        plt.subplot(221)
        sns.lineplot(x=x, y=y, estimator=None, lw=1, data=df3)
        plt.axhline(y=Xbar,linewidth=2, color='g')
        plt.axhline(y=xlcl,linewidth=2, color='orange')
        plt.axhline(y=xucl,linewidth=2, color='orange')
        
        
        
        #df3.plot(x, s, ax = axes[1])
        plt.subplot(222)
        sns.lineplot(x=x, y=r, estimator=None, lw=1, data=df3)
        plt.axhline(y=Rbar, linewidth=2, color='g')
        plt.axhline(y=rlcl,linewidth=2, color='orange')
        plt.axhline(y=rucl,linewidth=2, color='orange')
        
        plt.subplot(223)
        plt.text(0.1,0.5,eintrag_x, 
                         ha='left', va='center',
                         fontsize=12)
        plt.axis('off')
        plt.subplot(224)
        plt.text(0.1,0.5,eintrag_s, 
                         ha='left', va='center',
                         fontsize=12)
        plt.axis('off')
        
        plt.show()

###XmR-Chart
###################################################################################

def xmr_chart(df):
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
        
    print(list_columns_werte[int(value_column)])    
    y = list_columns_werte[int(value_column)]
    df['number'] = range(1, len(df) + 1)
    
    
    data = df[y]
    Xbar = df[y].mean()
    
    x = df['number']
    
    sd = 0
    r = []
    
    for i in range(len(data)-1):
        r.append(abs(data[i]-data[i+1]))
        sd += abs(data[i] - data[i+1])
        #print(sd)
    sd /= len(data) - 1
    
    rarray = np.array(r)
    
    dfr = pd.DataFrame(rarray)
    dfr.columns = ['R'] 
    dfr['number'] = range(1, len(dfr) + 1)
    
    xr = dfr['number']
    r = dfr['R']
    
    #print(dfr)
    
    
    
    rbar = rarray.mean()
    
    
    
    d2 = 1.128
    
    
    xlcl = Xbar - 3*sd/d2
    xucl = Xbar + 3*sd/d2
    
    center = sd
    rlcl = 0
    rucl = center + 3*sd/d2
    
    tXbar = truncate(Xbar, 5)
    trbar = truncate(center, 5)
    txlcl = truncate(xlcl,5)
    txucl = truncate(xucl, 5)
    trlcl = truncate(rlcl,5)
    trucl = truncate(rucl, 5)
    
    
    
    eintrag_x = 'X-mR-Chart' + '\nXbar: ' + str(tXbar) + '\nucl: ' + str(txucl) + '\nlcl: ' + str(txlcl)
    eintrag_s = 'rbar: ' + str(trbar) + '\nucl: ' +str(trucl) + '\nlcl: ' + str(trlcl)
    
    
    plt.figure(figsize=(6, 4))
    
    #df3.plot(x, y, ax=axes[0])
    plt.subplot(221)
    sns.lineplot(x=x, y=y, estimator=None, lw=1, data=df)
    plt.axhline(y=Xbar,linewidth=2, color='g')
    plt.axhline(y=xlcl,linewidth=2, color='orange')
    plt.axhline(y=xucl,linewidth=2, color='orange')
    
    
    
    #df3.plot(x, s, ax = axes[1])
    plt.subplot(222)
    sns.lineplot(x=xr, y=r, estimator=None, lw=1, data=dfr)
    plt.axhline(y=rbar, linewidth=2, color='g')
    plt.axhline(y=rlcl,linewidth=2, color='orange')
    plt.axhline(y=rucl,linewidth=2, color='orange')
    
    plt.subplot(223)
    plt.text(0.1,0.5,eintrag_x, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.subplot(224)
    plt.text(0.1,0.5,eintrag_s, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    
    plt.show()
    
        