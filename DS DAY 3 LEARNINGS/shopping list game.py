# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:29:59 2022

@author: HEMANTH NAGUNOORI
"""
"""
     We are going to make a "SHOPPING LIST" App
     Run the script to start using it
     Put the new things at a time
     Enter the word - DONE - in all CAPS to QUIT the program
     And once I quit, I want the app to show me everything that's on my list.

Hint :
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use 
    the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list     
"""
ListShopping = ['Tea', 'Coffee', 'Milk', 'Sugar', 'Ice', 'Bowl']
type(ListShopping)
len(ListShopping)
dir(ListShopping)
help(list.insert)

ListShopping.remove('Tea')
print(ListShopping)

ListShopping.append('Lemon')
ListShopping.insert(-4,'Honey')

#app building usig python
#building shopping list app 
#use above mentioned instructions & steps

#step_01 :
buying_list = []

#step_02 :
print("What to buy in store ?" )
print ("Enter 'FUll' to stop aadding items to the list")

#step_03 :
while True :
    new_item = input("Enter the item : ")

#step_05 :
    if (new_item == 'FULL') :
        break
    
#step_04 : 
buying_list.append(new_item)
       
#step_06:print out the list 
print("Here is your list items : ")
for items in buying_list :
   print(item)
   
   item = buying_list
   
       