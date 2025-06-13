######Python Basic Programs, Exercises#####

###1). Python Program to add two integer values.
a1 = 2
a2 = 4
print("Addition:", a1+a2) ##Addition: 6

### 2). Python Program to subtract two integer values.####
a1 = 5
a2 = 10
print("subtraction:", a1-a2) ##subtraction: -5

###3). Python program to multiply two numbers.####
a1 = 20
a2 = 40
print("Multiplication:", a1*a2) ##Multiplication: 800

###4). Python program to repeat a given string 5 times.###
str1 = "SQATools"
a1 = 5
print("result:", str1*a1) ##result: SQAToolsSQAToolsSQAToolsSQAToolsSQATools

###5). Python program to get the Average of given numbers.###
a = 40
b = 50
c = 30
print("Average of three numbers:", (a+b+c)/3) ##Average of three numbers: 40.0

###6). Python program to get the median of given numbers.
###Note: all the numbers should be arranged in ascending order
###Formula : (n+1)/2
###n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66


###7). Python program to print the square and cube of a given number.
num1 = 9
print("square:",num1**2 ) ##square: 81
print("cube:", num1**3) ##cube: 729

###Python program to interchange values between variables.
##Input :
a = 10
b = 20
a,b = b,a
print("value of a:",a)
print("value of b:",b)

###9).Python program to solve this Pythagorous theorem.

a = 2
b = 4
c = 3

Q  = a**2 + b**2 - c**2

print("Q:", Q )

#####10). Python program to solve the given math formula.
###Formula : (a + b)2 = a^2 + b^2 + 2ab

a = 2
b = 4

lhs  = (a+b)**2
rhs = a**2 + b**2 + 2*a*b

print("lhs:", lhs)
print("rhs:", rhs)

########11). Python program to solve the given math formula.######
###Formula : (a – b)2 = a^2 + b^2 – 2ab###

a = 4
b = 8
lhs = (a-b)**2
rhs = a**2 + b**2 - 2*a*b

print("lhs:", lhs)
print("rhs:", rhs)

########12). Python program to solve the given math formula.###
###Formula : a2 – b2 = (a-b)(a+b)###

a = 2
b = 6

lhs = a**2 - b**2
rhs = (a-b)*(a+b)

print("lhs:", lhs) ##lhs: -32
print("rhs:", rhs) ##rhs: -32

#############13). Python program to solve the given math formula#########
##Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a = 3
b = 2

lhs = (a+b)**3
rhs = a**3 + 3*a*b*(a+b) + b**3

print("lhs:", lhs) #lhs: 125
print("rhs:", rhs) #rhs: 125

###########14). Python program to solve the given math formula###
##Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

a = 4
b = 2

lhs = (a-b)**3
rhs = a**3 - 3*a**2*b + 3*a*b**2 - b**3

print("lhs:", lhs) ##lhs: 8
print("rhs:", rhs) ##rhs: 8

######15). Python program to calculate the area of the square####
##Formula : area = a*a

a = 3
area = a*a

print("area:", area) #area: 9

##########16). Python program to calculate the area of a circle.###
##Formula = PI*r*r

r = 6
PI = 3.14
area = PI*r*r

print("area:", area) ##area: 113.03999999999999

###17). Python program to calculate the area of a cube.##
##Formula = 6*a*a

a = 5
area = 6*a**2

print("area:", area) ##area: 150

####18). Python program to calculate the area of the cylinder###
##Formula = 2*PI*r*h + 2*PI*r*r

PI = 3.14
r = 6
h = 4

area = 2*PI*r*h + 2*PI*r**2

print("area:", area) ##area: 376.8

####19). Python program to check whether the given number is an Armstrong number or not.##
##Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

lhs = 153
rhs = 1**3 + 5**3 + 3**3

print("lhs:", lhs) ##lhs: 153
print("rhs:", rhs)##rhs: 153