# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:04:12 2020

@author: VI322910
"""

import os, sys


path = input("Enter Path to check")
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print(file)