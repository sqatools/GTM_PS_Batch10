"""
8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
Input : “SqaTOOlS”
Output : “sqatools”
"""
str1="SqaTOOlS"
for i in str1:
    if i.isupper():
        print(i.lower(),end=" ")
    else:
        print(i,end=" ")
