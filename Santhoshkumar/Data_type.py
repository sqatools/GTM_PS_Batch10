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

######### Integer Data Type ######
"""
Properties:
->  Integer is immutable data type, once it is defined we can not update.
->  Integer data type only contains whole number.
->  Integer can be positive or negative
->  There is no specific limit for integer datatype, we can assign any long number
    as integer value.


"""
######### Float Data Type ######
"""
Properties:
->  Float is immutable data type, once it is defined we can not update.
->  Float data type only contains pointer value number.
->  Float number can be positive or negative.
->  There is no specific limit for float datatype, we can assign any long number
    as float value.
"""
######### Complex Data Type ######
"""
Properties:
1.  complex data type is immutable data type
2.  complex data type is combination of real and imaginary number
    e.g x+yj
    x :  real number
    y :  imaginary number
3.  complex data type could be positive and negative both
"""
"""
str="santhoshkumar"
if len(str)<2:
    print(True)
else:
#    print(str[:2]+str[-2:])
     print(str[2:] + str[:-2])

"""

string="i", "am", "happy", "to", "in", "the", "community"
str=len(string)
print(str)

print("_"*50)

str="sqatools"
print(str[-2::]*4)

print("_"*50)

string = "sqatools"

if len(string) % 4 == 0:
    print(string[::-1])

print("_"*50)

string = "sqatoolspythonspy"
sub= "spy"
str = string.count("spy")
print(str)

print("_"*50)

Input = “Programming”
Output = “Prog$am$in$”

str= "Programming"

f1 = 0.0
f2 = 0.2
f3 = 898908908.78798
f4 = 6786478326784236234324.23432324344324
f5 = -4543.5095

print("f1 :", f1, type(f1))  # 0.0 <class 'float'>
print("f2 :", f2, type(f2))  # 0.2 <class 'float'>
print("f3 :", f3, type(f3))  # 898908908.78798 <class 'float'>
print("f4 :", f4, type(f4))  # 6.786478326784236e+21 <class 'float'>
print("f5 :", f5, type(f5))  # -4543.5095 <class 'float'>

print("_" * 50)
######### Complex Data Type ######
"""
Properties:
1.  complex data type is immutable data type
2.  complex data type is combination of real and imaginary number
    e.g x+yj
    x :  real number
    y :  imaginary number
3.  complex data type could be positive and negative both
"""

p1 = 10 + 20j
print("p1 : ", p1, type(p1))
# p1 :  (10+20j) <class 'complex'>

p2 = -400 - 500j
print("p2 :", p2, type(p2))
# p2 : (-400-500j) <class 'complex'>

print("real number :", p2.real, type(p2.real))
# real number : -400.0 <class 'float'>

print("imaginary number :", p2.imag, type(p2.imag))
# imaginary number : -500.0 <class 'float'>

############### Sequential data type ##############
print("_" * 50)
##### string #########
"""
Properties:
->  String in immutable data type, once is define can not update.
->  String can be defined with the help of single quote, double quotes and triple quotes.
->  String Follows positive and negative indexing.
->  String can contains any type of data


"""
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

# single quote inside double quote
s7 = "Hello we are Learning 'Python' Programming"

# double quote inside single quote
s8 = 'Hello we are Learning "Python" Programming'

s9 = """
Creating your own ads.txt 
file gives you 'more' control over 
who's "allowed" to sell ads on your 
"""

s10 = "343 &*&*(&*(& {}[] + - _"

print("_" * 50)
print("s1 :", s1, type(s1))

print("_" * 50)
print("s2 :", s2, type(s2))

print("_" * 50)
print("s3 :", s3, type(s3))

print("_" * 50)
print("s4 :", s4, type(s4))

print("_" * 50)
print("s5 :", s5, type(s5))

print("_" * 50)
print("s6 :", s6, type(s6))

print("_" * 50)
print("s7 :", s7, type(s7))

print("_" * 50)
print("s8 :", s8, type(s8))

print("_" * 50)
print("s9 :", s9, type(s9))

print("_" * 50)
print("s10 :", s10, type(s10))

print("_" * 50)
######### String Follows positive and negative indexing ########

str1 = "Python"

"""
 0  1  2  3  4  5
 P  y  t  h  o  n
-6 -5 -4 -3 -2 -1

"""

print(str1[0])  # P
print(str1[-3])  # h

print(str1.index('o'))  # 4

# get characters with +ve and -ve indexing
str2 = "Programming"
print(str2[5])  # a
print(str2[-8])  # g
print(str2[6])  # m
print(str2[-2])  # n

print("_" * 50)
######## list #########
"""
Properties:
->  List is mutable data type. we can modify the list at any point of time.
->  List store values in comma separated format
->  List can contain all the type of data, e.g. int, float, complex, string, list
    tuple, dict, set, bool.
->  List follows positive negative indexing as like string.
->  list store data in square brackets.
->  Usage of the list data type, where we update data regularly
    e.g employee management, there we can add, delete, and update employee info.
"""

list1 = [4, 5.6, 'Hello', 5 + 8j, [3, 5, 6], (1, 2, 3), {'a': 123}, {4, 7, 8, 4}, True]

print(list1, type(list1))
# [4, 5.6, 'Hello', (5+8j), [3, 5, 6], (1, 2, 3), {'a': 123}, {8, 4, 7}, True] <class 'list'>

# list follows positive and negative indexing

print(list1[4])  # [3, 5, 6]
print(list1[-2])  # {8, 4, 7}
print(list1[-6])  # (5+8j)
print(list1[6])  # {'a': 123}
print(list1[4][1])  # 5

list2 = [4, 6, 8]
list2.append(10)
print("list2 :", list2)  # list2 : [4, 6, 8, 10]

print("_" * 50)
################################# Tuple ####################################

"""
Properties:
->  Tuple is immutable data type. we can not modify the tuple.
->  Tuple store values in comma separated format.
->  Tuple can contain all the type of data, e.g. int, float, complex, string, list
    tuple, dict, set, bool.
->  Tuple follows positive negative indexing as like string and list.
->  Tuple store data in round brackets.
->  Usage of the tuple data type, where the data is fixed.
    e.g store days in a months, days in week, months in year.
->  Tuple is faster than list in terms of performance.
"""

tup1 = (2, 5.6, 'Python', (4, 6, 7), [1, 3, 5], {'b': 456}, {6, 8, 9}, True, False)

print(tup1, type(tup1))
# (2, 5.6, 'Python', (4, 6, 7), [1, 3, 5], {'b': 456}, {8, 9, 6}, True, False) <class 'tuple'>


print(tup1[4])  # [1, 3, 5]
print(tup1[2][2])  # t
print(tup1[-6][-1])  # 7
print(tup1[3][-1])  # 7

tup2 = (3, 6, 7)
# we don't have any method to update the tuple values


print("_" * 50)
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

print("_" * 50)
# get dict data with key
print(dict2['A'])  # [4, 6, 8, 2, 8]
print(dict2['A'][3])  # 2
print(dict2['B'])  # {'a': 123, 'b': 567, 'c': 890}
print(dict2['B']['c'])  # 890
