import math
print("Basic Arithmetic Operations")
print("-"*25)
# 1.Program to Add  2 integer values
a = 50
b = 40
c = a + b
print("Addition of 2 numbers:", c)

# 2.Program to Subtract 2 integer values
a = 50
b = 40
c = a - b
print("Subtraction of 2 numbers:", c)

# 3.Multiplication of 2 integer values
a = 50
b = 40
c = a * b
print("Multiplication of 2 numbers:", c)

# 4.Division of 2 integer values
a = 50
b = 5
c = a / b
d = a // b
print("Division of 2 numbers using /:", c)
print("Division of 2 numbers using //:", d)

# 5.Program to repeat a given string 5 times.
str1 = "Hello World "
print("String after repetition:", str1 * 5)

# 6.Program to interchange values between variables.
a = 5
b = 7
print("Values of A and B before interchange :", a, b)
a, b = b, a
print("Values of A and B after interchange :", a, b)

# 7.Program to get the Average of given numbers.
p = 100
q = 200
r = 400
s = 700
t = 900
print("Average of given numbers:", (p+q+r+s+t)/5)

# 8.Program to print the square and cube of a given number.
num1 = 6
square = num1 ** 2
cube = num1 ** 3
print("Square of a given Number:", square)
print("Cube of a given Number:", cube)

# 9.Program to calculate Simple Interest
# SI= (P*R*T)/100
# P : Principle
# R : Rate of Interest
# T : Total number of Years
P = 150000
R = 12
T = 2
Simple_Interest = (150000 * 12 * 2)/100
print("Simple Interest:", Simple_Interest)

# 10.Program to calculate Compound Interest
# P : Principle
# R : Rate of Interest
# T : Total number of Years
P = 150000
r = 12
t = 2
n = 100
CI = p * (1+r/n) ** n - p
print("Compound Interest:", CI)

# 11.Program to calculate Area of a Sphere
PI = 3.14
R = 3
Area = 4 * PI * R ** 2
print("Area of a Sphere:", Area)

# 12.Program to calculate Area of a Square
# Formula : area = a*a
a = 3
Area = a * a
print("Area of a Sphere:", Area)

# 13.Program to calculate Area of a Circle
# Formula = PI*r*r
PI = 3.14
R = 3
Area = PI * R ** 2
print("Area of a Circle:", Area)

# 14.Program to calculate Area of a Cube
# Formula : area = 6*a*a
a = 3
Area = 6 *a * a
print("Area of a Cube:", Area)

# 15.Program to calculate Area of a Cylinder
# Formula = 2*PI*r*h + 2*PI*r*r
PI = 3.14
r = 3
h = 4
Area = (2*PI*r*h) + (2*PI*r**2)
print("Area of a Cylinder:", Area)

# 16.Program to solve this Pythagoras theorem.
# Formula(a2 + b2 = c2)
a = 3
b = 4
lhs = a**2 + b**2
c = math.sqrt(lhs)
print("Pythagoras Theorem result")
print("-"*25)
print("value of lhs:", lhs)
print("value of rhs:", c**2)

# 17.Program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
a = 3
b = 4
lhs = (a + b)**2
rhs = (a ** 2)+(b ** 2) + 2*(a*b)
print("Linear Equation 1")
print("-"*25)
print("value of lhs :", lhs)
print("value of rhs :", rhs)

# 18.Program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
a = 10
b = 4
lhs = (a - b)**2
rhs = (a ** 2)+(b ** 2) - 2*(a*b)
print("Linear Equation 2")
print("-"*25)
print("value of lhs :", lhs)
print("value of rhs :", rhs)

# 19.Program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)
a = 10
b = 4
lhs = (a**2) - (b**2)
rhs = (a-b) * (a+b)
print("Linear Equation 3")
print("-"*25)
print("value of lhs :", lhs)
print("value of rhs :", rhs)

# 20.Program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a = 3
b = 4
lhs = (a + b)**3
rhs = (a ** 3) + 3*(a*b)*(a+b) + (b ** 3)
print("Linear Equation 4")
print("-"*25)
print("value of lhs :", lhs)
print("value of rhs :", rhs)

# 21.Program to solve the given math formula.
# Formula : (a - b)3 = a^3 - 3ab(a-b) - b^3
a = 4
b = 2
lhs = (a - b)**3
rhs = (a ** 3) - 3 * a * b * (a-b) - (b ** 3)
print("Linear Equation 5")
print("-"*25)
print("value of lhs :", lhs)
print("value of rhs :", rhs)


















