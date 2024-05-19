# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:42:08 2020

@author: 100964
"""

def set_list(list): 
    list.append("D") 
    print((list)) 
    list = ["A", "B", "C"] 
    return list
  


def add(list): 
    list.append("D") 
    return list

my_list = ["E"] 
  
print(set_list(my_list)) 
print((my_list)) 
  
print(add(my_list))
print((my_list)) 



def strtest(st1): 
    st1 = ' 123'
    return st1
  
    
st0 = 'test'
st0 = strtest(st0)
print(strtest(st0))
print(st0)




student={'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
def test(student):
   student={'alok':30,'Nevadan':28}
  # student.update(new)
   print("Inside the function",student)
   return
test(student)
print("outside the function:",student)