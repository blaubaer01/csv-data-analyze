#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:27:58 2020

@author: blaubaer (Ricky Helfgen )
Thanks to https://www.youtube.com/watch?v=Q8CLcGdr90Q
"""

from cx_Freeze import setup, Executable
import sys

datei = input('Von welcher Datei willst du eine EXE erstellen: \n?')

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_options = {"packages": ['os', 'pandas', 'numpy', 'statsmodels', 'matplotlib', 'scipy', 'seaborn','outlier_utils'],
                                  "excludes": ["tkinter"]}


    
setup(version = "1.0",
      description = "Analyze CSV - File",
      name = "csv-data-analyze",
      options = {"build_exe": {"packages": ["os"]}},
      executables = [Executable(datei, base="Win32GUI")])

print("Fertig!")
