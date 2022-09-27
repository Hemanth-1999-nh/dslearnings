#to learn File Handling : 
    
"""
File Handling means :
1. Reading the data from file
2. Writing the data to file
"""

#read the names in the file
ref = open("medicines.txt", "r")

#methods to read the data :
    
#1. read method :- reads data as a string but completely 
print(ref.read())    
#to close the file :
ref.close()  
#file once closed cant be opened or operated unless opened again  
ref.read() 

#2. readline method :- reads data as a string, but one line at a time
ref = open("medicines.txt", "r")
print(ref.readline())
print(ref.readline())
print(ref.readline(23))
print(ref.readline(6))
print(ref.readline(5))
print(ref.readline(12))
print(ref.readline(-6))
ref.close()

#3. readlines method :- reads data in the form of a list
ref = open("medicines.txt", "r")
print(ref.readlines())    
ref.close() 

ref2 = open("alcohol.txt", "w")
print(ref2.write("Bag Pipers"))
print(ref2.write("Red Wine"))
print(ref2.write("Black Rose"))
ref2.close()

