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


#######################################################################
###addition column
def addition_column(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      
 
#######################################################################
###addition column, value
def addition_val(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      





#######################################################################         
###substraction column          
def substraction_column(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)



#######################################################################
###substraction column, val
def substraction_val(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      




#######################################################################    
###multiplication column        
def multiplication_column(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)


#######################################################################
###multiplicate column, value
def multiplication_val(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      







#######################################################################
### diffision column        
def diffision_column(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)
    

#######################################################################
###diffision column, value
def diffision_val(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      


#######################################################################
###square column
def square_val(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      


#######################################################################
###square column
def take_root_val(df):
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
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      


#######################################################################
###statistic cross column
def statistic_cross_col(df):
    print('Statistic cross column:')
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
    
    df2 = pd.DataFrame()
    
    df2 = df[col1].describe()
        
    
    
    #np.sqrt(football[['wins', 'losses']].sum(axis=1))
    
    print(df2)
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df2.to_csv(fn, sep=';', decimal=',', header =True)      






######################################################################
#statistic functions
######################################################################
###min column
def min_column(df):
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
        file_in_html(df)
    
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
        file_in_html(df)

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
        file_in_html(df)
    
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
        file_in_html(df)
        
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)
    

######################################################################
###max column
def max_column(df):
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
        file_in_html(df)
    
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
        file_in_html(df)

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
        file_in_html(df)
    
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
        file_in_html(df)
        
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)

######################################################################
###mean column
def mean_column(df):
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
        file_in_html(df)
    
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
        file_in_html(df)

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
        file_in_html(df)
    
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
        file_in_html(df)
        
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)


######################################################################
###std column
def std_column(df):
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
        file_in_html(df)
    
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
        file_in_html(df)

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
        file_in_html(df)
    
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
        file_in_html(df)
        
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)


######################################################################
###range column
def range_column(df):
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
        file_in_html(df)
    
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
        file_in_html(df)

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
        file_in_html(df)
    
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
        file_in_html(df)
    else:
        print('Wrong Input (Choose Number between 2-5)')
    
    
    
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)

    
#####################################################################    
###menu calculate with columns   
    
def menu_calc_column(df):
    clear()
    
    print('Easy column calculation \nthis tool add columns with requested column calculations')
    calc_liste = ['addition', 'substraction', 'multiplication', 'diffision', 'mininmum', 'maximum', 'mean', 'deviation', 'range']
    for i in range(len(calc_liste)):
        print(i, calc_liste[i])
        i+=1
    calc = input('Which calculation: \n(choose a number) \n?')
    
    if calc =='0':
        addition_column(df)
    if calc =='1':
        substraction_column(df)
    if calc =='2':
        multiplication_column(df)
    if calc =='3':
        diffision_column(df)
    if calc =='4':
        #print('not available')
        min_column(df)
    if calc =='5':
        #print('not available')
        max_column(df)
    if calc =='6':
        #print('not available')
        mean_column(df)
    if calc =='7':
        #print('not available')
        std_column(df)
    if calc =='8':
        #print('not available')
        range_column(df)
    else:
        print('Wrong input, please try again')


def menu_calc_col_val(df):
    clear()
    
    print('Easy calculation column with value \nthis tool add columns with requested column calculations')
    calc_liste = ['addition', 'substraction', 'multiplication', 'diffision', 'square', 'extract a root']
    for i in range(len(calc_liste)):
        print(i, calc_liste[i])
        i+=1
    calc = input('Which calculation: \n(choose a number) \n?')
    
    if calc =='0':
        addition_val(df)
    if calc =='1':
        substraction_val(df)
    if calc =='2':
        multiplication_val(df)
    if calc =='3':
        diffision_val(df)
    if calc =='4':
        #print('not available')
        square_val(df)
    if calc =='5':
        #print('not available')
        take_root_val(df)
    
    else:
        print('Wrong input, please try again')
    


def menu_calc(df):
    menu_c = input('How to calculate? \n1: calculation between columns \n2: calculation within column \n3: statistic cross the column \n(choose nr.) \n?')
    if menu_c == '1':
        menu_calc_column(df)
    elif menu_c == '2':
        menu_calc_col_val(df)
    elif menu_c == '3':
        statistic_cross_col(df)
    else:
        print('Wrong input, please try again!')
    
