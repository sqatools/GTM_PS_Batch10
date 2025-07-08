# # import specific function
# from python_function_practice import calculator
#
# # import all function and theirvariable
# from python_function_practice import *
#
#
# print("----output from new module ------")
# calculator(2, 40, 7)
#
#

def addition(n1, n2):
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
