
def addition(n1, n2):
    print("value n1 :", n1)
    print("value n2 :", n2)
    print("addition value:", n1 + n2)


def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i

    print(f"factorials value {num}:", fact)

factorial(5)

print(__name__)
