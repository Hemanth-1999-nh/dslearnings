# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:07:46 2022

@author: HEMANTH NAGUNOORI
"""
#day_05 lesson begins here : tutor used repl.it while i used spyder
"""
Advanced Python - Functional Programming
aimed to learn : concepts (Map,Filter,Reduce); Supportive Tencture (Lambda) 
& A Data Structure (Dictionary)
"""
#file comprehension :
#Create a list (a list is a data structure which holds multiple values)

list1 = [10,20,30,40,50]
print(list1)

list2 = []
for data in list1 :
  list2.append(data**3)   
print(list2)  

list3 = [] 
for data in list1 :
    list3.append(data**2)
print(list3) 

list4 = []
print ([data*data for data in list3])

list4 = print(list4.append)
print(list4)

list4 = [list3.append(data*data for data in list3)]

list5 = ('Shiva', 'Mohan', 'Hanuman', 'Parvathi', 'Prasad', 'Ram')
print([len(naam) for naam in list5])

#---------------end of list comprehension-----------------------

listA = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
def squarevalue (y) :
    return (y**2)

squarevalue(2538472)

#introducing a map : a MAP is an ITERATOR
    #map should have both function and data source
    #whenever we use a map we should declare our function 
    #i.e., "map(funtion, datasource)
    #e.g.: map(squarevalue,listA)
    #use of map : map is much more efficient than a looping mechanism
print(map(squarevalue,listA))    
print(list(map(squarevalue,listA)))

print(list(map(squarevalue,[10,20,30,40])))

"""
in above code, map exectues funtion by organised series of values in data source
for e.g.: if map(squarevalue,listA) is executed, then internally the work flow will 
be as follows :
    map would pick each value in data set i.e., 10,20,30,40 and funtions each call 
    and output is presented in return
    **call/function**            **output of each call/function**
    squarevalue(10) ------>                  100
    squarevalue(20) ------>                  400
    squarevalue(30) ------>                  900
    squarevalue(40) ------>                 1600
printing map gives = [100,400,900,1600]    
"""

listH = [64,121,225,625,1000]
def cubevalue (e) :
    return(e*e*e) 

print(list(map(cubevalue,listH)))
    
listM = [2,12,21,13,31,14,41,15,51,16,61,17,71,18,81,19,91]
def iseven (w) :
    if (w % 2 == 0 ) :
      return True 
    else :
      return None

print(list(map(iseven,listM)))

#above line86 code alternate way is :
    
for data in listM :
    print(iseven(data))
    
"""
filter is another concept 
it filters our requirement and gives output
its not necessary to use if & else function as filter itself checks
and informs true/false
check below example :
"""
listM = [2,12,21,13,31,14,41,15,51,16,61,17,71,18,81,19,91]
def iseven (w) :
    return (w % 2 == 0 ) 
print(list(filter(iseven,listM)))

#lambda is a key word to indicate an anonymous function written in python
#an anonymous function do not have any name
#anonymous function a.k.a endline function

listS = [14, 32, 69,3,33,333,3333, 50]
print(list(map(lambda y : y**2, listS)))
print(list(map(lambda x : x % 1 == 0, listS)))
print(list(map(lambda z : z*z*z*z, listS)))

print(list(filter(lambda x : x % 3 == 0, listS)))
print(list(filter(lambda g : g**3, listS)))

# in all the above examples, only the way of handling a function got changed 
#but the output remained the same

"""
 in a functional programming language(F.P.L), we can use one function as a 
parameter by simultaneously while calling another function
 in a complete functional programming language, there's no looping concept
e.g.: erlang, 
 "recursion" is used to introduce looping in a complete F.P.L

python is partial F.P.L (since it has concept  of looping)
"""
listY = [1,2,4,6,8]
def fmultiply (a,b) :
    return (a*b*b*a)
import functools
print(functools.reduce(fmultiply, listY))

def fsquarevalue (a,b) :
    return (a*a+b*b)
print(functools.reduce(fsquarevalue, [0,2,4,6,8]))

print(functools.reduce(lambda a,b : a*b, [1,2,3,4,5]))

#dictionary : key-value pair


dict1 = {
    'name' : 'Hemanth',
    'salary' : 200000,
    'expenditure' : 50000,
    'incentives' : 20000,
    'bonus' : {'frstm' : 1000, 'scndm' : 19000}
    'savings' : 180000
    }

print(dict1)

dict1['expenditure'] = 100000
dict1 ['name'] = 'NAGUNOORI HEMANTH'
del dict1 ['bonus']
len(dict1)

dict1.keys()
dict1.values()

for key in dict1.keys() :
    print (key)

for value in dict1.values() :
    print(value)

dict1.clear()    
    print(dict1)
    len(dict1)

dir()    

divmod(32,5)
type(divmod(32,5))
len(divmod(32,5))

help(divmod)

#unpacking : extracting an individual value from a pack of tuple
a,b = (2,4)

divmod(2,4)

x,y = divmod(32,5)
x
y
#tuples are read only(i.e, immutable). 
#tuples once declared can't be modified just like string
# e.g.: (2,4,6,8)

t1 = (3,6,9,12)
len(t1)

















