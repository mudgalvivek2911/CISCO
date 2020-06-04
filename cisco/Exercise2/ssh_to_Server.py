# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:54:19 2020

@author: VI322910
"""
import paramiko

host = "test.rebex.net"
port = 22
username = "demo"
password = "password"

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)