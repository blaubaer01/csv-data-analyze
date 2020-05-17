import pandas as pd
import os
#import datetime
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from scipy.stats import stats
import scipy as spy
import statistics as stats
import pyspc
import webbrowser
import seaborn as sns
#import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from outliers import smirnov_grubbs as grubbs
from SPC_CPA import CPA
from L_REG import LREG
from table_functions import appendDFToCSV, mergecolumn, filter_setzen, sort_column, transposed_table, crosstab, contingency_tb
from regelkarte import x_chart, x_bar_s, x_bar_r, xmr_chart
from msa import msa_v1, msa_v2
from charts import pareto_plot

#alternatively, define the source
csv_dateien=['daten.csv']

#############################################################################
###main functions
#############################################################################
#read all CSV datas in the root folder
def csv_daten_im_verzeichnis():
    
    
    for dat in os.listdir(os.getcwd()):
        if dat.endswith(".csv") or dat.endswith(".CSV"):
            csv_dateien.append(dat)
            print(dat)
            
    
    return(csv_dateien)
            
        
###zahl überprüfen
def isfloat(x):
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True


#set read the file and set custom CSV elements
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
    while True:
        format_ist = input('Which separator is used by the file: \n1: Comma / 2: Semicolon \n(choose number)\n?').lower()
        if format_ist == '1':
            trennzeichen = ','
            dezimalzeichen = '.'
            break
        elif format_ist == '2':
            trennzeichen = ';'
            dezimalzeichen = ','
            break
        else:
            print('Wrong input, please try again')
        #file_einlesen(auswahl_datei)
    
    #custom header
    kopfzeile = input('Is there a header: y/n \n?').lower()
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
    
    ###set filter
    ######################################################################################
    filter_setzen = input('Would you like to set any filter: y/n \n?')
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
                    csvfilename = input('Filename (.csv will save automaticly) \n?')
                    fn = csvfilename + '.csv'
                    df.to_csv(fn, sep=';', decimal=',', header =True)
                if speichern_ja.lower() =='n':
                    break
            else:
                return(df)
    
    
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
                return(df)
                break
            #else: 
             #   return(df)
                   
    
    
    return(df)


### define our clear function 
#############################################################################
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 



#############################################################################
###pre-view functions
##############################################################################        
        
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




# all single data
##############################################################################
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
        
###Look at header and first data
################################################################################
def first_row(df):
    clear()
    print('first row view')
    print(df.iloc[0,:])
    

###View individual data
################################################################################
def einzeldaten_anschauen(df):
    eind = input('What do you want to see \n1: first row\n2: all cycle of 5 rows\n(choose a number) \n?' )
    if eind=='1':
        first_row(df)
    elif eind =='2':
        ind_trip_data(df)
    else:
        print('wrong input, please try again!')
        #einzeldaten_anschauen(df)



###############################################################################        
###Simple descriptive statistics        
###############################################################################
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
            nummer_spalte= input('Which column do you want to see: \n(choose number) \n?')
            try:
                print('Simple descriptive statiatics: \n')
                print(df[list_columns[int(nummer_spalte)]].describe(include='all'))
            except IndexError as error:
                print('wrong input, please try again!')
            except Exception as exception:
                print('wrong input, please try again!')
        else:
            print('wrong input, please try again!')
            
        
        
        restart = input('\nFurther describtive analysis: y/n \n?')
        if restart.lower() != 'y':
            break
        
        
        
##################################################################################
#graphical analyze
##################################################################################

####bar charts
### groupby barchart
#################################################################################

