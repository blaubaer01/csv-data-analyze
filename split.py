#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:50:54 2022

@author: blaubaer
"""

import pandas as pd

filename = 'tab.csv'

df=pd.read_csv(filename,sep=';' ,decimal=',', header=0, engine='python')
print(df)
#df['spalte2'], df['spalte4'] = df['spalte2'].str.split(':', 1).str
print(df)

df=pd.read_csv(filename,sep=';' ,decimal=',', header=0, engine='python')
print(df)
df[['spalte2','spalte4']] = df.spalte2.str.split(':',expand=True) 
print(df)

