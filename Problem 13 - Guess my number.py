# Problem 13 - Guess my number

import random

computerGuess = random.randint(0,1000)
count = 1

while True:
    guess = int(input("Try to guess my number! Tell me a number: "))
        
    if guess == computerGuess:
        print ("CORRECT! You needed " + str(count) + " guesses.")
        break
    elif guess < computerGuess:
        print ("No! My number is higher.")
        count += 1
    elif guess > computerGuess:
        print ("No! My number is lower")
        count += 1
    else:
        print ("Sorry, I didn't catch that...")
