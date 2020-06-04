# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:11:51 2020

@author: VI322910
"""

import mysql.connector
import pandas as pd

df = pd.read_csv("Data_file.csv")
Sap =[]
host_n = []
macadd = []
loopback = []


    

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO Routers ( Sapid, MacAddress, HostName, loopback ) VALUES (%s, %s, %s, %s)"

val = [
  ( "11", "192.168.0.1","local21","2314" ) ,

  ( "12", "192.168.0.2","local22","2315" ) ,

  ( "13", "192.168.0.3","local23","2316" ) ,

  ( "14", "192.168.0.4","local42","2317" ) ,

  ( "15", "192.168.0.5","local25","2318" ) ,

  ( "16", "192.168.0.6","local26","2319" ) ,

  ( "17", "192.168.0.7","local27","2310" ) ,

  ( "18", "192.168.0.8","local28","2311" ) ,

  ( "19", "192.168.0.9","local29","2312" ) ,

  ( "20", "192.168.0.21","local20","2313" ) ,

]

mycursor.execute( sql, val )

mydb.commit( )

print( mycursor.rowcount, "was inserted." )