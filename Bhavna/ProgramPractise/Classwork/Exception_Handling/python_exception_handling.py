# 07/07/2025 Session - Absent

# Exception :  Exception is an event that disrupts the normal flow of a program's execution.
#              It signifies that an error or unexpected situation occurred during the runtime.

def handle_exception():
    try:
        num = 150
        num1 = 'Hi'
        print(num+num1)

        print("Good Evening")
    except Exception as e:
        # print(e)
        print("Cannot add string with number")

handle_exception()
print("hi guys")

def handle_raise_exception():
    try:
        num1 = 25
        num2 = "Hi"
        print(num1+num2)

        print("Good Evening")
    except Exception as e:
        print("Cannot add string with number")
        raise e

# handle_raise_exception()
print("hi Good morning")

print('_'*70)

# 08/07/2025 Session - Absent

##### try-except-else#############
# else condition only executes the code if there is no exception in the code

def try_except_else(num1,num2):
    try:
        result = num1//num2
        print("Result:",result)

    except Exception as e:
        print(e)
    else:
        print("Execution Successfull, No error occured.")

# try_except_else(50,10)

'''
Result: 5
Execution Successfull, No error occured.
'''

# try_except_else(15,0)
# integer division or modulo by zero

print('_'*70)
############################## try-except-else-finally ###################
# finally block of code will always execute, whether function has exception or not exception.

def try_except_else_finally(num1,num2,num3):
    try:
        result = num1//num2
        print("Result:",result)
    except Exception as e:
        print(e)
    else:
        print("Excecution sucessful, no error occured")

    finally:
        for i in range(1,11,1):
            print(num3,"*",i,"=",num3*i)


try_except_else_finally(30,15,8)
'''
Result: 2
Excecution sucessful, no error occured
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80
'''
print('_'*70)
# try_except_else_finally(30,0,5)

############################# Nested exception  ####################

def try_except_else_finally_nested(num1,num2,num3):
    try:
        result = num1//num2
        print("result:",result)
        try:
            admin = num1+num2
            print("inner output:",admin)
        except Exception as f:
            print("inner execution")
            print(f)
    except Exception as e:
        print(e)
        print("Outer exception")
    else:
        print("exceution successful.no error occured")

    finally:
        for i in range(20,10,1):
            print(num3,'*',i,'=',num3*i)

# try_except_else_finally_nested(50,10,2)
#q1 :  write a python program to get even numbers from list with exeception handling.
# get list as input and provide  and even values from given list

def even_numbers(num):
    try:
        for i in num:
            if i%2==0:
                print(i)
            else:
                continue
    except Exception as e:
        print(e)

# num = [1,2,3,4,5,6,7,8,9]
# even_numbers(num)
# even_numbers("Abc")


####################### multiple exception handling ############

def check_multiple_exception(n1,n2,n3):
    try:
        add = n1+n2
        print("Addition:",add)
        mul = n1*n2
        print("Multiplication:",mul)
        div = n1//n2
        print("Division:",div)
        sub = n1-n2
        print("Subtract:",sub)
        assert n1 == n3
        assert n1>n3

    except ValueError as e:
        print("Provided Values are not correct")
    except TypeError as e:
        print(e)
    except AssertionError as e:
        print(e)
    except Exception as e:
        raise e

print('_'*70)
check_multiple_exception(10,20,5)