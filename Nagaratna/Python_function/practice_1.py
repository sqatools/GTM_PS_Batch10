a = 10
b = 5
c = 30
#Python Program to add two integer values.
add =(a+b)
print("Sum of two values : ",add,type(add))
# 2). Python Program to subtract two integer values.
sub = b/a
print(sub)
#3). Python program to multiply two numbers.
mul = a*b
print(mul,type(mul))
#4). Python program to repeat a given string 5 times.
str1 = "Hello"
repeat = str1*5
print(repeat)
print("*_-_"*20)

#5). Python program to get the Average of given numbers.
avg = a+b+c/3
print(avg)
#Python program to get the median of given numbers.
# Use the formula ((n/2 – 1) + n/2)/2 to find
list1=[97,34,25,66,20,11,32,33]

# sort the list
list1.sort()
n = len(list1)
if n % 2 == 0:
    med = list1[n // 2]
else:
    med = (list1[n // 2 - 1] + list1[n // 2]) / 2
print(f"The median is: {med}")


######  Python program to calculate simple interest.
# Formula = P+(P/r)*t
p = 794000
r = 10.49
t = 60
interest = (p*t*r)/100
print("simple ineterst is",interest)
 ###Python program to calculate days between 2 dates
from datetime import date

date1 = date(2024, 11, 22)
date2 = date(2026, 11, 22)

result = (date2 - date1).days
print ("Number of Days between the given Dates are: ", result, "days")

# Python program to reverse a given number
nom= int(input("Enter your number"))
reverse = int(str(nom)[::-1])
print(reverse)
print("_*_"*30)

#Program to get the Fibonacci series between 0 to 50.

num1 = 0
num2 = 1
count = 0

print("Sequ is: ",end=" ")
if count<50:
    print(num1,end=" ")
    n2 = num1+num2
    num1 = num2
    num2 = n2
    count += 1
#
