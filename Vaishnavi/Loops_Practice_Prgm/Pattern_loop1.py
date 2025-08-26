"""
Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
for i in range (0,5):#0,0 and 1
    for j in range(0,i+1):#0, 0 and 1
      print("*",end="")
    print()

for k in range(1,5):#1
    for j in range(5,k,-1):#5-1=4
        print("*", end="")
    print()
