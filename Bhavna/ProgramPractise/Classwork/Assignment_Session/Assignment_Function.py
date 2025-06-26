# Assignment_Function - 24/06/2025

#1 write a python function to check given number is prime or not
# -> take variable as num1 amd check that num1 is prime or not in the fucntion code.

def prime(num):
    n = 0
    for i in range(2,num):
        if num%i == 0:
            n += 1
    if n >0:
        print("It is not prime no.")
    else:
        print("It is a prime no.")

prime(7)

print('_'*70)
#2. Write a python function to print the table of any given number.

def table(num):
    for i in range(1,11):
        print(i,"*",num,"=",num*i )

table(5)

print('_'*70)

#3. write a python function to get max value from given list

def maximum(*num):
    for i in num:
        if isinstance(i,list):
            print("Maximum Value:",max(i))

maximum([4,5,6,98,65])

print('_'*70)

# 26/06/2025 session assignment - np

# write a python function code to get fabonaci value from 1 to 100
#fabonaci = [1, 2, 3, 5, 8, 13, 21 .....]

def fib():
    fib_output = []
    a,b = 1,2
    fib_output.append(a)
    while b<=100:
        fib_output.append(b)
        a,b = b,a+b
        # print(a,b)
    print(fib_output)

fib()

print('_'*70)

