'''
Program: Phloog's Class
Author: Ashmi Bidrupane Suresh
Purpose: Program to calculate grades for Dr. Phloog
         Drops lowest 1 out of every 3 grades and
         computes the letter grade (X < 80%, Z >90%, for Y everyone else)
Revisions:
    00 - Announce and define function code for function findGrade(grades)
    01 - Code to test the function
'''

# Announce the program name 
print('Program to calculate grades for Dr. Phloog\n')

#This function accepts the list of grades and drops the lowest grade out of 3 grades
#Then the average is computed and letter grade is calculated based on average.
#This accepts list data type and returns tuple data type.

def findGrade(grades):


  
    # To sort grade list in ascending 
    grades.sort()
    # 3-5 quizzes
    if len(grades)//2 <= 2:
        grades = grades[1:]
    # 6-8 quizzes
    elif len(grades)//3 <= 2:
        grades = grades[2:]
    # more
    else:
        grades = grades[3:]
    # compute sum of the remaining grades 
    grade_sum = 0
    for i in range(len(grades)):
        grade_sum += grades[i]
    # compute average grade
    average = grade_sum / len(grades)
    # determine letter-grade
    if average < 80:
        letter = 'X'
    elif average > 90:
        letter = 'Z'
    else:
        letter = 'Y'
    #Returns required result
    return (average,letter) 


# CODE TO TEST THE FUNCTION
grades = []
grades.append([50,100,60]) # [80.00,'Y']
grades.append([50,100,50,50,100,50,50,100,50]) # [75.00,'X']
grades.append([65,100,22,89,0,100,92,78,87,97]) # [91.86,'Z']
grades.append([90,70,60,100,65,95,27,55,79,60]) # [79.86,'X']
grades.append([65,100,22,89,45,92,78,87]) # [85.17,'Y']
for item in grades:
    grade = findGrade(item)
    print(f"{grade[0]:6.2f} --> {grade[1]} ")   

