###  (a - b)³ = a³ - 3a²b + 3ab² - b³ ###

a = 5
b = 3
rhs = (a - b)**3
lhs = a**3 - (3*((a)**2)*b) + (3*a*((b)**2)) - b**3

print("The value of lhs : " , lhs)
print("The value of rhs :" , rhs)
print("Verify lhs = rhs :" , lhs == rhs)
