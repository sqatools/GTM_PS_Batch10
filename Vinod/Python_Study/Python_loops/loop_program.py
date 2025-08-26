#Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).


# for i in range (1500,2701):
#     if i%7 == 0 and i%5 ==0:
#         print(i,end="")


#Python Loops program to count the number of even and odd numbers from a series of numbers using python.

# num1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even = 0
# odd = 0
#
# for val in num1:
#     if val%2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print("Number of even numbers: ",even)
# print("Number of odd numbers: ",odd)

#3  Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

# for i in range(0,11):
#         if i != 3 or i != 6:
#             print(i,end=" ")


#4 Write a program to get the Fibonacci series between 0 to 20 using python.

# num1 = 0
# num2 = 1
# count = 0
#
# while count < 20:
#     print(num1,end=" ")
#     n2 = num1 + num2
#     num1 = num2
#     num2 = n2
#     count += 1
#
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181


#5 Write a program to add odd numbers in an empty list from a given list using Python Loops.

# list1 = [3,8,5,0,2,7]
# odd = []
#
# for val in list1:
#     if val%2 != 0:
#         odd.append(val)
#
# print("Even numbers: ",odd)


#6 Print the following small alphabet letter pattern using Python Loops

char = 97  ## ASCII value of 'a'
var1 = 4
var2 = 4

for i1 in range(7):  #range(7) generates the numbers: 0, 1, 2, 3, 4, 5, 6
    if i1 < 4:   # i1 is less than 4, i.e., during the first 4 iterations of the loop (i1 = 0, 1, 2, 3).
        var1 = var1 - 1   #Decreases the value of var1 by 1 each time
        var2 = var2 + 1   # Increases the value of var2 by 1 each time.

        for j1 in range(9):

            if j1 > var1 and j1 < var2:

                print(chr(char), end=" ")
                char += 1
            else:
                print(" ", end=" ")
        print()

        # var1 = var1 - 1
        # var2 = var2 + 1
    else:
        var1 = var1 + 1
        var2 = var2 - 1
        for k in range(9):

            if k > var1 and k < var2:

                print(chr(char), end=" ")
                char += 1
            else:
                print(" ", end=" ")
        print()