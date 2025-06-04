# Compare two numbers

a = 20
b = 30
if a == b:
    print("a & b have same value")
else:
    print("a & b don't have same value")
# a & b don't have same value


print("-"*50)
# Write a program to check the given value is even or odd

num1= 20
if num1%2 == 0:
    print("Given number is even :", num1)
else:
    print("Given number is odd :", num1)
# Given number is even : 20


"""
AND Condition
True & False : False
True & True : True
False & True : False
False & False : False

OR Condition
True or False : True
True or True : True
False or True : True
False or False : False

# Logical Operators
> : Greater than
>= : Greater than equal to
< : Less than
<= : Less than equal to
== : Equal to
!= : not equal to


in : in operator
not in : not in operator
is : is operator
is not: is not operator 
"""


print("-"*50)
# Write a python program to check given number is divisible by 3 and 5

num2= 20
if num2%3 == 0 and num2%5 == 0:
    print("Number is divisible by 3 & 5 :", num2)
else:
    print("Number is not divisible by 3 & 5 :", num2)
# Number is not divisible by 3 & 5 : 20


print("-"*50)
# Write a python program to check given number is divisible by 5 or 7

num3 = 50
if num3%5 == 0 or num3%7 ==0:
    print("Number is divisible by 5 or 7 :", num3)
else:
    print("Number is not divisible by 5 or 7 :", num3)
# Number is divisible by 5 or 7 : 50


print("-"*50)
# if-elif- else condition
# check multiple condition in the program


# Write a program to check which number has greater value

a = 30
b = 20
c = 40
if a > b and a > c:
    print("a has greater value :", a)
elif b > a and b > c:
    print("b has greater value :", b)
elif c > a and c > b:
    print("c has greater value :", c)
else:
    print("No one has greater value")
# c has greater value : 40


print("-"*50)
# Nested If condition
"""
if cond1:
    code1
    if cond2:
        code2
        if code3:
            code3
        else:
            code3
    else:
        else code2
else:
    else code1
"""

# Write a program to for interview process with the help of nested if condition.

round1 = "pass"
round2 = "pass"
round3 = "pass"
if round1 == "pass":
    print("First round cleared")
    if round2 == "pass":
        print("Second round cleared")
        if round3 == "pass":
            print("Third round cleared")
        else:
            print("Sorry failed in third round")
    else:
        print("Sorry failed in second round")
else:
    print("Sorry failed in first round")
# First round cleared
# Second round cleared
# Third round cleared

print("-"*50)
# If condition with "in", "not in" operator

# Write a program to check given value v1 is available in list or not
# and v2 is not available list

list1 = [1, 2, 3, 4, 5, 6, 7]
v1 = 2
v2 = 9

if v1 in list1:
    print("v1 value is in list :", v1)
else:
    print("v1 is not in list :", v1)
# v1 value is in list : 2


if v2 not in list1:
    print("v2 is not in list :", v2)
else:
    print("v2 is in list :", v2)
# v2 is not in list : 9



print("-"*50)
# use of "is" and "is not" operator

# check given string in not None

str1 = "Hello we are learning python programming"
if str1 is not None:
    print("Str1 has value")
else:
    print("str is empty")
# Str1 has value


print("-"*50)
var1 = False
num1 = 2
if var1 is True:
    print("Square of num", num1, "is", (num1**2))
else:
    print("Cube of num", num1, "is", num1*3)
# Cube of num 2 is 6


print("-"*50)
p1 = "Hello"
if p1 is "Hello":
    print("p1 contains 'Hello'")
else:
    print("p1 does not contain Hello")
# p1 contains 'Hello'


print("_"*50)
# If condition in one line

num2= 49
output = ("even" if num2%2 == 0 else "odd")
print("Output :", output, num2)
# Output : odd 49