
# 24/06/2025 Session

# user define function
def greeting():
    print("Good Evening")

greeting()
greeting()

print('_'*70)
# User define function with parameter
def message(msg):
    print(msg)

# There are two ways to provide values to the function.

# 1. Pass by value
message("Hi how are you")
message("whatsup")
message({2, 4, 6, 9})

# 2. Pass by reference
a = "Python Programming"
message(a)

# provide param values more than required.
# message('hi',a)
# message() takes 1 positional argument but 2 were given

print('_'*70)

def addition(a,b):
    print("value of a:",a)
    print("value of b:",b)
    print("Addition:",a+b)

# Pass by value
addition(2,3)

#Pass by reference
t = 100
s = 200
addition(t,s)

print('_'*70)
# change the order of param value: If we want to change the order of param values, then we have to provide param name
# during the function calling.

addition(b=t,a=s)

print('_'*70)
##############################################
# write a python program to get factorial of any given number.
# fact of 5 = 5*4*3*2*1

def factorial(num):
    fact = 1
    for i in range(num,0,-1):
        fact = fact*i
    print(f"factorial value {num}:",fact)

factorial(5)
factorial(3)

print('_'*70)

#########################################
# function with default parameters value
"""
->  default param has to follow the non-default parameters.
    default param to  has to declare after non default parameter.

"""

def maths(n1,n2=10):
    print("value of n1:",n1)
    print("value of n2:", n2)
    print("Addition:",n1+n2)
    print("Multiplication:",n1*n2)

# if we dont provide any value of default param ,then it will take default value
maths(20)

print('_'*70)
# overwrite the default value, 20 value will overwrite the default value of n2.
maths(20,20)

print('_'*70)

##############################################

# *args parameter :  This parameter allow user to provide n number of values with one single parameter.

def user_info(*abc):
    sum = 0
    print("value of abc:",abc)
    for val in abc:
        if isinstance(val,int):
            sum+=val
        elif isinstance(val,list):
            print([x**2 for x in val])
    # print(val)

    print("Addition of numbers:",sum)
user_info('Atul',[5,6,7],'atul@gmail.com','9988774455','Maharashtra',1,2,3,4)

print('_'*70)

##########################################
# 25/06/2025 Session - Absent

# **kwargs parameter
# kwargs accepts values in dictionary format.

def get_user_details(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,':',v)

get_user_details(name='Shivani',email='shivani@gmial.com',phohe=7845129636)

print('_'*70)
##################################
# write a python program to verify the login functionality.

def verify_login(**kwargs):
    db_user = 'user1'
    db_pass = 'user1@123'
    if db_user == kwargs['username'] and db_pass == kwargs['Password']:
        print("login successful")
    else:
        print("Invalid Credentials")
verify_login(username='user1',Password="user1@123")

print('_'*70)
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

# Practice Program with kwargs:
# Write a python program to get list of all usersname from db_user which is matching there credentials
# db_users = [user1, user2, user3, user5, user7]

def db_users(**kwargs):
    print(kwargs)
    # for k in kwa
    db = [""]

db_users()

print('_'*70)
'''
def abc(**kwargs):
    output = []

    if db_user == kwargs['usernmae']:
        output.append(db_user)

    print(output)

db_user = ['username' = 'user1','password'= 'user1@12',
    'username' = 'user2','password'= 'user2@12'
    'username' = 'user3','password'= 'user3@12'
    'username' = 'user4','password'= 'user4@12'
    'username' = 'user5','password'= 'user5@12'
    'username' = 'user5','password'= 'user6@12'
    ]'''