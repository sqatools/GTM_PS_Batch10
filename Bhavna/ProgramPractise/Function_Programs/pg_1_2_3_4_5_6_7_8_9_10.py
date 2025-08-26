# FUNCTION PRACTICE PROGRAMS

# 1). Python function program to add two numbers.

def add(a,b):
    Addition = a+b
    print(Addition)

add(150,50)

print('_'*70)

# 2). Python function program to print the input string 10 times.

def str():
    string = "hello"*10
    print(string)

str()

print('_'*70)

# 3). Python function program to print a table of a given number.

def table(num):
    for i in range(1,11):
        print(i ,'*', num, '=',i*num)

table(5)

print('_'*70)

# 4). Python function program to find the maximum of three numbers.

def max(a,b,c):
    if a>b and a>c:
        print(f"{a} is greater")
    elif b>a and b>c:
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")

max(17,21,-9)

print('_'*70)

# 5). Python function program to find the sum of all the numbers in a list.
# Input = [6,9,4,5,3]

def sum(Input):
    t = 0
    for i in Input:
        t+=i
    print(t)

Input = [6,9,4,5,3]
sum(Input)

print('_'*70)
# 6). Python function program to multiply all the numbers in a list.

def multiply(Input):
    t=1
    for i in Input:
        t*=i
    print(t)

Input = [-8, 6, 1, 9, 2]
multiply(Input)

print('_'*70)

# 7). Python function program to reverse a string.
# Input: 'Python1234'

def reverse(Input):
    str = Input[::-1]
    print(str)

msg = "Python1234"
reverse(msg)

print('_'*70)

# 8). Python function program to check whether a number is in a given range.

def number(num):
        if num in range(2,21):
            print("Its in range")
        else:
            print("It is not in range")

number(7)

print('_'*70)

# 9). Python function program that takes a list and returns a new list with unique elements of the first list.

def new_list(list):
    output = []
    for i in list:
        if i not in output:
            output.append(i)

    print(output)

list = [2,2,3,1,4,4,4,4,4,6]
new_list(list)

print('_'*70)
# 10). Python function program that take a number as a parameter and checks whether the number is prime or not.
def prime(num):
    n = 0
    for i in range(2,num):
        if num%i == 0:
            n+=1
    if n>0:
        print("It is not a prime number")
    else:
        print("It is a prime number")

prime(23)

print('_'*70)
