"""
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.
  Hint: 
    Write a Python program without list comprehension first and then with list comprehension
    
    # Assume the data in form of list of list
    
    orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
"""
#my interpretation of given data :
"""
write a  list(as order summary) with 2 tuples
tuples should have order no., pdt price., quantity 
(if order value is < rs.100, then >it by rs.10)
"""
"""
#data to use :
    Order No.     Author          Book Title       Quantity      Price per Item
        1     Ross & Wilson,          HAP             7              40.95
        2      R.N.Chatwal,           PIC             9              56.80
        3    Morrison & Boyd,         POC             3              32.95
        4      Kokate,                COG             4              24.99   
"""        
#list written as tuple :
      order =   [[1,'Ross & Wilson','HAP',7, 42]
                 [2,'R.N.Chatwal', 'PIC', 9, 58]
                 [3,'Morriosn & Boyd', 'POC', 3, 34]
                 [4,'Kokate', 'COG', 4, 26]
                ]
print("Order Summary :", [(item(0),item(4)
                           if item[3]*item[4]>1000
                           else item(0),item[3]*item[4]+100 for item in order)]





















