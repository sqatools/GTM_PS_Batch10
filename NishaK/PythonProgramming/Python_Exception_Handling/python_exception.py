# Exception :  Exception is an event that disrupts the normal flow of a program's execution.
#              It signifies that an error or unexpected situation has occurred during the runtime.


def handle_exception():
    try:
        num1 = 10
        num2 = 'Hello'
        print(num1 + num2)

        print("Good Morning")
    except Exception as e:
        print(e)
        print("Can not add string with number")


handle_exception()
print("Good Morning")


print("-"*50)


def handle_raise_exception():
    try:
        num1 = 10
        num2 = 'Hello'
        print(num1+num2)

        print("Good Morning")
    except Exception as e:
        print("Can not add string with number")
        raise e


# handle_raise_exception()
print("Good Morning")

print("_"*50)
# try-except-else
# else condition only executes the code if there is no exception in the code


def try_except_else(num1, num2):
    try:
        result = num1//num2
        print("result:", result)
    except Exception as e:
        print(e)
    else:
        print("Execution successful, no error occurred")


try_except_else(70, 10)
# result: 7
# Execution successful, no error occurred

try_except_else(11, 0)
# integer division or modulo by zero


print("-"*50)
# try-except-else-finally
# finally block of code will always execute, whether function has exception or not exception.


def try_except_else_finally(num1, num2, num3):
    try:
        result = num1//num2
        print("result :", result)
    except Exception as e:
        print(e)
    else:
        print("Execution successful, no error occurred")

    finally:
        for i in range(1, 11, 1):
            print(num3, "*", i, "=", num3*i)


try_except_else_finally(30, 15, 8)
# result : 2
# Execution successful, no error occurred
# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# 8 * 6 = 48
# 8 * 7 = 56
# 8 * 8 = 64
# 8 * 9 = 72
# 8 * 10 = 80


print("-"*50)
# Nested exception

def try_except_else_finally_nested(num1, num2, num3):
    try:
        result = num1//num2
        print("result:", result)
        try:
            admin = num1+num2
            print("inner output :", admin)
        except Exception as f:
            print("inner exception")
            print(f)
    except Exception as e:
        print(e)
        print("outer exception")
    else:
        print("Execution successful, no error occurred")
    finally:
        for i in range(20, 10, 1):
            print(num3, "*", i, "=", num3*i)


try_except_else_finally_nested(50, 10, 2)
# result: 5
# inner output : 60
# Execution successful, no error occurred


print("-"*50)
#q1 :  write a python program to get even numbers from list with exeception handling.

def get_even_num(l1):
    try:
        for val in l1:
            if val%2 == 0:
                print(val)
            else:
                continue
    except Exception as e:
        print(e)


list_a = [2, 3, 4, 5, 6, 7, 8, 9]
get_even_num(list_a)
# 2
# 4
# 6
# 8
get_even_num('python')
# not all arguments converted during string formatting


print("-"*50)
# multiple exception handling

def check_multiple_exception(n1, n2, n3):
    try:
        add = n1 + n2
        print("Addition :", add)
        mul = n1 * n2
        print("multiplication :", mul)
        div = n1 // n2
        print("division :", div)
        subtract = n1 - n2
        print("subtract :", subtract)
        assert n1 == n3
        assert n1 > n3
    except ValueError as e:
        print("Provided values are not correct")
    except TypeError as e:
        print(e)
    except AssertionError as e:
        print(e)
    except Exception as e:
        raise e


check_multiple_exception(10, 20, 0)