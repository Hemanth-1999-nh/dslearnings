# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:09:43 2022

@author: HEMANTH NAGUNOORI
"""

#OOPS part 01 :
    
A = 56

print(A)
print(type(A))
print(id(A))

#56 is stored in heap
#id /address of A is stored in stack

b = 56
print(id(b))

c = 80.36
print(id(c))
print(type(c)) 

D = True
print(id(D))



#OOPS part 02 :-

#line 39 is a syntax part; __init__(self) is the name of constructor we create in python    
class Employee :
    
    #class variable 
    num_of_emps = 0
    
    def __init__(self,first_name,last_name,salary) : 
        #instance variables
        self.first = first_name
        self.last = last_name
        self.pay = salary
        self.email = first_name.lower()+"."+last_name.lower()+"@company.com"
        #print("Inside Employee Constructor")
        Employee.num_of_emps += 1
        
        
# Instance Methods
    def fullname (self) :
        return self.first+" "+self.last        


print(emp_1.fullname())
print (emp_2.fullname())

print(emp_1.fullname)
print (emp_2.fullname)

Employee.fullname(emp_1)
Employee.fullname(emp_2)  
 
print (Employee.num_of_emps)

emp_1 = Employee ("Nagunoori", "Hemanth", 1001) 
#print(emp_1)
"""    
when () used while executing a code line,
then a constructor function is called in memory
"""
#print(id(emp_1))


emp_2 = Employee ("Nagunuri", "Pavankumar", 2112 ) 
print(emp_2)
print(id(emp_2))

print(emp_1.pay)
print(emp_1.email)
print(emp_1.pay, emp_2.email)
print(emp_1.pay, emp_2.email, emp_1.first, emp_2.last)     
print(emp_1.email, emp_2.email)

#Manager Developer

class Developer (Employee) :
    pass

class Manager (Employee) :
    pass

print (issubclass (Developer, Employee))

print(issubclass (Manager, Employee))

print (issubclass (Employee, Developer))


emp_1 = Employee ("Nagunuri", "Pavankumar", 2112 )
dev_1 = Developer("Nagunuri", "Pavankumar", 2112 )
mgr_1 = Manager ("Nagunuri", "Pavankumar", 2112 )

print(isinstance(dev_1, Developer))
print(isinstance(dev_1, Manager))
print(isinstance(dev_1, Employee))










