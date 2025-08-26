# 1. write a python function to check given number is prime or not
# 2. write a python function to print the table of any given number
# 3. find the max value from a given list


# 1) write a python function to check given number is prime or not

def is_prime(num):
    try:
        if num % 2 == 0:
            print("Is a even number:", num)
        else:
            print("Is a not an even number:", num)
    except Exception as e:
        print("Can not validate a string value ")
        raise e


is_prime(17)


# 2. write a python function to print the table of any given number
def print_table(num1):
    print(f"Multiplication Table for {num1}:")
    for i in range(1, 11):
        print(f"{num1} x {i} = {num1 * i}")


print_table(5)


# 3. find the max value from a given list
def find_max(numbers):
    if not numbers:
        return "The list is empty."

    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


my_list = [12, 45, 2, 98, 33, 76]
print("Maximum value is:", find_max(my_list))


# 4) write a python function code to get fabonacii series from 1 to 100

def fibo_val():
    fib_numbers = []
    first_val = 0
    next_val = 1
    for i in range(first_val, 11):
        fib_val = first_val + next_val
        fib_numbers.append(fib_val)
        first_val = next_val
        next_val = fib_val
        print(fib_numbers)


fibo_val()
