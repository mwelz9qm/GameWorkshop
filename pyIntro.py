#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 13:30:31 2025

@author: mwelz
"""

#from random import randint

import random 

'''
# make a basic random number game


lowEnd = 0
highEnd = 100

randomNum = random.randint(lowEnd,highEnd)



myGuess = int(input(f"Pick a number from {lowEnd} to  {highEnd}: " ))

if (myGuess == randomNum):
    print("You nailed it! Good job!")
else:
    print("Too bad! You guessed ", myGuess, " and the answer is ", randomNum)
    

    
# now let's give multiple guesses

numGuesses = 5

for guess in range(1,numGuesses+1):
    print(f"Guess number {guess} ****************** ")
    myGuess = int(input(f"Pick a number from {lowEnd} to  {highEnd}: " ))
    if (myGuess > randomNum):
        print(f"Too high! You have {numGuesses - guess} left! ")
    elif (myGuess < randomNum):
        print(f"Too low! You have {numGuesses - guess} left! ")
    else:
        print("You nailed it! Good job!")
        break
        
if (myGuess != randomNum):
    print(f"Sorry you couldn't find the answer! It was {randomNum}.")
    
'''


#finally let's turn this into a function -- where we can choose number of guesses and range as we see fit


def guessingGame(lowEnd, highEnd, numGuesses):
    print(f"In this game, you'll have {numGuesses} guesses to pick a number between {lowEnd} and {highEnd}. Let's start!")
    randomNum = random.randint(lowEnd,highEnd)
    
    for guess in range(1,numGuesses+1):
        print(f"Guess number {guess} ****************** ")
        myGuess = int(input(f"Pick a number from {lowEnd} to  {highEnd}: " ))
        if (myGuess > randomNum):
            print(f"Too high! You have {numGuesses - guess} left! \n")
        elif (myGuess < randomNum):
            print(f"Too low! You have {numGuesses - guess} left! \n")
        else:
            print("You nailed it! Good job!")
            break
        
    if (myGuess != randomNum):
        print(f"Sorry you couldn't find the answer! It was {randomNum}.")
    
    


# without calling the function, nothing happens

guessingGame(lowEnd=40,highEnd=200,numGuesses=8)
