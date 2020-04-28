#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 08:17:57 2020

@author: blaubaer (Ricky Helfgen)
"""
import pandas as pd
import os

#Thanks to https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
#and https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
### define our clear function 
#############################################################################
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 



def appendDFToCSV(df, sep=","):
    
    while True:
        csv_dateien= []
        for dat in os.listdir(os.getcwd()):
            if dat.endswith(".csv") or dat.endswith(".CSV"):
                csv_dateien.append(dat)
                print(dat)
        
        add_table = input('Which table would yo like to add\n(pay attention to spelling)\n?' )
        if add_table in csv_dateien:
            break
        else:
            print('Wrong input, try again')
        
    
    
    clear()
    f = open(add_table, "r")
    
    print('#'*80)
    print('Preview to the first 2 lines: \n')
    print('first line:', f.readline())
    print('second line:', f.readline())
    print('#'*80)
    f.close
    
    #define structure
    while True:
        format_ist = input('Which separator is used by the file: \n1: Comma / 2: Semicolon \n(choose number)\n?').lower()
        if format_ist == '1':
            trennzeichen = ','
            break
        elif format_ist == '2':
            trennzeichen = ';'
            break
        else:
            print('Wrong input, please try again')
        #file_einlesen(auswahl_datei)
    
    
    
    if len(df.columns) != len(pd.read_csv(add_table, nrows=1, sep=trennzeichen).columns):
        print("Columns do not match!! Dataframe has " + str(len(df.columns)) + " columns. CSV file has " + str(len(pd.read_csv(add_table, nrows=1, sep=trennzeichen).columns)) + " columns.")            
        print('please try again!')
        
        #raise Exception("Columns do not match!! Dataframe has " + str(len(df.columns)) + " columns. CSV file has " + str(len(pd.read_csv(add_table, nrows=1, sep=trennzeichen).columns)) + " columns.")
    elif not (df.columns == pd.read_csv(add_table, nrows=1, sep=trennzeichen).columns).all():
        print("Columns and column order of dataframe and csv file do not match!!")
        print('please try again!')
        #raise Exception("Columns and column order of dataframe and csv file do not match!!")
    else:
        df2=pd.read_csv(add_table,sep=trennzeichen)
        df = df.append(df2)
        print(df)
        print('To work with you have to save this dataframe as file')
        save_yes = input('Would you like to save: \ny/n \n?')
        if save_yes.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                df.to_csv(fn, sep=';', decimal=',', header =True)
    
        
def mergecolumn(df):
    
    while True:
        csv_dateien= []
        for dat in os.listdir(os.getcwd()):
            if dat.endswith(".csv") or dat.endswith(".CSV"):
                csv_dateien.append(dat)
                print(dat)
        
        add_table = input('Which csv-file would yo like to merge\n(pay attention to spelling)\n?' )
        if add_table in csv_dateien:
            break
        else:
            print('wrong input, try again')
    
    clear()
    f = open(add_table, "r")
    
    print('#'*80)
    print('Preview to the first 2 lines: \n')
    print('first line:', f.readline())
    print('second line:', f.readline())
    print('#'*80)
    f.close
    
    #define structure
    while True:
        format_ist = input('Which separator is used by the file: \n1: Comma / 2: Semicolon \n(choose number)\n?').lower()
        if format_ist == '1':
            trennzeichen = ','
            break
        elif format_ist == '2':
            trennzeichen = ';'
            break
        else:
            print('Wrong input, please try again')
        #file_einlesen(auswahl_datei)
    
    df2=pd.read_csv(add_table,sep=trennzeichen)
    
    join_how = input('How would you like to join: \n1: full outer join \n2: full inner join \n3: inner join left \n4: inner join right \n(choose number) \n?')
    
    key_field = df.select_dtypes(exclude=['float'])
    
    #
    anz_col_key = len(key_field.columns)
        
    list_columns_key = []

    i=1
    for i in range(anz_col_key):
        list_columns_key.append(key_field.columns[i])
        print(i, key_field.columns[i])
        i+=1
    
    key_column= input('Key Field: \n(choose number) \n?')
    
    key_name = list_columns_key[int(key_column)]    
    
    if join_how == '1':
        result = pd.merge(df, df2, how='outer', on=key_name)
        print(result)
        print('To work with you have to save this dataframe as file')
        save_yes = input('Would you like to save: \ny/n \n?')
        if save_yes.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                result.to_csv(fn, sep=';', decimal=',', header =True)
    elif join_how == '2':
        result = pd.merge(df, df2, how='inner', on =key_name)
        print(result)
        print('To work with you have to save this dataframe as file')
        save_yes = input('Would you like to save: \ny/n \n?')
        if save_yes.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                result.to_csv(fn, sep=';', decimal=',', header =True)
    elif join_how =='3':
        result = pd.merge(df, df2, how='left', on=key_name)
        print(result)
        print('To work with you have to save this dataframe as file')
        save_yes = input('Would you like to save: \ny/n \n?')
        if save_yes.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                result.to_csv(fn, sep=';', decimal=',', header =True)
    elif join_how =='4':
        result = pd.merge(df, df2, how='right', on=key_name)
        print(result)
        print('To work with you have to save this dataframe as file')
        save_yes = input('Would you like to save: \ny/n \n?')
        if save_yes.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                result.to_csv(fn, sep=';', decimal=',', header =True)
    else:
        print('Wrong input, please try again')


################################################################################
##set filter
def filter_setzen(df):
    clear()
    while True:
        clear()
        anz_col = len(df.columns)
        
        list_columns = []

        i=1
        for i in range(anz_col):
            
            list_columns.append(df.columns[i])
            print(i, df.columns[i])
            i+=1      
                     
        inhalte_spalte= input('For which column you want to know the possible filter criteria \nchoose number! \n?')
        print(df.iloc[:,int(inhalte_spalte)].value_counts())
        
        filter_ja = input('Set a filter: y/n \n?')
        if filter_ja.lower() =='y':
            name_filter=input('Input Name/Value of the filter criteria(Pay attention to upper and lower case): \n?')
            df = df[df.iloc[:,int(inhalte_spalte)]==name_filter]
            
        restart = input('\nSet more filters: y/n \n?')
        if restart.lower() != 'y':
            speichern_ja = input('Save the table with the filters set (the only way to analyze with the filter set): y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                df.to_csv(fn, sep=';', decimal=',', header =True)
                
            
            tabelle_m_f_uebernehmen = input('The filters should be available for further analysis: y/n \n?')
            if tabelle_m_f_uebernehmen.lower() =='y':
            
                return(df)
                break
            else:
                break


def sort_column(df):
    ###sort by column
    ###################################################################################
    sort_yes = input('Would you like to sort the data frame: y/n\n?')
    if sort_yes =='y':
        while True:
            clear()
            anz_col = len(df.columns)

            list_columns = []

            i=1
            for i in range(anz_col):
    
                list_columns.append(df.columns[i])
                print(i, df.columns[i])
                i+=1      
             
            sort_column= input('Sort to which column: \n?')
            s_col = list_columns[int(sort_column)]
            
            while True:
                ascent_true_false = input('Ascending: \n1: true \n2: false \n?')
                if ascent_true_false =='1':
                    a_t_f = 1
                    break
                if ascent_true_false =='2':
                    a_t_f = 0
                    break
                else:
                    print('wrong input, try again')
            
            df = df.sort_values(by=s_col, ascending=a_t_f)
            
            restart_s = input('additional sorting: y/n \n?')
            if restart_s.lower() != 'y':
                speichern_ja = input('Save the table with the sorting (the only way to analyze with the filter set): y/n \n?')
                if speichern_ja.lower() =='y':
                    csvfilename = input('Filename (.csv will save automaticly) \n?')
                    fn = csvfilename + '.csv'
                    df.to_csv(fn, sep=';', decimal=',', header =True)
                return(df)   
                
                break
                   
    