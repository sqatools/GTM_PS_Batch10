# 1. Python program to add elements to the dictionary.
dict1 = {}
dict1['name'] = 'Aihaan'
dict1['class'] = 'lkg'
dict1['sex'] = 'male'
dict1['age'] = 6
dict1['name'] = 'Mishari'
print(dict1)

# adding diff value for same key
print(dict1)
# {'name': 'Mishari', 'class': 'lkg', 'sex': 'male', 'age': 6}

# 2. Print the square of all values in a dictionary.
dict2 = {'a': 5, 'b': 3, 'c': 6, 'd': 8}
output1 = {}
for val in dict2:
    output1 = dict2[val] ** 2
    print(output1)
print("*" * 20)
print(dict2.items())  # dict_items([('a', 5), ('b', 3), ('c', 6), ('d', 8)])

# Apply loop on dict with items method #
for data in dict2.items():
    print(data)
# ('a', 5)
# ('b', 3)
# ('c', 6)
# ('d', 8)

# 3.  Python Dictionary program to move items from dict1 to dict2.
# Input :
dict3 = {'name': 'john', 'city': 'London', 'country': 'UK'}
dict4 = {}
temp = dict3.copy()
for key in temp:
    dict4[key] = dict3.pop(key)
print(dict4)

# 4). Python Dictionary program to concatenate two dictionaries.
dict5 = {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan'}
dict6 = {'Age': 25, 'salary': '$25k'}
dict5.update(dict6)
print(dict5)

# 5. Program to get a list of odd and even keys from the dictionary
dict7 = {1: 25, 5: 'abc', 8: 'pqr', 21: 'xyz', 12: 'def', 2: 'utv'}
even_key = []
odd_key = []
for val in dict7:
    if val % 2 == 0:
        even_key.append([val, dict7[val]])
print(even_key)
for val in dict7:
    if val % 2 != 0:
        odd_key.append([val, dict7[val]])
print(odd_key)

# 6. Python Program to create a dictionary from two lists.
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
dict8 = {}
for a, b in zip(list1, list2):
    dict8[a] = b
print(dict8)

# 7. Store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
input_list = [4, 5, 6, 2, 1, 7, 11]
dict_output = {x: x ** 2 if x % 2 == 0 else x ** 3 for x in input_list}
print("output dictionary :", dict_output)

# 8. Python Dictionary program to clear all items from the dictionary.
dict9 = {'Name': 'Richard', 'Rollno': 34, 'Address': 'Japan'}
dict9.clear()
print(dict9)

# 9. Python program to remove duplicate values from Dictionary.
dict10 = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
dict11 = {}
for key, val in dict10.items():
    if val not in dict11.values():
        dict11[key] = val
print(dict11)

# 10. Python program to create a dictionary from the string.
string = "SQAToolss"
dict12 = {}
for char in string:
    dict12[char] = string.count(char)
print(dict12)

# 11. Python program to add a key in a dictionary.

dict13 = {1: 'a', 2: 'b'}

dict13.update({3: 'c'})

print(dict13)
