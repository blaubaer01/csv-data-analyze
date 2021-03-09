#excluded needed packages
#import numpy as np
#import matplotlib.pyplot as plt
#from scipy.stats import shapiro
#from scipy.stats import stats
#import scipy as spy
#import statistics as stats
#import seaborn as sns
#import statsmodels.api as sm
#from statsmodels.formula.api import ols
#from outliers import smirnov_grubbs as grubbs


import pandas as pd
import os
from SPC_CPA import CPA
from L_REG import LREG
from table_functions import appendDFToCSV, mergecolumn, filter_typ, sort_column, transposed_table, crosstab, contingency_tb, seq_numbers_add, delrep_value, melt_table, df_rename, combine_column
from table_functions import delete_column, change_datatype, menu_rand_data
from regelkarte import x_chart, x_bar_s, x_bar_r, xmr_chart
from msa import msa_v1, msa_v2
from charts import groupby_balkendiagramm, balkendiagramm, kuchendiagramm, line_diagram_menu, boxplot, boxplot_groupby, boxplot2f, violin, violin_groupby, violin2f,single_swarmplot,  swarmplot1f, swarmplot2f, single_stripplot, stripplot1f, stripplot2f, histogram, scatter, scatter_w_r, scatter_joint_plot, qq_plot, groupplot_menu, pareto, pareto_one_column, pointplot1f, pointplot2f, confidencelinechart, threeddplot, distriplot1f, histogram1f, decriptive_statistics
from tests import mediantest, normality_test, correl, outliert, f_test, ttest_o_s, ttest_t_s, ttest_i, anova_o_w, anova_t_w
from table_calc import menu_calc
from rand_data import menu_rd
from tableview import fehlende_daten, datentyp, file_in_html, einzeldaten_anschauen , filter_in_html
from mft import clear, save_CSV_new, isinteger
from date_function import convert_datetime, cal_info

import webbrowser

from sys import platform

#alternatively, define the source
csv_dateien=['daten.csv']


#read all CSV datas in the root folder
def csv_daten_im_verzeichnis():
    
    
    for dat in os.listdir(os.getcwd()):
        if dat.endswith(".csv") or dat.endswith(".CSV"):
            csv_dateien.append(dat)
            print(dat)
            
    
    return(csv_dateien)

#set read the file and set custom CSV elements
def file_einlesen(fn):
    
    clear()
    f = open(fn, "r", errors='ignore')
    
    print('Preview to the first 2 lines: \n')
    print('first line:', f.readline())
    print('second line:', f.readline())
    print('#'*150)
    f.close
    
    #define structure
    while True:
        format_ist = input('Which separator is used by the file: \n1: Comma \n2: Semicolon \n3: Tab \n4: Space\n(choose number)\n?').lower()
        if format_ist == '1':
            trennzeichen = ','
            dezimalzeichen = '.'
            break
        elif format_ist == '2':
            trennzeichen = ';'
            #dezimalzeichen = ','
            while True:
                dezimalz = input('Which delimiter is used: \n1: floatcomma \n2: pointcomma \n(choose nr) \n?')
                if dezimalz =='1':
                    dezimalzeichen =','
                    break
                elif dezimalz =='2':
                    dezimalzeichen ='.'
                    break
                else:
                    print('wrong input, choose a number!')
            break
        elif format_ist == '3':
            trennzeichen = '\t'
            while True:
                dezimalz = input('Which delimiter is used: \n1: floatcomma \n2: pointcomma \n(choose nr) \n?')
                if dezimalz =='1':
                    dezimalzeichen =','
                    break
                elif dezimalz =='2':
                    dezimalzeichen ='.'
                    break
                else:
                    print('wrong input, choose a number!')
            break
        elif format_ist == '4':
            trennzeichen = '\s+'
            while True:
                dezimalz = input('Which delimiter is used: \n1: floatcomma \n2: pointcomma \n(choose nr) \n?')
                if dezimalz =='1':
                    dezimalzeichen =','
                    break
                elif dezimalz =='2':
                    dezimalzeichen ='.'
                    break
                else:
                    print('wrong input, choose a number!')
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
    df=pd.read_csv(fn,sep=trennzeichen ,decimal=dezimalzeichen, header=kopfz, engine='python')
    
    
    
    ###set filter
    ######################################################################################
    filter_setzen = input('Would you like to set any filter: y/n \n?')
    if filter_setzen =='y':
        clear()
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
            
            while True:
                inhalte_spalte= input('For which column you want to know the possible filter criteria \nchoose number! \n?')
                
                if not isinteger(inhalte_spalte):
                    print("Input is not an integer, please try again")
                else:
                    if int(inhalte_spalte) not in range(0,i):
                        print('wrong choise, choose number!')
                    else:
                        break
            
            
            
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
                break
                   
    ####################################################################################
    ####delete nan rows
    drop_yes = input('Do you want to drop all "NAN" rows in the dataframe y/n \n?')
    
    if drop_yes.lower() =='y':
        df = df.dropna()
        print('nan data deleted')
        
    else:
        print('no data deleted')
    
    ####################################################################################
    ###save cda_file
    print('...save current state!')
    fn = 'cda_' + fn
        
    df.to_csv(fn, sep=';', decimal=',', header =True, index=False)
    
    
    print(df)
    file_in_html(fn, df)
    next = input('push button for next steps')
    return(df)






