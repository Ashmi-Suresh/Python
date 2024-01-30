"""
Program: Average Revisited 
Author: Ashmi Bidrupane Suresh
Description: This program is to collect the numbers and compute the average without knowing how many numbers to expect.
Revisions:
	00 - Announce and get each number from the user by pressing enter
	01 - Initialise number as empty list and use while loop to enter number
	02 - Calculate average and print the total numbers entered along with average.
"""
#Announce
print("Program to compute the average of the numbers provided.\n")

#To prompt each number from user when <enter> is pressed
print("Enter each number followed by <enter>.") 
print("When you are done, just hit <enter> in response to the prompt.\n")

#Initialise numbers to empty list
numbers = []

#While loop to enter each number when enter is pressed
while True:
    number = input("Enter a number: ")
    if number == '':
        break
    
#each number that the user inputs, the code converts the input string to a floating point number using the "float()" function and appends it to the "numbers" list.
    numbers.append(float(number))

#To check if the "numbers" list is not empty, and if it's not, it calculates the average of the numbers by summing up all the elements of the list and dividing by its length
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"\nYou entered {len(numbers)} numbers.")
    print(f"The average is {average:.1f}.")

