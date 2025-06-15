"""
#1) program to print the following pattern
1
12
123
1234
12345
"""
print("*" * 20)
for i in range(0, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

"""
#2) program to print the following pattern
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
"""
print("*" * 20)
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

"""
#3) program to print the following pattern
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
"""
print("*" * 20)
for i in range(0, 6):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()

"""
# 4) Python program to print the following pattern

5 4 3 2 1
5 4 3 2 
5 4 3
5 4 
5
"""
print("-" * 20)
for m in range(5, 0, -1):
    for n in range(5, 5 - m, -1):
        print(n, end=" ")
    print()

"""
# 5) Python program to print the following pattern
* * * * * 
* * * * 
* * * 
* * 
* 
* * 
* * * 
* * * * 
* * * * * 
"""
print("-" * 20)
for m in range(5, 0, -1):
    for n in range(5, 5 - m, -1):
        print("*", end=" ")
    print()
for m in range(1, 5):
    for n in range(0, m + 1):
        print("*", end=" ")
    print()
"""
# 6) Python program to print the following pattern
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
4 8 12 16 
3 6 9 
2 4 
1 
"""
print("*" * 20)
for i in range(0, 6):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()
"""
# 7) Python program to print the following pattern
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
print("*" * 20)
num = 65
for i in range(0, 5):
    for j in range(0, i + 1):
        print(chr(num), end=" ")
        num += 1
    print()
for k in range(1, 5):
    for l in range(4, k - 1, -1):
        print(chr(num), end=" ")
        num += 1
    print()
