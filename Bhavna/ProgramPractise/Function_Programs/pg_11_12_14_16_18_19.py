# Function Practice Programs

# 11). Python function program to find the even numbers from a given list.

def even(list):
    even1=[]
    for i in list:
        if i%2 == 0:
            even1.append(i)

    print(even1)

Input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even(Input)

print('_'*70)

# 12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.

def square():
    for i in range(1,10):
        print(i**2,end=" ")

square()
print()
print('_'*70)

# 14). Python function program to access a function inside a function.

def outer():
    def inner(msg):
        print("First msg:",msg)

    inner("Hello")

outer()

print('_'*70)

# 16). Python function program to calculate the sum of numbers from 0 to 10.

def sum():
    c = 0
    for i in range(1,11):
        c+=i
        print("Output:",c)

sum()

print('_'*70)

# 18). Python function program to create a function with *args as parameters.

def square(*abc):
    for val in abc:
        print(val**3,end=" ")

square(5,6,8,7)

print()

print('_'*70)

# 19). Python function program to get the factorial of a given number.

def factorial(num):
    fact = 1
    for i in range(num,0,-1):
        fact = fact*i
        print(f"factorial value {num}:",fact)

factorial(5)

print('_'*70)
'''
# 20). Python function program to get the Fibonacci series up to the given number.

def fibonacci():
    fib_out = []
    a,b = 1,1
    fib_out.append(a)
    while b<=50:
        fib_out.append(b)
        a,b = b,a+b
    print(fib_out)
fibonacci()
'''

