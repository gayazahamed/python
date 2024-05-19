# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:09:30 2020

@author: 100964
"""

class Student:
    name = "hello"
    age = 1000
    


class Test(Student):
    pass
    

test = Test()
test.name = 999
print (test.age)

print (test.name)
