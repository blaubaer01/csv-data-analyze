#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:59:08 2020

@author: blaubaer
"""
#import pandas as pd
from scipy.stats import shapiro
import matplotlib.pyplot as plt
import seaborn as sns ; sns.set()
import scipy as spy


def CPA(df):
            
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
        
    value_column= input('Which value column do you want to see: \n(choose number) \n?')
        
    y = df[list_columns_werte[int(value_column)]]
    #ly = y.count()
    #x = np.arange(1, ly, 1)
    
    print('Data-overview choosed column:')
    print(y)
    
    
    one_two_sided = input('Tolerance: \n1: both side tolerance \n2: one side ut \n3: one side lt \n(choose number) \n?')
    
    
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    
    
    
    ###both side tolerance
    if one_two_sided == '1':
        tol = input('upper tolerance , lower tolerance \n(choose point-comma / seperate with float-comma, example:2.2 , 1.9) \n?')
        ut, lt = tol.split(',')
        ut = float(ut)
        lt = float(lt)
        
        stat, p = shapiro(y)
        
        ###both side tolerance / normaldistribution
        if p >= 0.05:
        #normal verteilt
            print('both side tolerance - normal distribution')
            #calculation cp/cpk
            mean_y = y.mean()
            std_y = y.std()
            
            cp = (ut-lt) / (6*std_y)
            cpkut = (ut-mean_y)/(3*std_y)
            cpklt = (mean_y-lt)/(3*std_y)
            cpk = min(cpkut, cpklt)
            mean_p_3s = mean_y + 3*std_y
            mean_m_3s = mean_y - 3*std_y
            cpk = truncate(cpk, 2)
            cp = truncate(cp, 2)
            mean_y = truncate(mean_y, 3)
            std_y = truncate(std_y, 3)
            mean_p_3s = truncate(mean_p_3s, 3)
            mean_m_3s = truncate(mean_m_3s, 3)
            
            print(mean_y,std_y , cp, cpk)
            eintrag = 'Mean: ' + str(mean_y) + 's: ' + str(std_y) + '\n+3s: ' + str(mean_p_3s) + '\n-3s: ' + str(mean_m_3s) + '\nCp: ' + str(cp) + '\nCpk: ' + str(cpk)
            
            
            ##graphic
            
            plt.figure(figsize=(6, 4))
            plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
            sns.distplot(y);
            plt.axvline(x=ut,linewidth=2, color='r')
            plt.axvline(x=lt,linewidth=2, color='r')
            plt.subplot(222)
            spy.stats.probplot(y, dist="norm", plot=plt)
            plt.subplot(223)
            ax = sns.boxplot(x=y)
            plt.subplot(224)
            plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
            plt.axis('off')
            plt.show()
            
            
        
        ###both side tolerance / other distribution
        elif p < 0.05:
        #nicht normalverteilt
            print('both side tolerance other distribution')
            
            median_y = y.quantile(0.5)
            
            upper_q_y = y.quantile(0.99869)
            
            lower_q_y = y.quantile(0.00135)
            
            
            cp = (ut-lt) / (upper_q_y - lower_q_y)
            cpkut = (ut-median_y)/(upper_q_y-median_y)
            cpklt = (median_y-lt)/(median_y-lower_q_y)
            cpk = min(cpkut,cpklt)
            cpk = truncate(cpk, 2)
            cp = truncate(cp, 2)
            median_y = truncate(median_y, 3)
            upper_q_y = truncate(upper_q_y, 3)
            lower_q_y = truncate(lower_q_y, 3)
            
            print(median_y ,upper_q_y, lower_q_y , cp, cpk)
            
            eintrag = 'Median: ' + str(median_y) + '\nQ0.998: ' + str(upper_q_y) + '\nQ0.001: ' + str(lower_q_y) + '\nCp: ' + str(cp) + '\nCpk: ' + str(cpk)
            
            ##graphic
            
            plt.figure(figsize=(6, 4))
            plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
            sns.distplot(y);
            plt.axvline(x=ut,linewidth=2, color='r')
            plt.axvline(x=lt,linewidth=2, color='r')
            plt.subplot(222)
            spy.stats.probplot(y, dist="norm", plot=plt)
            plt.subplot(223)
            ax = sns.boxplot(x=y)
            plt.subplot(224)
            plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
            plt.axis('off')
            plt.show()
    
    ###one side tolerance ut
    elif one_two_sided =='2':
        ut = input('Upper tolerance: \n(choose point-comma) \n?')
        ut = float(ut)
        lt = 'none'
    
        stat, p = shapiro(y)
        
        ###one side tolerance ut / normal distribution
        if p >= 0.05:
            #normal verteilt
            print('one side tolerance ut / normal distribution')
            
            mean_y = y.mean()
            std_y = y.std()
            
            cpkut = (ut-mean_y)/(3*std_y)
            cpk = cpkut
            mean_p_3s = mean_y + 3*std_y
            mean_m_3s = mean_y - 3*std_y
            
            cpk = truncate(cpk, 2)
            mean_y = truncate(mean_y, 3)
            std_y = truncate(std_y, 3)
            mean_p_3s = truncate(mean_p_3s, 3)
            mean_m_3s = truncate(mean_m_3s, 3)
            
            
            eintrag = 'Mean: ' + str(mean_y) + '\n+3s: ' + str(mean_p_3s) + '\n-3s: ' + str(mean_m_3s) + '\nCpk: ' + str(cpk)
            
            
            ##graphic
            
            plt.figure(figsize=(6, 4))
            plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
            sns.distplot(y);
            plt.axvline(x=ut,linewidth=2, color='r')
            plt.subplot(222)
            spy.stats.probplot(y, dist="norm", plot=plt)
            plt.subplot(223)
            ax = sns.boxplot(x=y)
            plt.subplot(224)
            plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
            plt.axis('off')
            plt.show()
            
            
            
        ###one side tolerance ut / other distribution
        elif p < 0.05:
            #nicht normalverteilt
            print('one side tolerance ut / other distribution')
            
            median_y = y.quantile(0.5)
            upper_q_y = y.quantile(0.99869)
            lower_q_y = y.quantile(0.00135)
            
            cpkut = (ut-median_y)/(upper_q_y-median_y)
            cpk = cpkut
            
            cpk = truncate(cpk, 2)
            median_y = truncate(median_y, 3)
            upper_q_y = truncate(upper_q_y, 3)
            lower_q_y = truncate(lower_q_y, 3)
            
    
            eintrag = 'Median: ' + str(median_y) + '\nQ0.998: ' + str(upper_q_y) + '\nQ0.001: ' + str(lower_q_y) + '\nCpk: ' + str(cpk)
            
            ##graphic
            
            plt.figure(figsize=(6, 4))
            plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
            sns.distplot(y);
            plt.axvline(x=ut,linewidth=2, color='r')
            plt.subplot(222)
            spy.stats.probplot(y, dist="norm", plot=plt)
            plt.subplot(223)
            ax = sns.boxplot(x=y)
            plt.subplot(224)
            plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
            plt.axis('off')
            plt.show()
    
    
    
    
    
    
    ###one side tolerance lt
    elif one_two_sided =='3':
        lt = input('Lower tolerance: \n(choose point-comma) \n?')
        ut = 'none'
        lt = float(lt)
    
        stat, p = shapiro(y)
    
        if p >= 0.05:
            #normal verteilt
            print('one side tolerance /normal distribution')
            
            mean_y = y.mean()
            std_y = y.std()
            
            cpklt = (mean_y-lt)/(3*std_y)
            cpk = cpklt
            
            mean_p_3s = mean_y + 3*std_y
            mean_m_3s = mean_y - 3*std_y
            
            cpk = truncate(cpk, 2)
            mean_y = truncate(mean_y, 3)
            std_y = truncate(std_y, 3)
            mean_p_3s = truncate(mean_p_3s, 3)
            mean_m_3s = truncate(mean_m_3s, 3)
            
            
            eintrag = 'Mean: ' + str(mean_y) + '\n+3s: ' + str(mean_p_3s) + '\n-3s: ' + str(mean_m_3s) + '\nCpk: ' + str(cpk)
            
            
            ##graphic
            
            plt.figure(figsize=(6, 4))
            plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
            sns.distplot(y);
            plt.axvline(x=lt,linewidth=2, color='r')
            plt.subplot(222)
            spy.stats.probplot(y, dist="norm", plot=plt)
            plt.subplot(223)
            ax = sns.boxplot(x=y)
            plt.subplot(224)
            plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
            plt.axis('off')
            plt.show()
            
            
            
            
            
            
        elif p < 0.05:
            #nicht normalverteilt
            print('one side tolerance / other distribution')
            
            median_y = y.quantile(0.5)
            upper_q_y = y.quantile(0.99869)
            lower_q_y = y.quantile(0.00135)
            
            cpklt = (median_y-lt)/(median_y-lower_q_y)
            cpk = cpklt
        
            cpk = truncate(cpk, 2)
            median_y = truncate(median_y, 3)
            upper_q_y = truncate(upper_q_y, 3)
            lower_q_y = truncate(lower_q_y, 3)
            
            
            eintrag = 'Median: ' + str(median_y) + '\nQ0.998: ' + str(upper_q_y) + '\nQ0.001: ' + str(lower_q_y) + '\nCpk: ' + str(cpk)
            
            ##graphic
            
            plt.figure(figsize=(6, 4))
            plt.subplot(221) # äquivalent zu: plt.subplot(2, 2, 1)
            sns.distplot(y);
            plt.axvline(x=lt,linewidth=2, color='r')
            plt.subplot(222)
            spy.stats.probplot(y, dist="norm", plot=plt)
            plt.subplot(223)
            ax = sns.boxplot(x=y)
            plt.subplot(224)
            plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
            plt.axis('off')
            plt.show()



