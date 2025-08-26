# Program to calculate simple interest.
# Si = (P*r*t)/100
# P = Principle Amount
# r = interest rate
# t = time in year
from datetime import datetime

P = 1000
r = 10
t = 2

Amount = (P*r*t)/100
print("Simple Interest Amount :", Amount)  #Simple Interest Amount : 200.0


print("-"*50)
# Program to calculate compound interest.
# CI = P(1+r/n)^nt-P

P = 10000
r = 10
n = 1
t = 2

Amount = P*(1+r/n)**n*t-P
print("Compound Interest Amount :", Amount)  #Compound Interest Amount : 21000.0


print("-"*50)
# Find area of sphere
# Formula = 4*PI*R^2

R = 2
PI = 3.21

Area = 4*PI*R**2

print("Area of Sphere :", Area)  #Area of Sphere : 51.36


date_1 = datetime(2025, 1, 5)
date_2 = datetime(2025, 1, 22)
result = (date_2 - date_1).days
print("No of days :", result)


