dict1 = {'a': 123, 'b': 345, 'c': 789, 'a': 789}
print(dict1, type(dict1))
# {'a': 789, 'b': 345, 'c': 789} <class 'dict'>

print(dict['a'])
# dict['a']

dict1['d'] = 400
print("dict1 :", dict1)
# dict1 : {'a': 789, 'b': 345, 'c': 789, 'd': 400}


print("-"*50)
# Apply loop on dict data
for val in dict1:
    print(val)
"""
a
b
c
d
"""


print("-"*50)
# print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# items method in dict
print(dict1.items())
# dict_items([('a', 789), ('b', 345), ('c', 789), ('d', 400)])


print("-"*50)
# Apply loop on dict with items method #####
for data in dict1.items():
    print(data)
"""
('a', 789)
('b', 345)
('c', 789)
('d', 400)
"""


print("-"*50)
# Apply loop on dict with items method and 2 variable #####
for k, v in dict1.items():
    print("key :", k, "value :", v)
"""
key : a value : 789
key : b value : 345
key : c value : 789
key : d value : 400
"""


print("-"*50)
# write a python program to get the square of even value and cube of odd values in dict
dict2 = {'p': 5, 'q': 8, 'r': 11, 's': 12, 't': 7}
# output = {'p': 125, 'q': 64, 'r': 1331, 's': 144, 't': 343}
output = {}
for key, value in dict2.items():
    if value % 2 == 0:
        output[key] = value**2
    else:
        output[key] = value**3
print("Output :", output)
# Output : {'p': 125, 'q': 64, 'r': 1331, 's': 144, 't': 343}


print("-"*50)
# write a python to get count of each character in the given string without using count method.
str1 = "Python Programming"
# output = {'P': 2, 'y':1, 't':1, 'h':1, 'o': 2, 'n': 2, ' ': 1, 'r':2, 'g': 2, 'a': 1, 'm': 2, 'i':1}

output = {}
for char in str1:
    if char not in output:
        output[char] = 1
    else:
        output[char] += 1
print("Output :", output)
# Output : {'P': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}


print("-"*50)
# Dictionary Methods ###################

# get method: This method return the value of specific key.
user1 = {'name': 'Mehul', 'password': "$$#$#$$", 'email': 'test_email@gmail.com'}
print(user1.get('email'))
# test_email@gmail.com

print(user1['email'])
# test_email@gmail.com


print("-"*50)
# update method : This method update the value from one dict data to another dict.
dict1 = {'name': 'Mehul', 'password': "$$#$#$$", 'email': 'test_email@gmail.com'}
dict2 = {'a': 123, 'b': 456}
dict2.update(dict1)
print("dict2 :", dict2)
# dict2 : {'a': 123, 'b': 456, 'name': 'Mehul', 'password': '$$#$#$$', 'email': 'test_email@gmail.com'}
print("dict1 :", dict1)
# dict1 : {'name': 'Mehul', 'password': '$$#$#$$', 'email': 'test_email@gmail.com'}


print("-"*50)
# pop() method :  This method pop value of dictionary remove data from dict using key and return it.

dict3 = {'name': 'Mehul', 'password': "$$#$#$$", 'email': 'test_email@gmail.com'}
output3 = dict3.pop('email')
print("Output :", output3)
# Output : test_email@gmail.com
print("dict3 :", dict3)
# dict3 : {'name': 'Mehul', 'password': '$$#$#$$'}


print("-"*50)
# write a program to move data from one dict to another.
dict4 = {'A': 567, 'B': 789, 'C': 456}
dict5 = {}

temp = dict4.copy()
for key in temp:
    dict5[key] = dict4.pop(key)
print("dict5 :", dict5)
# dict5 : {'A': 567, 'B': 789, 'C': 456}
print("dict4 :", dict4)
# dict4 : {}


print("-"*50)
# keys() and values() method: This method return list of keys and values

dict6 = {'A': 567, 'B': 789, 'C': 456}

print("List of keys :", dict6.keys())
# List of keys : dict_keys(['A', 'B', 'C'])
print("List of values :", dict6.values())
# List of values : dict_values([567, 789, 456])


print("-"*50)
# popitems() method :  This method remove key value pair from dict and return the output as tuple of key and value.

dict7 = {'A': 567, 'B': 789, 'C': 456}
var = dict7.popitem()
print("Removed value :", var)
# Removed value : ('C', 456)
print("Updated Dict :", dict7)
# Updated Dict : {'A': 567, 'B': 789}


print("-"*50)
# clear() method :  clear method, clear all the data from dictionary.
dict8 = {'A': 567, 'B': 789, 'C': 456}
dict8.clear()
print("dict8 :", dict8)
# dict8 : {}


print("-"*50)
# del keyword:  this will remove entire dict variable from the memory

dict9 = {'A': 567, 'B': 789, 'C': 456}
del dict9
# print(dict9)
# NameError: name 'dict9' is not defined

dict10 = {'A': 567, 'B': 789, 'C': 456, 'D': 777, 'E': 443}
del dict10['D']
print("dict10 :", dict10)
# dict10 : {'A': 567, 'B': 789, 'C': 456, 'E': 443}


print("-"*50)
# fromkeys Method :  This method create a dictionary with the help of list of keys with one single value

list1 = ['P', 'Q', 'R']
output = dict.fromkeys(list1, 100)
print("Output :", output)
# Output : {'P': 100, 'Q': 100, 'R': 100}


print("-"*50)
# setdefault method :


