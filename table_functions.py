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
from mft import clear, truncate, isfloat, save_CSV, save_CSV_new
from tableview import filter_in_html
import numpy as np


#Thanks to https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
#and https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
### define our clear function 
#############################################################################

def appendDFToCSV(fn, df, sep=","):
    
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
        #file_in_html(df)
        
        save_CSV_new(df)
        
       

        
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
        save_CSV_new(df)
    elif join_how == '2':
        result = pd.merge(df, df2, how='inner', on =key_name)
        print(result)
        save_CSV_new(df)
    elif join_how =='3':
        result = pd.merge(df, df2, how='left', on=key_name)
        print(result)
        save_CSV_new(df)
        
    elif join_how =='4':
        result = pd.merge(df, df2, how='right', on=key_name)
        print(result)
        print('To work with you have to save this dataframe as file')
        save_CSV_new(df)
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
            break
            
    
    save_CSV_new(df)            
    print(df)
    press_enter=input('press enter to continue')
    return(df)            


###sort by column
###################################################################################
def sort_column(fn, df):
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
                save_CSV(fn, df)
                file_in_html(fn, df)
                return(df)   
                
                break

###transposed               
###############################################################################
def transposed_table(fn, df):
    clear()
    trans_yes = input('Would you like to transpose the table: y/n\n?')
    if trans_yes =='y':
        df = df.T
        save_CSV_new(df)
        file_in_html(fn, df)
        return(df)
    else:
        file_in_html(fn, df)
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
            save_CSV_new(df)
        else:
            ctcalc = pd.crosstab(index=df[tab1], columns=df[tab2])
            print(ctcalc)
            save_CSV_new(df)
    
    elif which_table =='2':
        
        with_sum = input('Crosstab with "Total": y/n \n?')
        
        if with_sum =='y':
            ct = pd.crosstab(index=df[tab1], columns=df[tab2], margins=True).applymap(lambda r: r/len(df))
            print(ct)    
            save_CSV_new(df)
        else:
            ct = pd.crosstab(index=df[tab1], columns=df[tab2], margins=False).applymap(lambda r: r/len(df))
            print(ct)
            save_CSV_new(df)

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
    
    
def seq_numbers_add(fn, df):
    
    seq_count = len(df)
    print(seq_count)
    seq_count=int(seq_count)
    seq_nr_from = input('Number from: ?')
    seq_nr_from = int(seq_nr_from)
    name_df = input('Table Name: ?')
    
    
    
    df[name_df] = range(seq_nr_from, seq_count+seq_nr_from)
    
    print(df)
    file_in_html(fn, df)
    print('To work with you have to save this dataframe as file')
    save_CSV(fn, df)
 
    
def del_empty_rows(fn, df):
    
    
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
    
    
    save_CSV(fn, df)    

def del_nan_rows(fn, df):
    
    
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
    
    
    save_CSV(fn, df)

def del_nan(fn, df):
    clear()
    drop_yes = input('Do you realy want to drop all "NAN" rows in the dataframe y/n \n?')
    
    if drop_yes.lower() =='y':
        df = df.dropna()
        print('nan data deleted')
        print(df)
        save_CSV(fn, df)
    else:
        print('no data deleted')
        


def del_zero_rows(fn, df):
    
    
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
    
    
    save_CSV(fn, df)



def del_NA_rows(fn, df):
    
    
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
    
    
    save_CSV(fn, df)





def del_sv_rows(fn, df):
    
    
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
    
    
    save_CSV(fn, df)


def replace_content_into_col(fn, df):
    
    
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
    
    
    save_CSV(fn, df)
    
def replace_number_into_col(fn, df):
    
    
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
    
    
    save_CSV(fn, df)


