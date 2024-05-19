# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:17:41 2024

@author: Adil
"""
 

import os
 
# Get the list of all files and directories
path = 'C:\Gayaz\MicroServices\code'
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)