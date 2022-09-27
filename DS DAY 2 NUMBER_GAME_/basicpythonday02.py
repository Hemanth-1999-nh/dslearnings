str1 = "Lenovo Vantage System Security"

type (str1)

print (len(str1))

str1 [11]

str1 [-15]

type (str1[3])

#indexing a.k.a slicing in python 
#slicing is used as follows :
    
    str1[2:22]
    
    str1 [0:30]
    
    str1 [20: ]
    
    str1 [:30]
    
    str1 [:]
    
    str2 = "The quick brown fox jumped over the lazy dog"
    type (str2)
    print (len(str2))
    str2 [26]
    str2[-40]
    type (str2[23])
    
    print (420-2)
    
    str1 [ : 3]
    print (dir(str))
    help(str.upper)
    help(str.format)
    help(str.lower)
    print(str1)
    str1.upper()
    str1.lower()
    
    print(str2)
    str2.upper()
    str2.lower()
    print(str1,str2)
    str1 str2.upper()
    str1,str2.lower.()
    
    str1[1] = 'E'
    
    """
    strings in python after slicing or indexing are immutable
    i.e., they cannot be edited
    they areread only strings 
    no changing is made or allowed
    """
    #after indexing, python strings are Immutable
    
    str1 = str1.upper()
    str2 = str2.upper()
    str3 = str1.lower()
    str4 = str2.lower ()
    str5 = str3.bold()
    str6 = str4.italic()
    
    """
    python is a very powerful porgramming language
    because it has many libraries and modules in it
    """
    #math library
    #include <math.h>
  #command import math in python is equivalent to command <math.h> in 'C' programme
import math
dir (math)
help(math.acos)
help(math.sqrt)

x = 3600
print (math.sqrt(x))

y = 100
math.sqrt(y)

a = 2500
math.sqrt(a)

x = input ("Enter the number : ")
# type casting : is the process of changing type of data in statement
x = int(x)
print (math.sqrt(x))

# infinite looping

#code version 01 :
 while (True) :
    x = input ("Enter the number : ")
    
    if (not x) :
        print ('Invalid Input...Leaving app')
        break
   #break is a statement which terminates the loop
    x = int(x)
    
    print (math.sqrt(x))

    #code version 2 :
        
 while (True) :
     
    x = input ("Enter the number : ")    
    
    if (not x) :
        
        print ('Invalid Input...Try next')
        
        continue      
    
    if (x.isdigit()):
        
         x = int(x)      
         
         print ("the square root is", math.sqrt(x))
         
 else :
       
       print ("the length is", len(x))
       
       
       
    """
    continue is a statement which doesn't terminate the loop but
    it continues to execute the code lyine the statement
    """
    #code version 3 :
 datastore = [ ]
 while (True) :
     
    x = input ("Enter the number : ")    
    
    if (not x) :
        
        print ('Invalid Input...Try next')
        
        continue      
    
    if (x.isdigit()):
        
         x = int(x)      
         
         datastore.append(math.sqrt(x))
         
 else :
       
       datastore.append(len(x))
    