def delrep_value(fn, df):
    clear()
    
    menu_del = input('What do you want to delete or replace: \n1: delete nan rows \n2: delete empty rows \n3: delete nan-data rows cross the dataframe \n4: delete NA rows \n5: delete 0 rows \n6: delete rows with special character \n7: replace content into column \n8: replace value into column \n9: replace float to point comma \n10: replace character into column \n11: delete first row \n12: delete last row \n13: delete defined rows \n14: delete rows contain string \n?' )
    
    if menu_del =='1':
        del_nan_rows(fn, df)
    elif menu_del =='2':
        del_empty_rows(fn, df)
    elif menu_del =='3':
        del_nan(fn, df)
    elif menu_del =='4':
        del_NA_rows(fn, df)
    elif menu_del =='5':
        del_zero_rows(fn, df)
    elif menu_del =='6':
        del_sv_rows(fn, df)
    elif menu_del =='7':
        replace_content_into_col(fn, df)
    elif menu_del =='8':
        replace_number_into_col(fn, df)
    elif menu_del =='9':
        replace_float_comma(fn, df)
    elif menu_del =='10':
        replace_character(fn, df)
    elif menu_del =='11':
        del_first_row(fn, df)
    elif menu_del =='12':
        del_last_row(fn, df)
    elif menu_del =='13':
        del_defined_row(fn, df)
    elif menu_del =='14':
        del_contains_word(fn, df)

    
    else:
        print('wrong input (choose number), try again')


def replace_float_comma(fn, df):
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
    
    save_CSV(fn, df)


def replace_character(fn, df):
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
    
    save_CSV(fn, df)

def del_last_row(fn, df):
    clear()
    print(df)
    del_l_r = input('Delete last row y/n \n?')
    
    
    if del_l_r.lower() =='y':
        df = df.drop(df.index[len(df)-1])
        print('Last row deleted')
        print(df)
        save_CSV(fn, df)
    else:
        print('no data deleted')
        
def del_first_row(fn, df):
    clear()
    print(df)
    del_f_r = input('Delete first row y/n \n?')
    
    
    if del_f_r.lower() =='y':
        df = df.drop(df.index[0])
        print('First row deleted')
        print(df)
        save_CSV(fn, df)
    else:
        print('no data deleted')

def del_defined_row(fn, df):
    clear()
    print(df)
    del_d_r = input('Delete defined rows y/n \n?')
    
    
    if del_d_r.lower() =='y':
        
        d_from_index = input('From which index \n?')
        count_index = input('How many rows to delete \n?')
        
        
        d_till_index = int(d_from_index) + int(count_index)
        print(d_till_index)
        
        index_del_list = []
        
        d_from_index = int(d_from_index)
        d_till_index = int(d_till_index)
        
        for i in range(d_from_index, d_till_index):
            index_del_list.append(d_from_index)
            d_from_index += 1
            print(d_from_index)
            
            
        print(index_del_list)
        
        
        df = df.drop(df.index[index_del_list])
        print('Defined Rows deleted')
        print(df)
        save_CSV(fn, df)
    else:
        print('no data deleted')
    
    
def del_contains_word(fn, df):
    clear()
    del_yes = input('Delete rows contains "Word" y/n \n?')
    print(df)
    if del_yes.lower() =='y':
        
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
        
        
        
        del_word = input('Keyword to delete row: \n?')
        
        
        df = (df[~df[col].str.contains(del_word)])
        print(df)
        
        save_CSV(fn, df)
    else:
        print('no rows deleted')
        
    
def melt_table(df):
    clear()
    print('Melt Colums by Category!')
    
    list_id_vars = []
    while True:
        add_id_vars = input('Add id column y/n \n?')
        if add_id_vars == 'y':
                
            kategorie=df.select_dtypes(exclude=['float'])
            
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
                groupby_column = input('Choose id column: \n(choose number) \n?')
                if groupby_column not in list_number:
                    print('wrong input, try again!')
                else:
                    break  
            x = list_columns_kategorie[int(groupby_column)]
            list_id_vars.append(x)
    
        else:
            break
    
    
    # add values
    list_vars = []
    while True:
        add_vars = input('Add values column y/n \n?')
        if add_vars == 'y':
            werte = df.select_dtypes(exclude=['object'])
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
                value_column= input('Choose value column: \n(choose number) \n?')
                if value_column not in list_number:
                    print('wrong input, try again!')
                else:
                    break
            y = list_columns_werte[int(value_column)]
            list_vars.append(y) 
        
        else:
            break
    
    print(list_vars)
    df = pd.melt(df, id_vars = list_id_vars, value_vars = list_vars, var_name= 'Values')
    
    print(df)
    
    save_CSV_new(df)


