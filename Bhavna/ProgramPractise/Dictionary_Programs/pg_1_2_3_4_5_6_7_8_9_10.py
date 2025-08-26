# Dictionary Practice Programs

# 1). Python Dictionary program to add elements to the dictionary.

dict = {}
dict['name'] = 'Kiaan'
dict['email'] = 'kiaan@gmail.com'
dict['monile'] = 8989898989
dict['ID'] = 1423
print(dict)

print('_'*70)

# 2). Python Dictionary program to print the square of all values in a dictionary.

Input = {'a': 5, 'b':3, 'c': 6, 'd' : 8}
output = {}
for k, v in Input.items():
    output[k] = v**2

print(output)

print('_'*70)

# 3). Python Dictionary program to move items from dict1 to dict2.

dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}

temp = dict1.copy()

for i in temp:
    dict2[i] = dict1.pop(i)

print("dict1:",dict1)
print("dict2:",dict2)

print('_'*70)

# 4). Python Dictionary program to concatenate two dictionaries.
dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age' : 25, 'salary': '$25k'}

dict1.update(dict2)
print("Output:",dict1)

print('_'*70)

# 5). Python Dictionary program to get a list of odd and even keys from the dictionary.
dict = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
Even_Key =[]
Odd_Key = []

for k in dict:
    if k%2==0:
        Even_Key.append([k,dict[k]])
    else:
        Odd_Key.append([k,dict[k]])

print("Even_Key:",Even_Key)
print("Odd_Key:",Odd_Key)

print('_'*70)

# 6). Python Dictionary Program to create a dictionary from two lists.

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]

output = {}

for i,j in zip(list1,list2):
    output[i]=j
print("Output:",output)

print('_'*70)

# 7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.

list = [4, 5, 6, 2, 1, 7, 11]
# output = {}
# for i in list:
#     if i%2==0:
#         output[i]=i**2
#     else:
#         output[i]=i**3
#
# print(output)

result = {i:i**2 if i%2==0 else i**3 for i in list}
print("Result:",result)

print('_'*70)

# 8). Python Dictionary program to clear all items from the dictionary.

dict = {'a':741,'b':984,'c':256}
dict.clear()
print(dict)

print('_'*70)

# 9). Python Dictionary program to remove duplicate values from Dictionary.

dict3 = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
output = {}
for k,v in dict3.items():
    if v not in output.values():
        output[k] = v

print(output)

print('_'*70)

# 10). Python Dictionary program to create a dictionary from the string.
Input = 'SQATools'
output = {}

for char in Input:
    if char not in output:
        output[char] = 1
    else:
        output[char]+=1
print(output)

print('_'*70)
