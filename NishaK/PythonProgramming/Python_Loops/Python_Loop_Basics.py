# range(start, end, step)
"""
-> range output will include start value and exclude end value
-> in the range function default initial value is zero (0)
-> in the range function default step value is one (1)


"""
# get value from 1 to 10 with the help of range
for i in range(1, 10):
    print(i)
"""
1
2
3
4
5
6
7
8
9
"""

print("-"*50)
# get value from 1 to 20 using range with default initial value (0) and step value (1)
for i in range(20):
    print(i, end=" ")
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

print()
print("-"*50)
# program to print a table of any number with default step value (1)
num = 5
for i in range(1, 11):
    print(i, "*", num, ":", num*i)
"""
1 * 5 : 5
2 * 5 : 10
3 * 5 : 15
4 * 5 : 20
5 * 5 : 25
6 * 5 : 30
7 * 5 : 35
8 * 5 : 40
9 * 5 : 45
10 * 5 : 50
"""


print("-"*50)
# get value with the help end value in range

for k in range(15, 5, -1):
    print(k, end=" ")
# 15 14 13 12 11 10 9 8 7 6

print()
print("-"*50)
for k in range(-7, 1, 1):
    print(k, end=" ")
# -7 -6 -5 -4 -3 -2 -1 0

print()
print("-"*50)
# Use if condition inside for loop #######
# program to get all the even numbers from 1 to 30

for i in range(1, 31):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        pass
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30

print()
print("-"*50)
for m in range(1, 31):
    if m % 2 != 0:
        print(m, end=" ")
    else:
        pass
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29


print()
print("_"*50)
# write a program to get check given string contains vowels
str1 = "Programming"
var = "aeiou"
for char in str1:
    if char in var:
        print(char, ": vowel")
    else:
        print(char)
"""
P
r
o : vowel
g
r
a : vowel
m
m
i : vowel
n
g
"""

print("_"*50)
# write a program to get square of even number and cube of odd number from given list
list_a = [5, 7, 12, 6, 8, 3, 5, 9]
for num in list_a:
    if num % 2 == 0:
        print(num, "square of num", num**2)
    else:
        print(num, "cube of num", num**3)

"""
5 cube of num 125
7 cube of num 343
12 square of num 144
6 square of num 36
8 square of num 64
3 cube of num 27
5 cube of num 125
9 cube of num 729
"""


print("-"*50)
# Nested For Loop ###############

for i in range(1, 6):
    print("Address :", i)
    for j in range(1, 4):
        print("Item :", j)
    print("-"*20)


print("-"*50)
"""
*
* *
* * *
* * * *
* * * * * 
"""
for i in range(1, 6):
    for j in range(0, i):
        print("*", end=" ")
    print()


print()
print("-"*50)

"""
* * * * * 
* * * *
* * *
* *
*
"""

for i in range(1, 6):  # 1, 2
    for j in range(1, 7-i):  # (1, 6), (1, 5)
        print("*", end=" ")
    print()


print()
print("-"*50)
# write a program to print O pattern

"""

- * * * -   # i=1
* - - - *   # i=2
* - - - *   # i=3
* - - - *   # i=4
* - - - *   # i=5
- * * * -   # i=6

"""

for i in range(1, 7):
    for j in range(0, 6):
        if i in [1, 6]:
            if j in [2, 3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [2, 3, 4, 5]:
            if j in [1, 5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")
    print()


print("-"*50)
# write a program to find out the given number is prime or not

num = 19
prime = True
for i in range(2, num//2):
    if num % i == 0:
        prime = False
    else:
        pass
if prime:
    print(num, ": This is prime number")
else:
    print(num, ": This is not prime number")

# 19 : This is prime number


print("-"*50)
# write a program to get list of all the prime numbers from 1 to 100
for num in range(1, 100):
    prime = True
    for i in range(2, num//2+1):
        if num % i == 0:
            prime = False
            break
        else:
            continue
    if prime:
        print(num, end=" ")
# 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
