print("Hello world")
print("_"*40)
a = 10
#a= variable
#10 = value
# : = assignment operator

print(a)
print(id(a))
# id = 140704426894536 (place where it variable is stored)

b = 10
c = 10
print("address of a:",id(a))
print("address of b:",id(b))
print("address of c:",id(c))

p, q, r = 40, 50, 60
print("value of p:" , p)
print("value of q:" , q)
print("value of r:" , r)

###Assign same values to different variables

x = y = z = 100
print("value of x:", x )
print("value of y:", y )
print("value of z:", z )
# or
print("value of x, y, z:", x, y, z )

print("_"*50)

# Rules to define the varaibale name
#1. cannot contain space in variable name
#eg var1 = 123
#var 23 = 456 incorrect

#2. Variable should not start with number
#var567 = 12436
#56var = 789456 incorrect

#3. There is no limit for variable name
#we_are_learning_python_programming = "Python Programming" correct
# m = 200 correct

#4. Variable names are case sensitive
name = 'Rohan'
Name = 'Prateik'
NAME = 'Sohan'
NAMe = 'Shyam'
print(name, Name, NAME, NAMe)

print("_"*90)

#5. The variable cannot contain special characters except underscore.
#var$abc = "Python" Incorrect
#var_abc_hello = "Correct"

print("_"*80)
#+ = addition
# - = subtraction
#/ = division with single/
#// = division with double //
#== = equal to
#!= =not equal to
#% = remainder operator
#** = power operator

#addition
a1 = 40
a2 = 50
print("addition:", a1+a2)

#Subtraction
print("subtraction:", a1-a2)

#Multiplication of values
print("multiplication:", a1*a2)

p = 50
q = 60
r = 40
print("p-q-r:", p-q-r)

#division of values
a1 = 32
a2 = 4
print("a1/a2:", a1/a2)

##########Division of values #################
d1 = 45
d2 = 4
print("division single/:", d1/d2)
print("division with double //:", d1//d2)

####Remainder Operator##############
v1 = 15
v2 = 4
print("remainder value:", v1%v2)

########Power Operator########
A = 6
print("cube:", A**3)
print("double:", A**2)

############compare two values with equal to and not equal to ##########

x = 40
y = 40
z = 70

print(x == y) #True
print(x == z)# False
print(x != z) #False

######### Write a python program to solve quadratic equation ########

# (a+b)^2 = a^2 + b^2 + 2ab
a = 9
b = 7

lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print("lhs output:", lhs)
print("rhs output:", rhs)

######write down to find the average of 5 numbers###########

n1 = 50
n2 = 60
n3 = 70
n4 = 90
n5 = 100

average = (n1 + n2 +n3 +n4 + n5)/5
print("average of numbers:", average)

######calculate simple interest.######

P = 1500
R = 5
T = 2

Q = P*R*T/100
print("Q:", Q )

#####Calculate compound interest ####
##CI = P(1+R/N)^NT - P



######Area of square######
##Area = 4pir^2

Pi = 3.21
R = 14

area = 4*3.21*R**2
print("area:", area)
