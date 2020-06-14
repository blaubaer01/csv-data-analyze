#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 07:23:07 2020

@author: blaubaer (Ricky Helfgen)
"""

import datetime as dt
from mft import clear
import pandas as pd

def convert_datetime(df):
    clear()
    datum = df.select_dtypes(exclude=['float', 'int'])
        
        #
    anz_col_datum = len(datum.columns)
        
    list_columns_datum = []
    list_number=[]
    i=1
    for i in range(anz_col_datum):
        list_columns_datum.append(datum.columns[i])
        list_number.append(str(i))
        print(i, datum.columns[i])
        i+=1
    
    while True:
        datum_column= input('Which value column do you want to see: \n(choose number) \n?')
        if datum_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    date_y = list_columns_datum[int(datum_column)]
    
    new_name_c = input('Input new column name: \n?')
    
    konv = input('Which datetime format do you have as input: \n1: yyyy/mm/dd hh:mm:ss \n2: dd/mm/yyyy hh:mm:ss \n3: dd-mm-yyyy hh:mm:ss \n4: yyyy-mm-ddThh:mm:ss \n5: dd.mm.yyyy hh:mm:ss \n?' )
    
    #date_format = input('Which Calendarinformation do you need: \1: Month \n2: day \n3: CW \n4: Day of the year \n5: Day of the week \n6: tz_Info \n7: Day name \n8: Month name \n?' )
    
    if konv =='1':
        df[new_name_c] = pd.to_datetime(df[date_y], format='%Y/%m/%d %H:%M:%S')
        df[new_name_c] = df[new_name_c].astype('datetime64[ns]')
    elif konv=='2':
        df[new_name_c] = pd.to_datetime(df[date_y], format='%d/%m/%Y %H:%M:%S')
        df[new_name_c] = df[new_name_c].astype('datetime64[ns]')
    elif konv=='3':
        df[new_name_c] = pd.to_datetime(df[date_y], format='%d-%m-%Y %H:%M:%S')
        df[new_name_c] = df[new_name_c].astype('datetime64[ns]')
    elif konv=='4':
        df[new_name_c] = pd.to_datetime(df[date_y], format='%Y/%m/%dT%H:%M:%S')
        df[new_name_c] = df[new_name_c].astype('datetime64[ns]')
    elif konv=='5':
        df[new_name_c] = pd.to_datetime(df[date_y], format='%d.%m.%Y %H:%M:%S')
        df[new_name_c] = df[new_name_c].astype('datetime64[ns]')
    
    else:
        print('Wrong input  (choose number), please try again!')

    
    speichern_ja = input('Save the table with the filters set (the only way to analyze with the filter set): y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)



def cal_info(df):
    
    clear()
        
    datum = df.select_dtypes(exclude=['float', 'int'])
        
        #
    anz_col_datum = len(datum.columns)
        
    list_columns_datum = []
    list_number=[]
    i=1
    for i in range(anz_col_datum):
        list_columns_datum.append(datum.columns[i])
        list_number.append(str(i))
        print(i, datum.columns[i])
        i+=1
    
    while True:
        datum_column= input('Which value column do you want to see: \n(choose number) \n?')
        if datum_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    date_y = list_columns_datum[int(datum_column)]
    
    new_name_c = input('Input new column name: \n?')
    
    konv = input('Which calendar information do you need: \n1: month \n2: day \n3: week \n4: year \n5: hour  \n6: minutes \n7: seconds \n?' )
    
    #date_format = input('Which Calendarinformation do you need: \1: Month \n2: day \n3: CW \n4: Day of the year \n5: Day of the week \n6: tz_Info \n7: Day name \n8: Month name \n?' )
    
    if konv =='1':
        df[new_name_c] = df[date_y].dt.month
        df[new_name_c] = df[new_name_c].astype('int')
    elif konv=='2':
        df[new_name_c] = df[date_y].dt.day
        df[new_name_c] = df[new_name_c].astype('int')
    elif konv=='3':
        df[new_name_c] = df[date_y].dt.week
        df[new_name_c] = df[new_name_c].astype('int')
    elif konv=='4':
        df[new_name_c] = df[date_y].dt.year
        df[new_name_c] = df[new_name_c].astype('int')
    elif konv=='5':
        df[new_name_c] = df[date_y].dt.hour
        df[new_name_c] = df[new_name_c].astype('int')
    elif konv=='6':
        df[new_name_c] = df[date_y].dt.minute
        df[new_name_c] = df[new_name_c].astype('int')
    elif konv=='7':
        df[new_name_c] = df[date_y].dt.second
        df[new_name_c] = df[new_name_c].astype('int')
# =============================================================================
#     elif konv=='8':
#         df[new_name_c] = df[date_y].dt.weekday()
#         df[new_name_c] = df[new_name_c].astype('str')
#     
# =============================================================================
    
    else:
        print('Wrong input  (choose number), please try again!')
    
    speichern_ja = input('Save the table with the filters set (the only way to analyze with the filter set): y/n \n?')
    if speichern_ja.lower() =='y':
        csvfilename = input('Filename (.csv will save automaticly) \n?')
        fn = csvfilename + '.csv'
        df.to_csv(fn, sep=';', decimal=',', header =True)
        