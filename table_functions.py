#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 08:17:57 2020

@author: blaubaer
"""
import pandas as pd
import os

#Thanks to https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file

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
    
    csv_dateien= []
    for dat in os.listdir(os.getcwd()):
        if dat.endswith(".csv") or dat.endswith(".CSV"):
            csv_dateien.append(dat)
            print(dat)
    
    add_table = input('Which table would yo like to add\n(pay attention to spelling)\n?' )
    
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
    
        
        
        
        
            
    




