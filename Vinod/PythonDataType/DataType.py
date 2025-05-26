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
num = 0
num1 = 10
num2 = 4545435
num3 = 56564356456456453635463456
num4 = -5678

print("num :", num, type(num))  # 0 <class 'int'>
print("num1 :", num1, type(num1))  # 10 <class 'int'>
print("num2 :", num2, type(num2))  # 4545435 <class 'int'>
print("num3 :", num3, type(num3))  # 56564356456456453635463456 <class 'int'>
print("num4 :", num4, type(num4))  # -5678 <class 'int'>

a = 100
print(a)  # 100
a = 200
print(a)  # 200

print("_" * 50)
######### Float Data Type ######
"""
Properties:
->  Float is immutable data type, once it is defined we can not update.
->  Float data type only contains pointer value number.
->  Float number can be positive or negative.
->  There is no specific limit for float datatype, we can assign any long number
    as float value.
"""

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