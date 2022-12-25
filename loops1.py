# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 02:42:32 2022

@author: Adil
"""


def testfn(n):
    #print(n)
    for v in range(n):
        print('*', end = ' ')
    print('')

for var in range(50):
    testfn(var)

 
var2 = 50
while(var2 > 0):
    testfn(var2)
    var2 = var2-1
    
    
