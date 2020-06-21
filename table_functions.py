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
from mft import clear, truncate, isfloat
from tableview import filter_in_html
import numpy as np

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


        
##############################################################################
###set filter

def filter_typ(df):
    
    while True:
        clear()
        
        crit = df.select_dtypes(exclude=['datetime'])
        
        
        anz_col = len(crit.columns)

        list_columns = []

        i=1
        for i in range(anz_col):

            list_columns.append(crit.columns[i])
            print(i, crit.columns[i])
            i+=1      
         
        inhalte_spalte= input('For which column you want to know the possible filter criteria \nchoose number! \n?')
        print(crit.iloc[:,int(inhalte_spalte)].value_counts())
        print(df[list_columns[int(inhalte_spalte)]].dtype)
        crit_col = df[list_columns[int(inhalte_spalte)]].dtype
        
        #########################################################################################
            ###create filter table (to copy filter criteria (str-c))
        df_filter = pd.DataFrame()
        df_filter = (df[list_columns[int(inhalte_spalte)]])
        
        
        df_filter.to_csv('df_filter.csv', sep=';', decimal=',')
                    
        df_filter = pd.read_csv('df_filter.csv', sep=';' , decimal=',', header=0)
        
        
        df_filter.columns=['indx', 'Filter']
        df_filter = df_filter.sort_values(by='Filter', ascending=1)
        
        df_filter = df_filter.drop_duplicates(subset='Filter', keep='last')
        df_filter = df_filter.drop(columns='indx')
        
        
        
        filter_in_html(df_filter)
        
        
        filter_ja = input('Set a filter: y/n \n?')
        
        if filter_ja.lower() =='y':
            
            which_filter=input('Which kind of filter: \n1: ==\n2: >=\n3: >\n4: <= \n5: <\n?')
            
            if which_filter == '1':
                name_filter=input('Input Name/Value of the filter criteria(Pay attention to upper and lower case): \n?')
                if crit_col == 'float64':
                    name_filter = float(name_filter)
                if crit_col == 'int64':
                    name_filter = int(name_filter)
                
                df = df[crit.iloc[:,int(inhalte_spalte)]==name_filter]
            
            elif which_filter =='2':
                name_filter=input('Input Name/Value of the filter criteria(Pay attention to upper and lower case): \n?')
                if crit_col == 'float64':
                    name_filter = float(name_filter)
                if crit_col == 'int64':
                    name_filter = int(name_filter)
                df = df[crit.iloc[:,int(inhalte_spalte)]>=name_filter]
            
            elif which_filter =='2':
                name_filter=input('Input Name/Value of the filter criteria(Pay attention to upper and lower case): \n?')
                if crit_col == 'float64':
                    name_filter = float(name_filter)
                if crit_col == 'int64':
                    name_filter = int(name_filter)
                df = df[crit.iloc[:,int(inhalte_spalte)]>name_filter]
            
            elif which_filter =='2':
                name_filter=input('Input Name/Value of the filter criteria(Pay attention to upper and lower case): \n?')
                if crit_col == 'float64':
                    name_filter = float(name_filter)
                if crit_col == 'int64':
                    name_filter = int(name_filter)
                df = df[crit.iloc[:,int(inhalte_spalte)]<=name_filter]
            
            elif which_filter =='2':
                name_filter=input('Input Name/Value of the filter criteria(Pay attention to upper and lower case): \n?')
                if crit_col == 'float64':
                    name_filter = float(name_filter)
                if crit_col == 'int64':
                    name_filter = int(name_filter)
                df = df[crit.iloc[:,int(inhalte_spalte)]<name_filter]

        restart = input('\nSet more filters: y/n.\n?')
        
        
        if restart.lower() != 'y':
        
            speichern_ja = input('Save the table with the filters set (the only way to analyze with the filter set): y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename (.csv will save automaticly) \n?')
                fn = csvfilename + '.csv'
                df.to_csv(fn, sep=';', decimal=',', header =True)
                break
            else:
                break
                
    print(df)
    press_enter=input('press enter to continue')
    return(df)            


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
 
    
def del_empty_rows(df):
    
    
    clear()
    
    print('clear emty rows')
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
        nummer_spalte= input('Which column do you want to clean: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    
    df[col].replace(' ', np.nan, inplace=True)
    df= df.dropna(subset=[col])
    
    print(df)
    
    
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)
    

