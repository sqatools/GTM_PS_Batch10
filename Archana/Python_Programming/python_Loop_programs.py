# For Loop Basics
# 1. Print values from 1 to 10 using loop
print("-" * 50)
for i in range(2, 5, 1):
    print(i)
print("-" * 50)
for i in range(12, 5, -1):
    print(i, end="")

print("-" * 50)
for i in range(-7, 1, 1):
    print(i, end="")


# Use if condition inside for loop
# Program to get all the odd numbers from 1 to 30

for val1 in range(1, 31):
    if val1 % 2 != 0:
        print(val1)
    else:
        pass
