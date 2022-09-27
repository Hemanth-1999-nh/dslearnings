#hangman task solution
"""
 We are going to make a "Hangman Letter" game 
 The computer will pick a word
 The player can guess it letter by letter or run out of chances.
 But if they make too many wrong guesses, they loose.
 If the player makes the right guesses he wins
 Cleaner interface and option to quit the game
"""
"""
Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.
"""

list = ['apple', 'banana', 'pomegranate', 'pineapple', 
'tomato', 'brinjal', 'snake guard', 'bitter guard', 'bottle guard', 'leafy vegetables' ]


import  random

while(True) :
    
    guessed_word = random.choice(list)
    
    guess = str(input("Guess the secret word : "))
    
    if (guess == guessed_word) :
        
        print("player wins and computer lose")
        
    else :
        
       print("computer wins and player lose")  
    