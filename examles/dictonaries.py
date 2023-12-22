# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:29:59 2020

@author: 100964
"""

thisdict = {"brand": "Ford",
  "model": "Mustang",
  "year": 1964}

thisdict["year"] = 2018


print(thisdict.get("brand1","NOOOOOOOOO"))
print(thisdict.get("year","NOOOOOOOOO"))

for x in thisdict:
  print(x)
  
for x, y in thisdict.items():
  print(x, y)
  
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  

print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

del thisdict["color"]
print(thisdict)

thisdict.clear()
print(thisdict)