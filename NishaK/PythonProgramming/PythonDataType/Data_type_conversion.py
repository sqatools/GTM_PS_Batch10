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

# 1. Integer
# Int to Float

n1 = 1234
f1 = float(n1)
print(f1, type(f1))
# 1234.0 <class 'float'>


print("-"*20)
# Int to String
n2 = 245
str1 = str(n2)
print(str1, type(str1), str1[1])
# 245 <class 'str'> 4


print("-"*20)
# Int to List : Conversion is not possible
# Int to Tuple : Conversion is not possible
# Int to Set : Conversion is not possible
# Int to Dict : Conversion is not possible

# Int to Boolean
a = 0
b1 = bool(a)
print("b1 :", b1, type(b1))
# b1 : False <class 'bool'>

c = 500
b2 = bool(c)
print("b2 :", b2, type(b2))
# b2 : True <class 'bool'>


print("-"*50)
# 2. Float

# Float to Int
f1 = 100.100
n1 = int(f1)
print("n1 :", n1, type(n1))
# n1 : 100 <class 'int'>


print("-"*20)
# Float to String
f2 = 205.5
str1 = str(f2)
print("str 1 :", str1, type(str1))
# str 1 : 205.5 <class 'str'>


print("-"*20)
# Float to List : Conversion is not possible
# Float to Tuple : Conversion is not possible
# Float to Set : Conversion is not possible
# Float to Dict : Conversion is not possible


# Float to Boolean
f1 = 0.0
b1 = bool(f1)
print("b1 :", b1, type(b1))
# b1 : False <class 'bool'>

f2 = 500.0
b2 = bool(f2)
print("b2 :", b2, type(b2))
# b2 : True <class 'bool'>


print("-"*50)
# 3. String

# String to Int
# 1. if string contains characters, then string to int conversion it not possible.
"""
s1 = 'Python'
p1 = int(s1)
print(p1, type(p1))
# ValueError: invalid literal for int() with base 10: 'Python
"""

# 2. If string contains only numbers without any space, then conversion is possible

s2 = '424242'
p2 = int(s2)
print("p2 :", p2, type(p2))
# p2 : 424242 <class 'int'>

print("-"*20)
# String to Float

# 1. if string contains characters, then string to float conversion it not possible.
# 2. If string contains numbers with pointers or without, then conversion is possible

s3 = '10.2'
f3 = float(s3)
print("f3 :", f3, type(f3), f3*10)
# f3 : 10.2 <class 'float'> 102.0


print("-"*20)
# String to List

s4 = 'Programming'
l1 = list(s4)
print("List :", l1, type(l1))
# List : ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'] <class 'list'>


print("-"*20)
# String to Tuple
s5 = 'Hello'
t1 = tuple(s5)
print("Tuple :", t1, type(t1))
# Tuple : ('H', 'e', 'l', 'l', 'o') <class 'tuple'>


print("-"*20)
# String to Dict
# . If string contains only character or number, then string to dict conversion is not possible
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


print("-"*20)
# String to Set
s7 = 'Python Programming'
set1 = set(s7)
print("set1 :", set1, type(set1))
# set1 : {'g', 'r', 'o', 'a', 'i', ' ', 'n', 'h', 'm', 'y', 'P', 't'} <class 'set'>


print("-"*20)
# String to Boolean
s8 = ''
b1 = bool(s8)
print("b1 :", b1, type(b1))
# b1 : False <class 'bool'>

s9 = 'Hey'
b2 = bool(s9)
print("b2 :", b2, type(b2))
# b2 : True <class 'bool'>


print("-"*50)
# 4. List

# List to Int : Conversion is not possible
# List to Float : Conversion is not possible
# List to complex : Conversion is not possible

# List to String
List1 = [1, 2, 3, 4, 5]
str1 = str(List1)
print("Str1 :", str1, type(str1))
# Str1 : [1, 2, 3, 4, 5] <class 'str'>


print("-"*20)
# List to Tuple

List2 = [6, 7, 8, 9, 10]
tup2 = tuple(List2)
print("Tuple :", tup2, type(tup2))
# Tuple : (6, 7, 8, 9, 10) <class 'tuple'>


print("-"*20)
# List to Dict

# direct conversion from list to dict is not possible

list_a = ['a', 'b', 'c']
list_b = [33, 55, 77]
output = dict(zip(list_a, list_b))
print("Dict :", output, type(output))
# Dict : {'a': 33, 'b': 55, 'c': 77} <class 'dict'>


print("-"*20)
# List to Set

List3 = [10, 20, 30, 40, 50]
set3 = set(List3)
print("Set :", set3, type(set3))
# Set : {40, 10, 50, 20, 30} <class 'set'>


print("-"*20)
# List to Boolean

List4 = []
b1 = bool(List4)
print("b1 :", b1, type(b1))
# b1 : False <class 'bool'>

List5 = [10, 20, 30, 40, 50]
b2 = bool(List5)
print("b2 :", b2, type(b2))
# b2 : True <class 'bool'>


