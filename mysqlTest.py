# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 02:31:32 2022

@author: Adil
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="social-media-user",
  password="dummypassword",
  database="social-media-database"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM person")

myresult = mycursor.fetchall()

print(type(myresult))

for x in myresult:
  print(x)
  print(type(x))