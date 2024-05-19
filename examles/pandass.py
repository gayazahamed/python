# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:38:43 2020

@author: 100964
"""

import pandas as pd

import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
p = pd.Series(data,index=[1,2,3,4])
print (s)
print (p)

df = pd.DataFrame(data)
print (df)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)


pp = np.random.randn(4)
print(pp)