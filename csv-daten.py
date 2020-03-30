import pandas as pd
#import shutil
import os
#import datetime
#import tkinter as tk


#Alternativquelle definieren
source='daten.csv'

#Quelle waehlen und als "source" speichern
def csv_daten_im_verzeichnis():
    csv_dateien = []
    for dat in os.listdir(os.getcwd()):
        if dat.endswith(".csv") or dat.endswith(".CSV"):
            csv_dateien.append(dat)
    print(csv_dateien)
    return(csv_dateien)
            
        


def file_einlesen(auswahl_datei):
    
    #Format festlegen
    format_ist = input('Welches Trennzeichen nutzt die Datei \na:Komma / b:Semikolon \n?').lower()
    if format_ist == 'a':
        trennzeichen = ','
        dezimalzeichen = '.'
    elif format_ist == 'b':
        trennzeichen = ';'
        dezimalzeichen =','
    else:
        trennzeichen =','
        dezimalzeichen ='.'
    
    print(trennzeichen, " ", dezimalzeichen)
    
    #Dateieinlesen
    csv_daten=pd.read_csv(auswahl_datei,sep=trennzeichen ,decimal=dezimalzeichen)
    print(csv_daten)



#Hauptprozesse starten
if __name__ == '__main__':
    #choosesource(source)
    print('Folgende CSV-Dateien zur zur Auswahl, welche möchten sie auswerten?')
    csv_daten_im_verzeichnis()    
    
    #print(csv_dateien)
    auswahl_datei = input('Welche Daten einlesen ? :')
    file_einlesen(auswahl_datei)
    
