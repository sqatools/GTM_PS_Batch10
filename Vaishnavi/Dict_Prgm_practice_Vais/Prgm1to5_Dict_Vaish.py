#1). Python Dictionary program to add elements to the dictionary.
dict1={'a':67,'b':95}
dict1['c']=100
dict1['f']=200
print(dict1)

"""2). Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64"""
Input = {'a': 5, 'b':3, 'c': 6, 'd' : 8}
for k,v in Input.items():
    print(k,":",v)

"""3). Python Dictionary program to move items from dict1 to dict2.
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}"""

dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}
temp=dict1.copy()
for key in temp:
    dict2[key]=dict1.pop(key)
print(dict2)
print(dict1)

"""4). Python Dictionary program to concatenate two dictionaries.
Input :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
Output :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}"""

dict11={'Name':'Harry','Rollno':345,'Address':'Jordan'}
dict12={'Age':25,'salary':'$25k'}
dict11.update(dict12)
print(dict11)

"""5). Python Dictionary program to get a list of odd and even keys from the dictionary.
Input :
{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
Output :
Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]"""

inp1={1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}
even={}
odd={}
for key in inp1:
    if key%2==0:
        even[key]=inp1[key]
    else:
        odd[key]=inp1[key]
print("even:",even)
print("odd :",odd)
