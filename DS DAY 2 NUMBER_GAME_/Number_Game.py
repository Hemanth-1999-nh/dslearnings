# Interactive Guess the Number Game 

"""

    The computer will think of a random number from 1 to 10 as 
    secret number.
    Then ask you ( Player ) to guess the number and store as 
    guess number.

    Compare the guess number with the secret number.
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.
    
"""

import random
dir (random)
help(random.randint)
secret_number = random.randint(5,25)
guess = int(input("Guess the number between 5 and 25 : "))
if (guess == secret_number) : 
    print ("Player wins & Computer looses")
else :
    print ("Computer wins & Player looses") 
    