#############################################################################



###############################################################################        
###Simple descriptive statistics        
###############################################################################


def beschreibende_stat(df):
    while True:
        clear()
        print('descriptive statistic')
        was_beschreibend_analysieren=input('What data do you want to analyze? \n1: all\n2: only the numerical\n3: one special column \n4: graphical (numerical) \n?')
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
        
        elif was_beschreibend_analysieren =='4':
            decriptive_statistics(df)
            
        
        
        
        else:
            print('wrong input, please try again!')
        
        
            
        
        
        restart = input('\nFurther descriptive analysis: y/n \n?')
        if restart.lower() != 'y':
            break
        


######################################################################
### menu of graphical plots
######################################################################
            
######################################################################        
### menu barcharts
def auswahl_balkendiagramm(df):
    clear()
    ausw_bd = input('Type of bar-chart: \n1: count column entries \n2: column grouped by 2 column entries \n(choose number) \n?')
    if ausw_bd =='1':
        balkendiagramm(df)
    elif ausw_bd =='2':
        groupby_balkendiagramm(df)
    else:
        print('wrong input!')
        
        

#######################################################################    
###menu categorigal data (boxplot, violinplot)
def menu_categorie_data(df):
    clear()
    menu_cd = input('Which Categorial Plot: \n1: Single Boxplot \n2: Boxplot by one factor \n3: Boxplot by two factors \n4: Single Violinplot \n5: Violinplot one factor \n6: Violinplot by two factors \n7: Single Swarmplot \n8: Swarmplot by one factor \n9: Swarmplot by two factors \n10: Single Stripplot \n11: Stripplot by one factor \n12: Stripplot by two factors  \n13: Pointplot by one factor \n14: Pointplot by two factors \n15: Distribution-Plot by one factor \n16: Histogram-Plot by one factor \n(choose a number) \n?')
    if menu_cd =='1':
        boxplot(df)
    elif menu_cd =='2':
        boxplot_groupby(df)
    elif menu_cd =='3':
        boxplot2f(df)
    elif menu_cd =='4':
        violin(df)
    elif menu_cd =='5':
        violin_groupby(df)
    elif menu_cd =='6':
        violin2f(df)
    elif menu_cd =='7':
        single_swarmplot(df)
    elif menu_cd =='8':
        swarmplot1f(df)
    elif menu_cd =='9':
        swarmplot2f(df)
    elif menu_cd =='10':
        single_stripplot(df)
    elif menu_cd =='11':
        stripplot1f(df)
    elif menu_cd =='12':
        stripplot2f(df)
    elif menu_cd =='13':
        pointplot1f(df)
    elif menu_cd =='14':
        pointplot2f(df)
    elif menu_cd =='15':
        distriplot1f(df)
    elif menu_cd =='16':
        histogram1f(df)
    
    else:
        print('Wrong input, try again!')


