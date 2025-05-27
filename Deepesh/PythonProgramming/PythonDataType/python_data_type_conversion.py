"""
Python Data Types
1.  Number data type
    i). Integer
    ii). Float
    iii). Complex Number

2.  Sequential data type
    i). String
    ii). List
    ii). Tuple

3.  Dictionary Data type
4.  Set Data type
5.  Boolean Data type



"""
##################### Integer ##################
####
### Int ->  float ###
n1 = 567
f1 = float(n1)
print(f1, type(f1))
# 567.0 <class 'float'>


### Int ->  string ###
n2  = 765767
s1 = str(n2)
print(s1, type(s1), s1[2])
# 765767 <class 'str'> 5


print("_"*50)
### Int ->  list ###
"""
n3 = 87765
l3 = list(n3)
print(l3)
"""
# TypeError: 'int' object is not iterable
list1 = [4, 6, 8, 2, 9]
for val in list1:
    print(val)

# iterable data type :  list, string, tuple, dict, set
# non iterable data type :  int, float, complex, boolean


### Int ->  tuple ###  conversion is not possible
### Int ->  dict ### conversion is not possible
### Int ->  set ### conversion is not possible

print("_"*50)
### Int ->  boolean ###
a = 0
b1 = bool(a)
print(b1, type(b1))
# False <class 'bool'>

c = 450
b2 = bool(c)
print(b2, type(b2))
# True <class 'bool'>


###################### Float ######################
print("_"*50)
### Float ->  int ###
f1= 60.67
n1 = int(f1)
print(n1, type(n1))
# 60 <class 'int'>


print("_"*50)
### Float ->  string ###
f2 = 79.56
s2 = str(f2)
print(s2, type(s2), s2[-1])
# 79.56 <class 'str'> 6

print("_"*50)
### Float ->  list ### conversion is not possible
### Float ->  tuple ### conversion is not possible
### Float ->  dict ### conversion is not possible
### Float ->  set ### conversion is not possible


print("_"*50)
### Float ->  boolean ###

f4 = 0.0
b1 = bool(f4)
print(b1, type(b1))
# False <class 'bool'>

f5 = 89.55
b2 = bool(f5)
print(b2, type(b2))
# True <class 'bool'>


############################# String #########################

print("_"*50)
### string ->  int ###
# 1. if string contains characters, then string to int conversion it not possible.
"""
s1 = 'Python'
n1 = int(s1)
print(n1)
"""
# invalid literal for int() with base 10: 'Python'

# 2. If string contains only numbers without any space, then conversion is possible
s2 = "457766523"
n2 = int(s2)
print(n2, type(n2), n2*2)
# 457766523 <class 'int'> 915533046



print("_"*50)
###### string ->  float #######

# 1. if string contains characters, then string to float conversion it not possible.
# 2. If string contains numbers with pointers or without, then conversion is possible

s3 = "5656.678"
f3 = float(s3)
print(f3, type(f3), f3*10)
# 5656.678 <class 'float'> 56566.78

print("_"*50)
###### string ->  list #######
s4 = "Programming"
l4 = list(s4)
print(l4, type(l4))
# ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'] <class 'list'>

print("_"*50)
###### string ->  tuple #######
s5 = "Programming"
t5 = tuple(s5)
print(t5, type(t5))
# ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g') <class 'tuple'>


print("_"*50)
###### string ->  dict #######
# 1. If string contains only character or number, then string to dict conversion is not possible
"""
s6 = "Python Programming"
d6 = dict(s6)
print(d6)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""

# 2. If  string follows rules of the dictionary then string to dict conversion with the help
# of json module.

details = '{"Name" : "Rahul", "Age": 35, "Email": "rahul@gmail.com", "mobile": 645646574}'
print(details, type(details))
# {"Name" : "Rahul", "Age": 35, "Email": "rahul@gmail.com", "mobile": 645646574} <class 'str'>

import json
dict_data = json.loads(details)
print(dict_data, type(dict_data))
# {'Name': 'Rahul', 'Age': 35, 'Email': 'rahul@gmail.com', 'mobile': 645646574} <class 'dict'>

print(dict_data['Email'])
# rahul@gmail.com


print("_"*50)
###### string ->  set #######
s7 = "Python Programming"
set1 = set(s7)
print(set1, type(set1))
# {'i', 'P', 'o', ' ', 'g', 'n', 'h', 'm', 'y', 'r', 'a', 't'} <class 'set'>


print("_"*50)
###### string ->  boolean #######
s8 = ''
b1 = bool(s8)
print(b1, type(b1))
# False <class 'bool'>

s9 = 'Hello'
b2 = bool(s9)
print(b2, type(b2))
# True <class 'bool'>
