# range(start, end, step)
"""
-> range output will include start value and exclude end value
-> in the range function default initial value is zero (0)
-> in the range function default step value is one (1)

"""
# get value from 1 to 10 with the help of range
for i in range(1, 10, 3):
    print(i)
print("_"*50)
# get value from 1 to 20 using range with default initial value (0) and step value (1)
for i in range(20):
    print(i,end="  ")
print("_"*50)
# program to print a table of any number with default step value (1)
num = int(input("Enter a number: "))
for j in range(1,11):
    print(j, "*" , num ,":" , j*num)
print("_"*50)


# get value with the help end value in range
for k in range(20,5,-5):
    print(k, end=" ")
print()

##
for l in range(-7,6,1):
    print(l, end=" ")
print()
print("_"*50)
# Use if condition inside for loop #######
# program to get all the even numbers from 1 to 30
for i in range(1,31):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        pass
print()
print("_"*50)
# all odd numbers in a given range
for i in range(1,21):
    if i % 2 != 0:
        print(i, end=" ")
    else:
        pass
print()
print("_"*50)
############################
# write a program to get check given string contains vowels
string = "Hi My self Prasanna it contains vowels"
vowels = "aeiou"
for char in string:
    if char in vowels:
        print(char, "vowel found ")
    else:
        print(char)
print("_"*50)

#####################################
# write a program to get square of even number and cube of odd number from given list
list_a = [5, 7, 12, 6, 8, 3, 5, 9]
for val in list_a:
    if val%2 == 0:
        print("Square is: ", val, val**2)
    else:
        print("Cube is :", val, val**3)
print("_"*50)

# Nested For Loop ###############

# outer loop
for i in range(1,6):
    print("Address :", i)
    # inner loop
    for j in range(1,6):
        print("Item :", j)
print()
print("_"*50)

# write a program to draw triangular pattern
for i in range(1, 6):
    for j in range(0, i):
        print("*", end=' ')
    print()
