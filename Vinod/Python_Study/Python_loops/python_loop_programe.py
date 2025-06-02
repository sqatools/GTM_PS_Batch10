# range (start, end, step)
"""
-> range output will include start value and exclude end value
-> in the range function default initial value is zero (0)
-> in the range function default step value is one (1)

"""

#get value from 1 to 10 with the help of range
for i in range(1, 10, ):
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
#get value from 1 to 20 using range with default initial value (0) and step value (1)

for i in range (0, 15):
    print(i)

"""
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14

"""

for j in range (15):
    print(j, end=" ")

"""
    
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 

"""

print()
print("_"*50)
#program to print a table of any number with default step value (1)
num = 8 # variable value declare
for j in range (1, 11): #This loop runs from 1 to 10 (inclusive of 1, exclusive of 11),
    # Each value of j will be used to generate one line of the multiplication table
    print(j, "*",num,":", j*num)
    #j The current multiplier (from loop)
    #"*"#	A string literal to show the multiplication sign
    #num The number you're multiplying
    #":"Just a label to make output clearer
    #j * numThe result of multiplying j × num

"""

1 * 8 : 8
2 * 8 : 16
3 * 8 : 24
4 * 8 : 32
5 * 8 : 40
6 * 8 : 48
7 * 8 : 56
8 * 8 : 64
9 * 8 : 72
10 * 8 : 80

"""

print("_"*50)
# get value with the help end value in range

for i in range (15,5,-1):
    print(i, end="")

"""
    
1514131211109876

"""
print()

for k in range (-5, 1, 1):
    print(k, end="")

"""
    
-5-4-3-2-10

"""

print()
print("_"*50)
###### Use if condition inside for loop #######
# program to get all the even numbers from 1 to 30

for val in range (1, 41):
    if val%2 == 0:
        print(val,end=" ")
    else:
        pass

"""

2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 

"""
print()


for m in range (1, 41):
    if m%2 != 0:
        print(m, end =" ")
    else:
        pass

"""
    
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39


"""

print()
print("_"*50)
#####################################
# write a program to get check given string contains vowels

str= "Programming"
vowel = "aeiou"

for char in str:
    if char in vowel:
        print(char," :vowel")
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

list_a =[5, 7, 12, 6, 8, 3, 5, 9]
for val in list_a:
    if val%2 == 0:
        print("square :", val, val**2)
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

  * * *   
*       * 
*       * 
*       * 
*       * 
  * * *   


"""

print("_" * 50)
################################################
# write a program to print T pattern

"""
* * * * * * #1=1
* * * * * * #1=2
    * *     #1=3
    * *     #1=4
    * *     #1=5
    * *     #1=6
    
"""

for i in range(1, 7):  # Rows
    for j in range(1, 6):  # Columns
        if i == 1:
            print("j", end=" ")  # Top row (horizontal line of T)
        elif j == 3:
            print("j", end=" ")  # Center column (vertical line of T)
        else:
            print(" ", end=" ")  # All other spaces
    print()  # Move to next line after each row