print("-"*50)
# 5. Tuple

# Tuple to Int : Conversion is not possible
# Tuple to Float : Conversion is not possible
# Tuple to Complex : Conversion is not possible


# Tuple to String
t1 = (1, 2, 3)
s1 = str(t1)
print("Str :", s1, type(s1), s1[0], s1[-2])
# Str : (1, 2, 3) <class 'str'> ( 3


print("-"*20)
# Tuple to List
t2 = (10, 12, 14)
l2 = list(t2)
print("List :", l2, type(l2))
# List : [10, 12, 14] <class 'list'>


print("-"*20)
# Tuple to Dict

# direct conversion is not possible
tup_a = ('p', 'q', 'r')
tup_b = (34, 789, 123)

output = dict(zip(tup_a, tup_b))
print("Dict :", output, type(output))
# Dict : {'p': 34, 'q': 789, 'r': 123} <class 'dict'>


print("-"*20)
# Tuple to Set

t3 = (1, 2, 3, 4, 5, 6, 7)
s3 = set(t3)
print("Set :", s3, type(s3))
# Set : {1, 2, 3, 4, 5, 6, 7} <class 'set'>


print("-"*20)
# Tuple to Boolean

tup1 = tuple()
b1 = bool(tup1)
print(b1, type(b1))
# False <class 'bool'>

tup2 = (3, 6, 8)
b2 = bool(tup2)
print(b2, type(b2))
# True <class 'bool'>


print("-"*50)
# 6. Dictionary

# Dict to Int : Conversion is not possible
# Dict to Float : Conversion is not possible
# Dict to Complex : Conversion is not possible


# Dict to String
dict1 = {'a': 101, 'b': 102}
str1 = str(dict1)
print("Str1 :", str1, type(str1), str1[4], str1[-2])
# Str1 : {'a': 101, 'b': 102} <class 'str'> : 2


print("-"*20)
# Dict to List
dict2 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
l2 = list(dict2)
print("List :", l2, type(l2))
# List : ['a', 'b', 'c', 'd'] <class 'list'>


print("-"*20)
# Dict to Tuple
dict3 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
t3 = tuple(dict3)
print("Tuple :", t3, type(t3))
# Tuple : ('a', 'b', 'c', 'd') <class 'tuple'>


print("-"*20)
# Dict to Set
dict4 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
s4 = set(dict4)
print("Set :", s4, type(s4))
# Set : {'a', 'd', 'b', 'c'} <class 'set'>

print(dict4.values())
# dict_values([100, 200, 300, 400])


print("-"*20)
# Dict to Boolean

dict1 = {}
b1 = bool(dict1)
print(b1, type(b1))
# False <class 'bool'>

dict_b = {'A': 'Python', 'B': 'Programming'}
b2 = bool(dict_b)
print(b2, type(b2))
# True <class 'bool'>


print("-"*50)
# 7. Set

# Set to Int : Conversion is not possible
# Set to Float : Conversion is not possible
# Set to Complex : Conversion is not possible


# Set to String

Set1 = {1, 2, 4, 5, 6, 7}
str1 = str(Set1)
print("String :", str1, type(str1), str1[4])
# String : {1, 2, 4, 5, 6, 7} <class 'str'> 2


print("-"*20)
# Set to List
set2 = {0, 2, 4, 6, 8}
list1 = list(set2)
print("List :", list1, type(list1))
# List : [0, 2, 4, 6, 8] <class 'list'>


print("-"*20)
# Set to Tuple
set3 = {1, 3, 5, 7, 9}
Tup3 = tuple(set3)
print("Tuple :", Tup3, type(Tup3))
# Tuple : (1, 3, 5, 7, 9) <class 'tuple'>


print("-"*20)
# Set to Dict

# Direct conversion is not possible we can create dict with set using zip function.

set_a = {'a', 'b', 'c'}
set_b = {55, 77, 23}
output = dict(zip(set_a, set_b))
print("Dict :", output, type(output))
# Dict : {'b': 55, 'c': 77, 'a': 23} <class 'dict'>


print("-"*20)
# Set to Boolean

set1 = set()
b1 = bool(set1)
print(b1, type(b1))
# False <class 'bool'>


set2 = {5, 7, 2, 7, 9}
b2 = bool(set2)
print(b2, type(b2))
# True <class 'bool'>


print("-"*50)
# 8.Boolean

# Bool to Int

b1 = True
n1 = int(b1)
print("Int :", n1, type(n1))
# Int : 1 <class 'int'>


print("-"*20)
# Bool to Float

b2 = False
f2 = float(b2)
print("Float :", f2, type(f2))
# Float : 0.0 <class 'float'>


print("-"*20)
# Bool to String

b3 = True
s3 = str(b3)
print("String :", s3, type(s3), s3[3])
# String : True <class 'str'> e


# Bool to List : Conversion is not possible
# Bool to Tuple : Conversion is not possible
# Bool to Dict : Conversion is not possible
# Bool to Set : Conversion is not possible