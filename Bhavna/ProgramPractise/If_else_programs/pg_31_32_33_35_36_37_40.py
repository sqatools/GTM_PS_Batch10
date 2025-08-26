
# 31. Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.

i = int(input("Enter the input:"))

if i%2==0 and i%3==0:
    print("FizzBuzz")
elif i%2==0:
    print("Fizz")
elif i%3==0:
    print("Buzz")
else:
    print("nothing")

# 32. Python program to check whether an alphabet is a vowel.

b1 = 'a'
vowel = ['a','e','i','o','u','A','E','I','O','U']
if b1 in vowel:
    print("True")
else:
    print("False")

# 33. Python program to check whether an alphabet is a consonant.

c1 = 'B'
vowel = ['a','e','i','o','u','A','E','I','O','U']

if c1 not in vowel:
    print("True")
else:
    print("False")

print('_'*70)

# 35. Python program to check whether a triangle is equilateral or not. An equilateral triangle is a triangle in which all three sides are equal.

a = int(input("Enter the length of the first sides of the triangle:"))
b = int(input("Enter the length of the second sides of the triangle:"))
c = int(input("Enter the length of the third sides of the triangle:"))

if a == b == c:
    print("True")
else:
    print("False")

print('_'*70)

# 36. Python program to check whether a triangle is scalene or not. A scalene triangle is a triangle that has three unequal sides.

d = int(input("Enter the length of the first sides of the triangle:"))
e = int(input("Enter the length of the second sides of the triangle:"))
f = int(input("Enter the length of the third sides of the triangle:"))

if d != e != f:
    print("True")
else:
    print("False")
'''
'# 37. Python program to check whether a triangle is isosceles or not. An isosceles triangle is a triangle with (at least) two equal sides.

a1 = int(input("Enter the length of 1st side:"))
a2 = int(input("Enter the length of 2nd side:"))
a3 = int(input("Enter the length of 3rd side:"))

if a1 == a2 != a3:
    print('True')
else:
    print('False')
'''
print('_'*70)
# 40. Python program to check whether the input number is divisible by 12 or not.

g = 144
if g%12 == 0:
    print("True")
else:
    print("False")

print('_'*70)