def del_nan_rows(df):
    
    
    clear()
    
    print('clear nan rows')
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
        nummer_spalte= input('Which column do you want to clean: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    #df[col].replace('NaN', np.nan, inplace=True)
    df= df.dropna(subset=[col])
    print(df)
    
    
    speichern_ja = input('Save the table with the filters set (the only way to analyze with the filter set): y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)

def del_nan(df):
    clear()
    drop_yes = input('Do you realy want to drop all "NAN" rows in the dataframe y/n \n?')
    
    if drop_yes.lower() =='y':
        df = df.dropna()
        print('nan data deleted')
        print(df)
        speichern_ja = input('Save the modified dataframe: y/n \n?')
        if speichern_ja.lower() =='y':
            csvfilename = input('Filename (.csv will save automaticly) \n?')
            fn = csvfilename + '.csv'
            df.to_csv(fn, sep=';', decimal=',', header =True)
    else:
        print('no data deleted')
        


def del_zero_rows(df):
    
    
    clear()
    
    print('clear ZERO rows')
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
        nummer_spalte= input('Which column do you want to clean: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    
    df[col].replace(0, np.nan, inplace=True)
    df= df.dropna(subset=[col])
    
    print(df)
    
    
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)



def del_NA_rows(df):
    
    
    clear()
    
    print('clear character into column')
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
        nummer_spalte= input('Which column do you want to clean: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    
    
    
    df[col].replace('NA', np.nan, inplace=True)
    df= df.dropna(subset=[col])
    
    print(df)
    
    
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)





def del_sv_rows(df):
    
    
    clear()
    
    print('clear character into column')
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
        nummer_spalte= input('Which column do you want to clean: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    
    del_what = input('Which character rows do you would like to delete: \n?')
    
    
    df[col].replace(del_what, np.nan, inplace=True)
    df= df.dropna(subset=[col])
    
    print(df)
    
    
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)


def replace_content_into_col(df):
    
    
    clear()
    
    print('Replace content into column')
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
        nummer_spalte= input('Into which column do you want to replace: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    
    rpl_what = input('Current character \n?')
    rpl_with = input('New charakter \n?')
    
    df[col].replace(rpl_what, rpl_with, inplace=True)
    
    print(df)
    
    
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)

def replace_number_into_col(df):
    
    
    clear()
    
    print('Replace number into column')
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
        nummer_spalte= input('Into which column do you want to replace: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    
    rpl_what = input('Current value \n?')
    
    while True:
            rpl_with = input('New Value: \n(choose point-comma) \n?')
    
            if not isfloat(rpl_with):
                print("target value is not a number with point-comma, please try again")
            else:
                break
    
    
    df[col].replace(float(rpl_what),float(rpl_with), inplace=True)
    
    print(df)
    
    
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)


def delrep_value(df):
    clear()
    
    menu_del = input('What do you want to delete or replace: \n1: delete nan rows \n2: delete empty rows \n3: delete nan-data rows cross the dataframe \n4: delete NA rows \n5: delete 0 rows \n6: delete rows with special character \n7: replace content into column \n8: replace value into column \n9: replace float to point comma \n10: replace character into column  \n?' )
    
    if menu_del =='1':
        del_nan_rows(df)
    elif menu_del =='2':
        del_empty_rows(df)
    elif menu_del =='3':
        del_nan(df)
    elif menu_del =='4':
        del_NA_rows(df)
    elif menu_del =='5':
        del_zero_rows(df)
    elif menu_del =='6':
        del_sv_rows(df)
    elif menu_del =='7':
        replace_content_into_col(df)
    elif menu_del =='8':
        replace_number_into_col(df)
    elif menu_del =='9':
        replace_float_comma(df)
    elif menu_del =='10':
        replace_character(df)
    else:
        print('wrong input (choose number), try again')


def replace_float_comma(df):
    clear()
    
    print('replace float comma - point comma into column')
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
        nummer_spalte= input('Into which column do you want to replace: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    
    df[col]=df[col].str.replace(',','.').astype(float)
    
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)



def replace_character(df):
    clear()
    
    print('replace character into column')
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
        nummer_spalte= input('Into which column do you want to replace: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    col = list_columns[int(nummer_spalte)]
    
    char_input = input('Current character \n?')
    char_output = input('New character \n?')
    
    
    df[col]=df[col].str.replace(char_input,char_output).astype(str)
    
    speichern_ja = input('Save the modified dataframe: y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)
        