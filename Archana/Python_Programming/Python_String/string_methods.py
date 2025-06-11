str1 = "Hello Python Programming"

print(str1, type(str1))
# Hello Python Programming <class 'str'>

# string formatting
str2 = "Hello my name is Rahul and age is 25 and living in Mumbai"
name = "Pankaj"
age = 30
city = "Pune"

# 1. String Concatenation:
val = "Hello"+" Good Morning"
print(val)
result1 = "Hello my name is "+name+" and age is "+str(age)+" and living in "+city
print(result1)
# Hello my name is Pankaj and age is 30 and living in Pune

# 2. Format Method:
result2 = "Hello my name is {} and age is {} and living in {}".format(name, age, city)
print(result2)
# Hello my name is Pankaj and age is 30 and living in Pune

# 3. F string formatting:
result3 = f"Hello my name is {name} and age is {age} and living in {city}"
print(result3)
# Hello my name is Pankaj and age is 30 and living in Pune



print("_"*50)
##############################################
# Apply loop on string data

str5 = "Programming"
# loop without indexing
for char in str5:
    print(char)

print("_"*50)
# loop with indexing
string_length = len(str5)
print(string_length)

for i in range(string_length):
    print(i, str5[i])

print("_"*50)
# loop with indexing
for i in range(-1, -string_length, -1):
    print(i, str5[i])

print("_"*50)
######### get character with index #########
str6 = "Python"

print(str6[3]) # h
print(str6[-5]) # y


print("_"*50)
######### slicing in string #########
"""
Rule1 : str[start_index: last index]
->  Default step value is 1
->  Result will include start_index character and exclude last index char in the output
->  Result value will always print from left to right:
->  start and index index value could be positive or negative
->  If we dont provide the last index the default last index would end of string. 
    e.g.  str[4:] # here output will be from 4 to end of string.
->  Default start_index is zero str[:3] # Here output will output value from 0 to 2

"""

str7 = "Good Morning"
print(str7[0:4]) # Good
print(str7[-7:-1]) # Mornin
# This will include output from -7 to end of string
print(str7[-7:]) # Morning
# This will include output from 0 to 7
print(str7[:8]) # Good Mor

print(str7[5:1])  # EMPTY
print(str7[2:-1]) # od Mornin
print(str7[-9:10]) # d Morni
print(str7[:]) # Good Morning


print("_"*50)
##################################
"""
Rule2 : str[start_index: last_index: step_value]
->  Output will include start_index and exclude last_index and return output as per the step value
->  default start_index is 0 and default last_index is end of string with positive step value
->  default start_index is -1 and default last_index is begining of string with negative step value
->  default step value is  1
"""
str8 = "Very Good Morning"
# here output will include 2 to 7 with 1 step value
print(str8[5:9:1])  # Good
# here output will include 2 to 14 with 2 step value
print(str8[2:15:2])  # r odMri

# default start_index is 0 and default last_index is end of string with positive step value
print(str8[:10:1]) # Very Good
print(str8[2::2]) # r odMrig

# default start_index is -1 and default last_index is begining of string with negative step value
print(str8[:8:-1]) # gninroM

print(str8[::-1]) # gninroM dooG yreV
# [-1:-len(str):-1]


# ->  default step value is  1
print(str8[2:14:])  # ry Good Morn
print(str8[-1:-10:])  # EMPTY output


# Home Work
"""
# str1 = "Virat is great Indian Player"
output1 = "Player is great Indian Virat"
output2 = "VVirat is great Indian Playerr"
output3 = "VViratt iiss ggreatt IIndiann PPlayerr"
output4 = "(Virat is great): reverse this part : Indian Player"
"""
str1 = "Virat is great Indian Player"

print("_"*50)
#Q1 :
w1 = str1[:5]
w3 = str1[-7:]
w2 = str1[5:-7]

output = f"{w3} {w2} {w1}"
print(output)

print("_"*50)
#Q2 :
f_chr = str1[0]
l_chr = str1[-1]
output2 = f"{f_chr}{str1}{l_chr}"
print(output2)
# VVirat is great Indian Playerr

#################################################
# string method
print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
 'translate', 'upper', 'zfill'
