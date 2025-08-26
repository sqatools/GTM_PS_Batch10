"""
*******
  ***
  ***
*******

"""
for i in range(1,5):
    for j in range(1,8):
        if i in [1,4]:
            if j in [1,2,3,4,5,6,7]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i in [2,3]:
            if j in [3,4,5]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()


"""
 *** 
*   *
*   *
*****
*   *
*   *
"""
print("_"* 60)
for i in range(1,7):
    for j in range(1,6):
        if i in [1]:
            if j in [2,3,4]:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        elif i in [2,3,5,6]:
            if j in [1,5]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i in [4]:
            if j in [1,2,3,4,5]:
                print("*",end=" ")
    print()


print("_"* 60)

"""
* *   * * * * *
* *   * * * * *
* *   * *
* * * * * * * *
* * * * * * * *
      * *   * *
* * * * *   * *
* * * * *   * *
"""

for i in range(1,9):
    for j in range(1,9):
        if i in [1,2]:
            if j in [1,2,4,5,6,7,8]:
                print("*",end=" ")
            else:
                print(" ", end = " ")
        elif i in [3]:
            if j in [1,2,4,5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [4,5]:
            if j in [1,2,3,4,5,6,7,8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [6]:
            if j in [4,5,7,8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [7,8]:
            if j in [1,2,3,4,5,7,8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

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
#A-Z (65-91)

num= 65
for i in range(1,6):
    for j in range (1,i+1):
        print(chr(num),end=" ")
        num+=1
    print()
for k in range(1,6):
    for l in range(5,k,-1):
        print(chr(num), end=" ")
        num+=1
    print()
"""
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
"""
rows = 5
for i in range(1, rows + 1):#(1,6)
    # Print leading spaces
    for space in range(rows - i):#(5)
        print("  ", end="")

    # Print increasing characters
    for j in range(i):
        print(chr(65 + j), end=" ")

    # Print decreasing characters
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end=" ")

    print()


