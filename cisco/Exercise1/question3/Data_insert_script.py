import mysql.connector
import pandas as pd

df = pd.read_csv("Data_file.csv")
Sap =[]
host_n = []
macadd = []
loopback = []
for i in range(len(df)):
    Sap.append(df['SapID'][i])
    host_n.append(df["Host_Name"][i])
    macadd.append(df["MacAddress"][i])
    loopback.append(df["LoopBack"][i])
    
    

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s, %s,%s)"
for i in range(len(df)):
    mycursor.execute(sql, (Sap[i],host_n[i],macadd[i],loopback[i]))

mydb.commit()

print(mycursor.rowcount, "record inserted.")
