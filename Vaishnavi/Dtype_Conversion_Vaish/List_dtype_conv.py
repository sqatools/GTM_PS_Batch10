#list -> string

list1=[1,2,'a','s',3,4]
str1=str(list1)
print(str1,type(str1)) #[1, 2, 'a', 's', 3, 4] <class 'str'>

print("_"*50)
#list -> Booloean
l1=[]
l2=[1,2,3]
b1=bool(l1)
b2=bool(l2)
print(b1,type(b1)) #False <class 'bool'>
print(b2,type(b2)) #True <class 'bool'>

print("_"*50)
#list -> Set
l12=[2,2,3,4,5,6,8,1,2,'a']
set1=set(l12)
print(set1,type(set1)) #{1, 2, 3, 4, 5, 6, 'a', 8} <class 'set'>

print("_"*50)
#list -> tuple
l22=[2,2,3,4,5,6,8,1,2,'a']
tup1=tuple(l22)
print(tup1,type(tup1)) #(2, 2, 3, 4, 5, 6, 8, 1, 2, 'a') <class 'tuple'>

print("_"*50)
#list -> dict

l10=['a','b','c']
l11=[1,2,3,4]
dict1=dict(zip(l10,l11))
print(dict1,type(dict1)) #{'a': 1, 'b': 2, 'c': 3} <class 'dict'>

print("_"*50)
l101=['a','b','c','d','e']
l111=[1,2,3,4]
dict2=dict(zip(l101,l111))
print(dict2,type(dict2)) #{'a': 1, 'b': 2, 'c': 3, 'd': 4} <class 'dict'>

