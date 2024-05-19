# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:49:02 2020

@author: 100964
"""


import numpy as np
print (np.version.version)
print(np.__version__)
#a = np.array([1,2,3])
#print( a)

a = np.array([[1, 2, 3], [4, 5 ,6],[7, 8, 9]]) 
print (a)

for nn in a:
    for pp in nn:
        print (pp)
        
        
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)