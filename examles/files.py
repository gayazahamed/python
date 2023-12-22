# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 00:56:15 2020

@author: 100964
"""
import os

import glob
lst = glob.glob("D:\Gayaz\AI\python\examles\*.*")

for val in lst:
    print(val)
    
    
    fo = open("D:\Gayaz\AI\python\examles\Person.py", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
#print ("Softspace flag : ", fo.softspace)



myfile = open("D:\Gayaz\AI\python\examles\myf2.txt", "a")
try:

 for i in range(1):
    #print('this')
    myfile.write('this\n')
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   myfile.close()


def printFiles(fname):
    print("----------------1")
    dirr2 = os.listdir(fname)
    print(dirr2)
    for dirr2Var in dirr2:
         print (dirr2Var)
         if(os.path.isfile(dirr2Var)):
             print (dirr2Var)
         else:
             printFiles(dirr2Var)
    print("----------------2")
 
# Getting the current work directory (cwd)
thisdir = os.getcwd()
print(thisdir)
arr = os.listdir(thisdir)
print(arr)
for dirr in arr:
    if(os.path.isfile(dirr)):
       print (dirr)
    else:
        print(dirr + " ??????????")
        printFiles(dirr)
        













