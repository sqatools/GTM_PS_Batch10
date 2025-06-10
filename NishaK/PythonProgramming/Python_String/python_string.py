str1 = "Hello Python Programming"

print(str1, type(str1))
# Hello Python Programming <class 'str'>


print("-"*50)

val = "Hello"+"Good Morning"
print(val)
print("-"*50)


# String Formatting
str2 = "Hello my name is Rahul and age is 25 and living in Mumbai"
name = "Pankaj"
age = 30
city = "Pune"

# String Concatenation
result1 = "Hello my name is "+name+" and age is "+str(age)+" and living in "+city
print(result1)
# Hello my name is Pankaj and age is 30 and living in Pune


print("-"*20)
# String Format Method
result2 = "Hello my name is {} and age is {} and living in {}".format(name, age, city)
print(result2)
# Hello my name is Pankaj and age is 30 and living in Pune


print("-"*20)
# F String Formatting
result3 = f"Hello my name is {name} and age is {age} and living in {city}"
print(result3)
# Hello my name is Pankaj and age is 30 and living in Pune


print("-"*50)
# Apply loop on string data
str5 = "Programming"
# loop without indexing
for char in str5:
    print(char)
"""
P
r
o
g
r
a
m
m
i
n
g
"""


print("-"*20)
# loop with indexing
string_length = len(str5)
print(string_length)
# 11

print("-"*20)
for i in range(string_length):
    print(i, str5[i])
"""
0 P
1 r
2 o
3 g
4 r
5 a
6 m
7 m
8 i
9 n
10 g


"""
for i in range(-1, -string_length, -1):
    print(i, str5[i])
"""
-1 g
-2 n
-3 i
-4 m
-5 m
-6 a
-7 r
-8 g
-9 o
-10 r
"""


print("_"*50)
# get character with index #########
str6 = "Python"
print(str6[5])  # n
print(str6[-2])  # 0


print("_"*50)
# slicing in string #########
"""
Rule1 : str[start_index: last index]
->  Default step value is 1
->  Result will include start_index character and exclude last index char in the output
->  Result value will always print from left to right:
->  start and end index value could be positive or negative
->  If we dont provide the last index the default last index would end of string. 
    e.g.  str[4:] # here output will be from 4 to end of string.
->  Default start_index is zero str[:3] # Here output will output value from 0 to 2

"""


str7 = "Good Morning"
print(str7[0:4])  # Good
print(str7[-7:-1])  # Mornin
# This will include output from -7 to end of string
print(str7[-7:])  # Morning
# This will include output from 0 to 7
print(str7[:8])  # Good Mor

print(str7[5:1])  # EMPTY
print(str7[2:-1])  # od Mornin
print(str7[-9:10])  # d Morni
print(str7[:])  # Good Morning


print("_"*50)
##################################
"""
Rule2 : str[start_index: last_index: step_value]
->  Output will include start_index and exclude last_index and return output as per the step value
->  default start_index is 0 and default last_index is end of string with positive step value
->  default start_index is -1 and default last_index is beginning of string with negative step value
->  default step value is  1
"""


str8 = "Very Good Morning"
# here output will include 2 to 7 with 1 step value
print(str8[5:9:1])  # Good
# here output will include 2 to 14 with 2 step value
print(str8[2:15:2])  # r odMri

# default start_index is 0 and default last_index is end of string with positive step value
print(str8[:10:1])  # Very Good
print(str8[2::2])  # r odMrig


# default start_index is -1 and default last_index is begining of string with negative step value
print(str8[:8:-1])  # gninroM

print(str8[::-1])  # gninroM dooG yreV
# [-1:-len(str):-1]


# ->  default step value is  1
print(str8[2:14:])  # ry Good Morn
print(str8[-1:-10:])  # EMPTY output


print("-"*50)
# string method

