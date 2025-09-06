# 1. Program to compare two numbers
a = 10
b = 20
if a == b:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

print("_" * 50)

# 2. Program to check the given value is even or odd

num1 = int(input("Enter any number:"))
if num1 % 2 == 0:
    print("The number is even number")
else:
    print("The number ais odd number")

"""
# AND condition
# Logical operators
> : Greater than
< : Less than
>= : Greater thn equal to
<= : Less than equal to
==: Equal to
!=: Not Equal to

in : in operator
not in : not in operator
is : is operator
is not : is not operator

"""
# 4.Program to find the result of interview using nested if condition
round1 = "pass"
round2 = "fail"
round3 = "pass"
if round1 == "pass":
    print("First round is cleared")
    if round2 == "pass":
        print("Second round is cleared")
        if round3 == "pass":
            print("Third round is cleared")
        else:
            print("Third round is not cleared")
    else:
        print("Second round is not cleared")
else:
    print("First round is not cleared")

# 5. Program to check if a number is available in List
List1 = [4, 5, 7, 10]
v1 = 7
v2 = 50
if v1 in List1:
    print("The value is available in the List")
else:
    print("The value is available in the List")

if v2 not in List1:
    print("The value is not available in the List")
else:
    print("The value is available in the List")
