# 1. Python Program to add two integer values.
import math

a = 50
b = 30
print("# 1. Addition of a & b :", a+b)

c = a+b
print("Value of c :", c)
print(id(a))


print("-"*50)
# 2. Python Program to subtract two integer values.
V1 = 95
V2 = 45
V3 = V1-V2
print("# 2. Subtraction of V1 & V2 :", V1-V2)
print("Value of V3 :", V3)


print("-"*50)
# 3. Python program to multiply two numbers.
A1 = 10
B1 = 40
C1 = A1*B1
print("# 3. Multiplication of A1 & B1 :", A1*B1)
print("Value of C1 :", C1)


print("-"*50)
# 4. Python program to repeat a given string 5 times.
String = "Nisha"
n = 5
print("# 4. Output :", String*n)


print("-"*50)
# 5. Python program to get the Average of given numbers.
N1 = 40
N2 = 50
N3 = 60
N4 = 70
print("# 5. Average of N1 N2 N3 & N4 :", N1+N2+N3+N4/4)


print("-"*50)
# 7. Python program to print the square and cube of a given number.
C1 = 10
print("# 7. Square of C1 :", C1**2)
print("# 7. Cube of C1 :", C1**3)


print("-"*50)
# 8. Python program to interchange values between variables.
H1 = 25
H2 = 45
H1, H2 = H2, H1
print("# 8. Value of H1 :", H1)
print("# 8. Value of H2 :", H2)

print("-"*50)
# 9. Python program to solve this Pythagoras theorem.
# Theorem : a^2+b^2=c^2
# Result : a**2+b**2
a = 2
b = 3
print("# 9. Hypotenuse c^2 :", a**2+b**2)
print("Value of c :", math.sqrt(a**2+b**2))


print("-"*50)
# 10. Python program to solve the given math formula.
# Formula : (a+b)^2 = a^2 + b^2 + 2ab
# Result : a**2 + b**2 + 2*a*b
a = 2
b = 3
print("# 10. Value of (a+b)^2 :", a**2 + b**2 + 2*a*b)


print("-"*50)
# 11. Python program to solve the given math formula.
# Formula : (a–b)^2 = a^2 + b^2 – 2ab
# Result : a**2 + b**2 - 2*a*b
a = 4
b = 5
print("# 11. Value of (a–b)^2 :", a**2 + b**2 - 2*a*b)


print("-"*50)
# 12. Python program to solve the given math formula.
# Formula : a^2 – b^2 = (a-b)(a+b)
# Result : (a-b)*(a+b)
a = 7
b = 6
print("# 12. Value of a^2–b^2 :", (a-b)*(a+b))


print("-"*50)
# 13. Python program to solve the given math formula.
# Formula : (a+b)^3 = a^3 + 3ab(a+b) + b^3
# Result : a**3 + 3*a*b*(a+b) + b**3

a = 3
b = 2
print("# 13. Value of (a+b)^3 :", a**3 + 3*a*b*(a+b) + b**3)



print("-"*50)
# 14. Python program to solve the given math formula.
# Formula : (a–b)^3 = a^3 – 3a^2b + 3ab^2 + b^3
# Result : a**3 - 3*a**2*b + 3*a*b**2 + b**3

a = 3
b = 2
print("# 14. Value of (a-b)^3 :", a**3 - 3*a**2*b + 3*a*b**2 + b**3)


print("-"*50)
# 15. Python program to calculate the area of the square.
# Formula : area = a*a
a = 4
print("# 15. Area of square :", a*a)


print("-"*50)
# 16. Python program to calculate the area of a circle.
# Formula = PI*r^2
# r = radius
# PI = 3.14

r = 4
PI = 3.14
print("# 16. Area of Circle :", PI*r**2)


print("-"*50)
# 17. Python program to calculate the area of a cube.
# Formula = 6*a*a

a = 6
print(" 17. Area of Cube : ", 6*a*a)