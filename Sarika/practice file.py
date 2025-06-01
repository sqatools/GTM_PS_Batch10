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

print("lhs:", lhs)
print("rhs:", rhs)