def groupby_balkendiagramm(df):
    
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
        nummer_spalte= input('Which column do you want to see: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
    
    while True:
        groupby_spalte = input('Group by column: \n(choose number) \n?')
        if groupby_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break
        
    df.groupby([list_columns[int(nummer_spalte)],list_columns[int(groupby_spalte)]]).size().unstack().plot(kind='bar',stacked=True)
    label_chart = (list_columns[int(nummer_spalte)] + ' grouped by count ' + list_columns[int(groupby_spalte)])
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()
    
    #df.groupby('state')['name'].nunique().plot(kind='bar')
    #plt.show()


### barcharts
###############################################################################
def balkendiagramm(df):
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
        nummer_spalte= input('Which column do you want to see: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break    
    
    
    ax = df[list_columns[int(nummer_spalte)]].value_counts().plot(kind='bar',
                                    figsize=(14,8),
                                    title=list_columns[int(nummer_spalte)], color='blue')
    ax.set_xlabel(list_columns[int(nummer_spalte)])
    ax.set_ylabel("Frequency")
    plt.show()

### menu barcharts
###############################################################################
def auswahl_balkendiagramm(df):
    clear()
    ausw_bd = input('Type of bar-chart: \n1: count column entries \n2: column grouped by 2 column entries \n(choose number) \n?')
    if ausw_bd =='1':
        balkendiagramm(df)
    elif ausw_bd =='2':
        groupby_balkendiagramm(df)
    else:
        print('wrong input!')

        
###pie charts
###############################################################################        
def kuchendiagramm(df):
    clear()
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
        nummer_spalte= input('Which column do you want to see: \n(choose number) \n?')
        if nummer_spalte not in list_number:
            print('wrong input, try again!')
        else:
            break    
    
        
    # Plot
    ax = df[list_columns[int(nummer_spalte)]].value_counts().plot(kind='pie',
                                    figsize=(14,8),
                                    title=list_columns[int(nummer_spalte)], autopct='%1.1f%%')
    #ax.set_xlabel(list_columns[int(nummer_spalte)])
    ax.set_ylabel("Frequency")
    
    
    plt.show()


###line-chart
#################################################################################
def liniendiagramm(df):
    clear()
    kategorie=df.select_dtypes(include=['object', 'datetime', 'int'])
    werte = df.select_dtypes(exclude=['object'])
    
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
        value_column= input('Which value column do you want to see: \n(choose number)\n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number = []
    i=1
    
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        list_number.append(str(i))
        print(i, kategorie.columns[i])
        i+=1
    
    
    while True:
        groupby_column = input('Group by column: \n(choose number) \n?')
        if groupby_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
      
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    
    
    df.plot(x, y, grid=True)
    
    plt.show()

###boxplots and violinplots
################################################################################
def boxplot(df):
    clear()
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    
    df.boxplot(column=y, widths=0.5)
    plt.show()

###boxplot with group
################################################################################
def boxplot_groupby(df):
    clear()
    kategorie=df.select_dtypes(include=['object'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    
    while True:
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    clear()
    #
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
        groupby_column = input('Group by column: \n(choose number) \n?')
        if groupby_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    
    df.boxplot(by=x, column=y)
    
    plt.show()
    
    
###violin plot
################################################################################    
def violin(df):
    clear()
    sns.set(style="whitegrid")
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    while True:
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    
    y = list_columns_werte[int(value_column)]
    
    sns.violinplot(x=df[y])
    plt.show()

###violin plot with group
###############################################################################
def violin_groupby(df):
    clear()
    sns.set(style="whitegrid")
    kategorie=df.select_dtypes(include=['object'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    
    while True:
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number = []
    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        list_number.append(str(i))
        print(i, kategorie.columns[i])
        i+=1
    
    
    while True:
        groupby_column = input('Group by column: \n(choose number) \n?')
        if groupby_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    
    
    sns.violinplot(x=x, y=y, data=df)
    
    plt.show()

###swarmplot
###############################################################################
def swarm_plot(df):
    clear()
    sns.set(style="whitegrid", palette="muted")

    kategorie=df.select_dtypes(include=['object'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    clear()
    #
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
        groupby_column = input('Group by column: \n(choose number) \n?')
        if groupby_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    y = df[list_columns_werte[int(value_column)]]
    x = df[list_columns_kategorie[int(groupby_column)]]
    
    
    # Draw a categorical scatterplot to show each observation
    sns.swarmplot(x=x, y=y, data=df)
    #sns.boxplot(x=x, y=y, data=df, whis=np.inf)
    plt.show()

    
###menu categorigal data (boxplot, violinplot)
###############################################################################
def menu_categorie_data(df):
    clear()
    menu_cd = input('Which Boxplox: \n1: Single Boxplot \n2: Boxplot by group \n3: Violin-Plot \n4: Violinplot by group \n5: Swarm-Plot \n(choose a number) \n?')
    if menu_cd =='1':
        boxplot(df)
    elif menu_cd =='2':
        boxplot_groupby(df)
    elif menu_cd =='3':
        violin(df)
    elif menu_cd =='4':
        violin_groupby(df)
    elif menu_cd =='5':
        swarm_plot(df)
    else:
        print('Wrong input, try again!')


################################################################################
###visual distribution and values
###histogram
################################################################################
def histogram(df):
    clear()
    sns.set(color_codes=True)

        
    werte = df.select_dtypes(exclude=['object'])
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
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
    list_number =[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    while True:
        value_column_y= input('y-value: \n(choose number) \n?')
        if value_column_y not in list_number:
            print('wrong input, try again!')
        else:
            break  
    while True:
        value_column_x= input('x-value: \n(choose number) \n?')
        if value_column_x not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    y = list_columns_werte[int(value_column_y)]
    
    x = list_columns_werte[int(value_column_x)]
    
    
    
    #df.hist(column=y)
    df.plot.scatter(y,x) # Histogram will now be normalized
    label_chart = ('Scatter-Plot')
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()

###scatter plot with regression line
###############################################################################    
def scatter_w_r(df):
    clear()
    sns.set(color_codes=True)        
    
    
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column_y= input('y-value: \n(choose number) \n?')
        if value_column_y not in list_number:
            print('wrong input, try again!')
        else:
            break  
    while True:
        value_column_x= input('x-value: \n(choose number) \n?')
        if value_column_x not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
        
    y = df[list_columns_werte[int(value_column_y)]]
    
    x = df[list_columns_werte[int(value_column_x)]]
    


    sns.regplot(x=x, y=y, data=df);


    
    label_chart = ('Linear-Regression-Plot')
    plt.title(label_chart, fontdict=None, loc='center', pad=None)
    plt.show()


###jointplot
###############################################################################
def scatter_joint_plot(df):
    clear()
    sns.set(color_codes=True)        
    
    
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column_y= input('y-value: \n(choose number) \n?')
        if value_column_y not in list_number:
            print('wrong input, try again!')
        else:
            break  
    while True:
        value_column_x= input('x-value: \n(choose number) \n?')
        if value_column_x not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    y = df[list_columns_werte[int(value_column_y)]]
    
    x = df[list_columns_werte[int(value_column_x)]]
    


    sns.jointplot(x=x, y=y, data=df, kind="reg");

    plt.show()

def menu_scatter(df):
    clear()
    m_scatter = input('Scatter-Plot: \n1: scatter only \n2: regression plot \n3: regression_jointplot \n(choose number) \n?')
    if m_scatter =='1':
        scatter(df)
    elif m_scatter =='2':
        scatter_w_r(df)
    elif m_scatter =='3':
        scatter_joint_plot(df)
    else:
        print('Wrong input,please try again!')



    
###qq-plot
###############################################################################
def qq_plot(df):
    clear()
    werte = df.select_dtypes(exclude=['object'])
    
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    y = df[list_columns_werte[int(value_column)]]
    
    spy.stats.probplot(y, dist="norm", plot=plt)
    plt.show() 


###Group Plot (show a plot by group)
###############################################################################    
def groupplot(df):
    clear()
    sns.set(style="ticks")

    
    kategorie=df.select_dtypes(exclude=['float'])
    werte = df.select_dtypes(exclude=['object'])
    zeitraum=df.select_dtypes(include=['object', 'datetime'])
    
    #
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    clear()
    #
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
        groupby_column = input('Group by column: \n(choose number) \n?')
        if groupby_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    anz_col_zeitraum = len(zeitraum.columns)
        
    list_columns_zeitraum = []
    list_number = []
    i=1
    for i in range(anz_col_zeitraum):
        list_columns_zeitraum.append(zeitraum.columns[i])
        list_number.append(str(i))
        print(i, zeitraum.columns[i])
        i+=1
    
    while True:
        datetime_column = input('Choose the Datetime-column \n(choose number) \n?')
        if datetime_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    z = list_columns_zeitraum[int(datetime_column)]
    
    df = df.sort_values(by=z, ascending=1)
    
    
    
    
    anz = df[x].nunique()    
    
    sns.relplot(x=z, y=y, hue=x, data=df, palette=sns.color_palette("Set1", anz))
    
    plt.xlim(df[list_columns_zeitraum[int(datetime_column)]].iloc[0], df[list_columns_zeitraum[int(datetime_column)]].iloc[-1])

    plt.show()
    

def pareto(df):
    
    clear()
    
    kategorie=df.select_dtypes(exclude=['float'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    
    while True:
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    clear()
    #
    anz_col_kategorie = len(kategorie.columns)
        
    list_columns_kategorie = []
    list_number = []
    i=1
    for i in range(anz_col_kategorie):
        list_columns_kategorie.append(kategorie.columns[i])
        list_number.append(str(i))
        print(i, kategorie.columns[i])
        i+=1
    
    
    while True:
        groupby_column = input('Group by column: \n(choose number) \n?')
        if groupby_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    
    df = df.groupby([x])[y].sum()
    df = df.reset_index()
    df= df.sort_values(y, ascending=False)
    df[x]=df[x].astype(str)
    
    print(df)
    pareto_plot(df, x=x, y=y, title='Pareto Chart')


def pareto_one_column(df):
    
    clear()
    
    werte = df.select_dtypes(exclude=['float'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    
    while True:
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    y = list_columns_werte[int(value_column)]
    
    
    
    df2 = df[y].value_counts()
    df2 = df2.reset_index()
    x = 'index'
    
    df2= df2.sort_values([y], ascending=False)
    df2[x]=df2[x].astype(str)
    
    
    print(df2)
    pareto_plot(df2, x=x, y=y, title='Pareto Chart')


def menu_pareto(df):
    clear()
    menu_par = input('Choose Pareto: \n1: count column \n2: count values \n?')
    
    if menu_par == '1':
        pareto_one_column(df)
    if menu_par == '2':
        pareto(df)
    else:
        print('wrong input, try again!')
        
    
def menu_spc_charts(df):
    
    clear()
    print('Choose graphical view:')
    gr_view_list= ['X-Chart','X-bar-s-Chart', 'X-bar-R-Chart', 'XmR-Chart']
    for i in range(len(gr_view_list)):
        print(i, gr_view_list[i])
        i+=1
    ausw_gr_view = input('Which Control-Chart: \n(choose a number) \n?')
    
    if ausw_gr_view =='0':
        x_chart(df)
    if ausw_gr_view =='1':
        x_bar_s(df)
    if ausw_gr_view =='2':
        x_bar_r(df)
    if ausw_gr_view =='3':
        xmr_chart(df)
    
    
    else:
        print('Wrong input, please try again')

    
###Menu graphical analysis
#################################################################################
def menu_graphical_analyze(df):
    clear()
    print('Choose graphical view:')
    gr_view_list= ['Barchart', 'Piechart', 'Histogram', 'Q-Q-Plot', 'Linechart', 'Group-Plot', 'Scatter-Plot',  
                   'Categorial Plots',  
                   'Control-Charts', 'Pareto-Chart']
    for i in range(len(gr_view_list)):
        print(i, gr_view_list[i])
        i+=1
    ausw_gr_view = input('Which graphical form of analysis \n(choose a number) \n?')
    
    if ausw_gr_view =='0':
        auswahl_balkendiagramm(df)
    elif ausw_gr_view =='1':
        kuchendiagramm(df)
    elif ausw_gr_view =='2':
        histogram(df)
    elif ausw_gr_view =='3':
        qq_plot(df)
    elif ausw_gr_view =='4':
        liniendiagramm(df)
    elif ausw_gr_view =='5':
        groupplot(df)
    elif ausw_gr_view =='6':
        menu_scatter(df)    
    elif ausw_gr_view =='7':
        menu_categorie_data(df)
    elif ausw_gr_view =='8':
        menu_spc_charts(df)
    elif ausw_gr_view =='9':
        menu_pareto(df)
        #print('currently not available')
    else:
        print('Wrong input, please try again')

        
###############################################################################
###Statistical Tests
###############################################################################        
        
###test of normality
###############################################################################
def normality_test(df):
    clear()
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column= input('Which value column do you want to verify: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
        
    y = df[list_columns_werte[int(value_column)]]
    
    
    stat, p = shapiro(y)
    
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
        decision = 'Sample looks Gaussian (fail to reject H0)'
    else:
        print('Sample does not look Gaussian (reject H0)')
        decision = 'Sample does not look Gaussian (reject H0)'
    

    eintrag = 'Shapiro-Wilk - Test:' + '\nStatistics: ' + str(stat) + '\np-Value: ' + str(p) + '\ndecision: ' + decision
    
    plt.figure(figsize=(6,2))
    plt.subplot(211)
    spy.stats.probplot(y, dist="norm", plot=plt)
    
    plt.subplot(212)
    plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.show() 

###correlation test
###############################################################################
def correl(df):
    clear()
    correlation_df = df.corr()
    print(correlation_df)
    
    
    
###Grubbs outlier test
###############################################################################
def outliert(df):
    
    sns.set(color_codes=True)
    
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column= input('Which value column do you want to verify: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    y = df[list_columns_werte[int(value_column)]]
    print('Value could be outlier:',grubbs.max_test_outliers(y, alpha=0.05))
    
       
    
    eintrag = 'Grubbs-Outlier Test' + '\nValue could be outlier:' + str(grubbs.max_test_outliers(y, alpha=0.05))
    
    plt.figure(figsize=(6,2))
    plt.subplot(211)
    sns.boxplot(x=y)
    plt.subplot(212)
    plt.text(0.1,0.5,eintrag, 
                     ha='left', va='center',
                     fontsize=12)
    plt.axis('off')
    plt.show()    

###f-test
###############################################################################    
def f_test(df):
    clear()
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column_a= input('a-value: \n(choose number) \n?')
        if value_column_a not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        value_column_b= input('b-value: \n(choose number) \n?')
        if value_column_b not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    d1 = df[list_columns_werte[int(value_column_a)]]
    
    d2 = df[list_columns_werte[int(value_column_b)]]
    
    
    
    f, p = spy.stats.f_oneway(d1, d2)
    
    
    print('f-Test:')
    
    print('F-Value:' ,f)
    print('p-value:' ,p)
    
    
    
    
    alpha = 0.05
    if p > alpha:
        print('Variances should be equal (fail to reject H0)')
    else:
        print('Variances should not be equal (reject H0)')    

    
###one single t-test
###############################################################################
def ttest_o_s(df, alpha=0.05, alternative='greater'):
    clear()
    
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column= input('Which value column do you want to verify: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        target_value = input('Input taget mean-value \n(choose point-comma \n?')
    
        if not isfloat(target_value):
            print("Target mean value is not a number with point-comma, please try again")
        else:
            break
    
    
    y = df[list_columns_werte[int(value_column)]]
    
    try:
        t, p = spy.stats.ttest_1samp(y, float(target_value))
    
    
        print('One sample t-Test:')
        print ('t-Value:',t)
        print ('p-Value:',p)
    
        alpha = 0.05
        if p > alpha:
            print('Means should not be different (fail to reject H0)')
        else:
            print('Means should be different (reject H0)')    
    except Exception as exception:
                print('Wrong input (choose point-comma), please try again!')
    
    
###two sided t-test
###############################################################################
def ttest_t_s(df):
    clear()
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column_a= input('a-value: \n(choose number) \n?')
        if value_column_a not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        value_column_b= input('b-value: \n(choose number) \n?')
        if value_column_b not in list_number:
            print('wrong input, try again!')
        else:
            break  
        
    a = df[list_columns_werte[int(value_column_a)]]
    b = df[list_columns_werte[int(value_column_b)]]
    
    
    
    try:
        t, p = spy.stats.ttest_rel(a,b)
    
    
        print('Two sample t-Test:')
        print ('t-Value:',t)
        print ('p-Value:',p)
    
        alpha = 0.05
        if p > alpha:
            print('Means should not be different (fail to reject H0)')
        else:
            print('Means should be different (reject H0)')    
    except Exception as exception:
                print('Wrong input (choose point-comma), please try again!')
                
    
    
                
###indipendent t-test
###############################################################################    
def ttest_i(df):
    clear()
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column_a= input('a-value: \n(choose number) \n?')
        if value_column_a not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        value_column_b= input('b-value: \n(choose number) \n?')
        if value_column_b not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    a = df[list_columns_werte[int(value_column_a)]]
    b = df[list_columns_werte[int(value_column_b)]]
    
    
    try:
        t, p = spy.stats.ttest_ind(a,b, equal_var = False)
    
    
        print('Two sample t-Test (for the means of two independent samples of scores):')
        print ('t-Value:',t)
        print ('p-Value:',p)
    
        alpha = 0.05
        
        if p > alpha:
            print('Means should not be different (fail to reject H0)')
        else:
            print('Means should be different (reject H0)')    
    except Exception as exception:
                print('Wrong input, please try again!')

    


###menu t-test
###############################################################################    
def ttest_menu(df):
    clear()
    menu_ttest = input('Which kind of t-test: \n1: one sample t-Test \n2: two sample t-Test \n3: two independent samples t-Test \n(choose a number) \n?')    
    if menu_ttest =='1':
        ttest_o_s(df)
    elif menu_ttest =='2':
        ttest_t_s(df)
    elif menu_ttest =='3':
        ttest_i(df)
    else:
        print('Wrong input, try again!')

###One way ANOVA    
###############################################################################    
def anova_o_w (df):
    clear()
    
    kategorie=df.select_dtypes(include=['object', 'int'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
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
        value_column= input('Which value column do you want to see: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    clear()
    #
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
        groupby_column = input('Group by column: \n(choose number) \n?')
        if groupby_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    y = list_columns_werte[int(value_column)]
    x = list_columns_kategorie[int(groupby_column)]
    
    mod = ols(y + '~' + x,
                data=df).fit()
                
    aov_table = sm.stats.anova_lm(mod, typ=2)
    print('one way ANOVA Result:' )
    print (aov_table)
    
    
    
    
    
    #aov_pyvttbl = pyvttbl.Dataframe.anova1way(y, x)
    #print (aov_pyvttbl)
    
###Two way ANOVA    
###############################################################################    
def anova_t_w(df):
    clear()
    kategorie=df.select_dtypes(exclude=['float'])
    werte = df.select_dtypes(exclude=['object'])
    
    #
    anz_col_werte = len(werte.columns)
        
    list_columns_werte = []
    list_number=[]
    i=1
    for i in range(anz_col_werte):
        list_columns_werte.append(werte.columns[i])
        list_number.append(str(i))
        print(i, werte.columns[i])
        i+=1
    
    
    while True:
        value_column= input('Which value column do you want to compare: \n(choose number) \n?')
        if value_column not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    clear()
    #
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
        faktor1 = input('Factor1: \n(choose number) \n?')
        if faktor1 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    while True:
        faktor2 = input('Factor2: \n(choose number) \n?')
        if faktor2 not in list_number:
            print('wrong input, try again!')
        else:
            break  
    
    
    
    y = list_columns_werte[int(value_column)]
    a = list_columns_kategorie[int(faktor1)]
    b = list_columns_kategorie[int(faktor2)]
    
    mod = ols(y + '~C(' + a + ')*C(' + b +')',
                data=df).fit()

    # Seeing if the overall model is significant
    print(f"Overall mod F({mod.df_model: .0f},{mod.df_resid: .0f}) = {mod.fvalue: .3f}, p = {mod.f_pvalue: .4f}")    
    
    mod.summary()
        
    aov_table = sm.stats.anova_lm(mod, typ=2)
    print('two way ANOVA Result:' )
    print (aov_table)
    

###############################################################################    
def ANOVA_menu(df):
    clear()
    anova_m = input('Which kind of ANOVA: \n1: one way ANOVA \n2: to way ANOVA \n(choose number) \n?')
    if anova_m =='1':
        anova_o_w(df)
    elif anova_m =='2':
        anova_t_w(df)
    else:
        print('Wrong input, try again!')
    
###Menu tests
###############################################################################
def menu_tests(df):
    clear()
    what_kind_of_test = input('Which Test do you would like to do: \n1: Test of normality  \n2: correlation \n3: t-test \n4: f-test \n5: ANOVA \n6: Outlier-Test\n(choose a number) \n?')
    if what_kind_of_test =='1':
        clear()
        normality_test(df)
    elif what_kind_of_test =='2':
        clear()
        correl(df)
    elif what_kind_of_test =='3':
        ttest_menu(df)
    elif what_kind_of_test =='4':
        clear()
        f_test(df)
    elif what_kind_of_test =='5':
        clear()
        ANOVA_menu(df)
    elif what_kind_of_test =='6':
        clear()
        outliert(df)
    
    else:
        print('Wrong input, try again!')


def MSA(df):
    clear()
    menu_MSA = input('Choose MSA Version: \n1: MSA_V1 \n2: MSA_V2 \n(choose number) \n?')
    if menu_MSA =='1':
        msa_v1(df)
    elif menu_MSA =='2':
        msa_v2(df)
        #print('not available yet')



### statistics menu
###############################################################################
def statistic(df):
    clear()
    menu_statistic = input('What kind of statistics: \n1: simple descriptive statistics \n2: graphical view \n3: tests \n4: process capability analysis \n5: linear regression analysis \n6: MSA \n7: contingency table  \n(choose number)  \n?')
    if menu_statistic =='1':
        beschreibende_stat(df)
    elif menu_statistic =='2':
        menu_graphical_analyze(df)
    elif menu_statistic =='3':
        menu_tests(df)
    elif menu_statistic =='4':
        CPA(df)
    elif menu_statistic =='5':
        LREG(df)
    elif menu_statistic =='6':
        MSA(df)
    elif menu_statistic =='7':
        contingency_tb(df)
    else:
        print('wrong input, please try again!')
        statistic(df)

        



###table preview
###############################################################################
def preview_table(df):
    while True:
        clear()
        menu_voranalyse = input('Preview Menu: \n1: Single-view \n2: Datatype \n3: Missing-Datas \n4: show Data in HTML \n?')
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
            print('Wrong input, please try again!')
            #voranalyse(df)
        
        restart = input('\nFurther pre-analysis: "y"\n?')
        if restart.lower() != 'y':
            break

###table function menu
###############################################################################
def table_functions(df):
    while True:
        clear()
        menu_tf = input('Table Functions: \n1: preview \n2: append csv-file \n3: merge csv-file \n4: set filter \n5: sort by column \n6: transpose table \n7: crosstable \n?')
        if menu_tf =='1':
            clear()
            preview_table(df)
        elif menu_tf =='2':
            clear()
            appendDFToCSV(df, sep=",")
        elif menu_tf =='3':
            mergecolumn(df)
        elif menu_tf =='4':
            filter_setzen(df)
        elif menu_tf =='5':
            sort_column(df)
        elif menu_tf =='6':
            transposed_table(df)
        elif menu_tf =='7':
            crosstab(df)
        else:
            print('Wrong input, please try again!')
            #voranalyse(df)
        
        restart = input('\nFurther pre-analysis: "y"\n?')
        if restart.lower() != 'y':
            break



###############################################################################
### work with the data's (Main menu)
###############################################################################
def mit_daten_arbeiten(df):
    while True:
        clear()
        m_d_a = input('Next Steps:\n1:Table Functions \n2:Statistics Analyze \n?')
        if m_d_a =='1':
            clear()
            table_functions(df)
        elif m_d_a =='2':
            clear()
            statistic(df)
        elif m_d_a =='p':
            clear()
            preview_table(df)
        elif m_d_a =='d':
            clear()
            beschreibende_stat(df)
        elif m_d_a =='g':
            clear()
            menu_graphical_analyze(df)
        elif m_d_a =='t':
            clear()
            menu_tests(df)    
        else:
            print('Wrong input, please try again!')
            #mit_daten_arbeiten(df)
            
            
            
        
        restart = input('\nDo you want to analyze further?: y/n \n?')
        if restart.lower() != 'y':
            break
        


### main prog
###############################################################################
def main():
    while True:
        print("\033[1;37;40m \n")
        clear()
        #choosesource(source)
        print('#'*80)
        print('CSV Data Analyze-Tool V0.2 (by Ricky Helfgen) \nThis is an open source project and is subject to the guidelines of GPL V3')
        print('This tool is used for data analysis of CSV files with python3,\n and packages:os, numpy, webbrowser, pandas, scipy, matplotlib, seaborn, pyspc')
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
                   
        
        restart = input('\nDo you want to analyze another CSV file: y/n \n?')
        if restart.lower() != 'y':
            break
          




###start main process
###############################################################################
if __name__ == '__main__':
    main()
    
    