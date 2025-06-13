#Dict -> string

d1 = {'a':23,'b':45,'c':"hello"}
str1=str(d1)
print(str1,type(str1))#{'a': 23, 'b': 45, 'c': 'hello'} <class 'str'>

print("_"*50)
#Dict -> list
d2 = {'A':23,'B':45,'C':"hello"}
list1=list(d2)
print(list1,type(list1))#['A', 'B', 'C'] <class 'list'>

print("_"*50)
#Dict -> tuple

d3 = {'AA':23,'BB':45,2:"hello"}
tup1=tuple(d3)
print(tup1,type(tup1)) #('AA', 'BB', 2) <class 'tuple'>

print("_"*50)
#Dict -> set

d4 = {'AA':23,'BB':45,2:"hello",'BB':44}
set1=set(d4)
print(set1,type(set1))#{2, 'AA', 'BB'} <class 'set'>

print("_"*50)
#Dict -> Boolean

d5={}
d6={'AA':23,'BB':45,2:"hello",'BB':44}
b1=bool(d5)
b2=bool(d6)
print(b1,type(b1)) #False <class 'bool'>
print(b2,type(b2)) #True <class 'bool'>
