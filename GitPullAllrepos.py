# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:20:44 2022

@author: Adil
"""




import os
print(os)

#os.removedirs("C:/Gayaz/test/new1")

 
import subprocess

def git_pull(repo_path):
    try:
        result = subprocess.run(['git', 'pull'], cwd=repo_path, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")
 
 
 
from os import listdir
from os.path import isfile, join
mypath = "C:/Gayaz/test/new1"
mypath = "C:/Gayaz/MicroServices/code/"

arr = os.listdir(mypath)


for x in arr:
 print(x)
 mypath2 = mypath + x
 print(mypath2)
 try:
    git_pull(mypath2)
 except OSError as ex:
    print(ex)
 

"""
for dirpath, dirnames, filenames in os.walk("C:/Gayaz/test/new1"):
   
    try:
       os.rmdir(dirpath)
       print(dirpath)
    except OSError as ex:
        print(ex)

"""



"""

f = open("C:/Gayaz/test/one.txt", "a")
#f.write("this is test file\n")
f.close()


f = open("C:/Gayaz/test/one.txt", "r")
print(f.read())
f.close()


"""