print("_"*50)
###### set ->  string #######

set1={2,3,4,5,5,7}
str1=str(set1)
print(str1,type(str1))#{2, 3, 4, 5, 7} <class 'str'>

print("_"*50)
###### set ->  List #######
set2={2,33,4,5,5,7}
list1=list(set2)
print(list1,type(list1)) #[33, 2, 4, 5, 7] <class 'list'>

print("_"*50)
###### set ->  Tuple #######

set3={2,33,4,5,5,7}
tup1=tuple(set3)
print(tup1,type(tup1))#(33, 2, 4, 5, 7) <class 'tuple'>

print("_"*50)
###### set ->  Dict #######

Set12={'a',2,2.3}
set22={2,2,4,5,5,7}
dict1=dict(zip(Set12,set22))
print(dict1,type(dict1)) #{2: 2, 2.3: 4, 'a': 5} <class 'dict'>

print("_"*50)
###### set ->  Bool #######
Set32={'a',2,2.3}
set33={}
b1=bool(set33)
b2=bool(Set32)
print(b1,type(b1))#False <class 'bool'>
print(b2,type(b2))#True <class 'bool'>
