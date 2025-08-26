"""
Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python
"""

for i in range (0,7):
    if i not in (3,6):
        print(i)
    else:
        continue