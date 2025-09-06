dict1 = {'a' : 123, 'b': 345, 'c': 789, 'a': 789}
print(dict1, type(dict1))
# {'a': 789, 'b': 345, 'c': 789} <class 'dict'>

print(dict1['a']) # 789

dict1['d'] = 400
print("dict1 :", dict1)
# dict1 : {'a': 789, 'b': 345, 'c': 789, 'd': 400}

print("_"*50)
#Apply loop on dict data
for val in dict1:
    print(val)

"""
a
b
c
d
"""

print("_"*50)
# items method in the dict
print(dict1.items())
# [('a', 789), ('b', 345), ('c', 789), ('d', 400)]

print("_"*50)
###### Apply loop on dict with items method #####
for data in dict1.items():
    print(data)
"""
('a', 789)
('b', 345)
('c', 789)
('d', 400)
"""

print("_"*50)
###### Apply loop on dict with items method and 2 variable #####
for k, v in dict1.items():
    print("Key :", k, "value :", v)

"""
Key : a value : 789
Key : b value : 345
Key : c value : 789
Key : d value : 400
"""

print("_"*50)
###################################
#Q1 write a python program to get the square of even value and cube of odd values in dict
dict2 = {'p': 5, 'q': 8, 'r': 11, 's': 12, 't': 7}
#output = {'p': 125, 'q': 64, 'r': 1331, 's': 144, 't': 343}
output = {}

for key, value in dict2.items():
    if value%2 ==0:
        output[key] = value**2
    else:
        output[key] = value**3


print("output :", output)
# output : {'p': 125, 'q': 64, 'r': 1331, 's': 144, 't': 343}



print("_"*50)
###################################
# write a python to get count of each character in the given string without using count method.
str1 = "Python Programming"
#output = {'P': 2, 'y':1, 't':1, 'h':1, 'o': 2, 'n': 2, ' ': 1, 'r':2, 'g': 2, 'a': 1, 'm': 2, 'i':1}
output = {}

for char in str1: # P, y, t, h, o, n, P
    if char not in output: #
        output[char] = 1
        # {'P': 1, 'y': 1, 't': 1, 'h': '1', 'o': 1, 'n': 1, ' ': 1, 'r': 1}
    else:
        output[char] += 1
        # {'P': 2, 'y': 1, 't': 1, 'h': '1', 'o': 1, 'n': 1, ' ': 1, 'r': 1}

print("output :", output)
# {'P': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}


# dict methods
########################################################
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values'

print("_"*50)
######################
# get method: This method return the value of specific key.
user1 = {'name': 'Mehul', 'password': "$$#$#$$", 'email': 'test_email@gmail.com'}

print(user1.get('email'))  # test_email@gmail.com
print(user1['email']) # test_email@gmail.com


print("_"*50)
######################
# update method : This method update the value one dict data to another dict.
dict1 = {'name': 'Mehul', 'password': "$$#$#$$", 'email': 'test_email@gmail.com'}
dict2 = {'a': 123, 'b': 456}
dict2.update(dict1)
print(dict2)


print("_"*50)
######################
# pop() method :  This method pop value of dictionary remove data from dict using key and return it.

dict3 = {'name': 'Mehul', 'password': "$$#$#$$", 'email': 'test_email@gmail.com'}
output = dict3.pop('email') # test_email@gmail.com
print(output) # test_email@gmail.com
print(dict3) # {'name': 'Mehul', 'password': '$$#$#$$'}

print("_"*50)
# write a program to move data from one dict to another.
dict4 = {'A': 567, 'B': 789, 'C': 456}
dict5 = {}
temp = dict4.copy()

for key in temp:
    dict5[key] = dict4.pop(key)

print("dict5 :", dict5)
print("dict4 :", dict4)

print("_"*50)
#######################################
# keys() and values() method: This method return list of keys and values

dict6 = {'A': 567, 'B': 789, 'C': 456}
print("list of keys :", dict6.keys()) # dict_keys(['A', 'B', 'C'])
print("list of keys :", dict6.values()) # dict_values([567, 789, 456])


print("_"*50)
#######################################
# popitems() method :  This method remove key value pair from dict and return the output as tuple of key and value.

dict7 = {'A': 567, 'B': 789, 'C': 456}
var = dict7.popitem()
print("removed value :", var) # ('C', 456)
print("updated dict7 :", dict7) # {'A': 567, 'B': 789}




print("_"*50)
#######################################
# clear() method :  clear method, clear all the data from dictionary.
dict8 = {'A': 567, 'B': 789, 'C': 456}
dict8.clear()
print("dict8 :", dict8) # dict8 : {}


