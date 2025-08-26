#1). Python Dictionary program to add elements to the dictionary.
dictionary1 = {}
dictionary1["village"] = "Gunavante"
dictionary1["age"] = 67
print(dictionary1)
"""
Output:
{'village': 'Gunavante', 'age': 67}
"""
#2)Python Dictionary program to print the square of all values in a dictionary.
my_dict= {'a': 5, 'b':3,'c': 6,'d' : 8}
for i in my_dict:
    print(i,my_dict[i]**2)
"""
Output:
a 25
b 9
c 36
d 64
"""
#3). Python Dictionary program to move items from dict1 to dict2.

dict1 = {'name':'john','city':'Landon','country':'UK'}
dict2 = {}
temp = dict1.copy()

for valu in temp:
    v1 = dict1.pop(valu)
    dict2[valu] = v1

print("dictionary 2 :", dict2)
print("dictionary 1 :", dict1)
"""
Output:
dictionary 2 : {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dictionary 1 : {}

"""
#Python Dictionary program to concatenate two dictionaries.

dict10 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}
dict20 = {'Age':25,'salary': '$25k'}

dict1.update(dict20)

print(dict10)
"""
Output:
{'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan', 'Age': 25, 'salary': '$25k'}
"""
#5)Python Dictionary program to get a list of odd and even keys from the dictionary.
dict6 = {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}

list1 = [[val,dict6[val]] for val in dict6 if val%2 == 0]
list2 = [[val,dict6[val]] for val in dict6 if val%2 != 0]

print("Even key = ",list1)
print("Odd key = ",list2)

#Python Dictionary Program to create a dictionary from two lists.
list1 = ['a','b','c','d','e']
list2 = [12, 23, 24, 25, 15, 16]
list1 = ['a','b','c','d','e']
list2 = [12,23,24,25,15,16]
dict1 = {}

for a,b in zip(list1,list2):
    dict1[a] = b

print(dict1)
"""
output:
{'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15}
"""

list1 = [4, 5, 6, 2, 1, 7, 11]
dict1 = {}

# In this python dictionary program, we will store squares of even and cubes of odd numbers in a dictionary using the dictionary comprehension method.
for val in list1:
    if val % 2 == 0:

        dict1[val] = val**2
    else:

        dict1[val] = val**3

print("result dictionary:", dict1)
"""
output:
result dictionary: {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
"""
# 8). Python Dictionary program to clear all items from the dictionary.
dict100 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}

dict100.clear()
print(dict100)

#Python Dictionary program to remove duplicate values from Dictionary.
dict11 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
dict22 = {}

for key,val in dict1.items():
    if val not in dict2.values():
        dict22[key] = val

print(dict22)
"""
output:
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
"""
