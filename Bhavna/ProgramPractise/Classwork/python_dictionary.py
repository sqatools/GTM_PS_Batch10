
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
