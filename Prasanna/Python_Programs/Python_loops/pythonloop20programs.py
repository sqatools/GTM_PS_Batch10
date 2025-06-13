# Write a Python loops program to find those numbers which are divisible by 7 and multiple
# of 5, between 1500 and 2700 (both included).
# Input1:1500
# Input2:2700
i = 1500
j = 2700
for num in range(1500, 2700):
    if (num % 7 == 0) and (num % 5 == 0):
        print(num, end=" ")
    else:
        continue

# Python Loops program to construct the following pattern, using a nested for loops.
for i in range(6):
    print(i * "*")
for i in range(4, -1, -1):
    print(i * "*")
# Python Loops program that will add the word from the user to the empty string using python.
# Input: “python”
# Output : “python”

input1 = input("Enter any string:")
output = " "
for char in range(len(input1)):
    output = output + input1[char]
print(output)
# Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Output :
# Number of even numbers: 4
# Number of odd numbers: 5
input2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for val in range(len(input2)):
    if val % 2 == 0:
        even += 1
    else:
        odd += 1
print("even count :", even)
print("odd count :", odd)

# Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
#
for i in range(0, 11):
    if i == 3 or i == 6:
        continue
    print(i, end=" ")

#  Write a program to get the Fibonacci series between 0 and 20 using python.
# Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
num1 = 0
num2 = 1
count = 0
while count < 20:
    print(num1, end=" ")
    fib = num1 + num2
    num1 = num2
    num2 = fib
    count += 1
# 7). Write a program that iterates the integers from 1 to 30 using python.
# For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
    elif i % 3 == 0:
        print("Fizz", i)
    elif i % 5 == 0:
        print("Buzz", i)

# 8).Write a program that accepts a word from the user and converts all uppercase in the word
# to lowercase using python.
# Input : “SqaTOOlS”
# Output : “sqatools”
str1 = str(input("Enter your string"))
print(str1.lower())
