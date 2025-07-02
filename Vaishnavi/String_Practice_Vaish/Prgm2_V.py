"""Python string program that takes a list of strings and returns the length of the longest string."""

str1="Python program to get a string"
word=str1.split()
great=0
second=0
str2=""
for i in word:
    len1=len(i)
    if len1>second:
        great=len1
        second=len1
        str2=i

    else:
        great=second
        str2 = i
print(len1)