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

# Program to remove extra spaces
sentence = " Python programming is fun! "
trimmed = sentence.strip()
print(trimmed)

# Program to Convert to all uppercase:
uppercase = trimmed.upper()
print(uppercase)

# Program to Replace "fun" with "awesome":
replaced = trimmed.replace("fun", "awesome")
print(replaced)

# Program to Find the position of "programming":
position = trimmed.find("programming")
print(position)

# Program to Split the string into a list:
data = "cherry,banana,grape,apple"
fruits = data.split(",")
print(fruits)

# Program to sort the string  list:
fruits.sort()
print(fruits)
