import pandas as pd
import os
#import datetime
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from scipy.stats import linregress
import scipy as spy
import statistics as stats
import pyspc
import webbrowser
import seaborn as sns
import numpy as np



#alternatively, define the source
csv_dateien=['daten.csv']

#############################################################################
#read all CSV datas in the root folder
def csv_daten_im_verzeichnis():
    
    
    for dat in os.listdir(os.getcwd()):
        if dat.endswith(".csv") or dat.endswith(".CSV"):
            csv_dateien.append(dat)
            print(dat)
            
    
    return(csv_dateien)
            
        

#set custom CSV elements
def file_einlesen(auswahl_datei):
    
    clear()
    f = open(auswahl_datei, "r")
    
    print('#'*80)
    print('Preview to the first 2 lines: \n')
    print('first line:', f.readline())
    print('second line:', f.readline())
    print('#'*80)
    f.close
    
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
    
    clear()
    
    print('Overview of data formats:\n')
    print(df.dtypes)
    
    datentyp_aendern = input('Would you like to change data types: y/n \n?')
    
    if datentyp_aendern == 'y':
    
        while True:
            welcher_datentyp = input('How to change: \n1: float \n2: integer \n3: string \n4: categorie \n5: datetime \n(choose number)?')
            
            if welcher_datentyp =='1':
                datent=df.select_dtypes(include=['int'])
                anz_col = len(datent.columns)
        
                list_columns = []

                i=1
                for i in range(anz_col):
                    list_columns.append(datent.columns[i])
                    print(i, datent.columns[i])
                    i+=1
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number)?')
                
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
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number)?')
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
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number)?')
                df[list_columns[int(nummer_spalte)]] = df[list_columns[int(nummer_spalte)]].astype(str)
            
            elif welcher_datentyp =='4':
                anz_col = len(df.columns)
        
                list_columns = []

                i=1
                for i in range(anz_col):
                    list_columns.append(df.columns[i])
                    print(i, df.columns[i])
                    i+=1
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number)?')
                df[list_columns[int(nummer_spalte)]] = df[list_columns[int(nummer_spalte)]].astype('category')
            elif welcher_datentyp =='5':
                anz_col = len(df.columns)
        
                list_columns = []

                i=1
                for i in range(anz_col):
                    list_columns.append(df.columns[i])
                    print(i, df.columns[i])
                    i+=1
            
                nummer_spalte= input('Which column do you want to change data type: \n(choose number)?')
                try:
                    df[list_columns[int(nummer_spalte)]] = df[list_columns[int(nummer_spalte)]].astype('datetime64[ns]')
                except Exception as exception:
                    print('Convert data not possible!')
            else:
                print('wrong input, please try again')
            
            
            clear()
            print('Overview of data formats:\n')
            print(df.dtypes)
            restart = input('\nChange additional data types: "y"\n?')
            if restart.lower() != 'y':
                break
                #print('next steps')
    filter_setzen = input('Would you like to set any filter: \ny/n?')
    if filter_setzen =='y':
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
                if speichern_ja.lower() =='n':
                    break
            else:
                return(df)
                    
        
    
            
    
    
    
    return(df)

#############################################################################

# define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 


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
##################################################################################

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


##############################################################################        
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

###################################################################################
###line-chart
def liniendiagramm(df):
    clear()
    kategorie=df.select_dtypes(include=['object', 'datetime'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []

    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        print(i, kategorie.columns[i])
        i+=1
    
    groupby_spalte = input('Group by column: \n(choose number)?')
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_spalte)]
    
    
    df.plot(x, y, grid=True)
    
    plt.show()

###boxplots
################################################################################
def boxplot(df):
    clear()
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    y = list_columns_werte[int(value_column)]
    
    df.boxplot(column=y, widths=0.5)
    plt.show()

def violin(df):
    clear()
    sns.set(style="whitegrid")
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    y = list_columns_werte[int(value_column)]
    
    sns.violinplot(x=df[y])
    plt.show()

def violin_groupby(df):
    clear()
    sns.set(style="whitegrid")
    kategorie=df.select_dtypes(include=['object'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []

    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        print(i, kategorie.columns[i])
        i+=1
    
    groupby_spalte = input('Group by column: \n(choose number)?')
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_spalte)]
    
    
    sns.violinplot(x=x, y=y, data=df)
    
    plt.show()


def boxplot_groupby(df):
    clear()
    kategorie=df.select_dtypes(include=['object'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []

    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        print(i, kategorie.columns[i])
        i+=1
    
    groupby_spalte = input('Group by column: \n(choose number)?')
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_spalte)]
    
    df.boxplot(by=x, column=y)
    
    plt.show()

