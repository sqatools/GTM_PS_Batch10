# 1. Python Program to add two integer values.
import math
from datetime import datetime

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
# 6. Python program to get the median of given numbers.
# Note: all the numbers should be arranged in ascending order
# Formula : (n+1)/2 for even
# Formula : ((n+2)+(n/2+1))/2 for odd
# n = Number of values

data = [10, 30, 20, 40, 50, 60]
data.sort()
n = len(data)
if n % 2 == 1:
    median_value = data[n//2]
else:
    median_value = (data[n//2-1]+data[n//2])/2
print("# 6. The median Value :", median_value)


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
# LHS = a**2+b**2
# RHS = c**2
a = 3
b = 4
LHS = a**2+b**2
c = math.sqrt(LHS)
print("# 9. Hypotenuse c :", c)

RHS = math.hypot(a, b)
print("# 9. Hypotenuse c :", RHS)


print("-"*50)
# 10. Python program to solve the given math formula.
# Formula : (a+b)^2 = a^2 + b^2 + 2ab
# RHS : a**2 + b**2 + 2*a*b
# LHS : (a+b)**2
a = 2
b = 3
RHS = a**2 + b**2 + 2*a*b
LHS = (a+b)**2
print("# 10. RHS (a^2+b^2+2ab) :", RHS)
print("# 10. LHS (a+b)^2 :", LHS)


print("-"*50)
# 11. Python program to solve the given math formula.
# Formula : (a–b)^2 = a^2 + b^2 – 2ab
# RHS = a**2 + b**2 - 2*a*b
# LHS = (a–b)**2
a = 3
b = 9
RHS = a**2 + b**2 - 2*a*b
LHS = (a-b)**2
print("# 11. RHS (a^2+b^2-2ab) :", RHS)
print("# 11. LHS (a-b)^2 :", LHS)


print("-"*50)
# 12. Python program to solve the given math formula.
# Formula : a^2 – b^2 = (a-b)(a+b)
# RHS = (a-b)*(a+b)
# LHS = a**2 - b**2
a = 7
b = 6
RHS = (a-b)*(a+b)
LHS = a**2 - b**2
print("# 12. RHS (a-b)(a+b) :", RHS)
print("# 12. LHS a^2 – b^2 :", LHS)


print("-"*50)
# 13. Python program to solve the given math formula.
# Formula : (a+b)^3 = a^3 + 3ab(a+b) + b^3
# RHS = a**3 + 3*a*b*(a+b) + b**3
# LHS = (a+b)**3

a = 3
b = 2
RHS = a**3 + 3*a*b*(a+b) + b**3
LHS = (a+b)**3
print("# 13. RHS a^3+3ab(a+b)+b^3 :", RHS)
print("# 13. LHS (a+b)^3 :", LHS)


print("-"*50)
# 14. Python program to solve the given math formula.
# Formula : (a–b)^3 = a^3 – 3a^2b + 3ab^2 + b^3
# RHS = a**3 - 3*a**2*b + 3*a*b**2 + b**3
# LHS = (a-b)**3

a = 3
b = 2
RHS = a**3 - 3*a*b*(a-b) - b**3
LHS = (a-b)**3
print("# 14. RHS a^3-3ab(a-b)-b^3 :", RHS)
print("# 14. LHS (a-b)^3 :", LHS)


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
Area = PI*r**2
print("# 16. Area of Circle :", Area)


print("-"*50)
# 17. Python program to calculate the area of a cube.
# Formula = 6a^2
a = 6
Area = 6*a**2
print("# 17. Area of Cube : ", Area)


print("-"*50)
# 18. Python program to calculate the area of the cylinder.
# Formula = 2PIr*h + 2PIr^2
r = 4
h = 5
PI = 3.14
Area = 2*PI*r*h + 2*PI*r**2
print("# 18. Area of the Cylinder :", Area)


print("-"*50)
# 19. Python program to calculate simple interest.
# Formula = P*r*t/100
# P = Principle Amount
# r = Annual interest rate
# t = time
P = 1000
r = 10
t = 2
SI = P*r*t/100
print("# 19. Simple Interest :", SI)


print("-"*50)
# 20. Python program to print the current date in the given format
# Note: Use the DateTime library
date = datetime.now()
print("# 20. Current Date :", date.strftime("%d/%m/%Y"))


print("-"*50)
# 21. Python program to calculate days between 2 dates.
# Input date : (2025, 5, 23) (2025, 5, 01)
Date1 = datetime(2025, 5, 25)
Date2 = datetime(2025, 5, 1)
Output = (Date1-Date2).days
print("# 21. Number of days between two dates are :", Output, "Days")


print("-"*50)
# 22. Python program to calculate compound interest.
# Formula : A = P(1+r/n)^(nt)
# A = Final Amount
# P = Principal Amount
# r = Annual interest rate
# n	= number of times interest applied per time period
# t	= number of time periods elapsed
# CI = A - P
P = 3000
r = 5
t = 3
A = P*(1+r/100)**t
CI = A - P
print("Final Amount :", A)
print("# 22. Compound Interest :", CI)


print("-"*50)
# 23. Python program to calculate the volume of a sphere.
# Formula = (4/3*pi*r^3)
r = 2
PI = 3.14
Volume = (4/3*PI*r**3)
print("# 23. Volume of sphere :", Volume)


print("-"*50)
# 24. Python program to find the square root of a number.
# Note: Use the math library to get the square root.
num1 = 49
print("# 24. Square root of number :", math.sqrt(num1))
