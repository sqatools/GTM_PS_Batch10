
# Math Operators
"""
+ : Plus
- :  substraction
* :  multiplication
/ :  division with single /
// :  division with double //
== :  equal to
!= :  not equal to
%  :  Remainder operator
** :  Power Operator
"""


# Addition of value ###
a1 = 40
a2 = 50
print("addition :", a1 + a2)
add = a1 + a2
print("Addition of variable :", add)

# subtraction of values
print("subtraction 500 - a1 :", 500 - a1, a2-a1)  # 460
p = 70
q = 80
r = 50
print("p-q-r :", p-q-r) #  -60

# multiplication of values
print("multiply a2 by 5 :", a2 * 5)  # 250

print("_"*50)
###### division of values ########
d1 = 50
d2 = 4

print("division single / :", d1/d2) # 12.5   # single / return output with pointer
print("division with double // :", d1//d2) # 12   # double // return output as whole number

print("_"*50)
###### remainder of values ########

v1 = 15
v2 = 4
# % : remainder operator
print("remainder value :", v1%v2) # 3

print("_"*50)
###### Power operator ** ########
A = 5
print("Square of 5 :", A**2) # 25
print("Cube of 5 :", A**3) # 125
print("5 repeat 5 time :", A**5) # 3125

print("_"*50)
########### compare two values with equal to and not equal to  ####

x = 40
y = 40
z = 70

# check and x and y have same value
print(x == y) # True

# check and x and z values are same
print(x == z) # False

# check and y and z values are not same
print(y != z)  # True


#############################################
# write a python program to solve quadratic equation
# (a+b)^2 = a^2 + b^2 + 2ab
a = 9
b = 7
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print("LHS output :", lhs)
print("RHS output :", rhs)



##################################################
# write a program to get average 5 numbers
n1 = 50
n2 = 60
n3 = 70
n4 = 90
n5 = 100

average = (n1+n2+n3+n4+n5)/5
print("average output :", average)
# average output : 74.0
