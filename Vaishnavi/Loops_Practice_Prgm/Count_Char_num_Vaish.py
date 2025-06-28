"""
Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4
"""
input1="python1234$"
char=0
num=0
for i in input1:
    if i.isalpha():
        char+=1
    elif i.isnumeric():
        num+=1
    else:
        continue
print("num :",num)
print("char :",char)


