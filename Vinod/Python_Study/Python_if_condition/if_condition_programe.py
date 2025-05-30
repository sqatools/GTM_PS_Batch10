# compare two number

# a = 10
# b = 10
#
# print(a == b)
#
# if a == b:
#     print(" a and b same vale")
# else:
#     print("a and b different value")


# write a program to check the given value is even or odd

num1 = 16

if num1 % 2 == 0:
    print("this is even number:", num1)
else:
    print("this is odd number:", num1)

# note You assign the value 16 to the variable num1
# The modulus operator % calculates the remainder of the division.
# num1 % 2 checks if the number is divisible by 2.
# If the remainder is 0, the number is even.
# In this case, 16 % 2 == 0 is True.


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

num2 = 17

if num2 % 3 == 0 and num2 % 5 == 0:
    print("this number is divided by 3 and 5:", num2)
else:
    print("This number is not divisible by 3 and 5 :", num2)

# You assign the value 17 to the variable num2
# This line checks two conditions using the and operator:
# num2 % 3 == 0 checks if num2 is divisible by 3 (no remainder).
# num2 % 5 == 0 checks if num2 is divisible by 5 (no remainder).
# and means both conditions must be True for the block to run.

# write a python program to check given number is divisible by 5 or 7

x = 46

if x % 5 == 0 or x % 7 == 7:
    print("This number is  divisible by 3 and 5 :", x)
else:
    print("This number is not divisible by 3 and 5 :", x)

print("_" * 50)
############################# if-elif- else condition #####################
# check multiple condition in the program
# program to check which number has greater value

a = 80
b = 90
c = 95

if a > b and a > c:
    print("a has greater value :", a)
elif b > a and b > c:
    print("b has greater value :", b)
elif c > a and c > b:
    print("b has greater value :", b)

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

print("_" * 50)
# write a program to for interview process with the help of nested if condition.

round1 = "pass"
round2 = "failed"
round3 = "pass"

if round1 == "pass":
    print("First round is cleared")
    if round2 == "pass":
        print("Second round is cleared")
        if round3 == "pass":
            print("Third round is cleared")
        else:
            print("Sorry failed in third round")
    else:
        print("Sorry failed in second round")

else:
    print("Sorry failed in first round")

# Q1. write a program to check the person is eligible to vote on the basis age > 18
# Q2. write a program to calculate the electricity bill amount on the basic of unit consumtion.
# 1. unit < 100 : per unit charge is 15
# 2. unit > 100  and num < 200 : per unit charge is 200
# 3. unit > 200 : per unit charge is 25


# Q1. write a program to check the person is eligible to vote on the basis age > 18

age = 19

if age <= 18:
    print("person is eligible to vote on the basis (age ≥ 18):", age)
else:
    print("person is not eligible to vote on the basis (age < 18):", age)
