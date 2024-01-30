'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    return fact

print(factorial(int(input())))



#to return maximum of 2 numbers
def max(a,b):
    if a>b:
        return a
    else:
        return b


print (max(7,6))

#to return max of 3 numbers entered
def max(a,b,c):
    if a>=b and a>=c:
        return a
    if b>=a and b>=c:
        return b
    else:
        return c

print(max(4,7,8))


def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))

def power(a,n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >=0:
        return res
    else:
        return (1/res)

print(power(float(input()),int(input())))

'''
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small)-ord('a')+ord('A'))
    return first_letter_big + word[1:]

source=input().split()
res=[]
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
