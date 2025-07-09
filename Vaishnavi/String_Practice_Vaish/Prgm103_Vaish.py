"""Write a program to remove repeated characters in a string and replace it with a single letter using python.
Input = ‘aabbccdd’
Output = ‘cabd’"""
str1="aabbccdd"
result=''
for i in str1:
    if i not in result:
        result=result+i
    else:
        continue
print(result)
