"""
Write a program to print the pyramid structure using Python Loops.

    Output:

              *
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
    * * * * * * * * * * *
"""

var1=4
var2=6
for i in range(0,6):
    for j in range(0,11):
        if j>var1 and j<var2:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    var1 -= 1
    var2 += 1
    print()

