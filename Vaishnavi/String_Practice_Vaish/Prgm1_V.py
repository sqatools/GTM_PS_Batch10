"""Write a Python program to get a string made of the first and the last 2 chars
 from a given string. If the string length is less than 2, return instead of the empty string"""

str1="Python string is a sequence of characters"
print(str1[0:2], str1[-2:])
if len(str1)<2:
    print("""""")