def df_rename(fn, df):
    
    rename_yes = input('rename column: y/n\n?')
    if rename_yes =='y':
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
                rename_column= input('Current column name: \n?')
                if rename_column not in list_number:
                    print('wrong input, try again!')
                else:
                    break 
    
            
            
            
            r_col = list_columns[int(rename_column)]
            
            print('The column name you will change call:', r_col)
            break
            
        new_column_name = input('Input new column name: \n?')
        
        df = df.rename(columns={r_col:new_column_name})
        
        print(df)

        save_CSV(fn, df)
        

#######################################################################
###combine factor column
def combine_column(fn, df):
    print('Combine factor columns:')
    print('#'*50)    
    
    werte = df.select_dtypes(include=['object', 'datetime' , 'category'])
    
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
    
    df[name_col] = df[col1] + "_" + df[col2]
    
    print(df)
    
    save_CSV(fn, df)
        
########################################################################
###del column
def delete_column(fn, df):
    
    rename_yes = input('delete column y/n\n?')
    if rename_yes =='y':
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
                rename_column= input('Column name to delete: \n?')
                if rename_column not in list_number:
                    print('wrong input, try again!')
                else:
                    break 

        
        
        
            d_col = list_columns[int(rename_column)]
        
            print('The column name you will delete call:', d_col)
            break
        
        
        df = df.drop(d_col, axis=1)
    
        print(df)

        save_CSV(fn, df)
        
####################################################################################
#####change datatype
def change_datatype(df):
    
    
    print('Overview of data formats:\n')
    print(df.dtypes)
    
    ###change data type
    ##################################################################################
    datentyp_aendern = input('Would you like to change data types: y/n \n?')
    
    if datentyp_aendern == 'y':
    
        while True:
            welcher_datentyp = input('How to change: \n1: float \n2: integer \n3: string \n4: categorie \n5: datetime \n(choose number) \n?')
            
            if welcher_datentyp =='1':
                datent=df.select_dtypes(include=['int'])
                anz_col = len(datent.columns)
        
                list_columns = []

                i=1
                for i in range(anz_col):
                    list_columns.append(datent.columns[i])
                    print(i, datent.columns[i])
                    i+=1
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number) \n?')
                
                df[list_columns[int(nummer_spalte)]] = df[list_columns[int(nummer_spalte)]].astype(float)
            elif welcher_datentyp =='2':
                datent=df.select_dtypes(include=['float', 'object'])
                anz_col = len(datent.columns)
        
                list_columns = []

                i=1
                for i in range(anz_col):
                    list_columns.append(datent.columns[i])
                    print(i, datent.columns[i])
                    i+=1
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number) \n?')
                try:
                    df[list_columns[int(nummer_spalte)]] = df[list_columns[int(nummer_spalte)]].astype(int)
                except Exception as exception:
                    print('Convert data not possible!')    
                    
            elif welcher_datentyp =='3':
                anz_col = len(df.columns)
        
                list_columns = []

                i=1
                for i in range(anz_col):
                    list_columns.append(df.columns[i])
                    print(i, df.columns[i])
                    i+=1
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number) \n?')
                df[list_columns[int(nummer_spalte)]] = df[list_columns[int(nummer_spalte)]].astype(str)
            
            elif welcher_datentyp =='4':
                anz_col = len(df.columns)
        
                list_columns = []

                i=1
                for i in range(anz_col):
                    list_columns.append(df.columns[i])
                    print(i, df.columns[i])
                    i+=1
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number) \n?')
                df[list_columns[int(nummer_spalte)]] = df[list_columns[int(nummer_spalte)]].astype('category')
            elif welcher_datentyp =='5':
                anz_col = len(df.columns)
        
                list_columns = []

                i=1
                for i in range(anz_col):
                    list_columns.append(df.columns[i])
                    print(i, df.columns[i])
                    i+=1
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number) \n?')
                try:
                    df[list_columns[int(nummer_spalte)]] = df[list_columns[int(nummer_spalte)]].astype('datetime64[ns]')
                except Exception as exception:
                    print('Convert data not possible!')
            else:
                print('wrong input, please try again')
            
            
            clear()
            print('Overview of data formats:\n')
            print(df.dtypes)
            restart = input('\nChange additional data types: "y" \n?')
            if restart.lower() != 'y':
                break
                #print('next steps')
    
        