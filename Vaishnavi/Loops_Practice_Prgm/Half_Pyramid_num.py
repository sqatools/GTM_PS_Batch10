"""
Write a program to print number patterns using Python Loops.

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
"""
count=1
for i in range (1,6):
    for j in range(i):
        print(count,end=" ")
        count+=1
    print()
temp=count-1
for k in range (4,-1,-1):
    for l in range(1,k+1):
        temp-=1
        print(temp,end=" ")
    print()