#######################################################################
### scatter plot menu        
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



#######################################################################
###pareto plot menu        
def menu_pareto(df):
    clear()
    menu_par = input('Choose Pareto: \n1: count column \n2: count values \n?')
    
    if menu_par == '1':
        pareto_one_column(df)
    if menu_par == '2':
        pareto(df)
    else:
        print('wrong input, try again!')
        
#######################################################################
###control-charts menu        
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

######################################################################    
###Main Menu graphical analysis
######################################################################
def menu_graphical_analyze(df):
    clear()
    print('Choose graphical view:')
    gr_view_list= ['Barchart', 'Piechart', 'Histogram', 'Q-Q-Plot', 'Linechart', 'Group-Plot', 'Scatter-Plot',  
                   'Categorical Plots',  
                   'Control-Charts', 'Pareto-Chart', 'Confidence Line-Chart', '3d-Plot']
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
        line_diagram_menu(df)
    elif ausw_gr_view =='5':
        groupplot_menu(df)
    elif ausw_gr_view =='6':
        menu_scatter(df)    
    elif ausw_gr_view =='7':
        menu_categorie_data(df)
    elif ausw_gr_view =='8':
        menu_spc_charts(df)
    elif ausw_gr_view =='9':
        menu_pareto(df)
    elif ausw_gr_view =='10':
        confidencelinechart(df)
    elif ausw_gr_view =='11':
        threeddplot(df)
    else:
        print('Wrong input, please try again')


######################################################################
###statistical test menu's
######################################################################
        
#######################################################################
###menu t-test
def ttest_menu(df):
    clear()
    print('t-Test \n')
    menu_ttest = input('Which kind of t-test: \n1: one sample t-Test \n2: two sample t-Test \n3: two independent samples t-Test \n(choose a number) \n?')    
    if menu_ttest =='1':
        ttest_o_s(df)
    elif menu_ttest =='2':
        ttest_t_s(df)
    elif menu_ttest =='3':
        ttest_i(df)
    else:
        print('Wrong input, try again!')



###############################################################################    
###anova menu
def ANOVA_menu(df):
    clear()
    print('ANOVA \n')
    anova_m = input('Which kind of ANOVA: \n1: one way ANOVA \n2: two way ANOVA \n(choose number) \n?')
    if anova_m =='1':
        anova_o_w(df)
    elif anova_m =='2':
        anova_t_w(df)
    else:
        print('Wrong input, try again!')
    
#######################################################################    
###Main menu test's
###############################################################################
def menu_tests(df):
    clear()
    print('Statistical Tests \n')
    what_kind_of_test = input('Which Test do you would like to do: \n1: Test for normal distribution  \n2: correlation all columns \n3: t-test \n4: f-test \n5: ANOVA \n6: Outlier-Test \n7: Median-Test \n(choose a number) \n?')
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
    elif what_kind_of_test =='7':
        clear()
        mediantest(df)
    else:
        print('Wrong input, try again!')

#######################################################################
###MSA menu
#######################################################################
def MSA(df):
    clear()
    print('Measurement System Analysis \n')
    menu_MSA = input('Choose MSA Version: \n1: MSA_V1 \n2: MSA_V2 \n(choose number) \n?')
    if menu_MSA =='1':
        msa_v1(df)
    elif menu_MSA =='2':
        msa_v2(df)
        #print('not available yet')


