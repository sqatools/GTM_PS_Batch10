# 8. Python program to interchange values between variables.

a = 10
b = 20

a,b = b,a
print("Value of a:",a)
print("Value of b:",b)

print("_"*70)

'''
# 9. Python program to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)

a = 8
b = 6
#a**2 + b**2 = c**2
lhs = a**2 + b**2
print(lhs)
c = lhs
rhs = c**2
print(rhs)

print("_"*70)

'''

# 10. Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab

a = 10
b = 20

lhs = (a+b)**2
print("lhs output:",lhs)
rhs = a**2+b**2+2*a*b
print("rhs output:",rhs)

print(lhs == rhs)


print("_"*70)


# 11. Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab

a = 50
b = 30

lhs = (a-b)**2
print("lhs output:",lhs)
rhs = a**2+b**2-2*a*b
print("rhs output:",rhs)

print(lhs == rhs)


print("_"*70)

# 12. Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)

a = 60
b = 60

lhs = a**2 - b**2
print("Output of lhs:", lhs)
rhs = (a-b)*(a+b)
print("Output of rhs:",rhs)

print("_"*70)

# 13. Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a = 8
b = 4
lhs = (a+b)**3
print(lhs)
rhs = a**3 + (3*a*b)*(a+b)+b**3
print(rhs)

print("_"*70)


