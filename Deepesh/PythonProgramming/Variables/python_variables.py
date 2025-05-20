a = 10
# a :  variable
# = : assignment operator
# 10 : value

print(a)  # 10
print(id(a))  # 140728139664088

# If multiple variable having same value, then their address will be same
b = 10
c = 10
print("Address of a:", a, id(a))  # 10 140728139664088
print("Address of b:", b, id(b))  # 10 140728139664088
print("Address of c:", c, id(c))  # 10 140728139664088

### Assign different value to different variable at a time  ####\

# multiline comment
"""
p, q, r = 40, 50, 60
print("value of p :", p) # value of p : 40
print("value of q :", q) # value of q : 50
print("value of r :", r) # value of r : 60
"""
# comment line
###  Assign same value to multiple variables at a time ####

x = y = z = 100
print("value of x:", x)  # value of x: 100
print("value of y:", y)  # value of y: 100
print("value of z:", z)  # value of z: 100
print("value of, x, y, z :", x, y, z)
# value of, x, y, z : 100 100 100


print("_" * 50)

### Rules to define the variable name ####
# 1. Can not contains space in variable name.
# var1 = 567 # correct
# var 123 = 700 # incorrect

# 2. Variable name should not start with number
# var567 = 90000 # correct
# 23x = 500 # incorrect


# 3. There is no limit for variable name, you can define any long name.
# we_are_learning_python_programming = 'Python Programing' # correct
# m = 800  # correct

# 4. Variable names are case-sensitive.
name = 'Rahul'
Name = 'Mohan'
NAME = 'Raghav'
NAMe = 'Pratik'
print(name, NAME, Name, NAMe)
# Rahul Raghav Mohan Pratik

# 5. Variable name can not contain special characters except underscore
# var$abc = 'Hello'  # incorrect
var_abc_hello = 'Python'  # correct

print("_" * 50)
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

print("_" * 50)
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

# class work
# 1. write a program to calculate simple interest
# si = (P*R*T)/100
# P = principle amount
# R = rate of interest
# T = time in year

# 2. write a program to calculate the compound interest
"""
CI = P(1+r/n)^nt - P
P : principle amount
r :  rate of interest
n :  Number of time interest is compounded
t : time in year

"""

# 3. Find area of sphere
"""
formula = 4*PI*R**2
PI = 3.21
R = radius


"""
