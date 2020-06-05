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
from statsmodels.formula.api import ols
import statsmodels.api as sm
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

###MSA-V1

def msa_v1(df):
    
    df['nr'] = range(1, len(df) + 1)
    
    nr = df['nr']
    ###get datas
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
        #notol = '1'
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
        tt='none'
        tp='none'
        
    
    
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
    
def msa_v2(df):
    
    sns.set(style="whitegrid")
    sns.set(style="dark", color_codes=True)


    
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
        value_column= input('Choose your value column: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break
    
    ########################################################################
    #Main Values
    y_df = list_columns_werte[int(value_column)]
    
    para = df.select_dtypes(exclude=['float'])
    
    #
    anz_col_para = len(para.columns)
        
    list_columns_para = []
    list_number=[]
    i=1
    for i in range(anz_col_para):
        list_columns_para.append(para.columns[i])
        list_number.append(str(i))
        print(i, para.columns[i])
        i+=1
    
    while True:
        operator_column= input('Choose your "Operator" column: \n(choose number) \n?')
        if operator_column not in list_number:
            print('wrong input, try again!')
        else:
            break
    
    
    ###Operator-Column
    operator = list_columns_para[int(operator_column)]
        
        
        
    while True:
        part_column = input('Choose your "Part" - Column \n(choose number)\n?')    
        if part_column not in list_number:
            print('wrong input, try again!')
        else:
            break
    
    ###Part-Column
    part = list_columns_para[int(part_column)]
    
# =============================================================================
#     while True:
#         measurement_column = input('Choose your "Measurment" Column \n(choose number \n?')
#         if measurement_column not in list_number:
#             print('wrong input, try again!')
#         else:
#             break
# =============================================================================
    
    ###Measurements-Column
    #measurement = list_columns_para[int(measurement_column)]
    
    ###Sort Database to get the right output
    df = df.sort_values(by=[part, operator])
    
    
    ###insert sequence number
    df['nr'] = range(1, len(df) + 1)
    
    
    ###create Xbar/R-Chart
    df2 = pd.DataFrame()
    
    df2 = df.groupby([part, operator])[y_df].describe()
    
    
    n = df2['count'][1][1]
    
    n= int(n)
    
    fn = 'describe.csv'
    
    
    
    
    
    
    df2 = df2.reset_index()
    df2 = df2.sort_values(by=[operator, part])    
    df2['nr'] = range(1, len(df2) + 1)
    df2.to_csv(fn, sep=';', decimal=',')
    
    df3 = pd.read_csv(fn, sep=';' , decimal=',', header=0)
    print(df3)
    
    df3['R'] = df3['max']-df3['min']
    
    
    
    x = 'nr'
    y = 'mean'
        
        
    Rbar = df3['R'].mean()
    r = 'R'
    
    Xbar = df3['mean'].mean()
    
    xlcl = Xbar - A2[n]*Rbar
    xucl = Xbar + A2[n]*Rbar
    
    rlcl = D3[n]*Rbar
    rucl = D4[n]*Rbar
    
    ###################################################################
    ###Two Way ANOVA  
    mod = ols(y_df + '~C(' + part + ')*C(' + operator +')',
                data=df).fit()

    # Seeing if the overall model is significant
    print(f"Overall mod F({mod.df_model: .0f},{mod.df_resid: .0f}) = {mod.fvalue: .3f}, p = {mod.f_pvalue: .4f}")    
    
    mod.summary()
        
    aov_table = sm.stats.anova_lm(mod, typ=2)
    print('two way ANOVA Result:' )
    print (aov_table)
    
    
    ##########################################################################
    ###calc GRR-Value
    ###Thanks to https://www.spcforexcel.com/knowledge/measurement-systems-analysis/anova-gage-rr-part-2
    
    xbar = df[y_df].mean()
    
    ###S-Square-Operator
    #########################################################################
    dfSSo= df.groupby([operator])[y_df].describe()
    dfSSo['SSq']=(dfSSo['mean']-xbar)**2
    
    SSo = dfSSo['SSq'].sum()
    #k-value
    k = len(dfSSo)
    cSSo = dfSSo['count'][1]
    cSSo = int(cSSo)
    
    ##SSo-Output
    SSocalc = SSo*cSSo
    MSo = SSocalc/(k-1)
    
    print('Calculation of GRR-Parameters')
    print('#'*40)
    print('S-Sqaure Opeartor')      
    print('SSo:',SSocalc)
    print('Mso:', MSo )
    
    ###S-Square Parts
    #########################################################################
    dfSSp= df.groupby([part])[y_df].describe()
    dfSSp['SSq']=(dfSSp['mean']-xbar)**2
    
    
    SSp = dfSSp['SSq'].sum()
    #n-value
    n = len(dfSSp)
    cSSp = dfSSp['count'][1]
    cSSp = int(cSSp)

    ##SSp-Output
    SSpcalc = SSp*cSSp
    MSp = SSpcalc/(n-1)
    
    print('#'*40)
    print('S-Sqaure Parts')    
    print('SSp:',SSpcalc)
    print('MSp:',MSp)
    
    
    ###S-Square Equipement
    ########################################################################
    ###df3 = Mean of the Repatability
    dfSSe=df
    
    dfSSe['pando']= (dfSSe[part]).astype(str) + (dfSSe[operator]).astype(str)
    
    df3['pando']= (df3[part]).astype(str) +  (df3[operator]).astype(str)
    #r-value
    cr = df3['count'][1]
    result = pd.merge(dfSSe, df3, how='outer', on='pando')
    
    #result['SSq']=(result['Value']-result['mean'])**2
    result['SSq']=(result[y_df]-result['mean'])**2
    
    SSe = result['SSq'].sum()
    MSe = SSe/(n*k*(cr-1))
    
    print('#'*40)
    print('S-Sqaure Equipment')
    print('SSe:',SSe)
    print('MSe:' , MSe)
    
    ###S-Square Total
    dfSST = df
    #dfSST['SSq'] = (dfSST['Value']-xbar)**2
    dfSST['SSq'] = (dfSST[y_df]-xbar)**2
    SST = dfSST['SSq'].sum()
    
    print('#'*40)
    print('S-Sqaure Total')
    print('SST:',SST)
    
    ###S-Square Opeartor*Parts
    SSop = SST-(SSocalc+SSpcalc+SSe)
    MSop = SSop/((k-1)*(n-1))
    
    print('#'*40)
    print('S-Sqaure Operator * Parts')
    print('SSop:',SSop)
    print('MSop:', MSop)
    
    ########################################################################
    ##calc Sigma**2
    
    ###Sigma²Operator*Parts
    sigmaqOP = (MSop-MSe)/cr
    if sigmaqOP < 0:
        sigmaqOP = 0
    
    
    ###Sigma² Part
    sigmaqP = (MSp-MSop)/(k*cr)    
    if sigmaqP < 0:
        sigmaqP =0
    
    
    ###Sigma² Operator
    sigmaqO = (MSo-MSop)/(cr*n)
    if sigmaqO < 0:
        sigmaqO = 0
        
    ###Sigma² Equipement
    sigmaqE = MSe
    
    print('#'*40)
    print('Sigma - Values')
    print('sigmaqOP: ', sigmaqOP)
    print('sigmaqP: ', sigmaqP)
    print('sigmaqO: ' , sigmaqO)
    print('sigmaqE:' , sigmaqE)
    
    ###GRR²
    GRRq = sigmaqE+sigmaqO
    print('GRRq: ', GRRq)
    
    ###Total-Variance
    TVq = sigmaqE + sigmaqP + sigmaqOP + sigmaqO
    print('TVq: ', TVq)
    
    ####Percent Values
    
    ###%GRR
    PercentGRR = (GRRq/TVq)*100
    
    ###%Part
    PercentPart = (sigmaqP/TVq)*100
    
    ###%Equipment
    PercentE = (sigmaqE/TVq)*100
    
    ###%Operator
    PercentO = (sigmaqO/TVq)*100
    
    ###%Operator*Parts
    PercentOP = (sigmaqOP/TVq)*100
    
    ###df of the Percent Values
    GRRdf = pd.DataFrame(np.array([['%GRR', PercentGRR], ['%Part', PercentPart], ['%Equi', PercentE], ['%Oper', PercentO], ['%Op*Pa', PercentOP]]),

                   columns=['Name', 'Value'])
    GRRdf['Value']= GRRdf['Value'].astype(float)
    
    dPercentGRR = truncate(PercentGRR, 2)
    
    print(GRRdf)
    
    if PercentGRR < 10:
        resultGRR = 'Measuring-System is capable'
    elif PercentGRR > 10:
        resultGRR = 'Measuring System is conditionally capable'
    elif PercentGRR > 30:
        resultGRR = 'Measuring System in not capable'
    
    
    eintrag = 'MSA V2 (GageR&R)' + '\n%GRR: ' + str(dPercentGRR) + '\n' + resultGRR
    
    
    ######create the diagram
    
    plt.figure(figsize=(8, 6))
        
    #df3.plot(x, y, ax=axes[0])
    plt.subplot(231)
    sns.lineplot(x=x, y=r, markers =True, style=operator, estimator=None, lw=1, data=df3)
    plt.axhline(y=Rbar, linewidth=2, color='g')
    plt.axhline(y=rlcl,linewidth=2, color='orange')
    plt.axhline(y=rucl,linewidth=2, color='orange')
    
    
    #df3.plot(x, s, ax = axes[1])
    plt.subplot(232)
    
    sns.boxplot(x=operator, y=y_df,data=df, palette="Set3")
    
    plt.subplot(233)
    
    sns.barplot(x='Value', y='Name', data=GRRdf, palette="deep")
    
    plt.subplot(234)
    
    #sns.lineplot(x=x, y=y, estimator=None, markers='o', lw=1, data=df3)
    sns.lineplot(x=x, y=y, markers =True, style=operator, lw=1, data=df3)
    plt.axhline(y=Xbar,linewidth=2, color='g')
    plt.axhline(y=xlcl,linewidth=2, color='orange')
    plt.axhline(y=xucl,linewidth=2, color='orange')
    
    
    
    
    plt.subplot(235)
    sns.boxplot(x=part, y=y_df,data=df, palette="Set3")
    sns.stripplot(x=part, y=y_df,data=df, hue=operator, palette="Set3")
    
    
    
    plt.subplot(236)
    plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    
    
    
    
    plt.show()

        