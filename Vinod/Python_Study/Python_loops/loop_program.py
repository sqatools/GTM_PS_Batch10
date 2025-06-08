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