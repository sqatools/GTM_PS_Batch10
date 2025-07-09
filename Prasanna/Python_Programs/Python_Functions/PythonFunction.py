""""# UserDefine Defination:
def greeting():
    print("Hello hi am Greeting to everyone")
greeting()

# pass by value and Reference

def show_msg(msg):
    print(msg)
# There are two ways to provide values to the function.
# 1. Pass by value
show_msg("Hi hello how are you")
show_msg("Good Evening Everyone")

# 2. Pass by reference
x = "We are Learning Python Programming"
show_msg(x)
# write a python program to get factorial of any given number.
# fact of 5 = 5*4*3*2*1
def factorial(num):
    fact =1
    for i in range(num, 0, -1):
        fact = fact*i

    print(f"factorials value {num}:", fact)

print("_"*50)
factorial(5)  # factorials value 5: 120
factorial(7) # factorials value 7: 5040
factorial(5+1) # factorials value 6: 720

# 1 write a python function to check given number is prime or not
def isprime(num):
    count = 0
    for i in range(2,num+1):
        if(num % i == 0):
            count += 1
        if(count == 2):
            print("Given number Is Prime")
isprime(7)

# 2. Write a python function to print the table of any given number.
# 3. write a python function to max value from given list


# Date: 25/6/2025
print("="*50)
# 1 Q) Write a Python Program to get fibinocci series between (1,100)
def fib( lower, upper):
    num1 = 0
    num2 = 1
    while num2 < upper:
        if num2 >= lower:
            print(num2, end=" ")
            num1,num2 = num2, num1 + num2
fib( 1, 100)
def fibonacci(i):
    a=0
    b=1
    for count in range(1,i,1):
        sum=a+b
        a=b
        b=sum
        print(sum,end=" " )

fibonacci(100)

#Write a python program to nget list of all usersname from db_user which is matching there credentials
db_users = [user1, user2, user3, user5, user7]
"""


# Basic Programs:
# 1). Python function program to add two 8numbers.
def add(num1, num2):
    return num1 + num2


total = add(4, 3)
print("Output:", total)


# 2). Python function program to print the input string 10 times.
def string(str1):
    print(str1 * 10)


str1 = input("Enter any string you want to print\n")
string(str1)


# 3). Python function program to print a table of a given number.
def table(number):
    value = 0
    for i in range(1, 11):
        value = number * i
        print(i, "*", number, "=", value)


table(5)
