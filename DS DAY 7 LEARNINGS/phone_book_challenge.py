
print(task_01.read)
print(task_01.read())

import re 

task_01 = open("simpson's phone book.txt", 'r')

for line in task_01 :
    if (re.search(r'^J\w*\s*(Neu)',line)) :
        print(line)

task_01.close