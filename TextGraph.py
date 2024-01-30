"""
Program: TextGraph Program 
Author: Ashmi Bidrupane Suresh
Description: This program generates bar graph when the user to enter up to ten positive whole numbers to give one bar for 
each valid number entered.
Revisions:
	00 - Announce and prompt the input from the user
	01 - Use of split() to split a string into a list of substrings
	02 - Use of loop to checkif the entered string consists of only digit and if each digit is less than or equal to 50
	03 - To print bar graph for each valid entry

"""



#Announce
print("TextGraph: Draw a bar graph using characters\n")

#To prompt the input from the user
response=input("Enter up to 10 positive whole numbers less than 50: ")

#To create a Python list containing the individual strings that represent each number entered.
numbers = response.split()

#To traverse the list in a for loop and use each list item to create a string consisting of the correct number of “=” characters
for num in numbers:

#To check if the entered string consists of only digit and if each digit is less than or equal to 50
    if num.isdigit() and int(num) <=50:

#Using string arithmetic to create each bar
        bar="="*int(num)

#To print the bar graph if valid
        print(bar) 
    else:

#To print ? if invalid input is entered
        print("?")
