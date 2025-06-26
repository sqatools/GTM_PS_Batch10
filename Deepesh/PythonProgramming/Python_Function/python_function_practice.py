# user define function
def greeting():
    print("Good Morning")


greeting()
greeting()
greeting()


# User define function with parameter
def show_msg(msg):
    print(msg)


# There are two ways to provide values to the function.
# 1. Pass by value
show_msg("All the best")
show_msg("Very good evening")
show_msg([4, 6, 7, 89])

# 2. Pass by reference
x = "We are Learning Python Programming"
show_msg(x)

# provide param values more than required.
# show_msg('Hello', x)
# show_msg() takes 1 positional argument but 2 were given

print("_" * 50)


def addition(n1, n2):
    print("value n1 :", n1)
    print("value n2 :", n2)
    print("addition value:", n1 + n2)


# Pass by value
#addition(20, 30)
# addition value: 50

# Pass by reference
p = 100
q = 700
addition(p, q)

# change the order of param value: If we want to change order param values, then we have to provide param name
# during the function calling.

print("_" * 50)
addition(n2=p, n1=q)


################################
# write a python program to get factorial of any given number.
# fact of 5 = 5*4*3*2*1
def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i

    print(f"factorials value {num}:", fact)


# print("_" * 50)
# factorial(5)  # factorials value 5: 120
# factorial(7)  # factorials value 7: 5040
# factorial(5 + 1)  # factorials value 6: 720

print("_" * 50)
################################
# function with default parameters value
"""
->  default param has to follow the non-default parameters.
    default param to  has to declare after non default parameter.

"""


def math_operation(num1, num2=30):
    print("value num1 :", num1)
    print("value num2:", num2)
    print("addition :", num1 + num2)
    print("multiplication :", num1 * num2)
    print("subtraction :", num1 - num2)


# if we dont provide any value of default param ,then it will take default value
# math_operation(100)
#
# print("_" * 50)
# # overwrite the default value, 20 value will overwrite the default value of num2.
# math_operation(80, 20)
#
# print("_" * 50)


######################################
# *args parameter :  This parameter allow user to provide n number of values with one single parameter.

def user_info(*args):
    sum = 0
    print("value of args :", args)
    for val in args:
        if isinstance(val, int):
            sum += val
        elif isinstance(val, list):
            print([x ** 2 for x in val])
        print(val)

    print("addition of numbers :", sum)


#user_info('John', 'john@gmail.com', '789798798', 'Mumbai', 'Maharashtra', 10, 30, 40, 50, [4, 6, 7])

"""
Home work :

#1 write a python function to check given number is prime or not
  -> take variable as num1 amd check that num1 is prime or not in the function code.
  
#2. Write a python function to print the table of any given number.
#3. write a python function to max value from given list 
"""

print("_" * 50)


######################################
# **kwargs parameter
# kwargs accepts values in dictionary format.
def get_user_details(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)


#get_user_details(name='John', email='john@gmail.com', phone=78979879878, address='Mumbai')

print("_" * 50)
##################################
# write a python program to verify the login functionality.
def verify_login(**kwargs):
    db_user = 'user1'
    db_pass = 'user@12345'
    if db_user == kwargs['username'] and db_pass == kwargs['password']:
        print("login successful")
    else:
        print("Invalid credentials")


# write a python function code to get fabonaci value from 1 to 100
#fabonaci = [1, 2, 3, 5, 8, 13, 21 .....]

print("_"*50)
########################### return value from function ################
def addition_values(n1, n2):
    return n1+n2

# result = addition_values(70, 60)
# print("output :", result)
# # output : 130
#
# print("_"*50)
# whenever we return any value from function then it will stop execution  of function
#  ->  we can define data type of parameters with :int or any other data type.
#  ->  we can provide return type of the function using -> int/str etc.
def get_sum_values(num: int) -> int:
    """
    This function will return the sum of all the values from 1 to num
    :param num: input value required to during the call of the function.
    :return:
    """
    sum = 0
    for i in range(1, num):
        print(i)
        sum = sum + i
        print("sum :", sum)
        if sum > 100:
            return sum
        else:
            continue


#result = get_sum_values(100)
#print("result :", result)

#result = get_sum_values('Hello')
#print("result :", result)

print(get_sum_values.__doc__)
"""
This function will return the sum of all the values from 1 to num
    :param num: input value required to during the call of the function.
    :return:
"""


print("_"*50)
#################################################
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

# calculator(2, 5, 6)
# # multiplication of values : 30
# calculator(1, 40, 700)
# # addition of values : 740
# calculator(3, 40, 5)
# # division of values : 8
# calculator(4, 50, 5)
# # subtraction of values : 45




print("_"*50)
######################## INNER FUNCTION #########################

def outer_func():
    def inner_fun1(msg):
        print("inner 1 msg :", msg)

    def inner_fun2(msg):
        print("inner 2 msg :", msg)


    inner_fun1("Hello good morning")
    inner_fun2("Hope you are doing good")

outer_func()
