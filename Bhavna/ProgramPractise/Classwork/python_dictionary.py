
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

print('_'*70)

# shallow copy : in case of shallow if we modify any of the dictionary, then changes will reflect on another dict as well

dict1 = {'a':555,'b':999,'c':777}
dict2 = dict1
dict2['d'] = 111
dict1['e'] = 222

print("dict1:",dict1)
print("dict2:",dict2)

print('_'*70)

# Deep Copy

dict_x = {'a':852,'b':741,'c':963}
dict_y = dict_x.copy()
dict_y['d'] = 159

print('dict_x:',dict_x)
print('dict_y:',dict_y)

print('_'*70)

################################ dict comprehension #################################

# Get square of values in the dictionary
dict_a = {'a':2,'s':5,'d':8}

result = {k:v**2 for k,v in dict_a.items()}
print('result:',result)
# result: {'a': 4, 's': 25, 'd': 64}
print('_'*70)

# write program to get the dict where the values are even
dict_b = {'a':1,'b':2,'c':3,'d':4}
result1 = {k:v for k,v in dict_b.items() if v%2==0}
print('result1:',result1)

# result1: {'b': 2, 'd': 4}
print('_'*70)

# write program repeat the keys 2 time if value is even and repeat key three times if values are odd
dict_B = {'p': 10, 'q': 15, 'r': 8, 's': 13, 't': 20}
result2 = {(k*2) if v%2==0 else (k*3):v for k,v in dict_B.items()}
print('result2:',result2)

# result2: {'pp': 10, 'qqq': 15, 'rr': 8, 'sss': 13, 'tt': 20}
print('_'*70)

#############################################################
# write a python program to calculate the bill amount of fruit purchased

fruits_with_price = {'Apple': 20, 'Mango': 60, 'Banana': 30, 'Lichi': 50}
purchased_fruits = {'Apple': 5, 'Mango': 6, 'Banana': 12, 'Lichi': 10}
total_bill = 0

for fruit,price in fruits_with_price.items():
    pur_fruits = purchased_fruits[fruit]
    fruit_bill = pur_fruits*price
    print(fruit,"|",price,"|",fruit_bill)
    total_bill = total_bill+fruit_bill

print("Total Bill Amount:", total_bill)

print('_'*70)

# write a python program to add duplicates values from given dictionary.
dict_C = {'a': 10, 'b': 20, 'c': 30, 'd': 10, 'e': 20}


# write a python program to calculate the bill amount of fruit purchased
fruit_inventory = {'Apple': 100, 'Mango': 500, 'Banana': 300, 'Lichi': 250}
fruits_with_price = {'Apple': 20, 'Mango': 60, 'Banana': 30, 'Lichi': 50}
purchased_fruits = {'Apple': 5, 'Mango': 6, 'Banana': 12, 'Lichi': 10}

# updated_fruit_investory = {'Apple': 95, 'Mango': 494, 'Banana': 288, 'Lichi': 240}

total_bill_1 = 0
for fruits, price in fruits_with_price.items():
    pur_fruits = purchased_fruits[fruits]
    fruit_bill = pur_fruits*price
    total_bill_1 = total_bill_1+fruit_bill
    fruit_inventory[fruits] = fruit_inventory[fruits]-pur_fruits
    # updated_fruit = fruit_inventory[fruits] - pur_fruits
    # print(fruits,'|',updated_fruit)

print('total_bill:',total_bill_1)
print(fruit_inventory)

'''
Apple | 95
Mango | 494
Banana | 288
Lichi | 240
total_bill: 1320
'''

print('_'*70)

# write a python program to add duplicates values from given dictionary.
dict_C = {'a': 10, 'b': 20, 'c': 30, 'd': 10, 'e': 20, 'f': 50, 'g': 60, 'h': 50}
# output = {'ad': 20, 'be': 40, 'c': 30}

output={}
temp = ""

for k1,v1 in dict_C.items():
    for k2,v2 in dict_C.items():
        if k1 != k2 and v1 == v2 and (k1 not in temp and k2 not in temp):
            output[f"{k1}{k2}"]=v1+v2
            temp = temp + k1
            temp = temp + k2

    if k1 not in temp:
            output[k1] = v1
            temp = temp+k1

print(output)

print('_'*70)

school  = {'student': [
                           {'name': 'rahul', 'email': 'rahul@gmail.com', 'phone': 4545445},
                           {'name': 'mohit', 'email': 'mohit@gmail.com', 'phone': 6543634564},
                            {'name': 'raju', 'email': 'raju@gmail.com', 'phone': 86786765786},
                            {'name': 'Santam', 'email': 'Santam@gmail.com', 'phone': 993878778545},
                             {'name': 'amit', 'email': 'amit@gmail.com', 'phone': 454544657676},
                            {'name': 'mitesh', 'email': 'mitesh@gmail.com', 'phone': 65436634564},
                            {'name': 'nitesh', 'email': 'nitesh@gmail.com', 'phone': 867866765786},
                            {'name': 'Raghav', 'email': 'Raghav@gmaill.com', 'phone': 998786778545},

                        ],
           'teacher' : [   {'name': 'Mohan Gupta', 'email': 'mohan@gmaill.com', 'phone': 545435345},
                           {'name': 'Raghav Sharma', 'email': 'raghav@gmaill.com', 'phone': 34543543}],
           }

from pprint import pprint

print(school['student'][1]['email']) #mohit@gmail.com

# print(list(school['teacher'][0].items())[0])
print('_'*70)

name = 'Santam'
for k1,v1 in school.items():
    # print(k1,':',v1)
    for val in v1:
        # print(val)
        print("name:", val['name'])
        print("email:", val['email'])
        print("Phone:", val['phone'])