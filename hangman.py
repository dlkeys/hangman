import time

# Personalize the game with the players name

name = input("What is your name? ")
print ("Hello " + name+", time to play hangman!")
print (" ")
time.sleep(2)
print ("Start guessing...")
time.sleep(0.5)

# For now, I will only have one word to guess
# Later, we will expand this greatly
# Initialize the variables

word = "christmas"
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:      
        if char in guesses:    
            print (char)
        else:    
            print ("_")
            failed += 1    
    if failed == 0:        
        print ("You win!!!")		
        break              

    time.sleep(0.5)
    print (" ")
    guess = input("Guess a character:") 
    guesses += guess                    
    print ("Letters used: ", guesses)
    if guess in word:
      print ("Right")
      print ("You have", turns, "more guesses")
    if guess not in word:  
        turns -= 1        
        print ("Wrong")
        print ("You have", turns, 'more guesses')
 
        if turns == 0:
