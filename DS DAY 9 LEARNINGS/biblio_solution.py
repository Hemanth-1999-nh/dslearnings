# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:36:21 2022

@author: HEMANTH NAGUNOORI

BIBLIO TASK SOLUTION 


# This class provides a template for holding and manipulating information about a book. 
# returns a formatted bibliographic reference for the book.

class Book:
    
    # authorlast, authorfirst, title, place, publisher and year
    def __init__(self, authorlast, authorfirst, title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
  
    def write_bib_entry(self):
        return self.authorlast \
               + ', ' + self.authorfirst \
               + ', ' + self.title + ', ' + self.place \
               + ':  ' + self.publisher + ', ' \
               + self.year + '.'
  
                                                          
# Create a few instances of Book classes:
beauty = Book( "Dubay", "Thomas", "The Evidential Power of Beauty", "San Francisco", "Ignatius Press", "1999", )
pynut  = Book( "Martelli", "Alex", "Python in a Nutshell", "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )


#How would you print out the book attribute of the pynut instance?
print(Book.write_bib_entry(pynut))
#other way is
print (pynut.write_bib_entry())

                            
#If you type print beauty.write_bib_entry() at the interpreter, what will happen?
print(beauty.write_bib_entry())
# It'll give all attributes values

#How would you change the publication year for the beauty book to"2010"?
beauty.year="2021"
print(beauty.write_bib_entry()) # It will year 2021 along with remaining attributes
"""

#task 01 : creation of book as class with mentioned variables

class Book :
    def __init__ (self,authorlast, authorfirst, title, place, publisher, year) :
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
        
    def write_bib_entry (self) :
        return self.authorlast + "," + self.authorfirst + "," + self.title \
               + self.place+ "," + self.publisher + "," + self.year + "."
        
#task 02 : creating objects for above class :

beauty = Book( "Dubay", "Thomas", "The Evidential Power of Beauty", "San Francisco", "Ignatius Press", "1999", )
pynut  = Book( "Martelli", "Alex", "Python in a Nutshell", "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )
    
#task 03 : print book of python object :

print (pynut.write_bib_entry())    
    
#task 04 : print book of beauty :   
    
print (beauty.write_bib_entry()) 
    
#task 05 : change the publication year for the beauty book to"2010" :

    beauty.year = "2010"

print (beauty.write_bib_entry ())
    
    
    
    