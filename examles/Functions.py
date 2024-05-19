# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:34:51 2020

@author: 100964
"""

def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

str = input("Enter your input: ")
#str = raw_input("Enter your input: ")
print ("Received input is : "+ str)