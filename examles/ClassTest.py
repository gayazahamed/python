# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:39:38 2020

@author: 100964
"""

class ClassTest:
    empCount = 0
    
    def __init__(self , name):
        self.name = name
        ClassTest.empCount += 1
        print(self.name )
        print( self.empCount)
        
        






clsTst = ClassTest('Testt')
print(clsTst.empCount)

ClassTest('Testt')
ClassTest('Testt')
ClassTest('Testt')
