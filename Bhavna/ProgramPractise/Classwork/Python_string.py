# 04/06/2025 Session
# Srings

str1 = "Hello Python Programming"
print(str1, type(str1))

# String Formatting
a = "Hello my name is Ryan and age is 25 and living in Bangalore "
name = "Isha"
age = 20
place = "Nagpur"

# 1. String Concatenation:

val = "Hello" + " Good Morning"
print(val)
result = "Hello my name is "+name+" and age is "+str(age)+" and living in "+place
print(result)

# 2. Format Method:
result1 = "Hello my name is {} and age is {} and living in {}".format(name,age,place)
print(result1)

# 3.F string Formatting:
result2 = f"Hello my name is {name} and age is {age} and living in {place}"
print(result2)

print('_'*70)
##############################################
# Apply loop on string data

str2 = "Python"
# loop without indexing
for i in str2:
    print(i)

print('_'*70)

# loop with indexing
string_length = len(str2)
print(string_length)

for i in range(string_length):
    print(i, str2[i])

print('_'*70)

for i in range(-1, -string_length,-1):
    print(i, str2[i])

print('_'*70)
######### get character with index #########

print(str2[3])
print(str2[-5])

print('_'*70)

######### slicing in string #########

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
str3 = "Good Morning"

print(str3[0:6])        #Good M
print(str3[-7:-2])      #Morni
print(str3[-7:])        #Morning
# This will include output from -7 to end of string

# This will include output from 0 to 7
print(str3[:8])         #Good Mo

print(str3[4:1])        #Empty
print(str3[2:-1])       #od Mornin
print(str3[-9:10])      #d Morni
print(str3[:])          #Good Morning

print('_'*70)

"""
Rule2 : str[start_index: last_index: step_value]
->  Output will include start_index and exclude last_index and return output as per the step value
->  default start_index is 0 and default last_index is end of string with positive step value
->  default start_index is -1 and default last_index is begining of string with negative step value
->  default step value is  1
"""

str4 = "Very Good Morning"

print(str4[5:9:1])      #Good
# here output will include 2 to 7 with 1 step value

print(str4[2:10:2])     #r od
# here output will include 2 to 9 with 2 step value

# default start_index is 0 and default last_index is end of string with positive step value
print(str4[:7:1])       #Very Go
print(str4[2::2])       #r odMrig

# default start_index is -1 and default last_index is begining of string with negative step value
print(str4[:8:-1])      #gninroM
print(str4[5::-1])      #G yreV

# ->  default step value is  1
print(str4[2:14:])      #ry Good Morn
print(str4[-1:-10:])       #empty output

print('_'*70)

######## ASSIGNMENT_3 ###########
"""
# str1 = "Virat is greate Indian Player"
output1 = "Player is greate Indian Virat"
output2 = "VVirat is greate Indian Playerr"
output3 = "VViratt iiss ggreatee IIndiann PPlayerr"
output4 = "(Virat is greate): reverse this part : Indian Player"
"""

str1 = "Virat is great Indian Player"
w1 = str1[:5]
w2 = str1[5:-6]
w3 = str1[-6:]
output1 = f"{w3}{w2}{w1}"
print("Output1:", output1)

f_char = str1[0]
l_char = str1[-1]
output2 = f"{f_char}{str1}{l_char}"
print("Output2:", output2)

a = str1[0]*2+str1[1:4]+str1[4]*2
b = str1[6]*2 + str1[7]*2
c = str1[9]*2 + str1[10:13] + str1[13]*2
d = str1[15]*2 + str1[16:20] + str1[20]*2
e = str1[-6]*2 + str1[-5:-1] + str1[-1]*2
output3 = f"{a}{b}{c}{d}{e}"
print("Output3:", output3)

r1 = str1[13::-1]
r2 = str1[14:28]
Output4 = f"{r1}{r2}"
print("Output4:", Output4)
print('_'*70)

