"""Python string program to reverse a string if it’s length is a multiple of 4."""
str1=input("enter the string")
if len(str1)%4!=0:
    print((str1[-1::-1])*2)
else:
    print((str1[-1::-1]) * 4)