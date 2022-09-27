#list is a data structure used to store data with multiple values

listS = [9,8,7,6,5,4,3,2,1]

type(listS)

dir(list)

listS.append(10)

print(listS)

listS[-1]

listS[1]

#list even after defining, can be modified
#strings are read only type, but list can be edited
#contents of list can be changed, removed, added, overwrited
#list can be mutable

listS[2] = 50
listS[4] = 90

# [9, 8, 50, 6, 90, 4, 3, 2, 1, 10, 10]
listS.insert(3,35)
    
type(print(listS))

"""
listS.append(....) used to add desired value at the end of data structure
listS.insert(index, new value added) used to add desired value at any position in data structure
"""

listS.remove(10)

print(listS)

listO = [2,30,2,32,34,2,36]
listO.count(2)

listO.remove(2)
print(listO)
listO.remove(2)

listO = [2,30,2,32,34,2,36]
while (2 in listO) :
    listO.remove(2)
    print(listO)
        
listU = ['Amar', 'Vikram', 'Sandhanam', 'Dhilli', 'Rolex', 'Arjundas']
listU[0]
listU[1]
listU[2]
listU[3]
listU[4]
listU[5]

for name in listU :
    print(name)
listU.count('Amar')
listU.count('Vikram')
listU.count('Rolex')
listU.count('Arjundas')
listU.count('Dhilli')
listU.count('Sandhanam')

listM = [2,4,6,8,10,12,14,16,18,20] 

for item in listM :
    print(item*item*item*item)

listY = []
for item in listM :
    listY.append(item*item*item)
print (listY)
#list comprehension 
[item*item for item in listM]

listU = ['Amar', 'Vikram', 'Sandhanam', 'Dhilli', 'Rolex', 'Arjundas']
listA = []
for item in listU :
    listA.append(len(item))

print(listA)
#list comprehension for length calculation 
listI = [len(item) for item in listU ]
print(listI)

"""
name : Apple
cost : five hundred bucks
warranty : three years
rating : four star
"""
student = {
    'name': 'Hemanth',
    'class': 'SSC',
    'Yop': 2015,
    'GPA': 97
    }
        
    type(student)
    len(student)
    
    }
dir(dict)
student['GPA']
student['Yop']
len(student['class'])

student['name']: 'NAGUNOORI HEMANTH'
print(student['name'])

student['city']: 'Jaggaiahpally'






