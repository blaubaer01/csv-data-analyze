#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:28:50 2020

@author: blaubaer
"""

import pandas as pd

auswahl_datei = 'Covid19.csv'

trennzeichen=','

dezimalzeichen='.'

kopfz=0

df=pd.read_csv(auswahl_datei,sep=trennzeichen ,decimal=dezimalzeichen, header=kopfz)

df['date']=df['year'].astype(str) + '-' + df['month'].astype(str) + '-' + df['day'].astype(str)

df.to_csv(auswahl_datei, sep=';', decimal=',', header =True)