#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:55:01 2020

@author: blaubaer (Ricky Helfgen)
"""
import seaborn as sns
import matplotlib.pyplot as plt
import os
import scipy as spy
from mft import isfloat, clear
from mpl_toolkits import mplot3d




    
##################################################################################
#graphical analyze
##################################################################################

#######################################################################
####bar charts
### groupby barchart

def groupby_balkendiagramm(df):
    
    anz_col = len(df.columns)
        
    list_columns = []
    list_number=[]
    i=1
    for i in range(anz_col):
        list_columns.append(df.columns[i])
        list_number.append(str(i))
        print(i, df.columns[i])
        i+=1
    
    while True:
        nummer_spalte= input('Which column do you want to see: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    
    while True:
        groupby_spalte = input('Group by column: \n(choose number) \n?')
        if groupby_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
        
    df.groupby([list_columns[int(nummer_spalte)],list_columns[int(groupby_spalte)]]).size().unstack().plot(kind='bar',stacked=True)
    label_chart = (list_columns[int(nummer_spalte)] + ' grouped by count ' + list_columns[int(groupby_spalte)])
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()
    
    #df.groupby('state')['name'].nunique().plot(kind='bar')
    #plt.show()

#######################################################################
### barcharts
def balkendiagramm(df):
    anz_col = len(df.columns)
        
    list_columns = []
    list_number=[]
    i=1
    for i in range(anz_col):
        list_columns.append(df.columns[i])
        list_number.append(str(i))
        print(i, df.columns[i])
        i+=1
        
    while True:
        nummer_spalte= input('Which column do you want to see: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break    
    
    
    ax = df[list_columns[int(nummer_spalte)]].value_counts().plot(kind='bar',
                                    figsize=(14,8),
                                    title=list_columns[int(nummer_spalte)], color='blue')
    ax.set_xlabel(list_columns[int(nummer_spalte)])
    ax.set_ylabel("Frequency")
    plt.show()


#######################################################################        
###pie charts
def kuchendiagramm(df):
    clear()
    anz_col = len(df.columns)
        
    list_columns = []
    list_number = []
    i=1
    for i in range(anz_col):
        list_columns.append(df.columns[i])
        list_number.append(str(i))
        print(i, df.columns[i])
        i+=1
    
    while True:
        nummer_spalte= input('Which column do you want to see: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break    
    
        
    # Plot
    ax = df[list_columns[int(nummer_spalte)]].value_counts().plot(kind='pie',
                                    figsize=(14,8),
                                    title=list_columns[int(nummer_spalte)], autopct='%1.1f%%')
    #ax.set_xlabel(list_columns[int(nummer_spalte)])
    ax.set_ylabel("Frequency")
    
    
    plt.show()

#######################################################################
###line-chart
def liniendiagramm(df):
    clear()
    kategorie=df.select_dtypes(include=['object', 'datetime', 'int'])
    werte = df.select_dtypes(exclude=['object'])
    
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
        value_column= input('Which value column do you want to see: \n(choose number)\n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number = []
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
    
    
    df.plot(x, y, grid=True)
    
    plt.show()


#######################################################################
###line-chart
def confidencelinechart(df):
    
    #df = sns.load_dataset(df)
    
    clear()
    kategorie=df.select_dtypes(include=['object', 'datetime', 'int'])
    werte = df.select_dtypes(exclude=['object'])
    
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
        value_column= input('Which value column do you want to see: \n(choose number)\n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number = []
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
    
    sns.relplot(x=x, y=y, kind="line", ci="sd", data=df)
    
    
    plt.show()




#######################################################################
###boxplots and violinplots

#######################################################################
###single boxplot    
def boxplot(df):
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    
    df.boxplot(column=y, widths=0.5)
    plt.show()

#######################################################################
###boxplot with group
def boxplot_groupby(df):
    clear()
    kategorie=df.select_dtypes(include=['object','int'])
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
    
    df.boxplot(by=x, column=y)
    
    plt.show()


######################################################################
### Boxplot by 2 groups
    
def boxplot2f(df):
    
    clear()
    sns.set(style="whitegrid")
    
    category=df.select_dtypes(exclude=['float'])
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
    anz_col_category = len(category.columns)
        
    list_columns_category = []
    list_number=[]
    i=1
    for i in range(anz_col_category):
        list_columns_category.append(category.columns[i])
        list_number.append(str(i))
        print(i, category.columns[i])
        i+=1
    
    while True:
        groupby1_column = input('Group1 by column: \n(choose number) \n?')
        if groupby1_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    while True:
        groupby2_column = input('Group2 by column \n(choose number) \n?')
        if groupby2_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_category[int(groupby1_column)]
    z = list_columns_category[int(groupby2_column)]
    
    sns.boxplot(x=x, y=y, hue=z, data=df, palette="Set3")
    plt.show()




#######################################################################    
###single violin plot
def violin(df):
    clear()
    sns.set(style="whitegrid")
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
        
    
    y = list_columns_werte[int(value_column)]
    
    sns.violinplot(x=df[y])
    plt.show()

#######################################################################
###violin plot with group
def violin_groupby(df):
    clear()
    sns.set(style="whitegrid")
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number = []
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
    
    
    sns.violinplot(x=x, y=y, data=df)
    
    plt.show()

#######################################################################
###violin Plot by 2 groups
def violin2f(df):
    clear()
    sns.set(style="whitegrid")
    
    category=df.select_dtypes(exclude=['float'])
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
    anz_col_category = len(category.columns)
        
    list_columns_category = []
    list_number=[]
    i=1
    for i in range(anz_col_category):
        list_columns_category.append(category.columns[i])
        list_number.append(str(i))
        print(i, category.columns[i])
        i+=1
    
    while True:
        groupby1_column = input('Group1 by column: \n(choose number) \n?')
        if groupby1_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    while True:
        groupby2_column = input('Group2 by column \n(choose number) \n?')
        if groupby2_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_category[int(groupby1_column)]
    z = list_columns_category[int(groupby2_column)]
    
    sns.violinplot(x=x, y=y, hue=z, data=df, palette="Set3")
    plt.show()

######################################################################
###single swarm plot
def single_swarmplot(df):
    clear()
    sns.set(style="whitegrid")
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
        
    
    y = list_columns_werte[int(value_column)]
    
    sns.swarmplot(x=df[y])
    plt.show()
    
    
    
    
#######################################################################
###swarmplot with group
def swarmplot1f(df):
    clear()
    sns.set(style="whitegrid", palette="muted")

    kategorie=df.select_dtypes(exclude=['float'])
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
    
    y = df[list_columns_werte[int(value_column)]]
    x = df[list_columns_kategorie[int(groupby_column)]]
    
    
    # Draw a categorical scatterplot to show each observation
    sns.swarmplot(x=x, y=y, data=df)
    #sns.boxplot(x=x, y=y, data=df, whis=np.inf)
    plt.show()

######################################################################
###swarmplot two factors
def swarmplot2f(df):
    clear()
    sns.set(style="whitegrid")
    
    category=df.select_dtypes(exclude=['float'])
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
    anz_col_category = len(category.columns)
        
    list_columns_category = []
    list_number=[]
    i=1
    for i in range(anz_col_category):
        list_columns_category.append(category.columns[i])
        list_number.append(str(i))
        print(i, category.columns[i])
        i+=1
    
    while True:
        groupby1_column = input('Group1 by column: \n(choose number) \n?')
        if groupby1_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    while True:
        groupby2_column = input('Group2 by column \n(choose number) \n?')
        if groupby2_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_category[int(groupby1_column)]
    z = list_columns_category[int(groupby2_column)]
    
    sns.swarmplot(x=x, y=y, hue=z, data=df)

    
    plt.show()
    

######################################################################
###single stripplot
def single_stripplot(df):
    clear()
    sns.set(style="whitegrid")
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
        
    
    y = list_columns_werte[int(value_column)]
    
    sns.stripplot(x=df[y])
    plt.show()
    
#######################################################################
###stripplot with group
def stripplot1f(df):
    clear()
    sns.set(style="whitegrid", palette="muted")

    kategorie=df.select_dtypes(exclude=['float'])
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
    
    y = df[list_columns_werte[int(value_column)]]
    x = df[list_columns_kategorie[int(groupby_column)]]
    
    
    # Draw a categorical scatterplot to show each observation
    sns.stripplot(x=x, y=y, data=df)
    #sns.boxplot(x=x, y=y, data=df, whis=np.inf)
    plt.show()
        
######################################################################
###stripplot two factors
def stripplot2f(df):
    clear()
    sns.set(style="whitegrid")
    
    category=df.select_dtypes(exclude=['float'])
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
    anz_col_category = len(category.columns)
        
    list_columns_category = []
    list_number=[]
    i=1
    for i in range(anz_col_category):
        list_columns_category.append(category.columns[i])
        list_number.append(str(i))
        print(i, category.columns[i])
        i+=1
    
    while True:
        groupby1_column = input('Group1 by column: \n(choose number) \n?')
        if groupby1_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    while True:
        groupby2_column = input('Group2 by column \n(choose number) \n?')
        if groupby2_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_category[int(groupby1_column)]
    z = list_columns_category[int(groupby2_column)]
    
    sns.stripplot(x=x, y=y, hue=z, data=df)

    
    plt.show()

#######################################################################
###stripplot with group
def pointplot1f(df):
    clear()
    sns.set(style="darkgrid")

    kategorie=df.select_dtypes(exclude=['float'])
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
    
    y = df[list_columns_werte[int(value_column)]]
    x = df[list_columns_kategorie[int(groupby_column)]]
    
    
    # Draw a categorical scatterplot to show each observation
    sns.pointplot(x=x, y=y, data=df)
    #sns.boxplot(x=x, y=y, data=df, whis=np.inf)
    plt.show()
        
######################################################################
###stripplot two factors
def pointplot2f(df):
    clear()
    sns.set(style="darkgrid")
    
    category=df.select_dtypes(exclude=['float'])
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
    anz_col_category = len(category.columns)
        
    list_columns_category = []
    list_number=[]
    i=1
    for i in range(anz_col_category):
        list_columns_category.append(category.columns[i])
        list_number.append(str(i))
        print(i, category.columns[i])
        i+=1
    
    while True:
        groupby1_column = input('Group1 by column: \n(choose number) \n?')
        if groupby1_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    while True:
        groupby2_column = input('Group2 by column \n(choose number) \n?')
        if groupby2_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_category[int(groupby1_column)]
    z = list_columns_category[int(groupby2_column)]
    
    sns.pointplot(x=x, y=y, hue=z, data=df)

    
    plt.show()



    
    
################################################################################
###visual distribution and values
###histogram
def histogram(df):
    clear()
    sns.set(color_codes=True)

        
    werte = df.select_dtypes(exclude=['object'])
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    y = df[list_columns_werte[int(value_column)]]
    
    sns.distplot(y);
    plt.show()




################################################################################
###visual distribution and values
###histogram
def histogram_w_g(df):
    clear()
    sns.set(color_codes=True)

        
    werte = df.select_dtypes(exclude=['object'])
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    group = df.select_dtypes(include=['object'])
    
    #
    anz_col_group = len(group.columns)
        
    list_columns_group = []
    list_number = []
    i=1
    for i in range(anz_col_group):
        list_columns_group.append(group.columns[i])
        list_number.append(str(i))
        print(i, group.columns[i])
        i+=1
    
    while True:
        group_column= input('Which value column do you want to see: \n(choose number) \n?')
        if group_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    
    y = df[list_columns_werte[int(value_column)]]
    g = df[list_columns_group[int(group_column)]]
    
    
    y.hist(by = g);
    
    
    plt.show()


def menu_hist(df):
    
    m_hist = input('Choose kind of histogram: \n1: single histogram \n2: histogram by group \n?')
    
    if m_hist == '1':
        histogram(df)
    elif m_hist == "2":
        histogram_w_g(df)
    else:
        print('wrong input, try again!')





#######################################################################    
###qq-plot
def qq_plot(df):
    clear()
    werte = df.select_dtypes(exclude=['object'])
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    y = df[list_columns_werte[int(value_column)]]
    
    spy.stats.probplot(y, dist="norm", plot=plt)
    plt.show() 


#######################################################################
###scatterplot
def scatter(df):
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
    
    
    
    y = list_columns_werte[int(value_column_y)]
    
    x = list_columns_werte[int(value_column_x)]
    
    
    
    #df.hist(column=y)
    df.plot.scatter(y,x) # Histogram will now be normalized
    label_chart = ('Scatter-Plot')
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()

#######################################################################
###scatter plot with regression line
def scatter_w_r(df):
    clear()
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
    


    sns.regplot(x=x, y=y, data=df);


    
    label_chart = ('Linear-Regression-Plot')
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()

#######################################################################
###jointplot
def scatter_joint_plot(df):
    clear()
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
    


    sns.jointplot(x=x, y=y, data=df, kind="reg");

    plt.show()



#######################################################################
###Group Plot (show a plot by group)
def groupplot(df):
    clear()
    sns.set(style="ticks")

    
    kategorie=df.select_dtypes(exclude=['float'])
    werte = df.select_dtypes(exclude=['object'])
    zeitraum=df.select_dtypes(exclude=['float'])
    
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
    
    anz_col_zeitraum = len(zeitraum.columns)
        
    list_columns_zeitraum = []
    list_number = []
    i=1
    for i in range(anz_col_zeitraum):
        list_columns_zeitraum.append(zeitraum.columns[i])
        list_number.append(str(i))
        print(i, zeitraum.columns[i])
        i+=1
    
    while True:
        datetime_column = input('Choose the X-axis-column \n(choose number) \n?')
        if datetime_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    z = list_columns_zeitraum[int(datetime_column)]
    
    df = df.sort_values(by=z, ascending=1)
    
    
    
    
    anz = df[x].nunique()    
    
    sns.relplot(x=z, y=y, hue=x, data=df, palette=sns.color_palette("Set1", anz))
    
    plt.xlim(df[list_columns_zeitraum[int(datetime_column)]].iloc[0], df[list_columns_zeitraum[int(datetime_column)]].iloc[-1])

    plt.show()


#######################################################################
###Group Plot (show a plot by group with Tolerance)
def groupplot_w_T(df):
    clear()
    sns.set(style="ticks")

    
    kategorie=df.select_dtypes(exclude=['float'])
    werte = df.select_dtypes(exclude=['object'])
    zeitraum=df.select_dtypes(exclude=['float'])
    
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
    
    anz_col_zeitraum = len(zeitraum.columns)
        
    list_columns_zeitraum = []
    list_number = []
    i=1
    for i in range(anz_col_zeitraum):
        list_columns_zeitraum.append(zeitraum.columns[i])
        list_number.append(str(i))
        print(i, zeitraum.columns[i])
        i+=1
    
    while True:
        datetime_column = input('Choose the X-axis-column \n(choose number) \n?')
        if datetime_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    z = list_columns_zeitraum[int(datetime_column)]
    
    df = df.sort_values(by=z, ascending=1)
    
    
    
    
    anz = df[x].nunique()    
    
    
    while True:
        one_two_sided = input('Tolerance: \n1: both side tolerance \n2: one side ut \n3: one side lt \n(choose number) \n?')
        nummer = [1,2,3]
        if int(one_two_sided) in nummer:
            break
        else:
            print('Wrong input, please try again')
    
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
    
    
    
    
        sns.relplot(x=z, y=y, hue=x, data=df, palette=sns.color_palette("Set1", anz))
        plt.axhline(y=ut,linewidth=2, color='r')
        
        plt.axhline(y=lt,linewidth=2, color='r')       
        plt.xlim(df[list_columns_zeitraum[int(datetime_column)]].iloc[0], df[list_columns_zeitraum[int(datetime_column)]].iloc[-1])
    
        plt.show()

    ###one side tolerance ut
    elif one_two_sided =='2':
        
        
        while True:
            ut = input('Upper tolerance: \n(choose point-comma) \n?')
    
            if not isfloat(ut):
                print("target mean value is not a number with point-comma, please try again")
            else:
                break
        
        
        ut = float(ut)
        lt = 'none'
        
        sns.relplot(x=z, y=y, hue=x, data=df, palette=sns.color_palette("Set1", anz))
        plt.axhline(y=ut,linewidth=2, color='r')
        plt.xlim(df[list_columns_zeitraum[int(datetime_column)]].iloc[0], df[list_columns_zeitraum[int(datetime_column)]].iloc[-1])
    
        plt.show()
        
    ###one side tolerance lt
    elif one_two_sided =='3':
        
        while True:
            lt = input('Lower tolerance: \n(choose point-comma) \n?')
    
            if not isfloat(lt):
                print("target mean value is not a number with point-comma, please try again")
            else:
                break
        
        
        
        
        ut = 'none'
        lt = float(lt)
        
        sns.relplot(x=z, y=y, hue=x, data=df, palette=sns.color_palette("Set1", anz))
        plt.axhline(y=lt,linewidth=2, color='r')
        plt.xlim(df[list_columns_zeitraum[int(datetime_column)]].iloc[0], df[list_columns_zeitraum[int(datetime_column)]].iloc[-1])
        
        plt.show()

def groupplot_menu(df):
    
    clear()
    gp_menu = input('Which kind of Groupplot: \n1: Groupplot \n2: Groupplot with Toleranceline \n?')
    
    if gp_menu == '1':
        groupplot(df)
    elif gp_menu == '2':
        groupplot_w_T(df)
    else:
        print('wrong input (choose number), try again!')


###Init pareto
######################################################################
###Thanks to https://tylermarrs.com/posts/pareto-plot-with-matplotlib/
#####################################################################
def pareto_plot(df, x=None, y=None, title=None, show_pct_y=False, pct_format='{0:.0%}'):
    xlabel = x
    ylabel = y
    tmp = df.sort_values(y, ascending=False)
    x = tmp[x].values
    y = tmp[y].values
    weights = y / y.sum()
    cumsum = weights.cumsum()
    
    fig, ax1 = plt.subplots()
    ax1.bar(x, y)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)

    ax2 = ax1.twinx()
    ax2.plot(x, cumsum, '-ro', alpha=0.5)
    ax2.set_ylabel('', color='r')
    ax2.tick_params('y', colors='r')
    
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['{:,.2%}'.format(x) for x in vals])

    # hide y-labels on right side
    if not show_pct_y:
        ax2.set_yticks([])
    
    formatted_weights = [pct_format.format(x) for x in cumsum]
    for i, txt in enumerate(formatted_weights):
        ax2.annotate(txt, (x[i], cumsum[i]), fontweight='heavy')    
    
    if title:
        plt.title(title)
    
    plt.tight_layout()
    plt.show()


#######################################################################    
###pareto plot with count column
def pareto(df):
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number = []
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
    
    df = df.groupby([x])[y].sum()
    df = df.reset_index()
    df= df.sort_values(y, ascending=False)
    df[x]=df[x].astype(str)
    
    print(df)
    pareto_plot(df, x=x, y=y, title='Pareto Chart')

#######################################################################
###single pareto plot, count the entrees of column    
def pareto_one_column(df):
    
    clear()
    
    werte = df.select_dtypes(exclude=['float'])
    
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
    
    y = list_columns_werte[int(value_column)]
    
    
    
    df2 = df[y].value_counts()
    df2 = df2.reset_index()
    x = 'index'
    
    df2= df2.sort_values([y], ascending=False)
    df2[x]=df2[x].astype(str)
    
    
    print(df2)
    pareto_plot(df2, x=x, y=y, title='Pareto Chart')


def three_d_scatterplot(df):
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
    
    while True:
        value_column_z= input('z-value: \n(choose number) \n?')
        if value_column_z not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
        
    y = df[list_columns_werte[int(value_column_y)]]
    
    x = df[list_columns_werte[int(value_column_x)]]
    
    z = df[list_columns_werte[int(value_column_z)]]

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    
    ax.scatter3D(x, y, z, c=z, cmap='hsv');
    
    plt.show()

    
def trisurfaceplot(df):
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
    
    while True:
        value_column_z= input('z-value: \n(choose number) \n?')
        if value_column_z not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
        
    y = df[list_columns_werte[int(value_column_y)]]
    
    x = df[list_columns_werte[int(value_column_x)]]
    
    z = df[list_columns_werte[int(value_column_z)]]

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    
    ax.plot_trisurf(x, y, z, linewidth=0, antialiased=False)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    plt.show()

def threeddplot(df):
    
    tdplot = input('Choose 3d-Plot: \n1: 3d-scatter-plot \n2: 3d-surface-plot \n?')
    
    if tdplot == '1':
        three_d_scatterplot(df)
    elif tdplot == '2':
        trisurfaceplot(df)
    else:
        print('wrong input, please try again')
