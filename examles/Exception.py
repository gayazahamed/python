# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:18:21 2020

@author: 100964
"""

try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
   
print("")
print("")
print("")
  
  
try:
  1/0
  print(x)
except BaseException as e:
    print(e)
    print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
    print('finally block')
    
    
      
print("")
print("")
print("")
  
  
try:
  1/0
  print(x)
except BaseException as e:
    print(e)
    print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
    print('finally block')
 