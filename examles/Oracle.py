# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:28:17 2020

@author: 100964
"""
import os
import platform
import cx_Oracle

LOCATION = r"C:\Users\100964\Anaconda3\Lib\site-packages\cx_Oracle-8.1.0.dist-info"
print("ARCH:", platform.architecture())
print("FILES AT LOCATION:")
for name in os.listdir(LOCATION):
    print(name)
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]


#cx_Oracle.init_oracle_client(lib_dir= r"C:\Users\100964\Desktop\AI\python\oracle\instantclient_19_10")

dsn_tns = cx_Oracle.makedsn('localhost', '7732', service_name='orcl') 
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)

c = conn.cursor()
c.execute('select * from employees') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1] , '-', row[2] , '-', row[3] ) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
conn.close()