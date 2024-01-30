"""
Program: Linear Prediction program
Author: Ashmi Bidrupane Suresh
Description: This program obtains two integers from a user at the console and uses them to predict the next number in the linear sequence Revisions:
	00 - Announce and get the first and second numbers from the user
	01 - Compute and print the next number in the sequence
"""

#Announce
print("Linear Prediction\n")

# prompt the user for an input
First_num = int(input("Enter the 1st  number: "))
Second_num = int(input("Enter the 2nd number: "))

#generates the next_sum
Common_diff = Second_num-First_num
Next_num = Second_num+Common_diff

# print the next number in the sequence
print("the linear sequence is : ", First_num , Second_num ,Next_num)

