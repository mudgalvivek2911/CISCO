# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:36:16 2020

@author: VI322910
"""

from pprint import pprint
import os                                                                                                                                                                     


'''
pidstat –d      List I/O statistics of all the PID
top             display system summary information and current utilization.
ps –ef          get a snapshot of the running proces
tcpdump         capture the network packets on a network interface.
iostat          diagnose performance issue with storage devices
ldd httpd       to diagnose the application startup problem.
netstat –s      show stats of all protocols
free -g         available out of available memory
sar -r          (System Activity Report) will be helpful to collect a number of a report including CPU, Memory and device load.
ipcs –q         provides a report on the semaphore, shared memory & message queue.
'''

print("--------------------")
du = os.popen("pidstat –d").readlines()
pprint(du)
print("--------------------")
du = os.popen("top").readlines()
pprint(du)
print("--------------------")
du = os.popen("tcpdump").readlines()
pprint(du)
print("--------------------")
du = os.popen("iostat -d").readlines()
pprint(du)
print("--------------------")
du = os.popen("ldd httpd").readlines()
pprint(du)
print("--------------------")
du = os.popen("netstat –s").readlines()
pprint(du)
print("--------------------")
du = os.popen("free -g").readlines()
pprint(du)
print("--------------------")
du = os.popen("sar -r").readlines()
pprint(du)
print("--------------------")
du = os.popen("ps –ef").readlines()
pprint(du)
print("--------------------")
du = os.popen("ipcs –q").readlines()
pprint(du)
