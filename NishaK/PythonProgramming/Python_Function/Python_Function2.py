# import specific function
from Python_Function_Practice import calculator

# import all function and their variable
from Python_Function_Practice import *

print("-----Output from new module-----")
calculator(2, 40, 70)


outer_func()


def addition_values(n1, n2):
    print("value n1 :", n1)
    print("value n2 :", n2)
    print("addition value:", n1 + n2)


def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i

    print(f"factorials value {num}:", fact)


if __name__ == '__main__':
    factorial(5)
    addition(700, 800)

print(__name__)