def menu_boxplot(df):
    clear()
    menu_bp = input('Which Boxplox: \n1: Single Boxplot \n2: Boxplot by group \n3: Violin-Plot \n4: Violinplot by group\n(choose a number)?')
    if menu_bp =='1':
        boxplot(df)
    elif menu_bp =='2':
        boxplot_groupby(df)
    elif menu_bp =='3':
        violin(df)
    elif menu_bp =='4':
        violin_groupby(df)
    else:
        print('wrong input, try again!')

###histogram
#####################################################################################
def histogram(df):
    clear()
    sns.set(color_codes=True)

        
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    y = df[list_columns_werte[int(value_column)]]
    
    sns.distplot(y);
    plt.show()


###scatterplot
##############################################################################
def scatter(df):
    clear()        
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column_y= input('y-value: \n(choose number)?')
    value_column_x= input('x-value: \n(choose number)?')
    
    y = list_columns_werte[int(value_column_y)]
    
    x = list_columns_werte[int(value_column_x)]
    
    
    
    #df.hist(column=y)
    df.plot.scatter(y,x) # Histogram will now be normalized
    label_chart = ('Scatter-Plot')
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()


def scatter_w_r(df):
    clear()
    sns.set(color_codes=True)        
    
    
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column_y= input('y-value: \n(choose number)?')
    value_column_x= input('x-value: \n(choose number)?')
    
    y = df[list_columns_werte[int(value_column_y)]]
    
    x = df[list_columns_werte[int(value_column_x)]]
    


    sns.regplot(x=x, y=y, data=df);


    
    label_chart = ('Linear-Regression-Plot')
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()

def scatter_joint_plot(df):
    clear()
    sns.set(color_codes=True)        
    
    
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column_y= input('y-value: \n(choose number)?')
    value_column_x= input('x-value: \n(choose number)?')
    
    y = df[list_columns_werte[int(value_column_y)]]
    
    x = df[list_columns_werte[int(value_column_x)]]
    


    sns.jointplot(x=x, y=y, data=df, kind="reg");

    plt.show()

def menu_scatter(df):
    clear()
    m_scatter = input('Scatter-Plot: \n1: scatter only \n2: regression plot \n3: regression_jointplot \n(choose number)?')
    if m_scatter =='1':
        scatter(df)
    elif m_scatter =='2':
        scatter_w_r(df)
    elif m_scatter =='3':
        scatter_joint_plot(df)
    else:
        print('wrong input,please try again!')

#############################################################################
###swarmplot
def swarm_plot(df):
    clear()
    sns.set(style="whitegrid", palette="muted")

    kategorie=df.select_dtypes(include=['object'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []

    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        print(i, kategorie.columns[i])
        i+=1
    
    groupby_spalte = input('Group by column: \n(choose number)?')
    
    y = df[list_columns_werte[int(value_column)]]
    x = df[list_columns_kategorie[int(groupby_spalte)]]
    
    
    
    
    # Draw a categorical scatterplot to show each observation
    sns.swarmplot(x=x, y=y, data=df)
    #sns.boxplot(x=x, y=y, data=df, whis=np.inf)
    plt.show()
    
###qq-plot
###########################################################################
def qq_plot(df):
    clear()
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    y = df[list_columns_werte[int(value_column)]]
    
    spy.stats.probplot(y, dist="norm", plot=plt)
    plt.show() 
    
def mr_chart(df):
    clear()
    
    werte = df.select_dtypes(exclude=['object'])
    #
    anz_col_werte = len(werte.columns)
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    value_column= input('Which value column do you want to see: \n(choose number)?')
    clear()
    #
    
    y = df[list_columns_werte[int(value_column)]]
    
    a = pyspc.spc(y) + pyspc.mr() + pyspc.rules()
    print(a)
    plt.show()

def dotplot_time(df):
    clear()
    sns.set(style="darkgrid")


    
    kategorie=df.select_dtypes(include=['object'])
    werte = df.select_dtypes(exclude=['object'])
    #zeitraum = df.select_dtypes(inculde=['datetime'])
    zeitraum=df.select_dtypes(include=['object', 'datetime'])
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []

    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        print(i, kategorie.columns[i])
        i+=1
    
    groupby_spalte = input('Group by column: \n(choose number)?')
    
    anz_col_zeitraum = len(zeitraum.columns)
        
    list_columns_zeitraum = []

    i=1
    for i in range(anz_col_zeitraum):
        list_columns_zeitraum.append(zeitraum.columns[i])
        print(i, zeitraum.columns[i])
        i+=1
    
    value_zeitraum = input('Choose the Datetime-column')
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_spalte)]
    z = list_columns_zeitraum[int(value_zeitraum)]
    
    #sns.relplot(x=z, y=y, hue=x, style="time", data=df);     
    
    g = sns.relplot(x=z, y=y, hue=x, data=df)
    g.fig.autofmt_xdate()
    
    plt.show()
    

