"""
Program: Cypher Program 
Author: Ashmi Bidrupane Suresh
Description: encryption scheme program where each letter in the alphabet is represented by a number.
Revisions:
	00 - Announce and prompt the input from the user
	01 - Converting the entered input to lowercase
	02 - Using function cypher_word(s) to code with for loop to traverse the string so each character can be isolated in sequence. 
	03 - Call the function and print the code for the entered word(s)
	

"""

#Announce
print("Program to encode a word\n")

#To prompt the input from the user
s = str(input("Enter a word: "))

#To use function cypher_word() so that the input word returns the numeric_code representic the encyption required.
def cypher_word(s):

#To convert the string s into lowercase
    s = s.lower()

#To create an empty list and assign it to the variable number
    number=[]

#For loop to traverse the string(S) so each character(C) can be isolated in sequence
    for c in (s):

#ord() built-in function to convert each character to the number used by the system to represent it
#.appnd() used to add an element to the end of a list
        number.append(ord(c) - ord('a'))


    return number

number = cypher_word(s)

#to print the output statement
print('The code for "{}" is: {}'.format(s.lower()," ".join(str(c) for c in number)))
