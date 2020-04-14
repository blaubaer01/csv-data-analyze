import pandas as pd
#import shutil
import os
#import datetime
#import tkinter as tk
# import only system from os 
import matplotlib.pyplot as plt
from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro



#alternatively, define the source
csv_dateien=['daten.csv']

#read all CSV datas in the root folder
def csv_daten_im_verzeichnis():
    
    
    for dat in os.listdir(os.getcwd()):
        if dat.endswith(".csv") or dat.endswith(".CSV"):
            csv_dateien.append(dat)
            print(dat)
            
    
    return(csv_dateien)
            
        

#set custom CSV elements
def file_einlesen(auswahl_datei):
    
    #define structure
    format_ist = input('Which separator is used by the file: \n1: Comma / 2: Semicolon \nchoose number?').lower()
    if format_ist == '1':
        trennzeichen = ','
        dezimalzeichen = '.'
    elif format_ist == '2':
        trennzeichen = ';'
        dezimalzeichen =','
    else:
        print('Wrong input, please try again')
        #file_einlesen(auswahl_datei)
    
    #custom header
    kopfzeile = input('Is there a header: \n"y"/"n" \n?').lower()
    if kopfzeile == 'y':
        kopfz = 0
    elif kopfzeile =='n':
        kopfz = None
    else:
        kopfz = 0
        
    
    #read the file
    df=pd.read_csv(auswahl_datei,sep=trennzeichen ,decimal=dezimalzeichen, header=kopfz)
    
    
    return(df)


# define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 


#############################################################################
#simple statistics
# all single data
def ind_trip_data(df):
    y=0
    while y < (len(df)):
        a = y
        for i in range(5):
            print(df.iloc[a,:])
            a +=1
        y += 5
                   
        end_data = input('More records? \nPress "ENTER" for "Yes" or "n" for "No" \n?')
        if (len(df)) <y+5:
            rest = abs((len(df))-y)
            for i in range(rest):
                print(df.iloc[a,:])
                a +=1
            print('The end of the table has been reached!')
            break
        if end_data.lower() == 'n':
            break
        
#Look at header and first data
def first_row(df):
    clear()
    print('first row view')
    print(df.iloc[0,:])
    

#View individual data
def einzeldaten_anschauen(df):
    eind = input('What do you want to see \n1: first row\n2: all cycle of 5 rows\nchoose a number?' )
    if eind=='1':
        first_row(df)
    elif eind =='2':
        ind_trip_data(df)
    else:
        print('wrong input, please try again!')
        #einzeldaten_anschauen(df)
        
# Simple descriptive statistics        
def beschreibende_stat(df):
    while True:
        clear()
        was_beschreibend_analysieren=input('What data do you want to analyze? \n1: all\n2: only the numerical\n3: one special column \n?')
        if was_beschreibend_analysieren =='1':
            print('Simple descriptive statistics: \n')
            print(df.describe(include="all"))
        elif was_beschreibend_analysieren =='2':
            print('Simple descriptive statistics: \n')
            print(df.describe())
        elif was_beschreibend_analysieren =='3':
            anz_col = len(df.columns)
        
            list_columns = []

            i=1
            for i in range(anz_col):
                list_columns.append(df.columns[i])
                print(i, df.columns[i])
                i+=1
            nummer_spalte= input('Which column do you want to see: \n(choose number)?')
            try:
                print('Simple descriptive statiatics: \n')
                print(df[list_columns[int(nummer_spalte)]].describe(include='all'))
            except IndexError as error:
                print('wrong input, please try again!')
            except Exception as exception:
                print('wrong input, please try again!')
        else:
            print('wrong input, please try again!')
            
        
        
        restart = input('\nFurther describtive analysis: "y"\n?')
        if restart.lower() != 'y':
            break
        
        
        
##################################################################################
#graphical analyze

####bar charts#####

