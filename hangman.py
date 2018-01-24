import time

# Personalize the game with the players name
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
print (" ")
time.sleep(3)
print ("Start guessing...")
time.sleep(0.5)

# For now, I will only have one word to guess
# Later, we will expand this greatly
word = "david"

# Initialize the variables
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:      
        if char in guesses:    
            print (char),
        else:    
            print ("_"),   
            failed += 1    
    if failed == 0:        
        print ("You won")		
        break              

    print

    guess = input("guess a character:") 
    guesses += guess                    

    if guess not in word:  
        turns -= 1        
        print ("Wrong")  
 
        print ("You have", + turns, 'more guesses')
 
        if turns == 0:           
    
            print ("You Lose")
