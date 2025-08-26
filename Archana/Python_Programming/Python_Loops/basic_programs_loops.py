# 1. Write a Python loops program to find those numbers which are divisible
# by 7 and multiple of 5, between 1500 and 2700 (both included).

num1 = 1500
num2 = 2700
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

"""
# 2. Python Loops program to construct the following pattern, using a nested for loops.
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

for i in range(1, 6):
    for j in range(0, i):
        print("*", end=' ')
    print()
for k in range(1, 6):
    for m in range(5, 0+k, -1):
        print("*", end=' ')
    print()

