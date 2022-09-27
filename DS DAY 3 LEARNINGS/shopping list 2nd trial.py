#STEP 1 : Make a list of things to hild on to items
shopping_list = []

#STEP 2 : Print out instructions on how to use
print ("What should we pick at the store ?")
print ("Enter 'DONE' to stop adding items to list")

#STEP 3 : Ask for new items
while True :
    #ask for new items
    new_item = input("Enter the item : ")
    
#STEP 5 : Be able to quit the app when 'DONE'   
    if (new_item == 'DONE') :
     break

#STEP 4 : Add new items to list
shopping_list.append(new_item)


#STEP 6 : print out the list
print("Here is your list items : ")
for item in shopping_list :
 print(item) 
 