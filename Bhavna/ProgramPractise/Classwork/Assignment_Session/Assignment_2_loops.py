# ASSIGNMENT 2 - For loop

# write a program to print T pattern
'''
* * * * * *
* * * * * *
    * *
    * *
    * *
    * *
'''

for i in range(1,7):
    for j in range(1,7):
        if i in [1,2]:
            if j in range(1,7):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in range(3,7):
            if j in [3,4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()

print('_'*70)
# write a program to print swastik pattern
"""

* *   * * * * *         #i=1
* *   * * * * *         #i=2
* *   * *               #i=3
* * * * * * * *         #i=4
* * * * * * * *         #i=5
      * *   * *         #i=6
* * * * *   * *         #i=7
* * * * *   * *         #i=8

"""

for i in range(1,9):
    for j in range(1,9):
        if i in [1,2]:
            if j not in [3]:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        elif i in [3]:
            if j in [1,2,4,5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [4,5]:
            if j in range(1,9):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [6]:
            if j in [4,5,7,8]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [7,8]:
            if j not in [6]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()

print('_'*70)