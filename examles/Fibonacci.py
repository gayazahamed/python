# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:24:26 2020

@author: 100964
"""

def Fibonaccii(inputt):
    a = 0
    b = 1
    print (a)
    print (b)
    for x in range (2, inputt):
        b = a+b
        a = b-a
        print (b)
        
Fibonaccii(10)