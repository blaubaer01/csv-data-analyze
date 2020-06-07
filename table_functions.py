#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 08:17:57 2020

@author: blaubaer (Ricky Helfgen)
"""
import pandas as pd
import os
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
#import scipy as spy
from scipy.stats import chi2_contingency
from tableview import file_in_html
from mft import clear, truncate

#Thanks to https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
#and https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
### define our clear function 
#############################################################################

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
        file_in_html(df)
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
    list_number =[]
    i=1
    for i in range(anz_col_key):
        list_columns_key.append(key_field.columns[i])
        list_number.append(str(i))
        print(i, key_field.columns[i])
        i+=1
    
    while True:
        key_column= input('Key Field: \n(choose number) \n?')
        if key_column not in list_number:
            print('wrong input, try again!')
        else:
            break 
    
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
        crit = df.select_dtypes(exclude=['float','int'])
            
            
        anz_col = len(crit.columns)

        list_columns = []

        i=1
        for i in range(anz_col):

            list_columns.append(crit.columns[i])
            print(i, crit.columns[i])
            i+=1      
        inhalte_spalte= input('For which column you want to know the possible filter criteria \nchoose number! \n?')
        print(crit.iloc[:,int(inhalte_spalte)].value_counts())
        
        filter_ja = input('Set a filter: y/n \n?')
        if filter_ja.lower() =='y':
            name_filter=input('Input Name/Value of the filter criteria(Pay attention to upper and lower case): \n?')
            df = df[crit.iloc[:,int(inhalte_spalte)]==name_filter]
            
            
        restart = input('\nSet more filters: y/n \n?')
        if restart.lower() != 'y':
            
            speichern_ja = input('Save the table with the filters set (the only way to analyze with the filter set): y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                df.to_csv(fn, sep=';', decimal=',', header =True)
            
            else:
                break
    


def set_value_filter(df):
    
    clear()
    while True:
        clear()
        crit = df.select_dtypes(exclude=['object'])
            
            
        anz_col = len(crit.columns)

        list_columns = []

        i=1
        for i in range(anz_col):

            list_columns.append(crit.columns[i])
            print(i, crit.columns[i])
            i+=1      
        inhalte_spalte= input('For which column you want to know the possible filter criteria \nchoose number! \n?')
        print(crit.iloc[:,int(inhalte_spalte)].value_counts())
        
        filter_ja = input('Set a filter: y/n \n?')
        if filter_ja.lower() =='y':
            name_filter=input('Input Name/Value of the filter criteria(Pay attention to upper and lower case): \n?')
            df = df[crit.iloc[:,int(inhalte_spalte)]==name_filter]
            
            
        restart = input('\nSet more filters: y/n \n?')
        if restart.lower() != 'y':
            
            speichern_ja = input('Save the table with the filters set (the only way to analyze with the filter set): y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                df.to_csv(fn, sep=';', decimal=',', header =True)
            
            else:
                break
    










###sort by column
###################################################################################
def sort_column(df):
    sort_yes = input('Would you like to sort the data frame: y/n\n?')
    if sort_yes =='y':
        while True:
            clear()
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
                sort_column= input('Sort to which column: \n?')
                if sort_column not in list_number:
                    print('wrong input, try again!')
                else:
                    break 
    
            
            
            
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
                file_in_html(df)
                return(df)   
                
                break

###transposed               
###############################################################################
def transposed_table(df):
    clear()
    trans_yes = input('Would you like to transpose the table: y/n\n?')
    if trans_yes =='y':
        df = df.T
        speichern_ja = input('Save the table with the sorting (the only way to analyze with the filter set): y/n \n?')
        if speichern_ja.lower() =='y':
            csvfilename = input('Filename (.csv will save automaticly) \n?')
            fn = csvfilename + '.csv'
            df.to_csv(fn, sep=';', decimal=',', header =True)
        file_in_html(df)
        return(df)
    else:
        file_in_html(df)
        return(df)

###crosstab
###############################################################################
def crosstab(df):
    clear()
    tab = df.select_dtypes(exclude=['float'])
    
    #
    anz_col_werte = len(tab.columns)
        
    list_columns_tab = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_tab.append(tab.columns[i])
        list_number.append(str(i))
        print(i, tab.columns[i])
        i+=1
    
    
    while True:
        tab1_column= input('Which column do you want to cross: \n(choose number) \n?')
        if tab1_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    tab1 = list_columns_tab[int(tab1_column)]
    
    
    while True:
        tab2_column= input('Which column do you want to cross: \n(choose number) \n?')
        if tab2_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
        
    tab2 = list_columns_tab[int(tab2_column)]
    
    which_table = input('1: sum -table \n2: percent -table \n(Choose number) \n?')
    
    if which_table =='1':
        
        with_sum = input('Crosstab with "Total": y/n \n?')
        
        if with_sum =='y':
            ctv=pd.crosstab(index=df[tab1], columns=df[tab2], margins=True)
            print(ctv)    
            speichern_ja = input('Save the crosstable: y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                ctv.to_csv(fn, sep=';', decimal=',', header =True)
        else:
            ctcalc = pd.crosstab(index=df[tab1], columns=df[tab2])
            print(ctcalc)
            speichern_ja = input('Save the crosstable: y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                ctcalc.to_csv(fn, sep=';', decimal=',', header =True)
    
    elif which_table =='2':
        
        with_sum = input('Crosstab with "Total": y/n \n?')
        
        if with_sum =='y':
            ct = pd.crosstab(index=df[tab1], columns=df[tab2], margins=True).applymap(lambda r: r/len(df))
            print(ct)    
            speichern_ja = input('Save the crosstable: y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                ct.to_csv(fn, sep=';', decimal=',', header =True)
        else:
            ct = pd.crosstab(index=df[tab1], columns=df[tab2], margins=False).applymap(lambda r: r/len(df))
            print(ct)
            speichern_ja = input('Save the crosstable: y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                ct.to_csv(fn, sep=';', decimal=',', header =True)

    else:
        print('wrong input, try again!')
    
    
    
    
###############################################################################        
### contingency table    
def contingency_tb(df):
    clear()
    tab = df.select_dtypes(exclude=['float'])
    
    #
    anz_col_werte = len(tab.columns)
        
    list_columns_tab = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_tab.append(tab.columns[i])
        list_number.append(str(i))
        print(i, tab.columns[i])
        i+=1
    
    
    while True:
        tab1_column= input('Which column do you want to cross: \n(choose number) \n?')
        if tab1_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    tab1 = list_columns_tab[int(tab1_column)]
    
    
    while True:
        tab2_column= input('Which column do you want to cross: \n(choose number) \n?')
        if tab2_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    tab2 = list_columns_tab[int(tab2_column)]
    
    
    print(tab1,tab2)
    
    ctcalc = pd.crosstab(index=df[tab1], columns=df[tab2])
    ctv=pd.crosstab(index=df[tab1], columns=df[tab2], margins=True)
    
    
    ct = pd.crosstab(index=df[tab1], columns=df[tab2], margins=True).applymap(lambda r: r/len(df))
    
   
    
    print(ctv)
    print(ct)
    print(chi2_contingency(ctcalc))
    #sns.heatmap(ct, annot=True, cmap='coolwarm')
    
    #The random variables A and B are stochastically independent of each other
    
    #The random variables A and B are not stochastically independent of each other
    
    chi2, p, degfree, table = chi2_contingency(ctcalc)
    
    
    
    if p < 0.05:
        erg = 'H1: The variables A and B are not stochastically \nindependent of each other'
    else:
        erg = 'H0: The variables A and B are stochastically \nindependent of each other'
    
    
    
    chi2 = truncate(chi2, 3)
    
    p = truncate(p, 5)
    
    eintrag = 'Chi²: ' + str(chi2) + '\np-Value: ' + str(p) + '\n' + erg
    
    plt.figure(figsize=(4, 1))
    
    plt.subplot(121).set_ylim([0,2]) # äquivalent zu: plt.subplot(2, 2, 1)
    
    sns.heatmap(ctv,
            cmap='coolwarm',
            annot=True,
            annot_kws={'size':8},
            cbar=False,
            xticklabels=1, 
            yticklabels=1,
            square=False)
    
    plt.subplot(122)
    plt.text(0.1,0.5,eintrag, 
                    ha='left', va='center',
                    fontsize=12)
    plt.axis('off')
    plt.show()
    
    
def seq_numbers_add(df):
    
    seq_count = len(df)
    print(seq_count)
    seq_count=int(seq_count)
    seq_nr_from = input('Number from: ?')
    seq_nr_from = int(seq_nr_from)
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = range(seq_nr_from, seq_count+seq_nr_from)
    
    print(df)
    file_in_html(df)
    print('To work with you have to save this dataframe as file')
    save_yes = input('Would you like to save: \ny/n \n?')
    if save_yes.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)      
 
    
    
