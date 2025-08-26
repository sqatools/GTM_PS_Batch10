"""
10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”

def replace_second_occurrence(text):
    count = {}
    result = ""
    for ch in text:
        count[ch] = count.get(ch, 0) + 1
        if count[ch] == 2:
            result += "$"
        else:
            result += ch
     return result

13). Write a python to count vowels from each word in the given string show as dictionary output.
Input = “We are Learning Python Codding”
output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
"""
test = "We are Learning Python Codding"
vowels = "aeiou"
result = dict()

for word in test.split():
    count = 0
    for i in word:
        if i in vowels:
         count += 1
         result[word]=count
print(result)

########
# Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string
"""
strg = input(str("Enter your values"))
for char in strg:
    if len(strg)< 3:
         print("true")
    else:
         print(strg[0:3:1]+strg[-1:-3:-1])

"""
### Python string program that takes a list of strings and returns the length of the longest string.
print("*_-_"*60)
print()

list1 = ["MY NAME IS NAGARATNA AND LIVING IN BANGALORE"]
words = list1[0].split()
print(words)
longest = max(words,key=len)
print("Longest word is",longest)
################################################################
# Repeat vowels and consonants 3 and 2 times resp.
test = ["Sqa Tools Learning"]
result = ""
print(result)
vowels = "a","A","e","E","i","I","o","O","u","U"
for char in test[0]:
    if char in vowels:
        result = result+char*3
    else:
        result= result + char*2

print(result)

print("*_-_"*30)

print("*_-_"*30)
"""
 Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”
"""
Input = "Cricket Plays Virat"

wd1 = "Cricket"
wd2 = "Plays"
wd3 = "Virat"
output= f"{wd3} {wd2} {wd1}"
print(output)
"""

16). Write a python program to get all the digits from the given string.
Input = “””
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
val = "Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organization’s 5324 success or failure is based on 555 leadership excellence and not managerial acumen"
new = val.split()
for i in new:
    if i.isdigit():
       print(i,end=" ")

# write a program to seperate words from given list

type = "675  you 7689 765t test 8796"
spt = type.split()
for j in spt:
    if j.isalpha():
        print(j)
# Write a program to seperate the char from given list

my_list = "G12hghghjhb8767hguyt5678"
list2 = my_list[0].split()
for char in my_list:
    if char.isdigit():
        print(char,end=" ")




"""
Write a python program to replace the words “Java” with “Python” in the given string.
Input = “JAVA is the Best Programming Language in the Market”
Output = “Python is the Best Programming Language in the Market”
"""
print("*_-_"*60)
rep = "JAVA is the Best Programming Language in the Market"
T = "Python"
Q = rep.split()
print(Q)
res= rep.replace("JAVA",T)
print(res)


