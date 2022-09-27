while (True) :
    try :
        age = int(input ("Enter your age >")
    except Exception :
        print ("Non Integer  value, try giving the age again")   
    else :
        print ("Your age is : ", age)     
    finally :
        print ("Program Ended")
        
        
        
        