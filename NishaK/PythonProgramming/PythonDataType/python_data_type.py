"""
Python Data Types
1.  Number data type
    i). Integer
    ii). Float
    iii). Complex Number

2.  Sequential data type
    i). String
    ii). List
    ii). Tuple

3.  Dictionary Data type
4.  Set Data type
5.  Boolean Data type
"""


# 1. Integer

v1 = 0
v2 = 20
v3 = 734697236
v4 = -36564
print("v1 :", v1, type(v1))
# v1 : 0 <class 'int'>
print("v2 :", v2, type(v2))
# v2 : 20 <class 'int'>
print("v3 :", v3, type(v3))
# v3 : 734697236 <class 'int'>
print("v4 :", v4, type(v4))
# v4 : -36564 <class 'int'>


print("-"*50)
# 2. Float

f1 = 0.0
f2 = 2.10
f3 = 12056.2354365
f4 = -13214.232
print("f1 :", f1, type(f1))
# f1 : 0.0 <class 'float'>
print("f2 :", f2, type(f2))
# f2 : 2.1 <class 'float'>
print("f3 :", f3, type(f3))
# f3 : 12056.2354365 <class 'float'>
print("f4 :", f4, type(f4))
# f4 : -13214.232 <class 'float'>


print("-"*50)
# 3. Complex Data Type

c1 = 10 + 20j
print("c1 :", c1, type(c1))
# c1 : (10+20j) <class 'complex'>
print("Real Number :", c1.real, type(c1.real))
# Real Number : 10.0 <class 'float'>
print("Imaginary Number :", c1.imag, type(c1.imag))
# Imaginary Number : 20.0 <class 'float'>


print("-"*50)
# 4. String

s1 = ""
s2 = "H"
s3 = "Hello"
s4 = 'We are learning Python Programming'
s5 = """ Hello How are you,
Hope you are doing good
Python Is very easy language to learn
"""
s6 = '''Creating your own ads.txt 
file gives you more control over 
who's allowed to sell ads on your 
site and helps prevent counterfeit 
inventory from being presented to advertisers.
'''
s7 = "Hello we are Learning 'Python' Programming"
s8 = 'Hello we are Learning "Python" Programming'
s9 = """
Creating your own ads.txt 
file gives you 'more' control over 
who's "allowed" to sell ads on your 
"""
s10 = "343 &*&*(&*(& {}[] + - _"


print("s1 :", s1, type(s1))
# s1 :  <class 'str'>

print("_" * 50)
print("s2 :", s2, type(s2))
# s2 : H <class 'str'>

print("_" * 50)
print("s3 :", s3, type(s3))
# s3 : Hello <class 'str'>

print("_" * 50)
print("s4 :", s4, type(s4))
# s4 : We are learning Python Programming <class 'str'>

print("_" * 50)
print("s5 :", s5, type(s5))
# s5 :  Hello How are you,
# Hope you are doing good
# Python Is very easy language to learn
#  <class 'str'>

print("_" * 50)
print("s6 :", s6, type(s6))
# s6 : Creating your own ads.txt
# file gives you more control over
# who's allowed to sell ads on your
# site and helps prevent counterfeit
# inventory from being presented to advertisers.
#  <class 'str'>

print("_" * 50)
print("s7 :", s7, type(s7))
# s7 : Hello we are Learning 'Python' Programming <class 'str'>

print("_" * 50)
print("s8 :", s8, type(s8))
# s8 : Hello we are Learning "Python" Programming <class 'str'>

print("_" * 50)
print("s9 :", s9, type(s9))
# s9 :
# Creating your own ads.txt
# file gives you 'more' control over
# who's "allowed" to sell ads on your
#  <class 'str'>


print("_" * 50)
print("s10 :", s10, type(s10))
# s10 : 343 &*&*(&*(& {}[] + - _ <class 'str'>


print("_" * 50)
str1 = "Programming"

"""
  0   1  2  3  4  5  6  7  8  9  10 
  P   r  o  g  r  a  m  m  i  n  g
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
"""

print(str1[10])
# g
print(str1[-1])
# g
print(str1.index('g'))
# 3


print("-"*50)
# 5. List

list1 = [2, 2.2, 10+20j,  "Hello", [1, 2, 3], (4, 5, 6), {'a': 11}, {7, 8, 9}, True]
print("list1 :", list1, type(list1))
# list1 : [2, 2.2, (10+20j), 'Hello', [1, 2, 3], (4, 5, 6), {'a': 11}, {8, 9, 7}, True] <class 'list'>

print(list1[0])
# 2
print(list1[4][0])
# 1

print("-"*50)
list3 = [2, 3, 4, 5]
list3.append(6)
print(list3)
# [2, 3, 4, 5, 6]


print("-"*50)
# 6. Tuple

tup1 = (10, 10.20, 10+40j, 'Python', [1, 2, 3], (4, 5, 6), {'b': 25}, {7, 8, 9}, True)
print("Tuple:", tup1, type(tup1))
# Tuple: (10, 10.2, (10+40j), 'Python', [1, 2, 3], (4, 5, 6), {'b': 25}, {8, 9, 7}, True) <class 'tuple'>


print("-"*50)
# 7. Dictionary

dict1 = {'a': 12, 'b': 24, 'c': 36}
print("dict1 :", dict1, type(dict1))
# dict1 : {'a': 12, 'b': 24, 'c': 36} <class 'dict'>


print("-"*50)
dict2 = {
    10: 20,
    10.10: 20.20,
    'Hello': 'Good Morning..!',
    (1, 2, 3): ('a', 'b', 'c'),
    10 + 20j: 20+30j,
    True: False,
    'A': [1, 2, 3, 4, 5],
    'B': {'a': 10, 'b': 20, 'c': 30},
    'C': {2, 4, 6, 8, 10}
}
print("Dict2 :", dict2, type(dict2))
# Dict2 : {10: 20, 10.1: 20.2, 'Hello': 'Good Morning..!', (1, 2, 3): ('a', 'b', 'c'), (10+20j): (20+30j), True: False, 'A': [1, 2, 3, 4, 5], 'B': {'a': 10, 'b': 20, 'c': 30}, 'C': {2, 4, 6, 8, 10}} <class 'dict'>

print(dict2['A'])
# [1, 2, 3, 4, 5]
print(dict2['A'][1])
# 2
print(dict2['B']['c'])
# 30


print("-"*50)
# 8. Set

set1 = {1, 2, 3, 4, 5, 5, 4, 3}
print("set :", set1, type(set1))
# set : {1, 2, 3, 4, 5} <class 'set'>

set2 = {1, 1.1, 'Python', (1, 2, 3), True, None}
print("set2 :", set2, type(set2))
# set2 : {None, 1, 1.1, 'Python', (1, 2, 3)} <class 'set'>

set3 = {2, 4, 6, 8}
set3.add(10)
print(set3)
# {2, 4, 6, 8, 10}

print("-"*50)
# 9. Boolean

v1 = True
v2 = False
print(v1, type(v1))
# True <class 'bool'>
print(v2, type(v2))
# False <class 'bool'>

a = 10
b = 15
c = 10
print(a == b)
# False
print(a == c)
# True
