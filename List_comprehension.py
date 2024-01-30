'''
Program: List Comprehension
Author: Ashmi Bidrupane Suresh
Description: Simple List Comprehension & Sorting Template
             To complete the list comprehension exercises
             functions wriiten includes
             (1) a docstring that describes the input parameters
             and the value returned
             (2) at least two significant tests that verify the function
'''


#Announce the program
print("List Comprehension\n\n")

###### 1. List comprehension analysis
def linc(a,b=2):
    '''
    description: To add value of b to all elements in the list
    input: list and int data type
    output: list data type
    '''
    return [x+b for x in a if type(x) is int]

x = [1,2,'3',4]
y = linc(x)  # [3,4,6]
z = linc(x,1) # [2,3,5]
print(x) #list x is printed as it is
print(y) #increases value by 2 expect for string x[2]
print(z) #increases value by 1 expect for string x[2]


###### 2. the listInc() function
def listInc(a):
    '''
    description: To add 1 to each elements in the list
    input: list data type
    output: list data type
    '''
    return [i+1 for i in a if type(i) == int] 


### listInc() tests
assert listInc([7,2,4,8]) == [8,3,5,9], 'listInc failed [7,2,4,8]'
assert listInc([9,-1,0.0,5]) == [10,0,6], 'listInc failed [9,-1,0.0,5]'
print('\nlistInc is OK\n')


###### 3. the listOut() function
def listOut(a):
    '''
    description: To print element of list in seperate line
    input: list data type
    output: int data type
    '''
    return [print(i) for i in a] 

### listOut() tests
listOut([7,2,'OK',8])
print()
listOut([[1,2],2.0,'$',8])
print()


###### 4. statements that move items between lists
### end of A to beginning of B
a,b = [1,2,3], [4,5,6]
# to pop out the a list value and insert into list b
b.insert(0,a.pop()) 
print(a,b)

### beginning of A to end of B
a,b = [1,2,3], [4,5,6]
#To pop out the a list value and insert into list b at last
b.append(a.pop(0))

print(a,b,'\n')


###### 5a. the rotateForward() function
def rotateForward(a):
    '''
    description: rotates list by 1 in forward direction
    input: list data type
    output: list data type
    '''
    last_element = a.pop()
    a.insert(0, last_element)
    return a

### rotateForward() tests
assert rotateForward([1,2,3,4]) == [4,1,2,3], 'rotateForward failed'
print('rotateForward ok\n')

###### 5b. the rotateBackward() function
def rotateBackward(a):
    '''
    description: rotates list by 1 in backward direction
    input: list data type
    output: list data type
    '''
    first_element = a.pop(0)
    a.append(first_element)
    return a

### rotateBackward() tests
assert rotateBackward([1,2,3,4]) == [2,3,4,1,], 'rotateBackward failed'
print('rotateBackward ok\n')


###### 6. Analysis of iSort()
def iSort(x,n=2):
    '''
    description:To sort a list according to a value of n
    input: list and int data type
    output: list data type
    '''
    #To sort the list and return the value
    return sorted(x,key =lambda a:a[n])

x = [(1,'one','uno'),(2,'two','dos'),(3,'three','tres')]
print(iSort(x))
print(iSort(x,1))
print()


###### 7. Length sorting
z = ['bzz','z','cz','azzz']

#to sort list by its length
z.sort(key=lambda z:len(z)) 
print(z,'\n')


###### 8. the backSort() function
def backSort(a):
    '''
    description: To sort a list according to last letter
    input: list data type
    output: list data type
    '''

    #to sort list by last charecter of each item
    return sorted(a,key=lambda a: a[-1])

### backSort() tests
assert backSort(['red','yellow','blue','green','black']) == \
       ['red', 'blue', 'black', 'green', 'yellow'], 'backSort FAILED'
print('backSort OK')


print("\n\n*** List Comprehension Program is Finished ***\n\n")
