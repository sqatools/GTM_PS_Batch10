"""Write a Python program to calculate the length of a string with loop logic"""

str1="Hello world"
count=0
for i in str1:
    if isinstance(i,str):
        count+=1

print(count)