# 05/06/2025 Session
############## String Method ##############
print(dir(str))
'''
'__add__', '__class__', '__contains__', '__delattr__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', 
'__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__mod__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
'__rmul__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', 'capitalize', 'casefold', 'center',
 'count', 'encode', 'endswith', 'expandtabs', 'find', 
 'format', 'format_map', 'index', 'isalnum', 'isalpha', 
 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
 'islower', 'isnumeric', 'isprintable', 'isspace', 
 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
  'maketrans', 'partition', 'removeprefix', 'removesuffix',
   'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
   'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
   'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''
print('_'*70)

########## upper() and lower() method ########

str_a = "Hello, How are you?"
print("upper output:", str_a.upper())
#upper output: HELLO, HOW ARE YOU?

print("Lower Output:", str_a.lower())
# Lower Output: hello, how are you?

print('_'*70)
######### isupper() and islower() method ########
# These method check the given string is in lower case or upper case.
str_b = "GOOD AFTERNOON"
print("isupper output:", str_b.isupper())
print("islower output", str_b.islower())

str_c = "good morning"
print("islower output for str_c", str_c.islower())
# islower output for str_c True
str_d = "everyday is a new chance to do something good"
print("isupper or islower output:", str_d.isupper(), str_d.islower())
#isupper or islower output: False True

str_e = "HELLO #$$122"
print("isupper output for str_e:", str_e.isupper())
#isupper output for str_e: True

print('_'*70)
################# title method #################

#title() method : This method convert the target string into titlecase, means, first
#                 letter of each word will convert into upper case.

str_f = "Embrace The Present"
str_f1 = "Be grateful for the simple joys"

print("istitle output of str_f:", str_f.istitle())
print("istitle output of str_f1 ", str_f1.istitle())

print('_'*70)

#################### SWAPCASE METHOD #################
# swapcase() method :  This method convert lower character to upper and upper character
# to lower case.

str_g = "You are stronger than you think."
print("str_g swapcase:", str_g.swapcase())
#str_g swapcase: yOU ARE STRONGER THAN YOU THINK.

print('_'*70)

################# Capitalize method #################
# capitalize() method : This method convert only first letter of string into capital case
# remaining character converted into lower case.

str_h = "Make Time for What Matters Most."
print("capitalize str_h:", str_h.capitalize())
# capitalize str_h: Make time for what matters most.
print('_'*70)

###################### COUNT METHOD ###############
# count() method : This method return the number occurrence of any char or substring in
# the given string.

str_i = "Believe in yourself and your abilities."
print("count output for str_i:", str_i.count('e'))
# count output for str_i: 5

print("count of you:", str_i.count('you'))
# count of you: 2

print('_'*70)

######################## INDEX METHOD #############
# index method : This method return the index position of char or substring in given target
# string
# ->  If same char/sub-string repeated multiple times, then index method will first value position.

str_j = "A little kindness can brighten someone's day in india."
print("index of i:", str_j.index('i'))
# index of i: 3

print("index of in:", str_j.index('in'))
# index of in: 10

count = 0
for i in range(len(str_j)):
    if str_j[i] == 'i':
        count+=1
        if count == 3:
            print(str_j[i], i)
    else:
        continue

# i 24


# get index of non existing letter
# print("index of w :", str_x.index('z'))
# ValueError: substring not found

print('_'*70)

###################### FIND METHOD ###################
# find method() :  This method return the index position of exiting letter
#                 and if letter is not available in the target string, then it will
#                 it will return -1

str_k = "Teachers can open the door, but you must enter it yourself."
print("find a:", str_k.find('a'))
#find a: 2

# check for non existing letter
print("Find A:", str_k.find('A'))
#Find A: -1

print('_'*70)

############################ SPLIT METHOD ##################

# split() Method : This method return list of sub-string from target string.
#                 ->  This method break the string from given delimeter and return output in list

str_l = "The expert in anything was once a beginner."
print("split with space:", str_l.split(" "))
# split with space: ['The', 'expert', 'in', 'anything', 'was', 'once', 'a', 'beginner.']

str_m = "The way to get started is to quit talking and begin doing."
print("split with a:",str_m.split('a'))
# split with a: ['The w', 'y to get st', 'rted is to quit t', 'lking ', 'nd begin doing.']

url = "https://www.google.com"
a1 = url.split("//")
print(a1)       #['https:', 'www.google.com']
a2 = url.split(("//"))[0][:-1]
print(a2)
# https

a3 = url.split("//")[1].split(".")[1]
print(a3)
#google

print('_'*70)

###############
# 06-06-2025 SESSION

# replace() method : This method replace the word1 with word2 from given target string and return the updated string.
#                     -> User can define the number of occurrences to replace from given string.
#                      -> str.replace(word1, word2, no_of_occurrences)
#                     -> if user don't provide any value for no_of_occurrences, then it will replace all available
#                        matching words.

str_n = "The best way to predict your future is to make it."
print("result:", str_n.replace("make","create"))
#result: The best way to predict your future is to create it.

ss = "you are braver than you believe, stronger than you seem and smarter than you think."
print("SS:", ss.replace("you","I",2).replace("stronger","lighter"))
# SS: I are braver than I believe, lighter than you seem and smarter than you think.

print('_'*70)

####################### STRIP METHOD ##########
# strip() method  :  This method remove all the trailing spaces from given string. it means the spaces which is
#                    available in the begining and end of the string.

str_o = "  Good Night   "
print(str_o.strip())     #Good Night  ## there is no space in output

# lstrip method :  This method will remove left side space or space available in the begining of the string

str_p = "   helloo have a great day   "
print(str_p.lstrip())       #helloo have a great day   # output does not contain left side spaces.

# rstrip method :  This method will remove right side space or space available at end of the string
print(str_p.rstrip())       #   helloo have a great day

print('_'*70)

##################### JOIN METHOD ################
# join() method :  This method will join each character of string with provided delimeter, e.g. -,*/

str_A = "Python"
result_1 = "*".join(str_A)
print(result_1)         #P*y*t*h*o*n

result_2 = "AA&".join(str_A)
print(result_2)         #PAA&yAA&tAA&hAA&oAA&n

print('_'*70)

########################## ISNUMERIC ####################
# isnumeric method(): This method return true if string contains only numbers

n1 = "12255212"
print(n1.isnumeric())       #True

n2 = "23 2323 223"
print(n2.isnumeric())       #False

print('_'*70)
######################## ISALNUM ###################
# isalnum() method:  This method return true if string contains alphabate and numbers

N = "Hi 12"
print(N.isalnum())          #False

N1 = "Hi1447"
print(N1.isalnum())         #True

N2 = "hi"
print(N2.isalnum())         #True

N3 = "8585"
print(N3.isalnum())         #True

print('_'*70)
########################## ISALPHA #################
# isalpha() method: This method return true if string contains only alphabate.

A = "Hello"
print(A.isalpha())          #True

A1 = "He llo"
print(A1.isalpha())         #False

A2 = "Hello123"
print(A2.isalpha())         #False
