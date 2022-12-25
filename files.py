# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:20:44 2022

@author: Adil
"""




import os
print(os)

#os.removedirs("C:/Gayaz/test/new1")

for dirpath, dirnames, filenames in os.walk("C:/Gayaz/test/new1"):
   
    try:
       os.rmdir(dirpath)
       print(dirpath)
    except OSError as ex:
        print(ex)


"""

f = open("C:/Gayaz/test/one.txt", "a")
#f.write("this is test file\n")
f.close()


f = open("C:/Gayaz/test/one.txt", "r")
print(f.read())
f.close()


"""