#######################################################################
### Main statistics menu
###############################################################################
def statistic(df):
    clear()
    change_datatype(df)
    
    while True:
        clear()
        print('\nStatitic Functions: \n')
        menu_statistic = input('What kind of statistics: \n1: simple descriptive statistics \n2: graphical view \n3: statistical significance tests \n4: process capability study \n5: linear regression study \n6: MSA (Measurement System Analysis) \n7: contingency table  \n(choose number)  \n?')
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
        
        restart = input('\nFurther statistic functions: "y"\n?')
        if restart.lower() != 'y':
            break
        
        

        


#######################################################################
###table preview menu
###############################################################################
def preview_table(fn, df):
    while True:
        clear()
        print('Table preview \n')
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
            file_in_html(fn, df)
        else:
            print('Wrong input, please try again!')
            #voranalyse(df)
        
        restart = input('\nFurther pre-analysis: "y"\n?')
        if restart.lower() != 'y':
            break

#######################################################################
###table function menu
###############################################################################
def table_functions(fn, df):
    while True:
        clear()
        #read the file
        print('open current file...')
        if 'cda_' in fn:
            df=pd.read_csv(fn,sep=';' ,decimal=',', header=0, engine='python')
            print('current file name: ' , fn)
        else:    
            fn = 'cda_' + fn
            df=pd.read_csv(fn,sep=';' ,decimal=',', header=0, engine='python')
            print('current file name: ' , fn)
        
        change_datatype(df)
        clear()
        print('Table Functions \n')
        menu_tf = input('Table Functions: \n1: preview \n2: append csv-file \n3: merge csv-file \n4: set filter \n5: sort by column \n6: transpose table \n7: crosstable \n8: easy table calculation \n9: add sequence number column \n10: convert datetime column \n11: get calendar info \n12: delete or replace value/characters \n13: melt columns \n14: rename column \n15: save to CSV-file \n16: combine factor columns \n17: delete column \n18: add random distribution-data \n?')
        
        if menu_tf =='1':
            clear()
            preview_table(fn, df)
        elif menu_tf =='2':
            clear()
            appendDFToCSV(fn, df, sep=",")
        elif menu_tf =='3':
            mergecolumn(df)
        elif menu_tf =='4':
            filter_typ(df)
        elif menu_tf =='5':
            sort_column(fn, df)
        elif menu_tf =='6':
            transposed_table(fn, df)
        elif menu_tf =='7':
            crosstab(df)
        elif menu_tf =='8':
            menu_calc(fn, df)
        elif menu_tf =='9':
            seq_numbers_add(fn, df)
        elif menu_tf =='10':    
            convert_datetime(df)
        elif menu_tf =='11':
            cal_info(df)
        elif menu_tf =='12':
            delrep_value(fn, df)
        elif menu_tf =='13':
            melt_table(df)
        elif menu_tf =='14':
            df_rename(fn, df)
        elif menu_tf =='15':
            save_CSV_new(df)
        elif menu_tf =='16':
            combine_column(fn, df)
        elif menu_tf =='17':
            delete_column(fn, df)
        elif menu_tf == '18':
            menu_rand_data(fn, df)
            
        
        
        
        else:
            print('Wrong input, please try again!')
            #voranalyse(df)
        
        restart = input('\nFurther table functions: "y"\n?')
        if restart.lower() != 'y':
            
            
            break
            






###############################################################################
### work with the data's (Main menu)
###############################################################################
def mit_daten_arbeiten(fn, df):
    
    while True:
        clear()
        #read the file
        print('open current file...\n')
        if 'cda_' in fn:
            df=pd.read_csv(fn,sep=';' ,decimal=',', header=0, engine='python')
            print('current file name: ' , fn)
        else:    
            fn = 'cda_' + fn
            df=pd.read_csv(fn,sep=';' ,decimal=',', header=0, engine='python')
            print('current file name: ' , fn)
        print('\n')
        m_d_a = input('Next Steps:\n1:Table Functions \n2:Statistics Analyze \np: preview table \nd: descriptice statistics \ng: grafical analyse \nt: statistical tests \n?')
        if m_d_a =='1':
            clear()
            table_functions(fn, df)
        elif m_d_a =='2':
            clear()
            statistic(df)
        elif m_d_a =='p':
            clear()
            preview_table(fn, df)
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
            
            
            
        
        restart = input('\nDo you want to analyze further?: y = yes / n = exit \n?')
        if restart.lower() != 'y':
            
            
            break