print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
'title', 'translate', 'upper', 'zfill']
"""

print("_"*50)
# upper() and lower() method

str_a = "Hello we are Learning Python"
print("Upper Output :", str_a.upper())
# Upper Output : HELLO WE ARE LEARNING PYTHON

print("Lower Output :", str_a.lower())
# Lower Output : hello we are learning python


print("_"*50)
# isupper() and islower() method

str_b = "GOOD MORNING"
str_c = "python programing"
str_d = "Hello Python"
print("isupper : ", str_b.isupper())
print("islower :", str_c.islower())
print("isupper or islower :", str_d.isupper(), str_d.islower())
# isupper :  True
# islower : True
# isupper or islower : False False

str_e = "HELLO &^%123"
print("str_e isupper :", str_e.isupper())
# str_e isupper : True

print("_"*50)
# title() method

str_f = "heLLo GoodMorning"
print("title :", str_f.title())
# title : Hello Goodmorning


print("_"*50)
# istitle()
str_g = "India is best cricket team &%^%$"  # istitle : False
str_j = "Virat Is Best Indian Player 2345"  # istitle : True
print("istitle :", str_g.istitle())
print("istitle :", str_j.istitle())


print("_"*50)
# swapcase() method
str_k = "Python is Very To Learn"
print("swap-case :", str_k.swapcase())
# swapcase : pYTHON IS vERY tO lEARN


print("_"*50)
# capitalize() method
str_l = "Python is Very To LeaRN"
print("Capitalize :", str_l.capitalize())
# Capitalize : Python is very to learn


print("_"*50)
# count() method
str_q = "Python Pycon and Learning is easy"
print("Count of a :", str_q.count("a"))
# Count of a : 3
print("Count of py :", str_q.count("Py"))
# Count of py : 2


print("_"*50)
# index method
str_x = "Python Pycon and Learning is easy"
print("Index of a :", str_x.index("a"))
# Index of a : 13


count = 0
for i in range(len(str_x)):
    if str_x[i] == 'a':
        count += 1
        if count == 3:
            print(str_x[i], i)
        else:
            continue
# a 30


print("_"*50)
# find method()
str_y = "India in Growing Country"
print("find G :", str_y.find('G'))
# find G : 9

print("find non existing b :", str_y.find("b"))
# find non existing b : -1

print("_"*50)
# split() Method
str_s = "India is Growing Country"
print("Split :", str_s.split(" "))
# Split : ['India', 'is', 'Growing', 'Country']

str_f = "India is Growainga Couantary"
print("Split2 :", str_f.split("a"))
# Split2 : ['Indi', ' is Grow', 'ing', ' Cou', 'nt', 'ry']

url = "https://facebook.com"
v1 = url.split("//")[0][:-1]
print("Split url: ", v1)

v2 = url.split("//")[1].split(".")[0]
print("v2 :", v2)
# v2 : facebook


print("_"*50)
# replace() method
str_m = "Python is Best 5 Programming, Python is Easy to Learn 5"
result1 = str_m.replace("Python", "JAVA")
print("Replace result :", result1)
# Replace result : JAVA is Best 5 Programming, JAVA is Easy to Learn 5


result2 = str_m.replace("Python", "JAVA", 1).replace("Easy", "Hard").replace("5", "10")
print("Result2 :", result2)
# JAVA is Best 10 Programming, Python is Hard to Learn 10


print("_"*50)
# strip() method

str_k = "  Python Programming  "
print("Strip :", str_k.strip())
# Strip : Python Programming

# lstrip method
str_p = "    We Are Learning Python     "
print("lstrip :", str_p.lstrip())
# lstrip : We Are Learning Python

# rstrip method
str_p = "    We Are Learning Python     "
print("rstrip :", str_p.rstrip())
# rstrip :     We Are Learning Python


print("_"*50)
# # join() method
str_A = "Programming"
result1 = "-".join(str_A)
print("Join :", result1)
# Join : P-r-o-g-r-a-m-m-i-n-g


result2 = "&*^%".join(str_A)
print("Join :", result2)
# Join : P&*^%r&*^%o&*^%g&*^%r&*^%a&*^%m&*^%m&*^%i&*^%n&*^%g


print("_"*50)
# isnumeric method()
s1 = "354543 34"
print(s1.isnumeric())
# False

s2 = "5464567456"
print(s2.isnumeric())
# True

print("_"*50)
# isalnum() method
s4 = "Hello77777"
print(s4.isalnum())
# True

s5 = "77777"
print(s5.isalnum())
# True

s6 = "Python"
print(s6.isalnum())
# True


print("_"*50)
# isalpha() method

s7 = "Python Programming"
print(s7.isalpha())
# False


s8 = "PythonProgramming"
print(s8.isalpha())
# True
