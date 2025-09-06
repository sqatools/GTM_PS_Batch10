#DATA TYPE CONVERSTION - 27/05/2025


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

# 2. If string follows rules of the dictionary then string to dict conversion with the help
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

############################## List #############################

print("_"*50)
###### list ->  int ####### conversion is not possible
###### list ->  float ####### conversion is not possible
###### list ->  complex ####### conversion is not possible


print("_"*50)
###### list ->  string #######
list1 = [5, 7, 8, 2]
str1 = str(list1)
print(str1, type(str1), str1[0], str1[1])
# [5, 7, 8, 2] <class 'str'> [ 5


print("_"*50)
###### list ->  tuple #######
list2 = [6, 8, 2, 3]
tup2 = tuple(list2)
print(tup2, type(tup2))
# (6, 8, 2, 3) <class 'tuple'>


print("_"*50)
###### list ->  dict #######
# direct conversion from list to dict is not possible

list_a = ['a', 'b', 'c']
list_b = [33, 55, 77]
output = dict(zip(list_a, list_b))
print(output, type(output))
# {'a': 33, 'b': 55, 'c': 77} <class 'dict'>


print("_"*50)
###### list ->  set #######
list3 = [6, 8, 2, 3, 6, 8, 7, 8]
set3 = set(list3)
print(set3, type(set3))
# {2, 3, 6, 7, 8} <class 'set'>


print("_"*50)
###### list ->  boolean #######
list4 = []
b1 = bool(list4)
print(b1, type(b1))
# False <class 'bool'>


list5 = [6, 8, 22]
b2= bool(list5)
print(b2, type(b2))
# True <class 'bool'>


############################### Tuple ################################

print("_"*50)
###### tuple ->  int ####### conversion is not possible
###### tuple ->  float ####### conversion is not possible
###### tuple ->  complex ####### conversion is not possible


print("_"*50)
###### tuple ->  string #######
tup1 = (5, 2, 8, 1, 3)
str1 = str(tup1)
print(str1, type(str1), str1[0], str1[-2])
# (5, 2, 8, 1, 3) <class 'str'> ( 3


print("_"*50)
###### tuple ->  list #######
tup2 = (5, 2, 8, 1, 3)
list2 = list(tup2)
print(list2, type(list2))
# [5, 2, 8, 1, 3] <class 'list'>


print("_"*50)
###### tuple ->  dict #######
# direct conversion is not possible

tup_a = ('p', 'q', 'r')
tup_b = (34, 789, 123)

output = dict(zip(tup_a, tup_b))
print(output, type(output))
# {'p': 34, 'q': 789, 'r': 123} <class 'dict'>


print("_"*50)
###### tuple ->  set #######
tup3 = (5, 7, 2, 7, 8, 5, 2, 5, 7)
set3 = set(tup3)
print(set3, type(set3))
# {8, 2, 5, 7} <class 'set'>


print("_"*50)
###### tuple ->  bool #######

tup1 = tuple()
b1 = bool(tup1)
print(b1, type(b1))
# False <class 'bool'>

tup2 = (3, 6, 8)
b2 = bool(tup2)
print(b2, type(b2))
# True <class 'bool'>



################################ dictionary ##########################
print("_"*50)
###### dict ->  int ####### conversion is not possible
###### dict ->  float ####### conversion is not possible
###### dict ->  complex ####### conversion is not possible

print("_"*50)
###### dict ->  string #######
dict1 = {'a': 567, 'b': 789}
str1 = str(dict1)
print(str1, type(str1), str1[-2], str1[2])
# {'a': 567, 'b': 789} <class 'str'> 9 a


print("_"*50)
###### dict ->  list #######
dict2 = {'a': 567, 'b': 789, 'c': 333, 'd': 673}
list2 = list(dict2)
print(list2, type(list2))
# ['a', 'b', 'c', 'd'] <class 'list'>


print("_"*50)
###### dict ->  tuple #######
dict3 = {'a': 567, 'b': 789, 'c': 333, 'd': 673}
tup3 = tuple(dict3)
print(tup3, type(tup3))
# ('a', 'b', 'c', 'd') <class 'tuple'>

print(dict3.values()) # dict_values([567, 789, 333, 673])

print("_"*50)
###### dict ->  set #######
dict3 = {'a': 567, 'b': 789, 'c': 333, 'd': 673}
set3 = set(dict3)
print(set3, type(set3))
# {'a', 'b', 'c', 'd'} <class 'set'>


print("_"*50)
###### dict ->  bool #######
dict1 = {}
b1 = bool(dict1)
print(b1, type(b1))
# False <class 'bool'>

dict_b = {'A': 'Python', 'B': 'Programming'}
b2 = bool(dict_b)
print(b2, type(b2))
# True <class 'bool'>


################################# SET ###################################

print("_"*50)
###### set ->  int ####### conversion is not possible
###### set ->  float ####### conversion is not possible
###### set ->  complex ####### conversion is not possible

print("_"*50)
###### set ->  string #######
set1 = {5, 7, 2, 7, 8}
str1= str(set1)
print(str1, type(str1), str1[-2])
# {8, 2, 5, 7} <class 'str'> 7


print("_"*50)
###### set ->  list #######
set2 = {5, 7, 2, 7, 8, 10}
list2 = list(set2)
print(list2, type(list2))
# [2, 5, 7, 8, 10] <class 'list'>


print("_"*50)
###### set ->  tuple #######
set3 = {5, 7, 2, 7, 8, 10, 12, 45}
tup3 = tuple(set3)
print(tup3, type(tup3))
# (2, 5, 7, 8, 10, 12, 45) <class 'tuple'>


print("_"*50)
###### set ->  dict ####### direct conversion is not possible

# we can create dict with set using zip function.
set_a = {'a', 'b', 'c'}
set_b = {55, 77, 23}
output = dict(zip(set_a, set_b))
print(output)
# {'b': 55, 'c': 77, 'a': 23}

print("_"*50)
###### set ->  bool #######

set1 = set()
b1 = bool(set1)
print(b1, type(b1))
# False <class 'bool'>


set2 = {5, 7, 2, 7, 9}
b2 = bool(set2)
print(b2, type(b2))
# True <class 'bool'>

####################################### Boolean #########################

print("_"*50)
###### bool ->  int #######
b1 = True
n1 = int(b1)
print(n1, type(n1))
# 1 <class 'int'>

print("_"*50)
###### bool ->  float #######
b2 = True
f2 = float(b2)
print(f2, type(f2))
# 1.0 <class 'float'>


print("_"*50)
###### bool ->  string #######
b3 = False
s3 = str(b3)
print(s3, type(s3), s3[0])
# False <class 'str'> F

print("_"*50)
###### bool ->  list ####### conversion is not possible
###### bool ->  tuple ####### conversion is not possible
###### bool ->  dict ####### conversion is not possible
###### bool ->  set ####### conversion is not possible