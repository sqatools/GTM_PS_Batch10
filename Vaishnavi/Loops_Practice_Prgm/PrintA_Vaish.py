"""
 Write a program to print the pattern A using Python Loops.

    Output :

      * * * *
    * * * * * *
    * *     * *
    * *     * *
    * * * * * *
    * * * * * *
    * *     * *
    * *     * *
    * *     * *
"""
for i in range(0,9):
    for j in range(0,6):
        if i in [0]:
            if j in [1,2,3,4]:
                print("*",end=" ")
            else:
                print(" ",end="")
        elif i in [1,4,5]:
            if j in [0,1,2,3,4,5]:
                print("*",end=" ")
            else:
                print(" ", end="")
        elif i in [2,3,6,7,8]:
            if j in [0,1,4,5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
