"""# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2,
# return instead of the empty string
str1 = str(input("Enter any string"))
length = len(str1)
if length < 2:
    print("True")
else:
    print(str1[:2] + str1[-2:])

#2 Python string program that takes a list of strings and returns the length of the longest string.
list1 = ["arjun","Suraj","sujathatha","prasannaprasanna",]
max_length = 0
for word in list1:
    a = len(word)
    if a > max_length:
        max_length = a
print("the longest string is: ",a)

string = ["prasanna123", "am", "learn", "python"]
temp = 0

for word in string:
    a = len(word)
    if a > temp:
        temp = a

#Printing output
print(temp)
# 3)Python string program to get a string made of 4 copies
# of the last two characters of a specified string (length must be at least 2).
string1 = str(input("enter your string:"))
char = string1[-2:]
print(char*4)

# 4). Python string program to reverse a string if it’s length is a multiple of 4.
string ="prasanna"
a = len(string)
if (a%4 == 0):
    print(string[::-1])

# 5). Python string program to count occurrences of a substring in a string.

string2 = "python is very powerful language python is easy to learn"
sub_string = "python"
string2.count("python")

"""
# # Q1: write a program to get count of upper case characters.
str1 = "Today Is sUNday So It Is HolidAy"
count = 0
for char in str1:
    if(char.isupper() == True):
        count = count + 1
        print(count)
    else:
        continue
print("Total number of Capital letters in Str1 is:",count)
###########################################################
# Q2: write a program to remove duplicate names from given string.
str2 ="Rahul Manoj Nisha Prasanna Nisha Deepesh Archana"
word_list = str2.split(" ")
print(word_list)
output = " "
for word in word_list:
    if word not in output:
        print(output)
        output = output + word + " "
    else:
        continue
print(output)
"""
# Q3: write a program to get max length word from given string.
str3 = "We Are Learning Python Programming , Its easy to learn"
word_list = str3.split(" ")
max_len = 0
max_len_word = " "
for word in word_list:

    if len(word) > max(len(word_list)):
        length = len(word)
        length > max_len_word
    else:
        continue
print("Maximum length of word is:",word,length)
"""

