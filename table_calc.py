#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:53:53 2020

@author: blaubaer (Ricky Helfgen)
"""

import pandas as pd
import numpy as np

from mft import isfloat, clear
from tableview import file_in_html
from mft import save_CSV_new, save_CSV


#######################################################################
###addition column
def addition_column(fn, df):
    print('Column addition:')
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column1: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        value_column2= input('Column2: \n(choose number)\n?')
        if value_column2 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    col1 = list_columns_werte[int(value_column1)]
    col2 = list_columns_werte[int(value_column2)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] + df[col2]
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)  
 
#######################################################################
###addition column, value
def addition_val(fn, df):
    print('Column addition with value:')
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    while True:
            value_col = input('Value: \n(choose point-comma) \n?')
    
            if not isfloat(value_col):
                print("target value is not a number with point-comma, please try again")
            else:
                break
    
    col1 = list_columns_werte[int(value_column1)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] + float(value_col)
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df) 





#######################################################################         
###substraction column          
def substraction_column(fn, df):
    print('Column substraction:')    
    
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column1: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        value_column2= input('Column2: \n(choose number)\n?')
        if value_column2 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    col1 = list_columns_werte[int(value_column1)]
    col2 = list_columns_werte[int(value_column2)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] - df[col2]
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)



#######################################################################
###substraction column, val
def substraction_val(fn, df):
    print('Column substraction with value:')
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    while True:
            value_col = input('Value: \n(choose point-comma) \n?')
    
            if not isfloat(value_col):
                print("target value is not a number with point-comma, please try again")
            else:
                break
    
    col1 = list_columns_werte[int(value_column1)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] - float(value_col)
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)



#######################################################################    
###multiplication column        
def multiplication_column(fn, df):
    print('Column multiplication:')

    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column1: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        value_column2= input('Column2: \n(choose number)\n?')
        if value_column2 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    col1 = list_columns_werte[int(value_column1)]
    col2 = list_columns_werte[int(value_column2)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] * df[col2]
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)


#######################################################################
###multiplicate column, value
def multiplication_val(fn, df):
    print('Column multiplication with value:')
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    while True:
            value_col = input('Value: \n(choose point-comma) \n?')
    
            if not isfloat(value_col):
                print("target value is not a number with point-comma, please try again")
            else:
                break
    
    col1 = list_columns_werte[int(value_column1)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] * float(value_col)
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)
    






#######################################################################
### diffision column        
def diffision_column(fn, df):
    print('Column diffision:')        

    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column1: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        value_column2= input('Column2: \n(choose number)\n?')
        if value_column2 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    col1 = list_columns_werte[int(value_column1)]
    col2 = list_columns_werte[int(value_column2)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] / df[col2]
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)

#######################################################################
###diffision column, value
def diffision_val(fn, df):
    print('Column diffision with value:')
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    while True:
            value_col = input('Value: \n(choose point-comma) \n?')
    
            if not isfloat(value_col):
                print("target value is not a number with point-comma, please try again")
            else:
                break
    
    col1 = list_columns_werte[int(value_column1)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] / float(value_col)
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)   


#######################################################################
###square column
def square_val(fn, df):
    print('Square Column values:')
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    
    col1 = list_columns_werte[int(value_column1)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[col1] **2
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)      


#######################################################################
###square column
def take_root_val(fn, df):
    print('Take root Column values:')
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    
    col1 = list_columns_werte[int(value_column1)]
    
    
    name_col = input('New column "Name": \n?')
    
    df[name_col] = df[[col1]].apply(np.sqrt, axis=1)
    
    #np.sqrt(football[['wins', 'losses']].sum(axis=1))
    
    print(df)
    file_in_html(fn, df)
    save_CSV(fn, df)    


#######################################################################
###statistic cross column
def statistic_cross_col(fn, df):
    print('Described Statistic cross the choosed column:')
    print('#'*50)    
    
    #werte = df.select_dtypes(include=['int', 'float'])
    
    #
    anz_col_werte = len(df.columns)
        
    list_columns_werte = []
    list_number = []
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(df.columns[i])
        list_number.append(str(i))
        print(i, df.columns[i])
        i+=1
    
    
    while True:
        value_column1= input('Column: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    
    col1 = list_columns_werte[int(value_column1)]
    
    df2 = pd.DataFrame()
    
    df2 = df[col1].describe()
        
    
    
    
    
    print(df2)
    
    df2.to_csv('described.csv', sep=';', decimal=',', header =True)  
    
    df3=pd.read_csv('described.csv',sep=';' ,decimal=',', header=1)
    df3.columns=['Stat Function', 'Value']
    print(df3)
    file_in_html(fn, df3)
    
    save_yes = input('Would you like to save this statistic table view as "CSV-File": \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df2.to_csv(fn, sep=';', decimal=',', header =True)      






######################################################################
#statistic functions
######################################################################
###min column
def min_column(fn, df):
    print('MIN of columns:')        

    print('#'*50)    
    
    count_col = input('With how many columns do you would like to calculate? \n(choose number: possible 2-5) \n?')      
          
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
    
####################################################################    
###2 columns    
    if count_col =='2':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
    
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2]].apply(np.min, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###3 columns
        
    if count_col =='3':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3]].apply(np.min, axis=1)
    
        print(df)
        file_in_html(fn, df)

####################################################################
###4 columns
        
    if count_col =='4':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4]].apply(np.min, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###5 columns
        
    if count_col =='5':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column5= input('Column5: \n(choose number)\n?')
            if value_column5 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        col5 = list_columns_werte[int(value_column5)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4,col5]].apply(np.min, axis=1)
    
        print(df)
        file_in_html(fn, df)
        
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    
    save_CSV(fn, df)
    

######################################################################
###max column
def max_column(fn, df):
    print('MAX of columns:')        

    print('#'*50)    
    
    count_col = input('With how many columns do you would like to calculate? \n(choose number: possible 2-5) \n?')      
          
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
    
####################################################################    
###2 columns    
    if count_col =='2':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
    
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2]].apply(np.max, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###3 columns
        
    if count_col =='3':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3]].apply(np.max, axis=1)
    
        print(df)
        file_in_html(fn, df)

####################################################################
###4 columns
        
    if count_col =='4':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4]].apply(np.max, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###5 columns
        
    if count_col =='5':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column5= input('Column5: \n(choose number)\n?')
            if value_column5 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        col5 = list_columns_werte[int(value_column5)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4,col5]].apply(np.max, axis=1)
    
        print(df)
        file_in_html(fn, df)
        
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    save_CSV(fn, df)

######################################################################
###mean column
def mean_column(fn, df):
    print('Mean of columns:')        

    print('#'*50)    
    
    count_col = input('With how many columns do you would like to calculate? \n(choose number: possible 2-5) \n?')      
          
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
    
####################################################################    
###2 columns    
    if count_col =='2':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
    
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2]].apply(np.mean, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###3 columns
        
    if count_col =='3':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3]].apply(np.mean, axis=1)
    
        print(df)
        file_in_html(fn, df)

####################################################################
###4 columns
        
    if count_col =='4':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4]].apply(np.mean, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###5 columns
        
    if count_col =='5':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column5= input('Column5: \n(choose number)\n?')
            if value_column5 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        col5 = list_columns_werte[int(value_column5)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4,col5]].apply(np.mean, axis=1)
    
        print(df)
        file_in_html(fn, df)
        
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    save_CSV(fn, df)

######################################################################
###std column
def std_column(fn, df):
    print('Deviation of columns:')        

    print('#'*50)    
    
    count_col = input('With how many columns do you would like to calculate? \n(choose number: possible 2-5) \n?')      
          
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
    
####################################################################    
###2 columns    
    if count_col =='2':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
    
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2]].apply(np.std, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###3 columns
        
    if count_col =='3':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3]].apply(np.std, axis=1)
    
        print(df)
        file_in_html(fn, df)

####################################################################
###4 columns
        
    if count_col =='4':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4]].apply(np.std, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###5 columns
        
    if count_col =='5':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column5= input('Column5: \n(choose number)\n?')
            if value_column5 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        col5 = list_columns_werte[int(value_column5)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4,col5]].apply(np.std, axis=1)
    
        print(df)
        file_in_html(fn, df)
        
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    save_CSV(fn, df)


######################################################################
###range column
def range_column(fn, df):
    print('Range of columns:')        

    print('#'*50)    
    
    count_col = input('With how many columns do you would like to calculate? \n(choose number: possible 2-5) \n?')      
          
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
    
####################################################################    
###2 columns    
    if count_col =='2':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
    
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2]].apply(np.max, axis=1)-df[[col1,col2]].apply(np.min, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###3 columns
        
    if count_col =='3':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
    
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3]].apply(np.max, axis=1)-df[[col1,col2,col3]].apply(np.min, axis=1)
    
        print(df)
        file_in_html(fn, df)

####################################################################
###4 columns
        
    if count_col =='4':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4]].apply(np.max, axis=1)-df[[col1,col2,col3,col4]].apply(np.min, axis=1)
    
        print(df)
        file_in_html(fn, df)
    
####################################################################
###5 columns
        
    if count_col =='5':
        while True:
            value_column1= input('Column1: \n(choose number)\n?')
            if value_column1 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        while True:
            value_column2= input('Column2: \n(choose number)\n?')
            if value_column2 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column3= input('Column3: \n(choose number)\n?')
            if value_column3 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        
        while True:
            value_column4= input('Column4: \n(choose number)\n?')
            if value_column4 not in list_number:
                print('wrong input, try again!')
            else:
                break  
        
        while True:
            value_column5= input('Column5: \n(choose number)\n?')
            if value_column5 not in list_number:
                print('wrong input, try again!')
            else:
                break  
    
        col1 = list_columns_werte[int(value_column1)]
        col2 = list_columns_werte[int(value_column2)]
        col3 = list_columns_werte[int(value_column3)]
        col4 = list_columns_werte[int(value_column4)]
        col5 = list_columns_werte[int(value_column5)]
        
        name_col = input('New column "Name": \n?')
    
        df[name_col] = df[[col1,col2,col3,col4,col5]].apply(np.max, axis=1)-df[[col1,col2,col3,col4,col5]].apply(np.min, axis=1)
    
        print(df)
        #file_in_html(df)
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    save_CSV(fn, df)

    
#####################################################################    
###menu calculate with columns   
    
def menu_calc_column(fn, df):
    clear()
    
    print('Easy column calculation \nthis tool add columns with requested column calculations')
    calc_liste = ['addition', 'substraction', 'multiplication', 'diffusion', 'minimum', 'maximum', 'mean', 'deviation', 'range']
    for i in range(len(calc_liste)):
        print(i, calc_liste[i])
        i+=1
    calc = input('Which calculation: \n(choose a number) \n?')
    
    if calc =='0':
        addition_column(fn, df)
    if calc =='1':
        substraction_column(fn, df)
    if calc =='2':
        multiplication_column(fn, df)
    if calc =='3':
        diffision_column(fn, df)
    if calc =='4':
        #print('not available')
        min_column(fn, df)
    if calc =='5':
        #print('not available')
        max_column(fn, df)
    if calc =='6':
        #print('not available')
        mean_column(fn, df)
    if calc =='7':
        #print('not available')
        std_column(fn, df)
    if calc =='8':
        #print('not available')
        range_column(fn, df)
    else:
        print('Wrong input, please try again')


def menu_calc_col_val(fn, df):
    clear()
    
    print('Easy calculation column with value \nthis tool add columns with requested column calculations')
    calc_liste = ['addition', 'substraction', 'multiplication', 'diffusion', 'square', 'extract a root']
    for i in range(len(calc_liste)):
        print(i, calc_liste[i])
        i+=1
    calc = input('Which calculation: \n(choose a number) \n?')
    
    if calc =='0':
        addition_val(fn, df)
    if calc =='1':
        substraction_val(fn, df)
    if calc =='2':
        multiplication_val(fn, df)
    if calc =='3':
        diffision_val(fn, df)
    if calc =='4':
        
        square_val(fn, df)
    if calc =='5':
        
        take_root_val(fn, df)
    
    else:
        print('Wrong input, please try again')

###############################################################################
##statistic functions
###############################################################################

def count__column(df, col1):
    
    
    count_c = df[col1].count()
    
    print('Count:', count_c)


def sum__column(df, col1):
    
    sum_c = df[col1].sum()
    
    print('SUM:', sum_c)


def mean__column(df, col1):
    
    
    mean_c = df[col1].mean()
    
    print('Mean:', mean_c)

def min__column(df, col1):
    
    min_c = df[col1].min()
    
    print('MIN:', min_c)
    
    
def max__column(df, col1):
    
    max_c = df[col1].max()
    
    print('MAX:', max_c)


def range__column(df, col1):
    
    max_c = df[col1].max()
    min_c = df[col1].min()
    range_c = max_c-min_c
    
    
    print('Range:', range_c)

def std__column(df, col1):
    
    
    std_c = df[col1].std()
    
    print('Standard Deviation:', std_c)



def quantile__column(df, col1):
    
    
    
    while True:
        quantile_value = input('Percent Probability (0.x-100): \n?')
        quantile_value = float(quantile_value)
        
        if not isfloat(quantile_value):
            print("Percent Probability has to be number with point-comma, please try again")
        else:
            if quantile_value < 0:
                print('Percent Probability has to be bigger "0"')
            elif quantile_value > 100:
                print('Percent Probability has to be less "100"')
            else:
                break
        
    
    
    q_value = quantile_value / 100
    
    quantile_c = df[col1].quantile(q_value)
    
    print(quantile_value,'%-Quantil:', quantile_c)




    
def menu_stat_column(fn, df):
    
    
    
    print('#'*50)    
    
    werte = df.select_dtypes(exclude=['object', 'datetime' , 'category'])
    
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
        value_column1= input('Column1: \n(choose number)\n?')
        if value_column1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    col1 = list_columns_werte[int(value_column1)]
    
    while True:
    
        menu_stat = input('Statistic functions: \n1: Count column \n2: SUM column \n3: Mean column \n4: MIN column \n5: MAX column \n6: Range column \n7: STD column \n8: Quantile column \n?')
        if menu_stat =='1':
            count__column(df, col1)
        elif menu_stat =='2':
            sum__column(df, col1)
        elif menu_stat =='3':
            mean__column(df, col1)
        elif menu_stat =='4':
            min__column(df, col1)
        elif menu_stat =='5':
            max__column(df, col1)
        elif menu_stat =='6':
            range__column(df, col1)
        elif menu_stat =='7':
            std__column(df, col1)
        elif menu_stat == '8':
            quantile__column(df, col1)
        else:
            print('Wrong Input, please try again')
        
        restart = input('\nFurther column calculation: "y"\n?')
        if restart.lower() != 'y':
            break

    

def menu_calc(fn, df):
    menu_c = input('How to calculate? \n1: calculation between 2 chosen columns \n2: calculation with chosen column and input value \n3: described statistics cross chosen column \n4: statistic funktions due to chosen column \n(choose nr.) \n?')
    if menu_c == '1':
        menu_calc_column(fn, df)
    elif menu_c == '2':
        menu_calc_col_val(fn, df)
    elif menu_c == '3':
        statistic_cross_col(fn, df)
    elif menu_c =='4':
        menu_stat_column(fn, df)
    else:
        print('Wrong input, please try again!')
    
