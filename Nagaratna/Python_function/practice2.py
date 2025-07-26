# pass by values

"""def rank1(test):
    print(test)
rank1("Hello Python")

def date1(date1):
    print(date1) #Hello Python
date1("11/06/1997") # 11/06/1997

#Pass by reference:

x="Hello Good morning"
rank1(x)

def my_message(msg):
    print(msg)
my_message("Selenuim is very easy to learn") #Selenuim is very easy to learn

y="I want to learn python quickly"
my_message(y)  #I want to learn python quickly


def name ( test):
    print()

# 1). Python function program to add two numbers.
def adding(x,y):
 value=x+y
 print(value)
adding(10,20)
#####
def mult(a,b):
    mult=int(a*b)
    print(mult)
num1= int(input("Enter your number1"))
num2= int(input("Enter your number2"))
mult(num1,num2)

output:
Enter your number1 5
Enter your number2 10
50



def add(a,b):
    total = a+b
    print("Total: ",total)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

add(num1,num2)
"""
#Python function program to print the input string 10 times.
def my_name(name):
    print(name * 10)
my_name("nagaratna")

# Python function program to find the maximum of three numbers.
def max_num(x, y, z):
    if x >= y and x >= z:
        print("Maximum value is x:", x)
    elif y >= x and y >= z:
        print("Maximum value is y:", y)
    else:
        print("Maximum value is z:", z)

max_num(43, 90, 12)

#5). Python function program to find the sum of all the numbers in a list.
def add(l,m,n,o):
    result = l+m+n+o
    print("Total number is ",result)
add(2,10,40,10)
"""
Output:
Total number is  62
"""
#7). Python function program to reverse a string.
def rev1(str1):
    a = str1[::-1]
    print("Reverse of the given string: ",a)

string = "Hello Good Morning"
rev1(string)

#Program to take a list and returns a new list with unique elements of the first list
def elem(list1):
    print(list(set(list1)))
l = [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
elem(l)

#Python function program that take a number as a parameter and checks whether the number is prime or not.
def prime1(r):
    if r%2 == 0:
        print("its prime")
    else:
        print("not a prime")
prime1(2)
#Python function program to find the even numbers from a given list.
#Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_num(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num, "is even number")
        else:
            print(num, "is odd number")

y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num(y)

