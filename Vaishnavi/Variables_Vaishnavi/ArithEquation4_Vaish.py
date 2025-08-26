### (a + b)3 = a3 + 3ab(a+b) + b3  ###

a = 5
b = 3
rhs = (a + b)**3
lhs = a**3 + (3*a*b * (a+b)) + b**3

print("The value of lhs : " , lhs)
print("The value of rhs :" , rhs)
print("Verify lhs = rhs :" , lhs == rhs)
