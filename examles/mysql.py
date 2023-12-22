# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:37:39 2020

@author: 100964
"""

#https://remotemysql.com/databases.php
#testtest@yomail.com
import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="qpMs683cF6",
  password="yMnbzmN1G9",
  database="qpMs683cF6"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
for i in range(100):
    mycursor.execute(sql, val)
    mydb.commit()
    print(i)

print(mycursor.rowcount, "record inserted.")
"""

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
print(myresult)

count = 0
for x in myresult:
  print(x)
  count+=1

print(count)