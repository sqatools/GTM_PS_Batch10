# PYTHON LOOPS PRACTICE PROGRAM

# 24.Python loops program to enter a number and print its reverse using python.

num = 5254
reverse = 0

while num > 0:
    temp = num % 10
    reverse = reverse * 10 + temp
    num = num // 10

print(reverse)

print('_' * 70)

'''
41).  Python loops program to print the pattern T using Python Loops.

       Output :

       * * * * * * * * *
       * * * * * * * * *
             * * *
             * * *
             * * *
             * * *
             * * *
'''

for i in range(1, 8):
    for j in range(1, 10):
        if i in [1, 2]:
            if j in range(1, 10):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in range(3, 8):
            if j in [4, 5, 6]:
                print('*', end=" ")
            else:
                print(" ", end=" ")
    print()

print('_' * 70)
'''
42).  Write a program to print number patterns using Python Loops.

     Output:

     1
     2   3
     4   5   6
     7   8   9   10
     11  12  13  14  15
     14  13  12  11
     10  9   8
     7   6
     5
'''
a = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(a, end=" ")
        a += 1
    print()
for k in range(5, 0, -1):
    for l in range(k - 1):
        a -= 1
        print(a, end=" ")

    print()

print('_' * 70)

'''
43). Write a program to print the pattern A using Python Loops.

    Output :

      *  *  *       #i=1
    * * * *  * *    #i=2
    * *      * *    #i=3
    * *      * *    #i=4
    * * * *  * *    #i=5
    * * * * * *     #i=6
    * *      * *    #I=7
    * *      * *    #i=8
    * *      * *    #i=9
'''

for i in range(1, 10):
    for j in range(1, 7):
        if i in [2, 5, 6]:
            if j in range(1, 7):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [1]:
            if j in [2, 3, 4, 5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [3, 4, 7, 8, 9]:
            if j not in [3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()

print('_' * 70)
'''
44). Write a program to print the pyramid structure using Python Loops.

    Output:

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

# for i in range(1,6):
#     for j in range(1,10):
#         if i in range(1,6):
#             if j in [5]:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         elif i in range(1,6):
#             if j in [2,4]:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()

# 45). Write a program to count total numbers of even numbers between 1-100 using Python Loops.

even = 0
for i in range(1, 101):
    if i % 2 == 0:
        even += 1
print("Total even no.:", even)

# 46). Write a program to count the total numbers of odd numbers between 1-100 using Python Loops.

odd = 0
for k in range(1, 101):
    if k % 2 != 0:
        odd += 1
print("Total Odd No.:", odd)
