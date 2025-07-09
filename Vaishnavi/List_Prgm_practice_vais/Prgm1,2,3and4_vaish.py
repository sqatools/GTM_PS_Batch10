#1Python program to calculate the square of each number from the given list.
l1=[2,3,4,5,6]
for val in l1:
    print(f"square of {val} is ", val**2)
 #2Python program to combine two lists.
 #extend()

la=[2,3,4]
lb=[3,4,5]
lb.extend(la)
print(la)#[2, 3, 4]
print(lb)#[3, 4, 5, 2, 3, 4]

#list concatination method
lc=[2,3,4]
ld=['a','b','c']
result=lc+ld
print(result)#[2, 3, 4, 'a', 'b', 'c']
print(lc)#[2, 3, 4]
print(ld)#['a', 'b', 'c']

print("_"*50)

#shallow copy
le=[2,3,4]
lf=['a','b','c']
le=lf
print(le)#['a', 'b', 'c']
print(lf)#['a', 'b', 'c']

print("_"*50)

#deep copy
e=[2,3,4]
f=['a','b','c']
e.append(100)
g=e.copy()
print(g)##[2, 3, 4, 100]
g.append(200)
print(g)#[2, 3, 4, 100]
print(e)

#3 Python program to calculate the sum of all elements from a list.
list2=[2, 3, 4, 100]
print("sum:",sum(list2))#sum: 109

#Python program to find a product of all elements from a given list.
list3=[2, 3, 4, 100]
multi=1
for val in list3:
    multi=multi*val
print(multi)#2400
