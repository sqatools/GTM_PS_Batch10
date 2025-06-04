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

###21 May ####

##Python Dta Type:
# 1. Number Data Type
#a. Integer Data Type
#b. Float Data Type
#c. Complex Number Data Type

#2. Sequential Data Type:
#a. String
#b. List
#c. Tuple

#3. Dictionary Data Type
#4. Set Data Type
#5. Boolean Data Type

###Integer Data Type#####

"""

Properties:
-> Immutable, once it is defined we cannot change.
-> Only contains whole number
-> Can be positive or negetive 
-> There is no specific number.
"""

num=0
num1=10
num2=100
num3=458875547894562588
num4=-456789

print("num:", num, type(num))
print("num1:", num1, type(num1))
print("num2:", num2, type(num2))
print("num3:", num3, type(num3))
print("num4:", num4, type(num4))

print("_" * 50)
###Float Data Type#####

"""
Immutable, once it is defined we cannot change.
-> Only contains pointer type values
-> Can be positive or negetive 
-> There is no specific number.

"""

f1 = 0.0
f2 = 0.2
f3 = 7218715678.58318784
f4 = 6843485145443432784186.5897664962693987565
f5 = -5463544.534843

print("f1:", f1, type(f1))
print("f2:", f2, type(f2))
print("f3:", f3, type(f3))
print("f4:", f4, type(f4))
print("f5:", f5, type(f5))

####Complex Number Data Type####
"""
Properties:

-> immutable data type
-> combination of real and imaginary numbers
-> Can be positive or negetive 

e.g. x+yj
x= real number
y = imaginary number

"""

z =  10- 20j
print("z:", z, type(z))

#2. Sequential Data Type:

####String####

"""
-> Immutable Data Type. 
-> Can be defined with the help of single double and triple quote.
-> follows positive and negative indexing.
-> Can contain any type of data.

"""

s1 = ""
s2 = "H"
s3 = "Hello"
s4 = 'Hello we are learning python'
s5 = """Hello, what a lovely dat it is,
I hope everything is good at your end and I wish you all 
the best

"""
s6 = ''' Hello, what a lovely dat it is,
I hope everything is good at your end and I wish you all 
the best. 
'''

s7 = "Hello, we are learning 'python' language."
s8 = 'Hello, we are learning "python" language.'

print("s1:", s1,type(s1))

###follows positive and negative indexing.####

str1 = "Python"

"""
0 1 2 3 4 5
P Y T H O N
-6-5-4-3-2-1

"""
print(str1[1])
print("str1:", str1[1])
print(str1[-2])


####### write characters with positive and negative indexing #####
str2 = "Programming"
print(str2[5])
print(str2[-8])
print(str2[6])

#####26 may Datatype #####

####List####

"""
##Properties###
-> Mutable, can be modified.
-> Store data in comma separated format.
-> contain all type od data i.e. integer, float, tuple, set complex, string, dict. set , bool
-> follows positive and negative indexing
-> Store data in square bracket.
-> Usage of the list data type, where updates are happening on regular basis.
e.g Employee Management.

"""
list1 = [4, 5.6, 'Hello', 5 + 8j, [3, 5, 6], (1, 2, 3), {'a': 123}, {4, 7, 8, 4}, True]
print("list1:", list1)
print(list1[4])
print(list1[-2])
print(list1[-6])
print(list1[6])
print(list1[4][2])

list2 = [4,5,6]
list2.append(10)
print("list2:", list2) ###list2: [4, 5, 6, 10]

print("_"*50)

####Tuple####

"""
-> IMMutable, cannot be be modified.
-> Store data in comma separated format.
-> contain all type od data i.e. integer, float, tuple, set complex, string, dict. set , bool
-> follows positive and negative indexing
-> Store data in round bracket.
-> Usage of the list data type, where data is fixed.
e.g. store days in a month, days in weeks, months in a year.
-> It is faster than list in terms of performance.
e.g Employee Management.
"""

tup1 = (2, 5.6, 'Python', (4,6,7), [1,3,5], {'b': 456}, {6,8,9}, True, False)
print("tup1:", tup1)
print("tup1:", tup1[4])
print("tup1:",tup1[2][2] ) #tup1: t
print("tup1:", tup1[-6][-1])

tup2 = (3, 6 ,7)
# We dont have any method to update the tuple value##

print("_"*50)

#3. Dictionary Data Type##
dict7 = {'a': 123, 'b': 4567}

"""
#Properties:
-> Mutable data type, we can modify the dict data. 
-> Stores data in key value form in the form of curly braces {key:value}.
-> Stores unique keys i.e. duplicate keys are not allowed. If we store duplicate key, it will only consider only the latest
-> Only immutable data type can be the key in dict e.g. int, float, complex, string, tuple, boolean
-> Can contain all data types as values and duplicate values are also allowed.
 
"""

dict2 = {12:456, 3.5:2.6, 'Python': 'We are learning python programming', (4,5,6):('a', 'b', 'c', 'd'), 4+50j: 500+600j, True : False}
print("dict2:", dict2)

print("_"*50)

###########04 June##########

str1 = "Hello Python programming"
print(str1, type(str1)) #Hello Python programming <class 'str'>

##string formatting##

str2 = "Hello my name is Rahul and age is 25 and living in Mumbai"
name = "Pankaj"
age = 30
city = "Pune"

###Methods used for formatting:###

#A. String Concatenation:

#result1 = "Hello my name is "+name+" and age is "+str(age)+" and living in "+city
#print(result1) #Hello my name is Pankaj and age is 30 and living in Pune

result1 = "Hello my name is "+name+" and age is "+str(age)+" and living in "+city
print(result1) #Hello my name is Pankaj and age is 30 and living in Pune

#B. Format Method:
#result2 = "Hello my name is {} and age is {} and living in {}".format(name, age, city)
#print(result2)#Hello my name is Pankaj and age is 30 and living in Pune

result2 = "Hello my name is {} and age is {} and living in {}".format(name,age,city)
print(result2) #Hello my name is Pankaj and age is 30 and living in Pune

print("_"*50)

#C. F String Formatting:
result3 = f"Hello my name is {name} and age is {age} and living in {city}"
print(result3) #Hello my name is Pankaj and age is 30 and living in Pune

print("_"*50)




