# groupby barchart
def groupby_balkendiagramm(df):
    
    anz_col = len(df.columns)
        
    list_columns = []

    i=1
    for i in range(anz_col):
        list_columns.append(df.columns[i])
        print(i, df.columns[i])
        i+=1
    nummer_spalte= input('Which column do you want to see: \n(choose number)?')
    groupby_spalte = input('Group by column: \n(choose number)?')
    df.groupby([list_columns[int(nummer_spalte)],list_columns[int(groupby_spalte)]]).size().unstack().plot(kind='bar',stacked=True)
    label_chart = (list_columns[int(nummer_spalte)] + ' grouped by count ' + list_columns[int(groupby_spalte)])
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()
    
    #df.groupby('state')['name'].nunique().plot(kind='bar')
    #plt.show()


# barcharts
def balkendiagramm(df):
    anz_col = len(df.columns)
        
    list_columns = []

    i=1
    for i in range(anz_col):
        list_columns.append(df.columns[i])
        print(i, df.columns[i])
        i+=1
    nummer_spalte= input('Which column do you want to see: \n(choose number)?')
    ax = df[list_columns[int(nummer_spalte)]].value_counts().plot(kind='bar',
                                    figsize=(14,8),
                                    title=list_columns[int(nummer_spalte)], color='blue')
    ax.set_xlabel(list_columns[int(nummer_spalte)])
    ax.set_ylabel("Frequency")
    plt.show()

# menu barcharts
def auswahl_balkendiagramm(df):
    clear()
    ausw_bd = input('Type of bar-chart: \n1: count column entries \n2: column grouped by 2 column entries \n(choose number)?')
    if ausw_bd =='1':
        balkendiagramm(df)
    elif ausw_bd =='2':
        groupby_balkendiagramm(df)
    else:
        print('wrong input!')
        
####pie charts####


def kuchendiagramm(df):
    clear()
    anz_col = len(df.columns)
        
    list_columns = []

    i=1
    for i in range(anz_col):
        list_columns.append(df.columns[i])
        print(i, df.columns[i])
        i+=1
    nummer_spalte= input('Which column do you want to see: \n(choose number)?')
    
    # Plot
    ax = df[list_columns[int(nummer_spalte)]].value_counts().plot(kind='pie',
                                    figsize=(14,8),
                                    title=list_columns[int(nummer_spalte)], autopct='%1.1f%%')
    #ax.set_xlabel(list_columns[int(nummer_spalte)])
    ax.set_ylabel("Frequency")
    
    
    plt.show()


def liniendiagramm(df):
    clear()
    #fig, ax = plt.subplots()
    anz_col = len(df.columns)
        
    list_columns = []

    i=1
    for i in range(anz_col):
        list_columns.append(df.columns[i])
        print(i, df.columns[i])
        i+=1
    value_column= input('Which value column do you want to see: \n(choose number)?')
    groupby_spalte = input('Group by column: \n(choose number)?')
    
    y = list_columns[int(value_column)]
    x = list_columns[int(groupby_spalte)]
    
    
    df.plot(x, y, grid=True)
    
    plt.show()




    
def menu_graphical_analyze(df):
    clear()
    print('Choose graphical view:')
    gr_view_list= ['Barchart', 'Piechart', 'Linechart', 'Dotplot', 'Histogram', 'Boxplots', 'Quantile-Quantile Plot']
    for i in range(len(gr_view_list)):
        print(i, gr_view_list[i])
        i+=1
    ausw_gr_view = input('Which graphical form of analysis \n(choose a number)?')
    
    if ausw_gr_view =='0':
        auswahl_balkendiagramm(df)
    elif ausw_gr_view =='1':
        kuchendiagramm(df)
    elif ausw_gr_view =='2':
        liniendiagramm(df)
    elif ausw_gr_view =='3':
        print('currently not available!')
    elif ausw_gr_view =='4':
        print('currently not available!')
    elif ausw_gr_view =='5':
        print('currently not available!')
    elif ausw_gr_view =='6':
        print('currently not available!')    
    else:
        print('wrong input')
        
    
    
def normality_test(df):
    clear()
    
    anz_col = len(df.columns)
        
    list_columns = []

    i=1
    for i in range(anz_col):
        list_columns.append(df.columns[i])
        print(i, df.columns[i])
        i+=1
    nummer_spalte= input('Which column do you want to see: \n(choose number)?')
    
    
    data = df[list_columns[int(nummer_spalte)]]
    stat, p = shapiro(data)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')    
    
    
    
