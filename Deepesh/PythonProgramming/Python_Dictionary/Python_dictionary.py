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
# write a python program to get the square of even value and cube of odd values in dict
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
