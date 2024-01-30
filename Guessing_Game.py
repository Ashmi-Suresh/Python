"""
Program name: Guessing Game
Author: Ashmi Bidrupane Suresh
Description: The guessing game is based on an algorithm called a “binary search”.  The code guesses a 
number within a certain range in the fewest number of guesses.
Revisions:
	00 - Announce,Import math and random modules and get the values for nMax and secretNumber.
	01 - Calculate number of guesses required to guess andomly generated number
	02 - While loop used to print appropriate message according to users guess
"""

# Announce

print("Guessing Game:")
print("Guess the Secret Number\n")

#To use import statement which allows  external modules and packages like math and random in code.

import math
import random

#To input the maximum number of a range, which is then converted to an integer data type and stored in a variable named Max_Num.
nMax = int(input("Enter the maximum number in the range: "))


# Generate a random secret number
secretNumber = random.randrange(1,nMax + 1)

print(f"\nTry to guess a secret number from 1 to {nMax} (inclusive).\n")

# To calculate the number of guesses required to guess a randomly generated number within a range.
nGuesses = int(math.log2(nMax)+1)

#Initialising n which is a  counter variable used to keep track of the number of guesses made by the user.
n = 0

#For loop used to print appropriate message according to users guess
for n in range(nGuesses):
    if(nGuesses - n != 1):
        print(f"You have {nGuesses - n} guesses available.") 
        guessInput = int(input("Enter your guess: "))
        if(guessInput<secretNumber): 
            print(f"The secret number is greater than {guessInput}.")
        elif(guessInput == secretNumber):
            print("Correct. Well done!")
            break # break if user have guessed the correct number
        else:
            print(f"The secret number is less than {guessInput}.")
    else: 
        print(f"Your have {nGuesses - n} guess available.")
        guessInput = int(input("Enter your guess: "))
        if(guessInput<secretNumber):
            print(f"The secret number is greater than {guessInput}.")
        elif(guessInput == secretNumber):
            print("Correct. Well done!")
            break
        else:
            print(f"The secret number is less than {guessInput}.")
else: 
    print("\nSorry. No more guesses are allowed.")
    print(f"The secret number was {secretNumber}.")