print("_"*50)
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

print("_"*50)
#######################################
# fromkeys Method :  This method create a dictionary with the help of list of keys with one single value

list1 = ['P', 'Q', 'R']
output = dict.fromkeys(list1, 100)
print("output :", output) #
# {'P': 100, 'Q': 100, 'R': 100}


print("_"*50)
#######################################
# setdefault method :

dict11 = {'A': 567, 'B': 789, 'C': 456, 'E': 443}
# get existing key data :  If provide keys is already available, then it will return the value of existing key
# without any modification in the dictionary.
output = dict11.setdefault('E',  300)
print("output :", output)
# output : 443

# Get non existing key data: If the key is not available, then it will return the default value for that
# that key and update same will update to the dictionary as well

output2 = dict11.setdefault('F', 500)
print("output :", output2) # output : 500
print("dict11 :", dict11)
# {'A': 567, 'B': 789, 'C': 456, 'E': 443, 'F': 500}

print("_"*50)
#################################################################
# shallow copy : in case of shallow if we modify any of the dictionary, then changes will reflect on another dict as
# well.

dict1 = {'a': 123, 'b' : 345, 'c': 789}
dict2 = dict1
dict2['d'] = 500
dict1['e'] = 989

print('dict1 :', dict1) # {'a': 123, 'b': 345, 'c': 789, 'd': 500, 'e': 989}
print('dict2 :', dict2) #{'a': 123, 'b': 345, 'c': 789, 'd': 500, 'e': 989}


print("_"*50)
# Deep Copy

dict_x = {'p': 777, 'q': 888, 'r': 567}
dicty = dict_x.copy()
dicty['s'] = 900
print("dictx :", dict_x) # dictx : {'p': 777, 'q': 888, 'r': 567}
print("dicty :", dicty) # {'p': 777, 'q': 888, 'r': 567, 's': 900}


print("_"*50)
################################ dict comprehension #################################

# Get square of values in the dictionary
dict_A = {'p': 10, 'q': 20, 'r': 30}

result = {k: v**2 for k, v in dict_A.items()}
print("result :", result)
# {'p': 100, 'q': 400, 'r': 900}


print("_"*50)
# write program to get the dict where the values are even
dict_B = {'p': 10, 'q': 15, 'r': 8, 's': 13, 't': 20}
result2 = {k: v for k, v in dict_B.items() if v%2 == 0}
print("result2 :", result2)
# result2 : {'p': 10, 'r': 8, 't': 20}



print("_"*50)
# write program repeat the keys 2 time if value is even and repeat key three times if values are odd
dict_B = {'p': 10, 'q': 15, 'r': 8, 's': 13, 't': 20}
# output = {'pp': 10, 'qqq': 15, 'rr': 8, 'sss': 13, 'tt': 20}

#result3 = {k:v*2 if v%2 == 0 else (k:v*2) for k, v in dict_B.items() }
#print(result3)

print("_"*50)
#############################################################
# write a python program to calculate the bill amount of fruit purchased

fruits_with_price = {'Apple': 20, 'Mango': 60, 'Banana': 30, 'Lichi': 50}
purchased_fruits = {'Apple': 5, 'Mango': 6, 'Banana': 12, 'Lichi': 10}

total_bill = 0

for fruit, price in fruits_with_price.items():
    pur_fruits = purchased_fruits[fruit]
    fruit_bill = pur_fruits*price
    print(fruit, "|" ,price,"|", pur_fruits,"|", fruit_bill)
    total_bill = total_bill + fruit_bill

print("_"*20)
print("Total Bill Amount :", total_bill)



##########################################
# write a python program to add duplicates values from given dictionary.
dict_C = {'a': 10, 'b': 20, 'c': 30, 'd': 10, 'e': 20}
#output = {'ad': 20, 'be': 40, 'c': 30}
output = {}
temp = ""
# for k, v in dict_C.items():
#     for p, q in dict_C.items():



# write a python program to calculate the bill amount of fruit purchased

fruit_investory = {'Apple': 100, 'Mango': 500, 'Banana': 300, 'Lichi': 250}
fruits_with_price = {'Apple': 20, 'Mango': 60, 'Banana': 30, 'Lichi': 50}
purchased_fruits = {'Apple': 5, 'Mango': 6, 'Banana': 12, 'Lichi': 10}
# updated
# fruit_investory = {'Apple': 95, 'Mango': 494, 'Banana': 288, 'Lichi': 240}