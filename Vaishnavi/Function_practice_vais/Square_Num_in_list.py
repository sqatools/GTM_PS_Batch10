"""
 Python function program to create and print a list where the values are squares of numbers between 1 to 10.
"""

def square(num):

    for i in range(1,num+1):
        value=i**2
        print(value)

square(10)