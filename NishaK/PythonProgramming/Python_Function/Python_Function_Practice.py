def greeting():
    print("Good Morning..!")


greeting()
greeting()
greeting()
"""
Good Morning..!
Good Morning..!
Good Morning..!
"""

print("-"*50)
# There are two ways to provide values to the function.
# 1. Pass by value


def show_msg(msg):
    print(msg)


show_msg("All The Best")
# All The Best
show_msg("Very Good Evening")
# Very Good Evening
show_msg([1, 2, 3, 4])
# [1, 2, 3, 4]

# 2. Pass by reference
x = 'We are learning Python programming'
show_msg(x)
# We are learning Python programming

"""
# provide param values more than required.
# show_msg('Hello', x)
# show_msg() takes 1 positional argument but 2 were given
"""


print("-"*50)


def addition(n1, n2):
    print("Value n1 :", n1)
    print("Value n2 :", n2)
    print("Addition of value :", n1+n2)


addition(20, 30)
# Value n1 : 20
# Value n2 : 30
# Addition of value : 50

print("\n")
p = 100
q = 200
addition(p, q)
# Value n1 : 100
# Value n2 : 200
# Addition of value : 300

print("\n")
addition(n1=q, n2=p)
# Value n1 : 200
# Value n2 : 100
# Addition of value : 300


print("-"*50)
# write a python program to get factorial of any given number.
# fact of 5 = 5*4*3*2*1


def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
    print(f"Factorial of value {num}: ", fact)


factorial(1)
# Factorial of value 1: 1
factorial(2)
# Factorial of value 2: 2
factorial(3)
# Factorial of value 3: 6
factorial(4)
# Factorial of value 4: 24
factorial(5)
# Factorial of value 5: 120


print("_" * 50)
# function with default parameters value
"""
default param has to follow the non-default parameters.
default param has to declare after non default parameter.
"""


def math_operation(num1, num2=10):
    print("Value of num1 :", num1)
    print("Value of num2 :", num2)
    print("addition :", num1 + num2)
    print("multiplication :", num1 * num2)
    print("subtraction :", num1 - num2)


math_operation(100)
# if we don't provide any value of default param ,then it will take default value.
# Value of num1 : 100
# Value of num2 : 10
# addition : 110
# multiplication : 1000
# subtraction : 90

print("\n")
math_operation(50, 20)
# overwrite the default value : 20 value will overwrite the default value of num2.
# Value of num1 : 50
# Value of num2 : 20
# addition : 70
# multiplication : 1000
# subtraction : 30


print("-"*50)
# *args parameter : This parameter allow user to provide n number of values with one single parameter.


def user_info(*args):
    sum1 = 0
    print("value of args :", args)
    for val in args:
        if isinstance(val, int):
            sum1 += val
        elif isinstance(val, list):
            print([x1 ** 2 for x1 in val])
        print(val)

    print("addition of numbers :", sum1)


user_info('John', 'john@gmail.com', '7856789509', 'Mumbai', 'Maharashtra', 65, 86, [4, 6, 8])
"""
# value of args : ('John', 'john@gmail.com', '7856789509', 'Mumbai', 'Maharashtra', 65, 86, [4, 6, 8])
# John
# john@gmail.com
# 7856789509
# Mumbai
# Maharashtra
# 65
# 86
# [16, 36, 64]
# [4, 6, 8]
# addition of numbers : 151
"""


print("-"*50)
# **kwargs parameter
# kwargs accepts values in dictionary format.


def get_user_details(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)


get_user_details(name='John', email='john@gmail.com', phone=78979879878, address='Mumbai')
"""
# {'name': 'John', 'email': 'john@gmail.com', 'phone': 78979879878, 'address': 'Mumbai'}
# name : John
# email : john@gmail.com
# phone : 78979879878
# address : Mumbai
"""


print("-"*50)
# write a python program to verify the login functionality.


def verify_login(**kwargs):
    db_user = 'user1'
    db_pass = 'user1@12345'
    if db_user == kwargs['username'] and db_pass == kwargs['password']:
        print("login successful")
    else:
        print("Invalid credentials")


verify_login(username='user1', password='user1@12345')
# login successful
verify_login(username='user1', password='user@12345')
# Invalid credentials


print("-"*50)
# Return value from function

# whenever we return any value from function then it will stop execution of function
# we can define data type of parameters with :int or any other data type.
# we can provide return type of the function using -> int/str etc.


def addition_values(n1, n2):
    return n1 + n2


result = addition_values(70, 30)
print("output :", result)
# output : 100


print("-"*50)


def get_sum_values(num: int) -> int:
    """
    This function will return the sum of all the values from 1 to num
    :param num: input value required during call of the function
    :return:
    """
    sum1 = 0
    for i in range(1, num):
        # print(i)
        sum1 = sum1 + i
        print("sum1 :", sum1)
        if sum1 > 100:
            return sum1
        else:
            continue


result = get_sum_values(100)
print("result :", result)

# result = get_sum_values("Hello")
# print("result :", result)

"""
sum : 1
sum : 3
sum : 6
sum : 10
sum : 15
sum : 21
sum : 28
sum : 36
sum : 45
sum : 55
sum : 66
sum : 78
sum : 91
sum : 105
result : 105
"""

print(get_sum_values.__doc__)
"""
This function will return the sum of all the values from 1 to num
:param num: input value required during call of the function
:return:
"""

print("-"*50)
# call function inside function


def add(v1, v2):
    return v1+v2


def multiplication(v1, v2):
    return v1*v2


def subtract(v1, v2):
    return v1-v2


def divide(v1, v2):
    return v1//v2


def calculator(opt, num1, num2):
    if opt == 1:
        print("addition of values :", add(num1, num2))
    elif opt == 2:
        print("multiplication of values :", multiplication(num1, num2))
    elif opt == 3:
        print("division of values :", divide(num1, num2))
    elif opt == 4:
        print("subtraction of values :", subtract(num1, num2))


calculator(2, 5, 6)
# multiplication of values : 30
calculator(1, 40, 700)
# addition of values : 740
calculator(3, 10, 5)
# division of values : 2
calculator(4, 20, 2)
# subtraction of values : 18


print("-"*50)
# INNER FUNCTION


def outer_func():
    def inner_fun1(msg):
        print("inner 1 msg :", msg)

    def inner_fun2(msg):
        print("inner 2 msg :", msg)
    inner_fun1('Good Morning')
    inner_fun2('Hope you are doing good')


outer_func()
# inner 1 msg : Good Morning
# inner 2 msg : Hope you are doing good
