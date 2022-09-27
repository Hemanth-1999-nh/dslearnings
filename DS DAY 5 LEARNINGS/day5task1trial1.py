#solution to task :
    order = [[34587,'Learning Python','Mark Lutz',4,40.95],
         [98762,'Programming Python','Mark Lutz',5,56.80],
         [77226,'Head First Python','Paul Barry',3,32.95],
         [88112,'Einführung in Python3','Bernd Klein',3,24.99]
        ]

#without using list comprehension

lists = []
for item in order:
   
  if item[-1]*item[-2] < 100:
        
        lists.append((item[0],item[-1]*item[-2]+10)) 
        
    else:
        
        lists.append((item[0],item[-1]*item[-2]))

print("Order Summary: ",lists)



#with using list comprehension
print("Order Summary: ",[(item[0],item[-1]) 
                         if item[-1]*item[-2] > 100 
                         else (item[0],item[-1]*item[-2]+10) for item in order])



