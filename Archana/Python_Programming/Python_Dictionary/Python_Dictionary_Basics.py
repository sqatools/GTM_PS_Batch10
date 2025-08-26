# 1. Write a program to count the number of characters repeated in a sentence

str1 = "Welcome to Python Coding"
output1 = {}
for char in str1:
    if char not in output1:
        output1[char] = 1
    else:
        output1[char] += 1
print(output1)

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values'

# 1. get method : This method return the value of specific key.
dict1 = {'name': 'Akshaya', 'age': 34, 'sex': 'female', 'email': 'user1`gmail.com'}
dict2 = {'dept': 'csc', 'batch': 2004}
print(dict1.get('sex'))
print(dict1.get('name'))

# 2. update method:This method update the value one dict data to another dict.
dict1.update(dict2)
print(dict1)

# 3. pop method:This method pop value of dictionary remove data from dict using key and return it.
dict3 = {'name': 'Akshaya', 'age': 34, 'sex': 'female', 'email': 'user1`gmail.com'}
output = dict3.pop('age')
print(output)  # age
print(dict3)

print("_" * 50)
# 4. Pop Method: move data from one dict to another
dict4 = {'name': 'Akshaya', 'age': 34, 'sex': 'female', 'email': 'user1@gmail.com'}
dict5 = {}
temp = dict4.copy()
for key in temp:
    dict5[key] = dict4.pop(key)
print(dict5)
print("dict4", dict4)

print("_" * 50)
# 5. popitem method:This method remove key value pair from dict and return the output as tuple of key and value.
dict4 = {'name': 'Akshaya', 'age': 34, 'sex': 'female', 'email': 'user1@gmail.com'}
print("dict4 before popitem :", dict4)
rem_val = dict4.popitem()
print("removed item", rem_val)
print("dict4 after popitem :", dict4)

# 6. keys() and values() method: This method return list of keys and values
dict6 = {'A': 567, 'B': 789, 'C': 456}
print("list of keys :", dict6.keys())  # dict_keys(['A', 'B', 'C'])
print("list of keys :", dict6.values())  # dict_values([567, 789, 456])

print("_" * 50)
#######################################
# clear() method :  clear method, clear all the data from dictionary.
dict8 = {'A': 567, 'B': 789, 'C': 456}
dict8.clear()
print("dict8 :", dict8)  # dict8 : {}

print("_" * 50)
#######################################
# del keyword:  this will remove entire dict variable from the memory

dict9 = {'A': 567, 'B': 789, 'C': 456}
del dict9
# print(dict9)
# NameError: name 'dict9' is not defined

dict10 = {'A': 567, 'B': 789, 'C': 456, 'D': 777, 'E': 443}
del dict10['D']
print("dict10 :", dict10)
# dict10 : {'A': 567, 'B': 789, 'C': 456, 'E': 443}

print("_" * 50)
#######################################
# fromkeys Method :  This method create a dictionary with the help of list of keys with one single value

list1 = ['P', 'Q', 'R']
output = dict.fromkeys(list1, 100)
print("output :", output)  #
# {'P': 100, 'Q': 100, 'R': 100}


print("_" * 50)
#######################################
# setdefault method :

dict11 = {'A': 567, 'B': 789, 'C': 456, 'E': 443}
# get existing key data :  If provide keys is already available, then it will return the value of existing key
# without any modification in the dictionary.
output = dict11.setdefault('E', 300)
print("output :", output)
# output : 443

# Get non-existing key data: If the key is not available, then it will return the default value for that
# that key and update same will update to the dictionary as well

output2 = dict11.setdefault('F', 500)
print("output :", output2)  # output : 500
print("dict11 :", dict11)
# {'A': 567, 'B': 789, 'C': 456, 'E': 443, 'F': 500}
