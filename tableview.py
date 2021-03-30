#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:51:24 2020

@author: blaubaer (Ricky Helfgen)
"""
import pandas as pd
import webbrowser
from mft import clear
from sys import platform

F1 = '\U0001f522 ?'
F2 = '\U0001f521 ?' 


###pre-view functions
##############################################################################        

#######################################################################        
#are there missing datas        
def fehlende_daten(df):
    clear()
    print('Checking for missing data gave the following result:\n')
    print(df.isnull().sum())
    
    

######################################################################
#wich datatype
def datentyp(df):
    clear()
    print('Overview of data formats:\n')
    print(df.dtypes)

######################################################################
###show DataFrame in browser    
def file_in_html(fn, df):
    
    show_in_html = input('Would you like to show in browser? y/n \n' + F1)
    if show_in_html.lower() != 'y':
        print('no html')
    else:
        pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>
    
        #fn = 'ja'
        html_string = '''
        <html>
        <head><title>HTML Pandas Dataframe with CSS</title></head>
        <link rel="stylesheet" type="text/css" href="df_style.css"/>
        <body>
        csv-data-analyze - tableview - Dataframe: ''' + fn + '''<br>
            {table}
            </body>
            </html>.
        '''
    
        # OUTPUT AN HTML FILE
        with open('myhtml.html', 'w') as f:
            f.write(html_string.format(table=df.to_html(classes='mystyle',index = False).replace('<th>','<th style = "background-color: red">')))
        
        url = 'myhtml.html'
        
        if platform == "linux" or platform == "linux2":
            webbrowser.open_new_tab(url)
        elif platform == "darwin":
            file_location = "file:///" + url
            webbrowser.open_new_tab(file_location)
        elif platform == "win32":
            webbrowser.open_new_tab(url)
    

###show DataFrame in browser    
def filter_in_html(df_filter):
    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

    html_string = '''
    <html>
    <head><title>HTML Pandas Dataframe with CSS</title></head>
    <link rel="stylesheet" type="text/css" href="df_style.css"/>
    <body>
    filter-table - Python Analyze Tool<br>
        {table}
        </body>
        </html>.
    '''

    # OUTPUT AN HTML FILE
    with open('myfilter.html', 'w') as f:
        f.write(html_string.format(table=df_filter.to_html(classes='mystyle',index = False).replace('<th>','<th style = "background-color: blue">')))
    
    url = 'myfilter.html'
    
    if platform == "linux" or platform == "linux2":
        webbrowser.open_new_tab(url)
    elif platform == "darwin":
        file_location = "file:///" + url
        webbrowser.open_new_tab(file_location)
    elif platform == "win32":
        webbrowser.open_new_tab(url)
    
    
   




#######################################################################
# all single data
def ind_trip_data(df):
    y=0
    while y < (len(df)):
        a = y
        for i in range(5):
            print(df.iloc[a,:])
            a +=1
        y += 5
                   
        end_data = input('More records? \nPress "ENTER" for "Yes" or "n" for "No" \n' + F1)
        if (len(df)) <y+5:
            rest = abs((len(df))-y)
            for i in range(rest):
                print(df.iloc[a,:])
                a +=1
            print('The end of the table has been reached!')
            break
        if end_data.lower() == 'n':
            break

#######################################################################        
###Look at header and first data
def first_row(df):
    clear()
    print('first row view')
    print(df.iloc[0,:])
    
#######################################################################
###View individual data
def einzeldaten_anschauen(df):
    eind = input('What do you want to see \n1: first row\n2: all cycle of 5 rows\n(choose a number) \n' + F1 )
    if eind=='1':
        first_row(df)
    elif eind =='2':
        ind_trip_data(df)
    else:
        print('wrong input, please try again!')
        #einzeldaten_anschauen(df)
