"""
 Python loops program to print the pattern T using Python Loops.

       Output :

       * * * * * * * * *
       * * * * * * * * *
             * * *
             * * *
             * * *
             * * *
             * * *

"""

for i in range(1,8):
    for j in range(1,10):
        if i in [1,2]:
            if j in [1,2,3,4,5,6,7,8,9]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i in[3,4,5,6,7]:
            if j in [4,5,6]:
                print("*",end=" ")
            else:
                print(" ", end=" ")
    print()