def menu_graphical_analyze(df):
    clear()
    print('Choose graphical view:')
    gr_view_list= ['Barchart', 'Piechart', 'Linechart', 'Scatter-Plot', 'Histogram', 
                   'Box/-Violin Plots', 'QQ-Plot', 
                   'MR-Chart', 'Time_Dot-Plot', 'Swarm-Plot']
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
        menu_scatter(df)
    elif ausw_gr_view =='4':
        histogram(df)
    elif ausw_gr_view =='5':
        menu_boxplot(df)
    elif ausw_gr_view =='6':
        qq_plot(df)    
    elif ausw_gr_view =='7':
        mr_chart(df)
    elif ausw_gr_view =='8':
        print('not available')
        #dotplot_time(df)
    elif ausw_gr_view =='9':
        swarm_plot(df)
        #print('currently not available')
    else:
        print('wrong input')
        
###############################################################################
###Tests
        
        
###test of normality   
def normality_test(df):
    clear()
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column= input('Which value column do you want to see: \n(choose number)?')
    
    y = df[list_columns_werte[int(value_column)]]
    
    
    stat, p = shapiro(y)
    
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')    

###correlation test    
def correl(df):
    clear()
    correlation_df = df.corr()
    print(correlation_df)

###f-test
def f_test(df):
    clear()
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []

    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        print(i, werte.columns[i])
        i+=1
    
    value_column_a= input('a-value: \n(choose number)?')
    value_column_b= input('b-value: \n(choose number)?')
    
    
    
    d1 = df[list_columns_werte[int(value_column_a)]]
    
    d2 = df[list_columns_werte[int(value_column_b)]]
    
    df1 = len(d1) - 1
    df2 = len(d2) - 1
    
    
    F = stats.variance(d1) / stats.variance(d2)
    single_tailed_pval = spy.stats.f.cdf(F,df1,df2)
    print('F-Value:' ,F)
    print('p-value:' ,single_tailed_pval)
    
def ttest_menu(df):
    clear()
    menu_ttest = input('Which kind of t-test: \n1: one sided \n2: two sided \n3: independent \n(choose a number)?')    
    if menu_ttest =='1':
        ttest_o_s(df)
    elif menu_ttest =='2':
        ttest_t_s(df)
    elif menu_ttest =='3':
        ttest_i(df)
    else:
        print('wrong input, try again!')
    
    
    
def ttest_o_s(df):
    clear()

def ttest_t_s(df):
    clear()

def ttest_i(df):
    clear()


    
    
def menu_tests(df):
    clear()
    what_kind_of_test = input('Which Test do you would like to do: \n1: Test of normality  \n2: correlation \n3: t-test \n4: f-test \n5: ANOVA \n6: Outlier-Test\n(choose a number)?')
    if what_kind_of_test =='1':
        clear()
        normality_test(df)
    elif what_kind_of_test =='2':
        clear()
        correl(df)
    elif what_kind_of_test =='3':
        clear()
        print('currently not available')
    elif what_kind_of_test =='4':
        clear()
        f_test(df)
    elif what_kind_of_test =='5':
        clear()
        print('currently not available')
    elif what_kind_of_test =='6':
        clear()
        print('currently not available')
    
    else:
        print('wrong input, try again!')


#############################################################################
###process capability analyse 
def pca():
    clear()



# statistics menu
def statistic(df):
    clear()
    menu_statistic = input('What kind of statistics: \n1: simple descriptive statistics \n2: graphical view \n3: tests \n4: process capability analysis \n(choose number)?')
    if menu_statistic =='1':
        beschreibende_stat(df)
    elif menu_statistic =='2':
        menu_graphical_analyze(df)
    elif menu_statistic =='3':
        menu_tests(df)
    elif menu_statistic =='4':
        print('still on work')
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
    
def file_in_html(df):
    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

    html_string = '''
    <html>
    <head><title>HTML Pandas Dataframe with CSS</title></head>
    <link rel="stylesheet" type="text/css" href="df_style.css"/>
    <body>
        {table}
        </body>
        </html>.
    '''

    # OUTPUT AN HTML FILE
    with open('myhtml.html', 'w') as f:
        f.write(html_string.format(table=df.to_html(classes='mystyle',index = False).replace('<th>','<th style = "background-color: red">')))
    
    url = 'myhtml.html'
    
    webbrowser.open_new_tab(url)
    
#pre-analysis
def voranalyse(df):
    while True:
        clear()
        menu_voranalyse = input('How do you want to look at the data: \n1: Single-view \n2: Datatype \n3: Missing-Datas \n4: show Data in HTML \n?')
        if menu_voranalyse =='1':
            clear()
            einzeldaten_anschauen(df)
        elif menu_voranalyse =='2':
            clear()
            datentyp(df)
        elif menu_voranalyse =='3':
            clear()
            fehlende_daten(df)
        elif menu_voranalyse =='4':
            file_in_html(df)
        else:
            print('wrong input, please try again!')
            #voranalyse(df)
        
        restart = input('\nFurther pre-analysis: "y"\n?')
        if restart.lower() != 'y':
            break

# Set filters


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
    
    