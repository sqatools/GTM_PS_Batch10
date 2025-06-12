# Python_Variables

a = 6
# a :  variable
# = : assignment operator
# 6 : value

print(a)       #6
print(id(a))   #140735000880200

# If multiple variable having same value, then their address will be same

b = 5
c = 5

print("Address of b:", b, id(b))    # 5 140735000880168
print("Address of c:", c, id(c))    # 5 140735000880168

print('_'*70)
### Assign different value to different variable at a time  ####

s, d, f = 20, 30, 40

print("value of s:", s)
print("value of d:", d)
print("value of f:", f)

print('_'*70)

###  Assign same value to multiple variables at a time ####

a = b = c = 80

print("value of a:", a)     #value of a: 80
print("value of b:", b)     #value of b: 80
print("value of c:", c)     #value of c: 80

print('_'*70)

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

print("_" * 70)
# Math Operators
"""
+ : Plus
- :  subtraction
* :  multiplication
/ :  division with single /
// :  division with double //
== :  equal to
!= :  not equal to
%  :  Remainder operator
** :  Power Operator
"""

print("_" * 70)

### Addition of value ###

b1 = 60
b2 = 20
print("addition:", b1 + b2)

add = b1 + b2
print("addition of variables:", add)

### subtraction of values ###

a1 = 200
a2 = 25
a3 = 50
print("a1-a2-a3:", a1-a2-a3)    #a1-a2-a3: 125


### multiplication of values ###

c1 = 10
c2 = 15

m = c1 * c2

print(m)
print("_"*70)

###### division of values ########
d1 = 60
d2 = 5

print("division single / :", d1/d2) # 12.0
print("division with double // :", d1//d2) # 12

print("_"*70)

###### remainder of values ########

v1 = 100
v2 = 3
# % : remainder operator
print("remainder value :", v1%v2) # 1

print("_"*70)
###### Power operator ** ########
A = 2
print("Square of 2 :", A**2) # 4
print("Cube of 2 :", A**3) # 8
print("2 repeat 5 time :", A**5) # 32

print("_"*70)

########### compare two values with equal to and not equal to  ####

x = 50
y = 50
z = 90

# check x and y have same value
print(x == y) # True

# check x and z values are same
print(x == z) # False

# check y and z values are not same
print(y != z)  # True

#############################################




