"""6). Python Dictionary Program to create a dictionary from two lists.
Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}"""

list1=['a','b','c','d','e']
list2 = [12, 23, 24, 25, 15, 16]
output={}
for i,j in zip(list1,list2):
    output[i]=j
print(output)

"""7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
Input :
[4, 5, 6, 2, 1, 7, 11]
Output :
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}"""

inp2=[4, 5, 6, 2, 1, 7, 11]
output={}
for i in inp2:
    if i%2==0:
      output[i]=i**2
    else:
        output[i]=i**3

print(output)

#8). Python Dictionary program to clear all items from the dictionary.

inp3={'a': 12, 'b': 2, 'c': 5, 'd': 35}
inp3.clear()
print(inp3)

"""9). Python Dictionary program to remove duplicate values from Dictionary.
Input :
{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
Output :
{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}"""
inp3={'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
output={}
for k,v in inp3.items():
    if v not in output.values():
        output[k]=v
print(output)

"""10). Python Dictionary program to create a dictionary from the string.
Input  = ‘SQATools’
Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}"""

inp4="SQATools"
output={}
for i in inp4:
    if i in output:
        output[i]+=1
    else:
        output[i]=1
print(output)