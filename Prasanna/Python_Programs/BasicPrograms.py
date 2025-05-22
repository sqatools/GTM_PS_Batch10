#1.Python Program to add two integer values.
import statistics

a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))

add = a+b
print("Adding of two integer Values is:",add)

sub = a-b
print("Subtraction of two integer Values is:",sub)

mul = a*b
print("Multiplication of two integer Values is:",mul)

div = a/b
print("Division of two integer Values is:",div)

#5. Python program to repeat a given string 5 times

string1 = "Prasanna"
repeat = string1*5
print(repeat)
print("Resulting String is:",repeat)

import statistics
#6.Python program to get the median of given numbers.
list1 = [20,98,78,67,54]
order_list1 = sorted(list1)
median_of_numbers = statistics.median(list1)

print(median_of_numbers)
#7.Python program to print the square and cube of a given number

number = int(input("Enter the number to find the square and cube:"))
square = number * number
print("Square is:",square)
print("square is :",number**2)
cube = number * number * number
print("Cube is:",cube)
print("Cube is:",number**3)

print("_"*50)
#9)Python program to interchange values between variables.
a = 20
b = 30
a = a + b
b = a - b
a = a - b
print("after Interchanging the values:",a,b)
print("_"*50)
#using comma operator
a = 90
b = 70
a,b = b,a
print("after Interchanging the values:",a,b)
print("_"*50)

#Python program to solve this Pythagoras theorem.
# a**2 + b**2 = c**2

a = int(input("Enter the a Value:"))
b: int = int(input("Enter the b Value:"))
result = a*a + b*b
print("The Pythagoras theorem is:",result)
print("_"*50)
#Python program to solve the given math formula.
formula1 = a**2 + b**2 + 2*a*b
print("The (a+b)^2 is:",formula1)
print("_"*50)
formula2 = a**2 + b**2 - 2*a*b
print("The (a-b)^2 is:",formula2)
print("_"*50)
formula3 = (a + b) * (a - b)
print("The (a^2 - b^2) is:",formula3)
print("_"*50)
formula4 = a**3 + 3 * a * b *(a + b) + b**3
print("The (a - b)^3 is:",formula4)



