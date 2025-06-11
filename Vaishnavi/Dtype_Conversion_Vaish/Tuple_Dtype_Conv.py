#Tuple -> string

tup1=(1,2,3,4)
str1=str(tup1)
print(str1,str1[1],type(str1))#(1, 2, 3, 4) 1 <class 'str'>

print("-"*50)
#Tuple -> List

tup2=(12,23,45,34)
list1=list(tup2)
print(list1,type(list1),list1[2]) #[12, 23, 45, 34] <class 'list'> 45

print("-"*50)
#Tuple -> set

tup3=(92,3,2,3,4,5,7)
set1=set(tup3)
print(set1,type(set1)) #{2, 3, 4, 5, 7, 92} <class 'set'>

print("-"*50)
#Tuple -> Dict

tup12=('a','b','c')
tup22=(2,3,4)
dict1=dict(zip(tup12,tup22))
print(dict1,type(dict1))#{'a': 2, 'b': 3, 'c': 4} <class 'dict'>

print("-"*50)
#Tuple -> bool

tup23=()
tup33=(2,3,4)
b1=bool(tup23)
b2=bool(tup33)
print(b1,type(b1))#False <class 'bool'>
print(b2,type(b2))#True <class 'bool'>

