'''
Program: Scramble Challenge
Author: Ashmi Bidrupane Suresh
Purpose: Program to unscramble words
Revisions: 
    00: To print announcement
    01: To Sort the tuples based on the integer value in each.
    02: To Use zip() function to transpose the characters of each word. 
    03: To Use the join() method to create a string for each of the four words and print them.

'''

#To print announcement
print("Scramble Challenge:\n") 

z = [('v', 'c', 'l', 6, 'r'), ('i', 'a', 'i', 4, 't'), ('a', 'f', 'g', 1, 'p'), ('h', 'n', 'r', 3, 's'), ('e', 'e', 'a', 7, 'e'), ('c', 'i', 'o', 2, 'a'), ('e', 'n', 'l', 5, 'u')]

# Step 1: Sort the tuples based on the integer value in each.
z_sorted = sorted(z, key=lambda x: x[3])
z.sort(key=lambda x: x[3])

# Step 2: Use zip() function to transpose the characters of each word.
s = [list(chars) for chars in zip(*[tpl[:3]+tpl[4:] for tpl in z])]

# Step 3: Use the join() method to create a string for each of the four words and print them.
for chars in s:
    print(''.join(chars), end=' ')


print("\n\n***Scramble Challenge Ended***") 
