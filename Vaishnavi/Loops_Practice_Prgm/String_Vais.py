"""
Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”
"""
str1="python"
str2=""
len1=len(str1)
for i in range(len1):
    str2+=str1[i]
print(str2)


