# PYTHON LOOPS PRACTICE PROGRAM

# 51). Write a program to calculate the sum of all odd numbers between 1-100 using Python Loops.
al = 0
for l in range(1,101):
    if l%2!=0:
        al+=l

print(al)

print('_'*70)

# 52). Find the numbers which are divisible by 5 in 0-100 using Python Loops.
for d in range(0,101):
    if d%5==0:
        print(d,end=" ")

print()

print('_'*70)
# 53). Write a program to construct the following pattern, using a for loop in Python.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print()


print('_'*70)

# 54). Write a program to construct the following pattern, using a for loop in Python.
# Output :
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(1,6):
    for j in range(1,7-i):
        print("*",end=" ")
    print()

# 55. Write a program to construct the following pattern, using a nested for loop in Python.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for k in range(1,6):
    for j in range(k):
        print(k,end=" ")
    print()

print('_'*70)
