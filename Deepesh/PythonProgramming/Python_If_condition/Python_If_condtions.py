    # compare two numbers

a = 20
b = 20

print(a == b)

if a == b:
    print("a and b have same value")
else:
    print("a and b does not have equal value")


print("_"*50)
# write a program to check the given value is even or odd
num1 = 21

if num1%2 == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)


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


print("_"*50)
# write a python program to check given number is divisible by 3 and 5

num2 = 15

if num2%3 == 0 and num2%5 ==0:
    print("This number is divisible by 3 and 5 :", num2)
else:
    print("This number is not divisible by 3 and 5 :", num2)



print("_"*50)
# write a python program to check given number is divisible by 5 or 7

x = 35
if x%5 ==0 or x%7 ==0:
    print("This number is divisible by 5 or 7 : ", x)
else:
    print("This number is not divisible by 5 or 7 : ", x)

print("_"*50)
############################# if-elif- else condition #####################
# check multiple condition in the program
# program to check which number has greater value
p = 500
q = 100
r = 500

if p > q and p > r :
    print("P has greater value :",  p)
elif q > p and q > r :
    print("Q has greater value :",  q)
elif r > p and r > q:
    print("R has greater value :", r)
else:
    print("No one has greater value")


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

print("_"*50)
# write a program to for interview process with the help of nested if condition.

round1 = "pass"
round2 = "pass"
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



#######################################
#HW :
# Q1. write a program to check the person is eligible to vote on the basis age > 18
# Q2. write a program to calculate the electricity bill amount on the basic of unit consumtion.
# 1. unit < 100 : per unit charge is 15
# 2. unit > 100  and num < 200 : per unit charge is 200
# 3. unit > 200 : per unit charge is 25
