"""dict1 = {'A': 567, 'B': 789,'C': 456}
dict2 = {}
temp = dict1.copy
for val in temp:
    v1 = dict1.pop(val)
    dict2[val] = v1
print("dictionary", dict1)
print("dictionary", dict2)
# 1). Python Dictionary program to add elements to the dictionary.
dictionary = {}
dictionary["Name"] = "Prasanna"
dictionary["age"] = "35"
print(dictionary)

# 2) Python Dictionary program to print the square of all values in a dictionary.
dictionary1 = {"a": 5, "b": 3, "c": 6, "d" : 8}
for val in dictionary1:
    print(val, ":", dictionary1[val]**2)

#3) Python Dictionary program to move items from dict1 to dict2.
dict1 = {"name":"john","city": "Landon", "country": "UK"}
dict2 = {}
temp = dict1.copy()
# dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
for val in temp:
    val = dict1.pop(val)
    dict2[val] = val
print("Dictionary 2:", dict2)
print("Dictionary 1:", dict1)

# Q1 write a python program to get the square of even value and cube of odd values in dict
dict3 = {'p': 5, 'q': 8, 'r': 11, 's': 12, 't': 7}
# output = {'p': 125, 'q': 64, 'r': 1331, 's': 144, 't': 343}
output = {}
for key, value in dict3.items():
    if value % 2 == 0:
        output[key] = value**2
    else:
        output[key] = value**3

print("output:", output)

print("_"*50)
################
# write a python to get count of each character in the given string without using count method.
str1 = "Python Programming"
# #output = {'P': 2, 'y':1, 't':1, 'h':1, 'o': 2, 'n': 2, ' ': 1, 'r':2, 'g': 2, 'a': 1, 'm': 2, 'i':1}
output = {}

for char in str1:
    if char not in output:
        output[char] = 1
    else:
        output[char] += 1
print("output",output)

# dict methods
########################################################
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values'
"""
# update method : This method update the value one dict data to another dict.
dict1 = {'name': 'Mehul', 'password': "$$#$#$$", 'email': 'test_email@gmail.com'}
dict2 = {'a': 123, 'b': 456, 'c': 567}
dict2.update(dict1)
print(dict2)

# shallow copy : in case of shallow if we modify any of the dictionary, then changes will reflect on another dict as
# well.

dict1 = {'a': 123, 'b' : 345, 'c': 789}
dict2 = dict1
dict2['d'] = 500
dict1['e'] = 989
print(dict1)
print(dict2)


# Deep Copy
dict_x = {'p': 333, 'q': 999, 'r': 587}
dict_y = dict_x.copy()
dict_y['s'] = 546
print("dict_x:", dict_x)
print("dict_y:", dict_y)

# Get square of values in the dictionary
dict_A = {'p': 10, 'q': 20, 'r': 30}
result = {k: v**2 for k, v in dict_A.items()}
print(result)
"""for key, values in dict_A.items():
    dict_A[key] = values **2
print(dict_A)"""

print("_"*50)
# write program to get the dict where the values are even
dict_B = {'p': 10, 'q': 15, 'r': 8, 's': 13, 't': 20}
result ={k : v for k , v in dict_B.items() if v%2==0 }
print("result:",result)

print("_"*50)
# write program repeat the keys 2 time if value is even and repeat key three times if values are odd
#dict_B = {'p': 10, 'q': 15, 'r': 8, 's': 13, 't': 20}
# result = {k: k}

print("_"*50)
#############################################################
# write a python program to calculate the bill amount of fruit purchased

fruits_with_price = {'Apple': 20, 'Mango': 60, 'Banana': 30, 'Lichi': 50}
purchased_fruits = {'Apple': 5, 'Mango': 6, 'Banana': 12, 'Lichi': 10}

total_bill = 0
for fruit,price in fruits_with_price.items():
    pur_fruits = purchased_fruits[fruit]
    fruit_bill = pur_fruits*price
    print(fruit, "|", price, "|", pur_fruits, "|", fruit_bill)
    total_bill = total_bill + fruit_bill
print("total Bill :", total_bill)

##########################################
""" write a python program to add duplicates values from given dictionary.
dict_C = {'a': 10, 'b': 20, 'c': 30, 'd': 10, 'e': 20}
# output = {'ad': 20, 'be': 40, 'c': 30}
output = {}
temp = ""
for k,v in dict_C.items():
    for p , q in dict_C()
"""
# Python Dictinary Practicing Programs######
# Q4)  Python Dictionary program to concatenate two dictionaries.
dict_1 = {"Name": "Harry", "Rollno": 345, "Address": "Jordan"}
dict_2 = {"Age": 25, "salary": "$25k"}
dict_1.update(dict_2)
print(dict_1)
# Q5) Python Dictionary program to get a list of odd and even keys from the dictionary.
Input = {1: 25, 5:"abc", 8:"pqr", 21:"xyz", 12:"def", 2:"utv"}

# Output :
# Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
# Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
list1 = [[val, Input[val]] for val in Input if val%2 == 0]
list2 = [[val, Input[val]] for val in Input if val%2 != 0]
print("Even Key:",list1)
print("Odd Keys:",list2)

