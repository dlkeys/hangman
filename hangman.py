# import modules
import time
import random
import replit

# beginning verbage personalized with name
name = input("What is your name? ")
print (" ")
print ("Hello " + name + ", time to play hangman!")
print (" ")
time.sleep(1.5)
print ("Start guessing...")
print (" ")
time.sleep(0.5)

# words used in game
words = ['christmas', 'easter', 'thanksgiving', 'halloween', 'valentines', 'fourthofjuly', 'memorialday', 'calendar', 'month', 'year', 'holiday']
word = random.choice(words)

# variables initialized
guesses = ''
turns = 7

# 
while turns > 0:
    failed = 0
    for letter in word:
        if letter in guesses:
            print (letter)
        else:
            print ("_")
            failed += 1
    if failed == 0:
        print (" ")
        print ("You win, " + name)
        break

    time.sleep(0.5)
    print (" ")
    guess = input("Guess a character:")
    guesses += guess
    replit.clear()
    print ("Letters used: ", guesses)
    if guess in word:
      print ("Correct")
      print ("You have", turns, "more guesses")
      print (" ")
    if guess not in word:
        turns -= 1
        print ("Incorrect")
        print ("You have", turns, 'more guesses')
        print (" ")
        if turns == 0:
          print ("You Lose, " + name)
          break
