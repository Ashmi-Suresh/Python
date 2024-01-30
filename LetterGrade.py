"""
Program: Letter Grade Project
Author: Ashmi Bidrupane Suresh
Description: This program Computes final course grades for students based on percentage scores using a function where the numerical score is converted to letter grdae(A+ to F).
Revisions:
	00 - To Announce and code is written for the function letterGrade()
	01 - To Prompt the score input from the user in numercial format
	02 - To print the letter grade
"""

#Announce
print("Program to compute a letter grade for a numerical score\n")

#Function creation
def letterGrade(score):

    """
    
    # To return the letter grade of the score in the format score(float) [0.00 to 100.00]
    # To return letter grade (str) according to the following scale

    A+  : if score >= 95
    A   : if 90 <= score < 95
    A-  : if 85 <= score < 90
    B+  : if 80 <= score < 85
    B   : if 75 <= score < 80
    B-  : if 70 <= score < 75
    C+  : if 65 <= score < 70
    C   : if 60 <= score < 65
    C-  : if 55 <= score < 60
    F   : if score < 55
    
    """


    #check for A+s
    if score >= 95:
        return "A+"

    #Check for As
    elif score <95 and score >=90:
        return"A"

    #check for A-
    elif score <90 and score >=85:
        return"A-"

    #check for B+s
    elif score <85 and score >=80:
        return"B+"

    #check for Bs
    elif score <80 and score >=75:
        return"B"

    #check for B-s
    elif score <75 and score >=70:
       return"B-"

    #check for C+
    elif score <70 and score >=65:
        return"C+"

    #check for Cs
    elif score <65 and score >=60:
        return"C"

    #check for C-s
    elif score <60 and score >=55:
        return"C-"

    #check for Fs
    elif score <55 and score >=0:
       return"F"
        

# To prompt the user for an input
score = float(input("Enter the numerical score:"))

#To print the letter garde
print("The letter grade for",score,"percent is",letterGrade(score))




