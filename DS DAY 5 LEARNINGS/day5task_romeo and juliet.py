# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:36:21 2022

@author: Tanushree Gupta
"""

# To open the file
ref = open("romeo.txt", "rt")
content = ref.readlines()

    
    # List to hold the list of the words
req_content = []
for var in content:

    req_content.append(var.split())
    
    # To count the words using dictionary
r_and_j = {}
for var2 in req_content:
    for var3 in var2:
        if var3 not in r_and_j:
            r_and_j[var3] = 1
        else:
            r_and_j[var3]+=1
                
    print(str(r_and_j))    

    len(r_and_j)
    type(r_and_j)