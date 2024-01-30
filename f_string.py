

"""
Program: f-string exercises 
Author: Ashmi Bidrupane Suresh
Description: # f-string exercises
# x, y, z variables for the exercise
x = 27
y = 3.14159
z = 'pi'
# build f-strings to each specification below
# 10 different exercises of increasing complexity 

"""

# x, y, z variables for the exercise
x = 27
y = 3.14159
z = 'pi'

''' #1
Create a string variable s that uses
variable x to create this string ...
"27 is a whole number"
'''

s=f"{x} is a whole number"
print(f"#1 ...\n{s}")

''' #2
Create a string variable s that uses variable x
and the type() function to create this string ...
"27 is <class 'int'>"
'''

s=f"{x} is {type(x)}"
print(f"#2 ...\n{s}")

''' #3
Create a string variable q that uses
variable y to create this string ...
"pi to 6 digits is 3.14159"
'''

s=f"{z} to 6 digits is {y:.5f}"
print(f"#3 ...\n{s}")

''' #4
Create a string variable q that uses
variable y to create this string ...
"pi to 3 digits is 3.14"
'''

s=f"pi to 3 digits is {y:.2f}"
print(f"#4 ...\n{s}")

''' #5
Create a string variable r that uses
variables y and z to create this string ...
"pi to 4 digits is 3.142"
'''

s=f"{z} to 4 digits is {y:.3f}"
print(f"#5 ...\n{s}")

''' #6
Create a string variable r that uses variables x,
y, and z to create this output ...
"    27     3.14159      pi    "
Each variable is centered across 10 spaces
'''

s=f"{x:^10} {y:^10.5f} {z:^10}"
print(f"#6 ...\n{s}")

''' #7
Create a string variable r that uses variables x,
y, and z to create this table ...
"    x         y         z     
     27     3.14159      pi   "
Each item is centered across 10 spaces.
Use the newline escape sequence as needed.
'''

s=f"{'x':^10}{'y':^10}{'z':^10}\n{x:^10}{y:^10.5f}{z:^10}"
print(f"#7 ...\n{s}")

''' #8
Create a string variable q that uses variables x and
y as US currency (two decimal places, preceded
by a dollar sign, left justified across 10 spaces ...
"$27.00    $3.14     "
'''

s=f"${x:<10.2f}    ${y:<10.2f}"
print(f"#8 ...\n{s}")

''' #9
Create a string variable q that uses variables x and
y as US currency (two decimal places, preceded
by a dollar sign, center justified across 10 spaces ...
"  $27.00    $3.14   "
'''

s=f"{f'${x:.2f}':^10}{f'${y:.2f}':^10}"
print(f"#9 ...\n{s}")

''' #10
Create a string variable s that uses variables x and
y as US currency (two decimal places, with room for
4 digits left of the decimal point preceded
by a dollar sign and center justified across 10 spaces ...
" $  27.00  $   3.14 "
'''


s=f" ${x:>7.2f}  ${y:>7.2f}"
print(f"#10 ...\n{s}")




