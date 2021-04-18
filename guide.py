#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 19:50:47 2021

@author: blaubaer
"""

from mft import clear, session_write
from tabulate import tabulate
import pandas as pd
from charts import decriptive_statistics
from charts import groupby_balkendiagramm, balkendiagramm, kuchendiagramm, line_diagram_menu
from charts import boxplot, boxplot_groupby, boxplot2f, violin, violin_groupby, violin2f,single_swarmplot
from charts import swarmplot1f, swarmplot2f, single_stripplot, stripplot1f, stripplot2f, histogram, scatter
from charts import scatter_w_r, scatter_joint_plot, qq_plot, groupplot_menu, pareto, pareto_one_column, pointplot1f, pointplot2f, confidencelinechart
from charts import threeddplot, distriplot1f, histogram1f, decriptive_statistics, scatter_by_o_factor, pairplot_menu
from charts import cond_mean_w_ob_by_1f, cond_mean_w_ob_by_2f, bivariate_plot_w_m_elements, stacked_hist
from charts import scatterplot_w_varying_point_sizes, scatterplot_w_varying_point_sizes_with_cat



def beschreibende_stat(df):
    while True:
        clear()
        print('\U0001f9ee  descriptive statistic \U0001f9ee')
        was_beschreibend_analysieren=input('What data do you want to analyze? \n1: all\n2: only the numerical datas \n3: one special column \n4: graphical (numerical data) \n?')
        if was_beschreibend_analysieren =='1':
            print('Simple descriptive statistics: \n')
            print(df.describe(include="all"))
            
            ################################################################################
            ###Log-file
            fname = 'Simple descriptive statistics'
              
            log = fname + '\n'
            session_write(log)
    
        elif was_beschreibend_analysieren =='2':
            print('Simple descriptive statistics: \n')
            print(df.describe())
            
            ################################################################################
            ###Log-file
            fname = 'Simple descriptive statistics'
              
            log = fname + '\n'
            session_write(log)
            
        elif was_beschreibend_analysieren =='3':
            anz_col = len(df.columns)
        
            list_columns = []

            i=1
            for i in range(anz_col):
                list_columns.append(df.columns[i])
                print(i, df.columns[i])
                i+=1
            nummer_spalte= input('Which column do you want to see: \n(choose number) \n?')
            try:
                print('Simple descriptive statiatics: \n')
                print(df[list_columns[int(nummer_spalte)]].describe(include='all'))
                col1 = list_columns[int(nummer_spalte)]
    
                df2 = pd.DataFrame()
    
                df2 = df[col1].describe()
                
                df2.to_csv('described.csv', sep=';', decimal=',', header =True)  
    
                df3=pd.read_csv('described.csv',sep=';' ,decimal=',', header=1)
                df3.columns=['Stat Function', 'Value']
                
                print(tabulate(df3, headers='keys', tablefmt='psql'))
                
                view1 = tabulate(df3, headers='keys', tablefmt='psql')
    
            except IndexError as error:
                print('wrong input, please try again!')
            except Exception as exception:
                print('wrong input, please try again!')
            
            
            
            
            ################################################################################
            ###Log-file
            fname = 'Simple descriptive statistics one column'
              
            log = fname + '\n' + view1 + '\n'
            session_write(log)
        
        elif was_beschreibend_analysieren =='4':
            decriptive_statistics(df)
            
        
        
        
        else:
            print('wrong input, please try again!')
        
        
            
        
        
        restart = input('\nFurther descriptive analysis: y/n \n?')
        if restart.lower() != 'y':
            break
        


def first_question(df):
    clear()
    while True:
        f_question = input('What would you like to do: \n1: descriptive statistik \n2: graphical analyse \n3: statistical tests \n?')
        if f_question =='1':
            beschreibende_stat(df)
            break
        elif f_question =='2':
            graph_question(df)
            break
        elif f_question =='3':
            menu3
            break
        else:
            print('wrong input, try again')

def graph_question(df):
    clear()
    n_v_question = input('How many values: \n1: one value \n2: two values \n3: tree values \n?')
    n_f_question = input('How many values: \n1: no factors \n2: one factor \n3: two factors \n?')
    
    if n_v_question == '1' and n_f_question == '1':
        one_val_no_fact(df)
    elif n_v_question == '1' and n_f_question == '2':
        one_val_one_fact(df)
    elif n_v_question == '1' and n_f_question == '3':
        one_val_two_fact(df)
    elif n_v_question == '2' and n_f_question == '1':
        two_val_no_fact(df)
    elif n_v_question == '2' and n_f_question == '2':
        two_val_one_fact(df)
    elif n_v_question == '2' and n_f_question == '3':
        two_val_two_fact(df)
    elif n_v_question == '3' and n_f_question == '1':
        tree_val_no_fact(df)
    elif n_v_question == '3' and n_f_question == '2':
        tree_val_one_fact(df)
    elif n_v_question == '3' and n_f_question == '3':
        tree_val_two_fact(df)
    else:
        print('Wrong input, please try again')

def one_val_no_fact(df):
    clear()
    
    g_val_no_fact = input('Choose graph: \n1: Boxplot \n2: Violinplot \n3: Swarmplot \n4: Stripplot \n5: Histogram \n6: Q-Q-Plot \n?' )
    if g_val_no_fact == '1':
        boxplot(df)
    elif g_val_no_fact == '2':
        violin(df)
    elif g_val_no_fact == '3':
        single_swarmplot(df)
    elif g_val_no_fact == '4':
        single_stripplot(df)
    elif g_val_no_fact == '5':
        histogram(df)
    elif g_val_no_fact == '6':
        qq_plot(df)
    else:
        print('wrong input, please try again')
        
        
        
        
        

def one_val_one_fact(df):
    clear()
    g_val_one_fact = input('Choose graph: \n1: Boxplot \n2: Violinplot \n3: Swarmplot \n4: Stripplot \n5: Pointplot \n6: Histogram \n7: Histogram stacked \n8: Distributionsplot \n9: Conditional Mean Plot \n?')
    if g_val_one_fact == '1':
        boxplot_groupby(df)
    elif g_val_one_fact == '2':
        violin_groupby(df)
    elif g_val_one_fact == '3':
        swarmplot1f(df)
    elif g_val_one_fact == '4':
        stripplot1f(df)
    elif g_val_one_fact == '5':
        pointplot1f(df)
    elif g_val_one_fact == '6':
        histogram1f(df)
    elif g_val_one_fact == '7':
        stacked_hist(df)
    elif g_val_one_fact == '8':
        distriplot1f(df)
    elif g_val_one_fact == '9':
        cond_mean_w_ob_by_1f(df)
    else:
        print('wrong input, please try again')
        
    
    
def one_val_two_fact(df):
    clear()

def two_val_no_fact(df):
    clear()

def two_val_one_fact(df):
    clear()

def two_val_two_fact(df):
    clear()

def tree_val_no_fact(df):
    clear()

def tree_val_one_fact(df):
    clear()

def tree_val_two_fact(df):
    clear()




