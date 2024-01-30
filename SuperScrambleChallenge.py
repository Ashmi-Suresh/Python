
'''
Program: Super Scramble Challenge
Author: Ashmi Bidrupane Suresh
Purpose: Program to unscramble words by rotating,sorting and joining characters on position.
Revisions: 
    00: To print announcement
    01: To create function to rotate list in mess.
    02: To use or loop to sort and build 


'''
#To print announcement
print("Super Scramble Challenge:\n")

mess = [['o', 'c', 'h', 'c', 'a', 64, 'd'],
        ['o', 'o', 91, 'y', 'y', 'e', 'i'],
        ['u', 'r', 'o', 'u', 'y', 46, 'e'],
        ['u', 'y', 'e', 'r', 19, 't', 't'],
        ['a', 'h', 55, 's', 'n', 'i', 's'],
        [27, 'u', 'r', 't', 'r', 'r', 'n'],
        [72, 'a', 'c', 'p', 't', 'g', 'm']]

#To Define a function named rotate that takes a list of lists named mess as input
def rotate(mess):
    #To determine the maximum length of the words in mess
    max_len = max(len(word) for word in mess)
    #To iterate over each word in mess
    for word in mess:
        #To iterate over each character position in the current word
        for i in range(len(word)):
            #if the first character in the current word is an integer, exit the loop
            if type (word[0]) is int:
                break
            #To shift the first character to the end of the current word otherwise
            word.append(word.pop(0))

# To use or loop to sort and build 
    for i in range(len(mess[0])-1):
        #To sort the words in mess based on the character at the current position
        mess = sorted(mess,key = lambda a : a[i])
        #To print the characters at the current position for each word in mess, starting from the second character
        print(''.join([word[i+1] for word in mess]))
rotate(mess)

print("\n\n***Super Scramble Challenge Ended***") 

        

