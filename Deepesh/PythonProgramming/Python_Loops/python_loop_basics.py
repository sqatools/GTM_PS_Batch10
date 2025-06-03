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
print("_"*50)

# get value from 1 to 20 using range with default initial value (0) and step value (1)
for j in range(15):
    print(j, end=" ")

"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
"""
print()
print("_"*50)
#program to print a table of any number with default step value (1)
num = 7
for j in range(1, 11):
    print(j, "*", num, ":", j*num)

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

print("_"*50)
# get value with the help end value in range

for k in range(15, 5, -1):
    print(k, end=" ")

# 15 14 13 12 11 10 9 8 7 6

print()

for l in range(-7, 1, 1):
    print(l, end=" ")
# -7 -6 -5 -4 -3 -2 -1 0


print()
print("_"*50)
###### Use if condition inside for loop #######
# program to get all the even numbers from 1 to 30
for val in range(1, 31):
    if val%2 == 0:
        print(val, end=" ")
    else:
        pass
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30

print()

for m in range(1, 31):
    if m%2 != 0:
        print(m, end=" ")
    else:
        pass
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29

print()
print("_"*50)
#####################################
# write a program to get check given string contains vowels
str1 = "Programming"
vowel = "aeiou"

for char in str1:
    #print(char)
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

print("_"*50)
#####################################
# write a program to get square of even number and cube of odd number from given list
list_a = [5, 7, 12, 6, 8, 3, 5, 9]
for val in list_a:
    if val%2 == 0:
        print("square :", val, val**2)
    else:
        print("cube :", val, val**3)

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

print("_"*50)
##################### Nested For Loop ###############

# outer loop
for i in range(1, 6): # i =1, 2, 3
    print("Address :", i)
    # Inner loop
    for j in range(1, 4): # j = 1, 2, 3
        print("Item :", j)

    print("_"*50)


print("_"*50)
# write a program to draw triangular pattern
"""
*
* *
* * *
* * * *
* * * * * 
"""

for i in range(1, 6): # i = 1, 2, 3
    for j in range(0, i): # j = 0 | 0, 1 | 0, 1, 2
        print("*", end=' ')

    print()


print("_"*50)
# write a program to draw reverse triangular pattern

"""
* * * * * 
* * * *
* * *
* *
*
"""

for i in range(1, 6): # i = 1, 2, 3 ....
    for j in range(1, 7-i): # j = (1, 6), (1, 5), (1, 4)...
        print("*", end=" ")

    print()


print("_"*50)
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


print("_"*50)
##############################
# write a program to find out the given number is prime or not

num = 23
prime = True
for i in range(2, num//2): # 2, 3, 4
    if num%i == 0:
        prime = False
    else:
        pass

if prime:
    print("This is prime number :", num)
else:
    print("This is not an prime number :", num)


print("_"*50)
###########################################
# write a program to get list of all the prime numbers from 1 to 100

for num in range(1, 100):
    prime = True
    for i in range(2, num//2+1):
        if num%i == 0:
            prime = False
            break
        else:
            continue

    if prime:
        print(num, end=" ")


# 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97


print()
print("_"*50)
############################ continue and break statement ###############
#
# continue statement :  If for value in matching with continue statement condition
#                       then it will skip remaining code execution and move in iteration of foor loop
for i in range(1, 10):
    if i == 5 or i == 6:
        continue

    print(i)


print("_"*50)
# break statement :  If for loop value is matching with break condition then it will break the loop execution
#                    and won't execute further code.

for j in range(1, 10):
    if j == 5:
        break
    print(j)

print("_"*50)
########################################
# while loop in python:
# while loop code execute until the certain condition is matching.

n = 1

while n <= 10:
    print(n)
    n += 1


print("_"*50)
# infinite loop
"""
n = 1

while True:
    print(n)
    n += 1
    if n == 100000:
        break
"""


print("_"*50)
# write a program to reverse any given number

num = 782356
# num = 123
# output = 321
reverse = 0

while num > 0: # 12 > 0, 1 > 0, 0> 0
    temp = num%10  # 3, 2, 1
    reverse = reverse*10 + temp # 3  | 3*10 + 2 = 32 | 32*10 + 1 = 321
    num = num//10 #  12, 1, 0


print("reverse value : ", reverse)

print("_"*50)
#####################################  ASCII VALUES ################

# Capital A-Z : 65-90
# Small a-z : 97-122

# ord() function :  ord function return the ascii value of given character


# get ascii with character
char = 'A'
print(ord(char)) # 65
####################################################################
# chr() function :  chr function return the character of given ascii value.

# get character name with ascii
print(chr(90)) # Z

for i in range(65, 91):
    print(chr(i), end=" ")
#
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

print()
for i in range(97, 123):
    print(chr(i), end=" ")
# a b c d e f g h i j k l m n o p q r s t u v w x y z



print()
for i in range(1, 65):
    print(chr(i), end=" ")

# ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @


print()
print("_"*50)
###############################################
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in letters:
    print(ord(char), end=" ")
# 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90


print()
print("_"*50)
##################################
# write a program to print a given pattern with letter

"""
A
B C
D E F
G H I J
K L M N O
"""

num = 65
for i in range(1, 6):
    for j in range(1, i+1):
        print(chr(num), end=" ")
        num += 1

    print()

# ASCII: American Standard Code for Information Interchange


print()
print("_"*50)
####################################################

#  program to print below pattern
"""
A
B C
D E F
G H I J
K L M N O
P Q R S
T U V
W X
Y
"""

num = 65
for i in range(1, 6):
    for j in range(1, i+1):
        print(chr(num), end=" ")
        num += 1

    print()

for k in range(1, 5):
    for l in range(5, 0+k, -1):
        print(chr(num), end=" ")
        num += 1

    print()
