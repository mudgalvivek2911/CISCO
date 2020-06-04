# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:59:03 2020

@author: VI322910
"""


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE VIEW [Router_view] AS SELECT * from Routers")


