################################# Dictionary ####################################
from pprint import pprint

dict1 = {'a': 123, 'b': 4567}
"""
# properties:
->  Dictionary is mutable data type, we can modify the dict data.
->  Dict store in key value format with curly braces { key: value}
->  Dict store unique keys, duplicate keys are not allowed.
    if we store duplicate key, then it will only consider latest defined key.
->  Only immutable data type can be key in dict e.g. int, float, complex, string, tuple, boolean
->  Dict can contains all types of data as value and duplicate values are also allowed.
    e.g. int, float, complex, string, list, tuple, dict, set, bool.
"""

dict2 = {
    12: 456,
    3.5: 5.6,
    'Python': 'We are learning Python',
    (4, 6, 7): ('a', 'b', 'c', 'd'),
    4 + 50j: 500 + 400j,
    True: False,
    # list, dict, set as key in not allowed
    # [3, 5, 6] : [6, 7, 9, 2, 34]
    'A': [4, 6, 8, 2, 8],
    'B': {'a': 123, 'b': 567, 'c': 890},
    'C': {3, 6, 8, 3, 7, 8}
}

pprint(dict2)

print(type(dict2))
# <class 'dict'>

print("_"*50)
# get dict data with key
print(dict2['A']) # [4, 6, 8, 2, 8]
print(dict2['A'][3]) # 2
print(dict2['B']) # {'a': 123, 'b': 567, 'c': 890}
print(dict2['B']['c']) # 890
