import pandas as pd
#import shutil
import os
#import datetime
#import tkinter as tk
# import only system from os 



#Alternativquelle definieren
csv_dateien=['daten.csv']

#Quelle waehlen und als "source" speichern
def csv_daten_im_verzeichnis():
    #csv_dateien = []
    
    for dat in os.listdir(os.getcwd()):
        if dat.endswith(".csv") or dat.endswith(".CSV"):
            csv_dateien.append(dat)
            print(dat)
            
    
    return(csv_dateien)
            
        


def file_einlesen(auswahl_datei):
    
    #Format festlegen
    format_ist = input('Welches Trennzeichen nutzt die Datei: \n1: Komma / 2: Semikolon \n?').lower()
    if format_ist == '1':
        trennzeichen = ','
        dezimalzeichen = '.'
    elif format_ist == '2':
        trennzeichen = ';'
        dezimalzeichen =','
    else:
        trennzeichen =','
        dezimalzeichen ='.'
    
    #print(trennzeichen, " ", dezimalzeichen)
    #Kopfzeile
    kopfzeile = input('Gibt es eine Kopfzeile \n"j"/"n" \n?').lower()
    if kopfzeile == 'j':
        kopfz = 0
    elif kopfzeile =='n':
        kopfz = None
    else:
        kopfz = 0
        
    
    #Dateieinlesen
    df=pd.read_csv(auswahl_datei,sep=trennzeichen ,decimal=dezimalzeichen, header=kopfz)
    #print(csv_daten)
    
    return(df)


# define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

# all single data
def ind_trip_data(df):
    y=0
    while y < (len(df)):
        a = y
        for i in range(5):
            print(df.iloc[a,:])
            a +=1
        y += 5
                   
        end_data = input('Weitere Datensätze? \nDrücke "ENTER" für "Ja" oder "n" für "Nein" \n?')
        if (len(df)) <y+5:
            rest = abs((len(df))-y)
            #print(rest, y)
            for i in range(rest):
                print(df.iloc[a,:])
                a +=1
            print('Das Ende der Tabelle ist erreicht !')
            break
        if end_data.lower() == 'n':
            break
        
#Kopfzeile und erste Daten anschauen
def first_row(df):
    print(df.iloc[0,:])
    

#Einzeldaten anschauen
def einzeldaten_anschauen(df):
    eind = input('Was möchten Sie sehen \n1: erste Reihe\n2: alles je 5 Reihen\n?' )
    if eind=='1':
        first_row(df)
    elif eind =='2':
        ind_trip_data(df)
    else:
        first_row(df)
        
# Einfache beschreibende Statitik        
def beschreibende_stat(df):
    clear()
    print('Beschreibende Statistik \n', df.describe(include="all"))

def statistic(df):
    clear()
    menu_statistic = input('Welche Art der Statistik: \n1:Beschreibende Statistik \n2:Grafische Darstellung \n?')
    if menu_statistic =='1':
        beschreibende_stat(df)
        
def fehlende_daten(df):
    clear()
    print('Überprüfung auf fehlende Daten ergab folgendes Ergebnis: \n',    df.isnull().sum())

def datentyp(df):
    clear()
    print('Überischt der Datenformate: \n', df.dtypes)

def voranalyse(df):
    while True:
        clear()
        menu_voranalyse = input('Wie möchtest du die Daten anschauen: \n1:Einzeldaten \n2:Datenformat \n3:fehlende Daten \n?')
        if menu_voranalyse =='1':
            clear()
            einzeldaten_anschauen(df)
        elif menu_voranalyse =='2':
            clear()
            datentyp(df)
        elif menu_voranalyse =='3':
            clear()
            fehlende_daten(df)
        restart = input('\nWeitere Voranalyse: "j"\n?')
        if restart.lower() != 'j':
            break

# Daten filtern (Baustelle)
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
                     
        inhalte_spalte= input('Zu welcher Spalte möchtest du die möglichen Filterkriterien erfahren \nbitte Nummer auswählen \n?')
        print(df.iloc[:,int(inhalte_spalte)].value_counts())
        
        filter_ja = input('Hierzu einen Filter setzen: j/n \n?')
        if filter_ja =='j':
            name_filter=input('Name/Wert des Filters(Auf Groß und Kleinschreibung achten: \n?')
            df = df[df.iloc[:,int(inhalte_spalte)]==name_filter]
            
        restart = input('\nWeitere Filter setzen: j/n.\n?')
        if restart.lower() != 'j':
            speichern_ja = input('Tabelle mit gesetzten Filtern speichern: j/n \n?')
            if speichern_ja =='j':
                csvfilename = input('Filename \n?')
                fn = csvfilename + '.csv'
                df.to_csv(fn, sep=';', decimal=',', header =True)
                
            #break
            tabelle_m_f_uebernehmen = input('Sollen die Filter zur weiteren Analyse zur Verfügung stehen: j/n \n?')
            if tabelle_m_f_uebernehmen =='j':
                return(df)
        
def mit_daten_arbeiten(df):
    while True:
        clear()
        m_d_a = input('Welche Art der Analyse möchten sie durchführen\n1:Voranalyse \n2:Filter setzen \n3:Statistik \n?')
        if m_d_a =='1':
            clear()
            voranalyse(df)
        elif m_d_a =='2':
            clear()
            filter_setzen(df)
        elif m_d_a =='3':
            clear()
            statistic(df)
            
            
        
        restart = input('\nMöchtest du weiter analysieren: j/n.\n?')
        if restart.lower() != 'j':
            break
        


# Programm-Ablauf
def main():
    while True:
        print("\033[1;37;40m \n")
        clear()
        #choosesource(source)
        print('#'*80)
        print('CSV Daten Analyse-Tool V0.1 (by Ricky Helfgen) \nDies ist ein Open Source Projekt und unterliegt den Richtlinien der GPL V3')
        print('Dieses Tool dient der Datenanalyse von CSV-Dateien')
        print('Have Fun!')
        print('#'*80)
        
              
        print('Folgende CSV-Dateien zur zur Auswahl, welche möchten sie auswerten?')
        csv_daten_im_verzeichnis()    
    
        #print(csv_dateien)
        auswahl_datei = input('Welchen CSV-File einlesen (auf Schreibweise achten)\n?')
        if auswahl_datei in csv_dateien:
            df=file_einlesen(auswahl_datei)
        else:
            print('Datei nicht gefunden! Bitte überprüfen Sie ihre Eingabe! \nachten sie auf Groß und-Keinschreibung!')
            #break
            main()
        
        clear()
                    
        print('#'*70)
        mit_daten_arbeiten(df)
                   
        
        restart = input('\nMöchtest du eine weitere CSV-Datei analysieren: j/n.\n?')
        if restart.lower() != 'j':
            break
          




#Hauptprozesse starten
if __name__ == '__main__':
    main()
    
    