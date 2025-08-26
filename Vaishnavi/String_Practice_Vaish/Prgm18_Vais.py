"""Write a Python program to get all the palindrome words from the string.
Input = “Python efe language aakaa hellolleh”
output = [“efe”, “aakaa”, “hellolleh”]"""

input1="Python efe language aakaa hellolleh"
word=input1.split()

for k in word:
    if k[-1::-1]==k:
        print(k)
    else:
        continue