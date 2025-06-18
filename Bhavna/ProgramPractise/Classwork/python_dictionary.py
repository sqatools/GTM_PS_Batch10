
# 16/06/2025 Session
# PYTHON DICTIONARY

dict = {'a':'741','b':'852','c':'963','b':'741'}
print(dict,type(dict))
# {'a': '741', 'b': '741', 'c': '963'} <class 'dict'>

print(dict['b'])    #741

dict['d'] = 900
print("dict:",dict)
#dict: {'a': '741', 'b': '741', 'c': '963', 'd': 900}

print('_'*70)

#Apply loop on dict data

for val in dict:
    print(val)

'''
a
b
c
c
'''

print('_'*70)

# items method in the dict
print(dict.items())
# dict_items([('a', '741'), ('b', '741'), ('c', '963'), ('d', 900)])

print('_'*70)

###### Apply loop on dict with items method #####

for data in dict.items():
    print(data)

print('_'*70)

###### Apply loop on dict with items method and 2 variable #####

for k, v in dict.items():
    print("key:",k,"value:",v)

'''
key: a value: 741
key: b value: 741
key: c value: 963
key: d value: 900
'''
print('_'*70)

# write a python program to get the square of even value and cube of odd values in dict
dict1 = {'a': 2,'b':3,'c':4,'d':5,'e':6}
output = {}

for key, value in dict1.items():
    if value%2 == 0:
        output[key] = value**2
    else:
        output[key] = value**3
print("output:",output)

# output: {'a': 4, 'b': 27, 'c': 16, 'd': 125, 'e': 36}

print('_'*70)
#################################################
# 17/06/2025 Session

# write a python program to get count of each character in the given string without using count method.
str_z = "Good Morning"

output = {}

for char in str_z:
    if char not in output:
        output[char]=1
    else:
        output[char] +=1

print("output:",output)
# output: {'G': 1, 'o': 3, 'd': 1, ' ': 1, 'M': 1, 'r': 1, 'n': 2, 'i': 1, 'g': 1}

print('_'*70)
############### Dictionary Methods ############

print(dir(dict))

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values'

print('_'*70)

#######################################
# get method: This method return the value of specific key.

dict_1 = {'name':'Ananya','Password':'##@@**','email':'ananya@gmail.com','mobile':'7878787878'}
print(dict_1.get('Password')) # ##@@**
print(dict_1['name']) # Ananya

print('_'*70)

# update method : This method update the value from one dictonary data to another dict.

dict_1 = {'name':'Ananya','Password':'##@@**','email':'ananya@gmail.com','mobile':'7878787878'}
dict_2 = {'gender':'female', 'age':'20'}

dict_1.update(dict_2)
print(dict_1)
#{'name': 'Ananya', 'Password': '##@@**', 'email': 'ananya@gmail.com', 'mobile': '7878787878', 'gender': 'female', 'age': '20'}

print('_'*70)

# pop() method :  This pop method  remove data from dictionary using key and return it.

dict_1 = {'name':'Ananya','Password':'##@@**','email':'ananya@gmail.com','mobile':'7878787878'}
output = dict_1.pop('Password')
print(output) # ##@@**
print(dict_1) # {'name': 'Ananya', 'email': 'ananya@gmail.com', 'mobile': '7878787878'}

print('_'*70)

# write a program to move data from one dict to another.

dict_3 = {'a':'123','b':'456','c':'789'}
dict_4 = {}

temp = dict_3.copy()

for key in temp:
    dict_4[key] = dict_3.pop(key)

print("dict_4:",dict_4)
print("dict_3:",dict_3)

print('_'*70)

#######################################
# keys() and values() method: This method return list of keys and values

dict_5 = {'a':'123','b':'456','c':'789'}

print("List of keys:",dict_5.keys()) # List of keys: dict_keys(['a', 'b', 'c'])
print("List of Values:",dict_5.values()) # List of Values: dict_values(['123', '456', '789'])

print('_'*70)

# popitems() method :  This method remove last key value pair from dict and return the output as tuple of key and value.

dict_6 = {'a':'123','b':'456','c':'789'}
output = dict_6.popitem()
print("Output:",output) # Output: ('c', '789')
print("Updated Dictionary:",dict_6) # Updated Dictionary: {'a': '123', 'b': '456'}

print('_'*70)

# clear() method :  clear method, clear all the data from dictionary.
dict_7 = {'a':'123','b':'456','c':'789'}
dict_7.clear()
print(dict_7)

print('_'*70)

# del keyword:  this method will remove entire dict variable from the memory
dict_8 = {'a':'123','b':'456','c':'789'}
del dict_8
# print(dict_8)
# NameError: name 'dict_8' is not defined. Did you mean: 'dict_1'?

dict_9 = {'a':'123','b':'456','c':'789'}
del dict_9['a']
print(dict_9) # {'b': '456', 'c': '789'}

print('_'*70)

# fromkeys Method :  This method create a dictionary with the help of list of keys with one single value

list = ['q','r','t','y']
output = dict.fromkeys(list,50)
print(output)
# {'q': 50, 'r': 50, 't': 50, 'y': 50}

print('_'*70)

# setdefault method :
dict10 = {'A': 567, 'B': 789, 'C': 456, 'E': 443}
# get existing key data :  If provide keys is already available, then it will return the value of existing key
# without any modification in the dictionary.

output = dict10.setdefault('A',250)
print("Output:",output)
# Output: 567

# Get non existing key data: If the key is not available, then it will return the default value for that
# key and same will update to the dictionary as well

output1 = dict10.setdefault('D',300)
print("Output:",output1) #Output: 300
print('dict10:',dict10) # dict10: {'A': 567, 'B': 789, 'C': 456, 'E': 443, 'D': 300}



































# dict4 = {'A':567,'B':789,'C':456}
# dict5 = {}
# # output = dict4.copy()
# # for i in dict4:
# #     out = dict4.pop(i)
# #     dict5[i] = out
# # for i in output:
# #     a = dict4.pop(i)
# #     dict5[i] = a
#
# # print(dict5)
# # print(dict4)
#
# print('_'*70)
# # dict4 = {'A':567,'B':789,'C':456}
# # dict5 = {}
# # temp = dict4.copy()
# #
# # for i in temp:
# #     dict5[i] = dict4.pop(i)
# #
# # print(dict5)
# # print(dict4)
#
# dict4 = {'A':567,'B':789,'C':456}
# a = dict4.popitem()
# print(a)
# b = dict4.popitem()
# print(b)