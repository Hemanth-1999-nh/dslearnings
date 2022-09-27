"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of two tuples with 
    (order number, total amount of order).
    
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""

#crete a list with sublists 
#each sublist should contain order no., article no., quantity, price per unit
#develop program where output will be (ordernumber, total order amt)
#trainer advise is to use lambda, map and reduce concept to solve the problem & 
#from functools import reduce

bookshop_list = [[1,("3234", 2, 585.90)], [2, ("2324", 4, 610.20)],
                 [3,("4546", 6, 238.58)], [4, ("7895", 8, 431.20)],
                 [5,("1234", 10, 456.70)], [6, ("3235", 3, 560.28)]
    ]
#now use lambda,map,reduce to generate  output of list with 2 tuples
#a map contains both function and datasource
print(list(map(lambda reduce,bookshop_list )))


















