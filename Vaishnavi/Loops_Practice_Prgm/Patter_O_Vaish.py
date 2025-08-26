"""
 Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
   ***
*       *
*       *
*       *
*       *
*       *
   ***

"""

for i in range(1,8):
    for j in range(1,6):
        if i in [1,7]:
            if j in [2,3,4]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i in [2,3,4,5,6]:
            if j in [1,5]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
