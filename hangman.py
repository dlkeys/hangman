import time
import secrets

name = input("What is your name? ")
print (" ")
print ("Hello " + name+ ", time to play hangman!")
print (" ")
time.sleep(1.5)
print ("Start guessing...")
time.sleep(0.5)

words = ['christmas', 'easter', 'thanksgiving', 'halloween', 'valentines']
word = secrets.choice(words)
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for letter in word:
        if letter in guesses:
            print (letter)
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
      print ("Correct")
      print ("You have", turns, "more guesses")
      print (" ")
    if guess not in word:
        turns -= 1
        print ("Incorrect")
        print ("You have", turns, 'more guesses')
        print (" ")
        if turns == 0:
          print ("You Lose!!!")
          break
