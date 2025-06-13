# IF_ELSE PYTHON PRACTISE PROGRAM
# 21). Python program to check whether the given number is positive or negative and even or odd.
# Input = 26
# Output = The given number is positive and even
'''
Input = int(input("Enter the number:"))

if Input >=0:
    print("the no. is postive")
    if Input%2 == 0:
        print("The no. is even")
    else:
        print("The no. is odd.")
else:
    print("the no. is negative")
#issue in this program
'''

print('_'*70)

# 22). Python program to print the largest number from two numbers.
# Input:
# 25, 63
# Output = 63

a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number:"))

if a>b:
    print("a has largest number:",a)
else:
    print("b has the largest number:",b)

print('_'*70)
# 25). Python program to check whether the given number is an integer or not.

g = 54

if type(g) == int:
    print("True")
else:
    print("False")

print('_'*70)

# 26). Python program to check whether the given number is float or not.

h = 12.6

if type(h) == float:
    print("True")
else:
    print("False")

print('_'*70)

# 27). Python program to check whether the given input is a string or not.
# Input = ‘sqatools’
# Output = True

P = "sqatools"
if type(P) == str:
    print("True")
else:
    print("False")

print('_'*70)

# 28). Python program to print all the numbers from 10-15 except 13
for i in range(10,16):
    if i!= 13:
        print(i)