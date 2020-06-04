# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:46:15 2020

@author: VI322910
"""

import getpass
import telnetlib

HOST = "http://localhost:8000/"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

print(tn.read_all())
