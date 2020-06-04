# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:22:13 2020

@author: VI322910
"""

import pysftp

myHostname = "host"
myUsername = "user"
myPassword = "password"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print("Connection succesfully stablished ... ")

    # Define the file that you want to download from the remote directory
    remoteFilePath = '/destinations/file.txt'

    # Define the local path where the file will be saved
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
    localFilePath = './file1.txt'

    sftp.get(remoteFilePath, localFilePath)