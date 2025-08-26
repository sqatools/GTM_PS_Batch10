#write a program to calculate Simple Interest

# SI = (400 * 5 * 4) / 100
#
# # Output the result
# print(f"Simple Interest is: {SI:.2f}")


a = 10
#a : variable
# = : assignment
# 10 : variable

print(a) # 10
print(id(a)) # 140721131103432


b = 10
c = 10
print("Address of a:", a , id(a))  #140721131103432
print("Address of b:", b , id(b))  #140721131103432
print("Address of c:", c , id(c))  #140721131103432

#assign different variable value to different at a time ###

p, q, r = 40, 50, 60
print("values of p :", p)  #40
print("values of q :", q)  #50
print("values of r :", r)  #60

### Assign same value to multiple variable at a time ###

x = y = z = 100
print("value of x:", x)  #100
print("value of y:", y)  #100
print("value of z:", z)  #100


print("_"*50)

#1 can not contain space in variable name
#var1 = 567 # correct
# var 123 = 700 # incorrect

#2 variable name should not start with number
#var567 + 900 # correct
#567 = 600 # incorrect

#3 there is no limit for variable name you can define any long name.
#we are learing_python_proramming = "python programming " # correct
# n = 800 # correct

# 4 variable name are case sensitive

name = 'vinod'
Name = 'vinod'
NAME = 'vinod'
NAMe = 'vinod'
print(name,Name, NAME, NAMe )

#5 variable name can not contain special characters except underscore
# var$abc = 'hello'  # incorrect
var_abc_hello = 'python' #correct

print("_"*50)
#math Operators

""""
+ : plus
- : substraction
* : multiplication
/ : division with single /
// : division with double //
== : equal to
!= : not equal to
%  : Remainder operator
** : Power Operator
"""

# Addition pf value ##
a1 = 40
a2 = 50
print("addtion :", a1+a2)
add =a1 + a2
print("Addition of varaible :", add)

#subtraction of values
print("subtraction - a1:", 500-a1, a2-a1)
p =70
q = 80
r = 50
print("p-q-r:", p-q-r)

#multiplication

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
# """
# CI = P(1+r/n)^nt - P
# P : principle amount
# r :  rate of interest
# n :  Number of time interest is compounded
# t : time in year
#
# """
#
# # 3. Find area of sphere
# """
# formula = 4*PI*R**2
# PI = 3.21
# R = radius


"""

# 
# Python Program to add two integer values.
# 
# 1. Take two numbers as input.
# 2. Add the two numbers using the + operator.
# 3. Print the result.
# 
# num1 = 10
# num2 = 20
# 
# print("Addition of num1+num2:",num1+num2)
# 
# Python program to check whether the given number is an Armstrong number or not.
# num = a = 153
# rev = 0
# 
# while a>0:
#     rem = a%10
#     rev = rev +rem**3
#     a= a//10
# 
# if rev == num:
#     print("It is a armstrong number")
# else:
#     print("It is not a armstrong number")
# 
# #Python Program to subtract two integer values.
# num1 = 50
# num2 = 20
# 
# print(" subsraction of num1-num2:", num1-num2)
# 
# 
# #########
# Python program to multiply two numbers.
# num1 = 20
# num2 = 40
# 
# print("multiplication of num1*num2:", num1*num2)
# 
# 
# 
# ##########
# Python program to repeat a given string 5 times.
# 
# str1 = "hellow"
# n1 = 4
# 
# print("result:",str1*n1)
# 
# 
# 
# Python program to get the Average of given numbers.
# 
# a = 40
# b = 50
# c = 30
# 
# print(" total sum of number:", (a+b+c)/3)
# 
# 
# 
# 
# Python program to get the median of given numbers.
# all the numbers should be arranged in ascending order
# 
# values = [10, 20, 30, 40, 50]
# 
# # sort the list
# values.sort()
# 
# # get length of the list
# n = len(values)
# 
# if n % 2 == 1:
#     median_value = values[n // 2]
# else:
#     median_value = (values[n // 2 - 1] + values[n // 2]) / 2
# 
# print(f"The median is: {median_value}")
# 
# 
# Python program to print the square and cube of a given number.
# 
# num1 = 9
# print("Square of number :", num1**2)
# 
# print("Cube of number :", num1**3)
# 
# Python program to interchange values between variables.
# a = 10
# b = 20
# a, b = b, a
# 
# print("value of a :", a)
# print("value of b :", b)
# 
# 
# Python program to solve this Pythagorous theorem.
# 
# a = 10
# b = 20
# 
# c = math.sqrt(a**2 + b**2)
# 
# print("The length of the hypotenuse is:", c)
# 
# 
# 
# Python program to solve the given math formula.
# Take two variables as input and assign value to them.
# 
# a = 2
# b = 3
# result = a**2+2*a*b+b**2
# 
# print("(a+b)^2: ",result)
# 
# Python program to solve the given math formula.
# a = 2
# b = 3
# result = a**2-2*a*b+b**2
# 
# print("(a-b)^2: ",result)
# 
# 
# Python program to solve the given math formula.
# a = 3
# b = 2
# result = (a+b)*(a-b)
# 
# print("(a^2-b^2): ",result)
# 
# Python program to solve the given math formula.
# 
# a = 3
# b = 2
# result = a**3+3*a*b*(a+b)+b**3
# 
# print("(a+b)^3: ",result)
# 
# 
# 
# Python program to solve the given math formula.
# 
# a = 3
# b = 2
# result = a**3-3*a**2*b+3*a*b**2+b**3
# 
# print("(a-b)^3: ",result)
# 
# Python program to calculate the area of the square.
# side = int(input("Enter the side of a square: "))
# print("Area of sqaure: ",side**2)
# 
# Python program to calculate the area of a circle.
# radius = int(input("Enter radius of circle: "))
# area = 3.14*radius*radius
# 
# print("Area of circle: ",area)
# 
# Python program to calculate the area of a cube.
# side = int(input("Enter side of a cube: "))
# area = 6*side*side
# 
# print("Area of cube: ",area)



#Python program to calculate the area of the cylinder.
r = int(input("Enter radius of cylinder: "))
h = int(input("Enter height of cylinder: "))
area = 2*3.14*r*h+2*3.14*r*r

print("Area of cylinder:",area)

"""""







