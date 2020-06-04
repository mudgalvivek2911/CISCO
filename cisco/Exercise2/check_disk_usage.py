# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:01:06 2020

@author: VI322910
"""
from pprint import pprint
import os                                                                                                                                                                     
du = os.popen("df -h").readlines()

pprint(du)