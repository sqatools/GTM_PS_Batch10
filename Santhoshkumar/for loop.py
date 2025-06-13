 # range(start, end, step)
"""
-> range output will include start value and exclude end value
-> in the range function default initial value is zero (0)
-> in the range function default step value is one (1)


"""
# get value from 1 to 1o with the help of range
for i in range(1, 10, 3):
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
print("_" * 50)

# get value from 1 to 20 using range with default initial value (0) and step value (1)
for j in range(15):
    print(j, end=" ")

"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
"""
print()
print("_" * 50)
# program to print a table of any number with default step value (1)
num = 7
for j in range(1, 11):
    print(j, "*", num, ":", j * num)

"""
1 * 7 : 7
2 * 7 : 14
3 * 7 : 21
4 * 7 : 28
5 * 7 : 35
6 * 7 : 42
7 * 7 : 49
8 * 7 : 56
9 * 7 : 63
10 * 7 : 70
"""

print("_" * 50)
# get value with the help end value in range

for k in range(15, 5, -1):
    print(k, end=" ")

# 15 14 13 12 11 10 9 8 7 6

print()

for l in range(-7, 1, 1):
    print(l, end=" ")
# -7 -6 -5 -4 -3 -2 -1 0


print()
print("_" * 50)
###### Use if condition inside for loop #######
# program to get all the even numbers from 1 to 30
for val in range(1, 31):
    if val % 2 == 0:
        print(val, end=" ")
    else:
        pass
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30

print()

for m in range(1, 31):
    if m % 2 != 0:
        print(m, end=" ")
    else:
        pass
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29

print()
print("_" * 50)
#####################################
# write a program to get check given string contains vowels
str1 = "Programming"
vowel = "aeiou"

for char in str1:
    # print(char)
    if char in vowel:
        print(char, " :vowel")
    else:
        print(char)

"""
P
r
o  :vowel
g
r
a  :vowel
m
m
i  :vowel
n
g
"""

print("_" * 50)
#####################################
# write a program to get square of even number and cube of odd number from given list
list_a = [5, 7, 12, 6, 8, 3, 5, 9]
for val in list_a:
    if val % 2 == 0:
        print("square :", val, val ** 2)
    else:
        print("cube :", val, val ** 3)

"""
cube : 5 125
cube : 7 343
square : 12 144
square : 6 36
square : 8 64
cube : 3 27
cube : 5 125
cube : 9 729
"""

print("_" * 50)
##################### Nested For Loop ###############

# outer loop
for i in range(1, 6):  # i =1, 2, 3
    print("Address :", i)
    # Inner loop
    for j in range(1, 4):  # j = 1, 2, 3
        print("Item :", j)

    print("_" * 50)

print("_" * 50)
# write a program to draw triangular pattern
"""
*
* *
* * *
* * * *
* * * * * 
"""

for i in range(1, 6):  # i = 1, 2, 3
    for j in range(0, i):  # j = 0 | 0, 1 | 0, 1, 2
        print("*", end=' ')

    print()

print("_" * 50)
# write a program to draw reverse triangular pattern

"""
* * * * * 
* * * *
* * *
* *
*
"""

for i in range(1, 6):  # i = 1, 2, 3 ....
    for j in range(1, 7 - i):  # j = (1, 6), (1, 5), (1, 4)...
        print("*", end=" ")

    print()

print("_" * 50)
################################################
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
    for j in range(1, 6):
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

"""
# write a program to print T pattern
* * * * * * 
* * * * * * 
    * * 
    * * 
    * *
    * *

# write a program to print swastik pattern

* *   * * * * *
* *   * * * * *
* *   * *
* * * * * * * *
* * * * * * * *
      * *   * *
* * * * *   * *
* * * * *   * *

"""

print("_" * 50)
##############################
# write a program to find out the given number is prime or not

num = 23
prime = True
for i in range(2, num // 2):  # 2, 3, 4
    if num % i == 0:
        prime = False
    else:
        pass

if prime:
    print("This is prime number :", num)
else:
    print("This is not an prime number :", num)

"""
*           i=1
* *            2
* * *         3
* * * *       4
* * * * *     5
"""

for i in range(1,6):
    for j in range(0,i):
        print('*', end=' ')

    print()

print("_"*50)

"""
* * * * * 
* * * *
* * *
* *
*
"""
for i in range(1,6):
    for j in range(0,6-i):
        print("*",end=' ')
    print()
print()
print("_"*50)

"""
# write a program to print T pattern
* * * * * * 
* * * * * * 
    * * 
    * * 
    * *
    * *
"""
for i in range(2):
    for j in range(6):
        print("*", end=" ")
    print()

# Print the vertical part of the T (4 rows of 2 stars, shifted to the right)
for i in range(4):
    print(" "*4, end="")  # 4 spaces for alignment (each space = 1 character)
    for j in range(3,5):
        print("*", end=" ")
    print()

print("_"*50)

"""
# write a program to print swastik pattern

* *   * * * * *
* *   * * * * *
* *   * *
* * * * * * * *
* * * * * * * *
      * *   * *
* * * * *   * *
* * * * *   * *


for i in range(9):
    for j in range(9):
        if i in [1,3]:
            #if j in [9]:
                print("*",end="")
            else:
                print("*",end="")
    print()



for i in range(6):
    print(i * "*", end=" ")
    for i in range(4-i):
        print("*",end=" ")
    print()
"""



for i in range(1, 11):


    if i != 3 and i != 6:
        print(i)