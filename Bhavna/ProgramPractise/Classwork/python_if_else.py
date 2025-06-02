# 29/05/2025

# compare two numbers

a = 18
b = 50

if a == b:
    print("a and b have same value.")
else:
    print("a and b doesn't have same value.")

print('_'*70)

# write a program to check the given value is even or odd

num = 15

if num%2 == 0:
    print("The is a even number")
else:
    print("The is a odd number.")

print('_'*70)

"""
AND Condition
cond1 and cond2

True and False :  False
False and True :  False
False and False :  False
True and True : True


or Condition
cond1 or cond2
True or False :  True
False or True :  True
True or True :  True
False or False :  False

# Logical operators
> :   Greater than
< :   Less than
>= :  Greater than equal to
<= :  Less than equal to
== :  Equal to 
!= :  Not equal to

in : in operator
not in : not in operator
is : is operator
is not :  is not operator
"""
# write a python program to check given number is divisible by 3 and 5

num2 = 25

if num2%3 == 0 and num2%5 == 0:
    print("This number is divisible by 3 and 5:", num2)
else:
    print("This number is not divisible by 3 and 5:", num2)

print('_'*70)
# write a python program to check given number is divisible by 5 or 7

a = 14

if a%5 ==0 or a%7 == 0:
    print("This number is divisible by 5 or 7:", a)
else:
    print("This number is not divisible by 5 or 7:", a)

print('_'*70)

############################# if-elif- else condition #####################
# check multiple condition in the program

# program to check which number has greater value

m = 10
n = 20
o = 80

if m > n and m > o:
    print("m is greater:", m)
elif n > m and n > o:
    print("n is greater:", n)
elif o > m and o > n:
    print("o is greater:", o)
else:
    print("No one has greater value")

print('_'*70)
###################### Nested If condition #################
"""
if cond1:
    code1
    if cond2:
        code2
        if cond3:
            code3
        else:
            code3
    else:
        else code2

else:
    else code1
"""
# write a program for interview process with the help of nested if condition.

Round1 = "Pass"
Round2 = "Pass"
Round3 = "Pass"

if Round1 == "Pass":
    print("First round is cleared")
    if Round2 == "Pass":
        print("Second round is cleared")
        if Round3 == "Pass":
            print("Third round is cleared")
        else:
            print("Sorry, Failed in third round")
    else:
        print("Sorry, Failed in second round")

else:
    print("Sorry, Failed in first round")

print('_'*70)

# 30-05-2025 Session

#################### If condition with "in", "not in" operator #########

# program to check given value v1 is available in list or not
# and v2 is not available list

list = [8, 1, 6, 7, 15]

v1 = 8
v2 = 15

if v1 in list:
    print("v1 is available in the list")
else:
    print("v1 is not available in the list")

# check v2 is not available in list

if v2 not in list:
    print("v2 is not available in the list")
else:
    print("v2 is available in the list")

print('_'*70)

#################### use of "is" and "is not" operator ###############
# check given string in not None

str1 = "Hello world"

if str1 is not None:
    print("str1 has values")
else:
    print("str1 is empty")

print('_'*70)

# use of "is" operator

a = False
num = 5

if a is True:
    print("square of num:", num**2)
else:
    print("Cube of the num:", num**3)

print('_'*70)

a1 = "Hello"
if a1 is "Hello":
    print("a1 contains Hello")
else:
    print("a1 does not contain hello")

print('_'*70)
# use of "is not" operator

b1 = "Bhavna"
if b1 is not "Bhavana":
    print("Bhavna Prakash")
else:
    print("Nothing")

print('_'*70)

############# If condition in one line ############

number = 80
result = "even" if number%2 == 0 else "odd"
print(result)