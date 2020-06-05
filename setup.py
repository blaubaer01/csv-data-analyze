#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:27:58 2020

@author: blaubaer (Ricky Helfgen )
Thanks to https://www.youtube.com/watch?v=Q8CLcGdr90Q
"""

###create executable file from csv-data-analyze 
###Problems with the scipy package!
###after installing change the filename: lib/scipy/spatial/cKDTree.cp37-win_amd64.pyd in ckdtree.pyd

from cx_Freeze import setup, Executable
import sys

datei = input('Von welcher Datei willst du eine EXE erstellen: \n?')

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'


build_exe_options = {
    "packages": ["os", "sys", "pandas", "numpy", "statsmodels", "matplotlib", "scipy", "seaborn", "outliers", "webbrowser"], 
    "excludes": ["tkinter"],
    "include_files": ["SPC_CPA.py", "L_REG.py", "table_functions.py", "regelkarte.py", "msa.py", "charts.py", "tests.py", "table_calc.py", "rand_data.py", "mkl_core.dll", "mkl_def.dll", "mkl_intel_thread.dll", "mk_mc.dll", "mkl_mc3.dll", "platforms/"], # <-- Include easy_gui
    "includes": ["SPC_CPA", "L_REG", "table_functions", "regelkarte", "msa", "charts", "tests", "table_calc", "rand_data"]
}

#build_exe_options = {"packages": ['os', 'pandas', 'numpy', 'statsmodels', 'matplotlib', 'scipy', 'seaborn','outlier_utils'],
 #                                 "excludes": ["tkinter"]}


    
setup(version = "1.0",
      description = "Analyze CSV - File",
      name = "csv-data-analyze",
      options = {"build_exe": build_exe_options},
      executables = [Executable(datei)])

print("Fertig!")
