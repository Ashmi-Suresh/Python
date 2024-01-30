
'''
Program: Double Scramble Challenge
Author: Ashmi Bidrupane Suresh
Purpose: Program to unscramble words by rotating,sorting and joining characters on position.
Revisions: 
    00: To print announcement
    01: To Rotate each list in z so the integer is in the zero position without changing the order of the characters
    02: To Sort the lists based on the integer value in each and To Create a list of characters for each word.
    03: To Create a string for each of the four words and print them.

'''
#To print announcement
print("double Scramble Challenge:\n")

z = [['s', 'a', 3, 't', 'n'], ['h', 'b', 'c', 1, 'p'], ['h', 'y', 'c', 'k', 5], [4, 'c', 'e', 'i', 'l'], ['o', 'a', 'h', 2, 'i']]


# To Rotate each list in z so the integer is in the zero position without changing the order of the characters
def rotate(lst):
    index = lst.index([x for x in lst if isinstance(x, int)][0])
    return lst[index:] + lst[:index]

t = [rotate(i) for i in z]

# To Sort the lists based on the integer value in each
t_sorted = sorted(t, key=lambda x: x[0])

# To Create a list of characters for each word.
a = [[j[i] for j in t_sorted] for i in range(1, len(t_sorted[0]))]

# To Create a string for each of the four words and print them.
for word in a:
    print(''.join(word), end=' ')

print("\n\n***Double Scramble Challenge Ended***") 




