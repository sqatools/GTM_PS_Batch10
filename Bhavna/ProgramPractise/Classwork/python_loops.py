# 30/05/2025 session

# Loops
# range(start, end, step)
"""
-> range output will include start value and exclude end value
-> in the range function default initial value is zero (0)
-> in the range function default step value is one (1)

"""
#  1. get value from 1 to 10 with the help of range

for i in range(1, 10, 2):
    print(i)

print('_'*70)

# 2.Get value from 1 to 20 using range with default initial value (0) and step value (1)
for a in range(20):
    print(a)

print('_'*70)

# 3.Program to print a table of any number with default step value (1)

num = 2
for j in range(1,11):
    print(j, "*", num ,":", j*num)

print('_'*70)

# get value with the help of end value in range

for k in range(15, 5, -1):
    print(k, end= ",")

print()
for l in range(-7, 1, 1):
    print(l, end= " ")

print()
print('_'*70)

###### Use if condition inside for loop #######
# Program to get all the even numbers from 1 to 30

for e in range(1, 31):
    if e%2 == 0:
        print(e, end=" ")
    else:
        pass
print()
print('_'*70)

for m in range(1, 31):
    if m%2 != 0:
        print(m, end=" ")

print()
print('_'*70)
#####################################
# write a program to get check given string contains vowels

h = "Hello World"
vowel = "aeiou"

for i in h:
    if i in vowel:
        print(i,":vowel")
    else:
        print(i)

print('_'*70)
#####################################
# write a program to get square of even number and cube of odd number from given list

list1 = [1, 3, 8, 12, 7, 2]

for i in list1:
    if i%2 == 0:
        print("Square:", i**2)
    else:
        print("Cube:", i**3)

print('_'*70)

# 02/06/2025 Session
############### Nested For Loop ###############

for i in range(1,6):  #1,2,3,4,5
    print("Address:", i)
    for j in range(1,4): #1, 2, 3
        print("Items:", j)

print('_'*70)
# write a program to draw triangular pattern
"""
*
* *
* * *
* * * *
* * * * * 
"""

for i in range(1,6):
    for j in range(0, i):
        print("*", end=" ")

    print()
print('_'*70)
# write a program to draw reverse triangular pattern
"""
* * * * * 
* * * *
* * *
* *
*
"""

for i in range(1,6): #1,2,3,4,5
    for j in range(1, 7-i): #(1,6),(1,5)
        print("*", end=" ")

    print()

print('_'*70)

# write a program to print O pattern
"""

- * * * -   # i=1
* - - - *   # i=2
* - - - *   # i=3
* - - - *   # i=4
* - - - *   # i=5
- * * * -   # i=6

"""

for i in range(1,7):
    for j in range(1,6):
        if i in [1,6]:
            if j in [2,3,4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [2,3,4,5]:
            if j in [1,5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")

    print()

# write a program to find out the given number is prime or not

k = 12
prime = True
for i in range(2, k//2):
    if k%i == 0:
        prime = False
    else:
        pass

if prime:
    print("This is prime no.:",k)
else:
    print("This is not prime no.:",k)


print('_'*70)