dict11 = {'A': 567, 'B': 789, 'C': 456, 'E': 443}
# get existing key data : If provide keys is already available, then it will return the value of existing key
# without any modification in the dictionary.

output = dict11.setdefault('E', 300)
print("Output :", output)
# Output : 443


# Get non-existing key data: If the key is not available, then it will return the default value for that
# key and update same will update to the dictionary as well

output = dict11.setdefault('F', 500)
print("Output :", output)
# Output : 500
print("dict11 :", dict11)
# dict11 : {'A': 567, 'B': 789, 'C': 456, 'E': 443, 'F': 500}


print("-"*50)
# shallow copy : in case of shallow if we modify any of the dictionary, then changes will reflect on another dict as
# well.

dict1 = {'a': 123, 'b' : 345, 'c': 789}
dict2 = dict1
dict2['d'] = 225
dict1['e'] = 335
print("dict2 :", dict2)
# dict2 : {'a': 123, 'b': 345, 'c': 789, 'd': 225, 'e': 335}
print("dict1 :", dict1)
# dict1 : {'a': 123, 'b': 345, 'c': 789, 'd': 225, 'e': 335}


print("-"*50)
# Deep Copy

dict_x = {'p': 777, 'q': 888, 'r': 567}
dict_y = dict_x.copy()
dict_y['s'] = 900
print("dict_y :", dict_y)
# dict_y : {'p': 777, 'q': 888, 'r': 567, 's': 900}
print("dict_x :", dict_x)
# dict_x : {'p': 777, 'q': 888, 'r': 567}


print("-"*50)
# dict comprehension #################################

# Get square of values in the dictionary
dict_A = {'p': 10, 'q': 20, 'r': 30}
result = {k: v**2 for k, v in dict_A.items()}
print("Result :", result)
# Result : {'p': 100, 'q': 400, 'r': 900}


print("-"*50)
# write program to get the dict where the values are even
dict_B = {'p': 10, 'q': 15, 'r': 8, 's': 13, 't': 20}
result2 = {k: v for k, v in dict_B.items() if v % 2 ==0}
print("Result :", result2)
# Result : {'p': 10, 'r': 8, 't': 20}


print("-"*50)
# write program repeat the keys 2 time if value is even and repeat key three times if values are odd
dict_C = {'p': 10, 'q': 15, 'r': 8, 's': 13, 't': 20}
# output = {'pp': 10, 'qqq': 15, 'rr': 8, 'sss': 13, 'tt': 20}
# result3 = {if v % 2 == 0 (k*2: v) for k, v in dict_C.items() else (k*3)}


print("_"*50)
# write a python program to calculate the bill amount of fruit purchased

fruits_with_price = {'Apple': 20, 'Mango': 60, 'Banana': 30, 'Lichi': 50}
purchased_fruits = {'Apple': 5, 'Mango': 6, 'Banana': 12, 'Lichi': 10}

Total_bill = 0
for fruit, price in fruits_with_price.items():
    pur_fruits = purchased_fruits[fruit]
    fruit_bill= pur_fruits*price
    print(fruit, "|", price, "|", pur_fruits, "|", fruit_bill)
    Total_bill = Total_bill + fruit_bill
print("Total bill :", Total_bill)


print("_"*50)
# write a python program to add duplicates values from given dictionary.
dict_C = {'a': 10, 'b': 20, 'c': 30, 'd': 10, 'e': 20, 'f': 50, 'g': 60, 'h': 50}
# output = {'ad': 20, 'be': 40, 'c': 30}
output = {}
temp = ""
for k1, v1 in dict_C.items():
    for k2, v2 in dict_C.items():
        if k1 != k2 and v1 == v2 and (k1 not in temp and k2 not in temp):
            output[f"{k1}{k2}"] = v1 + v2
            temp = temp + k1
            temp = temp + k2
    if k1 not in temp:
        output[k1] = v1
        temp = temp + k1
print("Output :", output)
# Output : {'ad': 20, 'be': 40, 'c': 30, 'fh': 100, 'g': 60}


print("_"*50)
school = {'student': [
                       {'name': 'rahul', 'email': 'rahul@gmail.com', 'phone': 4545445},
                       {'name': 'mohit', 'email': 'mohit@gmail.com', 'phone': 6543634564},
                       {'name': 'raju', 'email': 'raju@gmail.com', 'phone': 86786765786},
                       {'name': 'Rohan', 'email': 'Santam@gmail.com', 'phone': 993878778545},
                       {'name': 'amit', 'email': 'amit@gmail.com', 'phone': 454544657676},
                       {'name': 'mitesh', 'email': 'mitesh@gmail.com', 'phone': 65436634564},
                       {'name': 'nitesh', 'email': 'nitesh@gmail.com', 'phone': 867866765786},
                       {'name': 'Raghav', 'email': 'Raghav@gmaill.com', 'phone': 998786778545},
                        ],
           'teacher': [{'name': 'Mohan Gupta', 'email': 'mohan@gmaill.com', 'phone': 545435345},
                       {'name': 'Raghav Sharma', 'email': 'raghav@gmaill.com', 'phone': 34543543}],
           }

print(school['student'][1]['email'])
# mohit@gmail.com
print(list(school['teacher'][0].items())[0])
# ('name', 'Mohan Gupta')

print("-"*50)
name = 'Raghav'
for k1, v1 in school.items():
    for val in v1:
        if val['name'] == name:
            print("Name :", val['name'])
            print("Email :", val['email'])
            print("Phone :", val['phone'])
