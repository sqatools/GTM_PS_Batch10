'''#1.Python Program to add two integer values.
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
'''
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


