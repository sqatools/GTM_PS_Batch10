# IF_ELSE PRACTICE PROGRAMS

# 43). Python program to check whether two numbers are equal or not.
# Input :A=26,B=88

A = 26
B = 88
if A == B:
    print("The no. is equal")
else:
    print("The no. is not equal")
print('_'*70)

# 44. Python program to check whether the given input is a complex type or not.
# Input: a=5+6j

a = 5+6j
if type(a) == complex:
    print("True")
else:
    print("False")

print('_'*70)
# 45. Python program to check whether the given input is Boolean type or not.
# Input: a=True

a = True
if type(a) == bool:
    print("True")
else:
    print("False")

print('_'*70)
# 46. Python program to check whether the given input is List or not.

a = [1, 3, 6, 8]
if type(a) == list:
    print("True")
else:
    print("False")

print('_'*70)

# 47. Python program to check whether the given input is a dictionary or not.
# Input: A={‘name’:’Virat’,’sport’:’cricket’}

A = {'name':'Virat','sport':'cricket'}
if type(A) == dict:
    print("True")
else:
    print("False")
print('_'*70)

# 48. Python program to check the eligibility of a person to sit on a roller coaster ride or not. Eligible when age is greater than 12.

Age = int(input("Enter the age:"))
if Age >= 12:
    print("You are eligible")
else:
    print("You are not eligble")

print('_'*70)



