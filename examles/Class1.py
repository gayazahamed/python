# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:28:19 2020

@author: 100964
"""

class Test:
    
    def __init__(self, name, age) :
        self.var1 = "var1"
        self.name = name
        self.age = age
        
    var2 = 5
    var3 = "test"
    
    def myfunc(self):
       print("Hello my name is " + self.name)
 
    
    
    
    
c1 = Test("John", 36)
c2 = Test("John", 8)


c1.var2 = "10"

print(c1.var1)
print(c1.var2)
print(c1.var3)

print(c1.name)
print(c1.age)

c1.myfunc()