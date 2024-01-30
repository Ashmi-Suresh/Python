"""
Program: Area of a Circle
Author: Ashmi Bidrupane Suresh
Description: This program calculates the area of a circle after reading the diameter from the user
Revisions:
	00 - Announce and get the diameter from the user
	01 - Compute and print the area of the circle
"""
#Announce
print("Computing the area of the Circle\n")

import math

# prompt the user for an input
D = float(input("Enter the diameter of the circle: "))

#Calculate the radius from the diameter entered
R=float(D/2)


# generates area of the circle
A = float(math.pi * R*R)

# print the area of the circle
print("The area of the circle of diameter",D,"is:",A)