def menu_create_random_data():
    print('not available yet!')

        

#######################################################################
### main prog
###############################################################################
def main():
    
    df = pd.DataFrame()
    
    print("\033[1;37;40m \n")
    clear()
    print('#'*92)
    print('#                                                                                          #')
    print('#               CSV Data Analyze-Tool V2.6 (turtel) by Ricky Helfgen                       #')
    print('#      This is an open source project and is subject to the guidelines of GPL V3           #')
    print('#                           Analyze CSV-Data files with:                                   #')
    print('#   python3, pandas, numpy, matplotlib, seaborn, statsmodels, os-sys, scipy, webbrownser   #')
    print('#              Download under: https://github.com/blaubaer01/csv-data-analyze              #')
    print('#   More Infos: http://www.reh-webdesign.de/csv-data-analyze/howto/csv-data-analyze.html   #')
    print('#                                     Have Fun!                                            #')
    print('#                                                                                          #')
    print('#_|__________###____ _____|____###___####___#___#___###_____####___#####__####_____##______#')
    print('#_|________#######________|___#______#______#___#___#__#____#__#_____#_______#____#__#_____#')
    print('#_|_______#########_______|___#______####___#___#___#___#___####_____#____####___#____#____#')
    print('#_|_____#############_____|___#_________#____#_#____#__#____#__#_____#____#_______#__#_____#')
    print('#_|_#####################_|____###___####_____#_____###_____#__#_____#____####_##__##______#')
    print('#                                                                                          #')
    print('#'*92)
    
    
    while True:
        start = input('Start Menue \n1: Create random data \n2: Open exsisting csv-file (root folder) \n3: More infos about this app (Wiki) \n4: OMG, close this scary app \n(choose number) \n?')
        
        if start == '1':
            menu_rd(df)
            clear()
                
            print('#'*70)
            
            fn = 'new_cda_file.csv'
            df.to_csv(fn, sep=';', decimal=',', header =True)
            mit_daten_arbeiten(fn, df)
                       
            
            break
        
        elif start == '2':
            clear()
            print('The following CSV-Files are in the root-folder:')
            csv_daten_im_verzeichnis()
                        #print(csv_dateien)
            while True:
                
                fn = input('Which CSV file to import (pay attention to spelling)\n?')
                if fn in csv_dateien:
                    df=file_einlesen(fn)
                    break
                else:
                    print('File not found! Please check your Input! \npay attention to upper and lower case!')
                    #break
            clear()
                
            print('#'*70)
            mit_daten_arbeiten(fn, df)
            
            break
        
        elif start =='3':
            print('This function will start the Wiki -page of csv-data-analyze \nyou need internet connection to do that')
            
            url = 'https://github.com/blaubaer01/csv-data-analyze/wiki'
    
            if platform == "linux" or platform == "linux2":
                webbrowser.open_new_tab(url)
            elif platform == "darwin":
                file_location = "file:///" + url
                webbrowser.open_new_tab(file_location)
            elif platform == "win32":
                webbrowser.open_new_tab(url)
                
        
        
        elif start =='4':
            print("It's your decision ;-) , have a nice day!")
            break
                
        else:
            print('Wrong input, try again (Choose number)')
            



#######################################################################
###start main process
###############################################################################
if __name__ == '__main__':
    while True:
        main()
        restart = input('\nDo you want to re-start the app?: y = yes / n = exit \n?')
        if restart.lower() != 'y':
            break
        
    
    