#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:20:56 2020

@author: blaubaer
"""

import numpy
import pyspc
import pandas as pd
import matplotlib.pyplot as plt

auswahl_datei = 'production.csv'

trennzeichen =';'
dezimalzeichen =','
kopfz = 0

df=pd.read_csv(auswahl_datei, sep=trennzeichen , decimal=dezimalzeichen, header=kopfz)
#print(df)

#df2 = df.groupby('Stichprobe').agg({'Istwert':['mean', 'std'].reset_index()})
#print(df2)
df2 = pd.DataFrame()

#df2['mean_istwert'] = df.groupby('Stichprobe')['Istwert'].describe()
df2 = df.groupby('Stichprobe')['Istwert'].describe()

fn = 'describe.csv'
df2.to_csv(fn, sep=';', decimal=',', header =True)

#df2=df.groupby(['Stichprobe'])[['mean']].mean().reset_index()
print (df2)

df2.plot('mean', grid=True)
    
plt.show()
#x = df2['Stichprobe']

#print(x)

#y = df2['mean']

#ax.scatter(x=x, y=y, grid=True)

#plt.show()

#print(df2)