def menu_tests(df):
    clear()
    what_kind_of_test = input('Which Test do you would like to do: \n1: Test of normality  \n2: t-test \n2(choose a number)?')
    if what_kind_of_test =='1':
        clear()
        normality_test(df)
    elif what_kind_of_test =='2':
        clear()
        print('currently not available')
    else:
        print('wrong input, try again!')


        



# statistics menu
def statistic(df):
    clear()
    menu_statistic = input('What kind of statistics: \n1: simple descriptive statistics \n2: graphical view \n3: tests \n?')
    if menu_statistic =='1':
        beschreibende_stat(df)
    elif menu_statistic =='2':
        menu_graphical_analyze(df)
    elif menu_statistic =='3':
        menu_tests(df)
    else:
        print('wrong input, please try again!')
        statistic(df)
        
        
        
#are there missing datas        
def fehlende_daten(df):
    clear()
    print('Checking for missing data gave the following result:\n')
    print(df.isnull().sum())

#wich datatype
def datentyp(df):
    clear()
    print('Overview of data formats:\n')
    print(df.dtypes)
#pre-analysis
def voranalyse(df):
    while True:
        clear()
        menu_voranalyse = input('How do you want to look at the data: \n1:Single-view \n2:Datatype \n3:Missing-Datas \n?')
        if menu_voranalyse =='1':
            clear()
            einzeldaten_anschauen(df)
        elif menu_voranalyse =='2':
            clear()
            datentyp(df)
        elif menu_voranalyse =='3':
            clear()
            fehlende_daten(df)
        else:
            print('wrong input, please try again!')
            #voranalyse(df)
        
        restart = input('\nFurther pre-analysis: "y"\n?')
        if restart.lower() != 'y':
            break

# Set filters
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
            
        restart = input('\nSet more filters: y/n.\n?')
        if restart.lower() != 'y':
            speichern_ja = input('Save the table with the filters set (the only way to analyze with the filter set): y/n \n?')
            if speichern_ja.lower() =='y':
                csvfilename = input('Filename \n?')
                fn = csvfilename + '.csv'
                df.to_csv(fn, sep=';', decimal=',', header =True)
                
            
            tabelle_m_f_uebernehmen = input('The filters should be available for further analysis: y/n \n?')
            if tabelle_m_f_uebernehmen.lower() =='y':
            
                return(df)
                break
            else:
                break


# work with the datas (Main menu)
def mit_daten_arbeiten(df):
    while True:
        clear()
        m_d_a = input('What type of analysis do you want to perform\n1:pre-analysis \n2:set some filters \n3:statistics analyze \n?')
        if m_d_a =='1':
            clear()
            voranalyse(df)
        elif m_d_a =='2':
            clear()
            filter_setzen(df)
        elif m_d_a =='3':
            clear()
            statistic(df)
        else:
            print('wrong input, please try again!')
            #mit_daten_arbeiten(df)
            
            
            
        
        restart = input('\nDo you want to analyze further?: y/n.\n?')
        if restart.lower() != 'y':
            break
        


# main prog
def main():
    while True:
        print("\033[1;37;40m \n")
        clear()
        #choosesource(source)
        print('#'*80)
        print('CSV Data Analyze-Tool V0.1 (by Ricky Helfgen) \nThis is an open source project and is subject to the guidelines of GPL V3')
        print('This tool is used for data analysis of CSV files with python3 and pandas')
        print('https://github.com/blaubaer01/csv-data-analyze')
        print('Have Fun!')
        print('#'*80)
        
              
        print('The following CSV-Files are in the root-folder, which you would like to evaluate?')
        csv_daten_im_verzeichnis()    
    
        #print(csv_dateien)
        auswahl_datei = input('Which CSV file to import (pay attention to spelling)\n?')
        if auswahl_datei in csv_dateien:
            df=file_einlesen(auswahl_datei)
        else:
            print('File not found! Please check your Input! \npay attention to upper and lower case!')
            #break
            main()
        
        clear()
                    
        print('#'*70)
        mit_daten_arbeiten(df)
                   
        
        restart = input('\nDo you want to analyze another CSV file: y/n.\n?')
        if restart.lower() != 'y':
            break
          




#Hauptprozesse starten
if __name__ == '__main__':
    main()
    
    