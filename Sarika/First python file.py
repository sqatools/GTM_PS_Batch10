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