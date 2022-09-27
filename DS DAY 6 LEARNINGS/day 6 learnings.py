# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:30:50 2022

@author: HEMANTH NAGUNOORI
"""

#revising dictionary
#a dictionary is a key value pair 
heman = {
    'name' : 'Hitler',
    'spouse' : 'i dont know',
    'kids' : 30,
    'nationality' : 'german',
    'profession' : 'military general'
    }
    print(heman)
# to know a particular value against a key
heman['kids']    
heman['name']
# to change any value fora key
heman['spouse'] = 'llalorana'   
# -----> this indicates that dictionary can be modified

#to delete any key-value pair in the dictionary
del heman['spouse']

#to find length of dictionary
len(heman)

# to know the no.of keys in our  dict
heman.keys()

# to know the no.of values in our  dict
heman.values()

#to know the functions applicable on our dictionary
dir(heman)

heman = {'name': 'Hitler', 
               'kids': [10,20], 
    'nationality':'german', 
'profession': 'military general'
     }

heman['kids']

marks : {
    'brm' : 20,
    'spp' : 43,
    'pj'  : 45,
    'nt'  : {'t1' : 20,'t2' : 24}
    }

type('nt')
######
marks['nt']['t1'] ---------> not working
######

#phenomenon of unpacking

divmod(32,5)
divmod(6,2)
x,y = divmod(32,5)

et = (7,0,9,3,4)