"""

print("_"*50)
##### upper() and lower() method ######

str_a = "Hello we are Learning Python"
print("Upper output :", str_a.upper())
# Upper output : HELLO WE ARE LEARNING PYTHON
print("Lower output :", str_a.lower())
# Lower output : hello we are learning python

print("_"*50)
##### isupper() and islower() method ######
# These method check the given string is in lower case or upper case.
str_b = "GOOD MORNING"
str_c = "python programing"
str_d = "Hello Python"
print("isupper str_b :", str_b.isupper()) # True
print("islower str_c :", str_c.islower()) # True

print("islower or islower for str_d", str_d.isupper(), str_d.islower())
# False , False

str_e = "HELLO &^%123"
print("str_e isupper :", str_e.isupper())
# str_e isupper : True

print("_"*50)
#####################################
#title() method : This method convert the target string into titlecase, means, first
#                 letter of each word will convert into upper case.

str_f = "heLLo GoodMorning"
print("title output :", str_f.title()) # Hello Goodmorning


print("_"*50)
#####################################
# istitle():  this method check given string is title string or not
str_g = "India is best cricket team &%^%$"
str_j = "Virat Is Best Indian Player 2345"
print("str_g istitle :", str_g.istitle()) # False
print("str_j istitle :", str_j.istitle()) # True

print("_"*50)
#####################################
# swapcase() method :  This method convert lower character to upper and upper character
# to lower case.

str_k = "Python is Very To Learn"
print("str_k swapcase :", str_k.swapcase())
# str_k swapcase : pYTHON IS vERY tO lEARN


print("_"*50)
#####################################
# capitalize() method : This method convert only first letter of string into capital case
# remaining character converted into lower case.

str_l = "Python is Very To LeaRN"
print("str_l to capitalize :", str_l.capitalize())
# str_l to capitalize : Python is very to learn

print("_"*50)
#####################################
# count() method : This method return the number occurrence of any char or substring in
# the given string.

str_q = "Python Pycon and Learning is easy"
print("count of a :", str_q.count('a'))
# count of a : 3

print("count of Py :", str_q.count('Py'))
# count of Py : 2

print("_"*50)
#####################################
# index90 method : This method return the index position of char or substring in given target
# string
# ->  If same char/sub-string repeated multiple times, then index method will first value position.



str_x = "Python Pycon and Learning is easy"
print("Index of a :", str_x.index('a'))
# Index of a : 13

print("Index of ea :", str_x.index('ea'))
# Index of ea : 18

count = 0
for i in range(len(str_x)):
    if str_x[i] == 'a':
        count +=1
        if count == 3:
            print(str_x[i], i)
    else:
        continue

# third a index position
# a 30

# get index of non existing letter
# print("index of w :", str_x.index('w'))
# ValueError: substring not found

print("_"*50)
#######################################
# find method() :  This method return the index position of exiting and letter
#                 and if letter is not available in the target string, then it will
#                 it will return -1

str_y = "India in Growing Country"
print("find G :", str_y.find('G'))
# find G : 9

# check for non existing letter
print("Find W :", str_y.find("W"))
# Find W : -1 # find method return -1

print("_"*50)
############################################
# split() Method : This method return list of sub-string from target string.
#                  ->  This method break the string from given delimeter and return output
# in list

str_s = "India is Growing Country"
print("split with space :", str_s.split(" "))
# split with space : ['India', 'is', 'Growing', 'Country']

str_f = "India is Growainga Couantary"
print("split with a letter :", str_f.split("a"))
# split with a letter : ['Indi', ' is Grow', 'ing', ' Cou', 'nt', 'ry']

url = "https://facebook.com"
v1 = url.split("//")[0][:-1]
print("v1 :", v1) # https
# v1 : https

v2 = url.split("//")[1].split(".")[0]
print("v2 :",v2)
# v2 : facebook

print("_"*50)
##############################
# replace() method : This method replace the word1 with word2 from given target string and return the updated string.
#                     -> User can define the number of occurrences to replace from given string.
#                      -> str.replace(word1, word2, no_of_occurrences)
#                     -> if user don't provide any value for no_of_occurrences, then it will replace all available
#                        matching words.

str_m = "Python is Best 5 Programming, Python is Easy to Learn 5"
result = str_m.replace("Python", "JAVA")
print("result :", result)
# JAVA is Best Programming, JAVA is Easy to Learn


result2 = str_m.replace("Python", "JAVA", 1).replace("Easy", "Hard").replace("5", "10")
print("Result2 :", result2)
# JAVA is Best 10 Programming, Python is Hard to Learn 10


print("_"*50)
##############################
# strip() method  :  This method remove all the trailing spaces from given string. it means the spaces which is
#                    available in the begining and end of the string.

str_k = "  Python Programming  "
print(str_k)
#   Python Programming

# remove trailing spaces
output2 = str_k.strip()
print(output2)  #Python Programming  # there is no space in output

# lstrip method :  This method will remove left side space or space available in the begining of the string

str_p = "    We Are Learning Python     "
print(str_p.lstrip())  # We Are Learning Python      # output does not contain left side spaces.

# rstrip method :  This method will remove right side space or space available at end of the string
print(str_p.rstrip())  #     We Are Learning Python


print("_"*50)
###############################
# join() method :  This method will join each character of string with provided delimeter, e.g. -,*/

str_A = "Programming"

result1 = "-".join(str_A)
print("result1 :", result1) # result1 : P-r-o-g-r-a-m-m-i-n-g

result2 = "&*^%".join(str_A)
print("result2 :", result2) # P&*^%r&*^%o&*^%g&*^%r&*^%a&*^%m&*^%m&*^%i&*^%n&*^%g


print("_"*50)
##########################################
# isnumeric method(): This method return true if string contains only numbers

s1 = "354543 34"
print(s1.isnumeric()) # False

s2 = "5464567456"
print(s2.isnumeric()) # True

print("_"*50)
###########################################
# isalnum() method:  This method return true if string contains alphabate and numbers

s3 = "Hello 345"
print(s3.isalnum()) # False

s4 = "Hello77777"
print(s4.isalnum()) # True

s5 = "77777"
print(s5.isalnum()) # True

s6 = "Python"
print(s6.isalnum()) # True


print("_"*50)
###########################################
# isalpha() method: This method return true if string contains only alphabate.

s7 = "Python Programming"
print(s7.isalpha()) # False

s8 = "PythonProgramming"
print(s8.isalpha()) # True

###############################################################

