#String -> int
#s1='a'
s2='234'
#i1=int(s1)
i2=int(s2)
#print(i1,type(i1)) #ValueError: invalid literal for int() with base 10: 'a'

print("_"*50)
print(i2,type(i2)) #234 <class 'int'>

print("_"*50)
#String -> float
s1='2345'
f1=float(s1)
print(f1,type(f1)) #2345.0 <class 'float'>

print("_"*50)
#String -> boolean

s3=0
s12=98
b1= bool(s3)
b2= bool(s12)
print(b1,type(b1))#False <class 'bool'>
print(b2,type(b2))#True <class 'bool'>

print("_"*50)
#String -> List

str1 = "3456a7.6"
l1=list(str1)
print(l1,type(l1))#['3', '4', '5', '6', 'a', '7', '.', '6'] <class 'list'>


print("_"*50)
#String -> Dict

str2='{"a":"fine", "hello":"hi", "c" : "r@gmail.com","b":2345}'
import json
d_type= json.loads(str2)
print(d_type,type(d_type)) #{'a': 'fine', 'hello': 'hi', 'c': 'r@gmail.com', 'b': 2345} <class 'dict'>


print("_"*50)
#String -> Dict
str22="aa123422"
set1=set(str22)
print(set1,type(set1)) #{'3', 'a', '4', '1', '2'} <class 'set'>

print("_"*50)
#String -> tuple
str22="aa123422"
tup1=tuple(str22)
print(tup1,type(tup1)) #('a', 'a', '1', '2', '3', '4', '2', '2') <class 'tuple'>













