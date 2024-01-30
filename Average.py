"""
Program: Average
Author:  Ashmi Bidrupane Suresh
Description: This program uses a loop and an accumulation pattern to calculate the average of a 
sequence of numbers
	00 - Announce and prompt the user for input
	01 - Declare sum and initialise it to 0 and declare an empty list
	02 - Loop to iterate the num to get the numbers to calculate the average
	03 - Loop to iterate and calculate sum and avearge
"""

#Announce
print("Program to compute the average of the numbers provided.\n")

# prompt the user for an input
Num=int(input("How many numbers would you like to average? "))

# Declare the sum variable and initialize it to 0
sum=0

# declare an empty list
list=[]

#for loop from i=0 to the total number user wants to find the average of
for i in range(Num):
        Numbers=int(input("Enter number "+str(i+1)+": "))

        #make a list of all the numbers entered
        list.append(Numbers)
        
#for loop from i=0 to the total number user wants to find the average of
for i in range(Num):
    
        #set sum=sum+list[i], Calculate sum of all element 
        sum = sum + list[i]

        # Calculate average of list element
        avg = sum/ Num

#To print average
print("\nThe average is "+str(avg)+".");



 



