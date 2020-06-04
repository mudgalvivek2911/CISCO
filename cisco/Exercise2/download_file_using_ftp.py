# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:09:15 2020

@author: VI322910
"""
from ftplib import FTP

#domain name or server ip:
ftp = FTP('server.ip')
ftp.login(user='username', passwd = 'password')
path = input("Path from you want to access the file")
ftp.cwd(path)

filename = 'test.txt'

localfile = open(filename, 'wb')
ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

ftp.quit()
localfile.close()