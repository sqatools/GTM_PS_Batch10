# 10/06/2025 Session

list = [5,8,4,'y','u','t']
print(list,type(list))
# [5, 8, 4, 'y', 'u', 't'] <class 'list'>

print('_'*70)

list1 = [8,9,52,45,62,11]
# apply loop on list values

# 1. loop without indexing
for i in list1:
    print(i,end=" ")
# 8 9 52 45 62 11
print()
print('_'*70)

# 2.loop with indexing

for j in range(len(list1)):
    print(j, list1[j])

'''
0 8
1 9
2 52
3 45
4 62
5 11
'''
print('_'*70)
############################# slicing in list values #######################
list2 = [5, 8, 12, 'a', 'b', 'c', 'd', 'Hello', [4, 7, 9]]
print(list2[3:7]) #['a', 'b', 'c', 'd']
print(list2[-3:-7:-1]) #['d', 'c', 'b', 'a']
print(list2[0::2]) #[5, 12, 'b', 'd', [4, 7, 9]]
print(list2[-1::-1]) #[[4, 7, 9], 'Hello', 'd', 'c', 'b', 'a', 12, 8, 5]
print(list2[::-1]) #[[4, 7, 9], 'Hello', 'd', 'c', 'b', 'a', 12, 8, 5]
print(list2[-2:-7:-2]) #['Hello', 'c', 'a']
print(list2[-2][1]) #e
print(list2[-1][:2])

print('_'*70)
############################ List Methods ###################
print(dir(list))
# ['__add__', '__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear', 'copy',
# 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']

print('_'*70)
####################### Add data to the list ##########################
# append() method :  This method add new value at end of the list.

list_1 = ['a','b','c','d']
list_1.append(500)
print("list_1:",list_1) # list_1: ['a', 'b', 'c', 'd', 500]

list_1.append(250)
print("list_1:",list_1) # list_1: ['a', 'b', 'c', 'd', 500, 250]

print('_'*70)

###################################
# insert() method:  This method add value to specified index location

list_2 = ['a', 'b', 'c', 'd']
list_2.insert(2, 400)
print("list_2:", list_2)  #list_2: ['a', 'b', 400, 'c', 'd']

list_2.insert(-1,500)
print("list_2:", list_2) #list_2: ['a', 'b', 400, 'c', 500, 'd']

list_2.insert(1,[5,7,8])
print("list_2:", list_2) #list_2: ['a', [5, 7, 8], 'b', 400, 'c', 500, 'd']

print('_'*70)

###################################
# extend() method: This method extend one list data to another list, each value will have its own index position.

list_a = [3,98,74,65,77]
list_b = ['z','j','s','d']
# It will modify original list_b and include all the values of list_a into list_d

list_b.extend(list_a)
print("list_b:",list_b)
print("list_a:",list_a)

print('_'*70)

###################################
# list concatenation : List concatenation takes two lists values and generate the updated list data and return.
#                      does not modify the original list

list_c = [55,66,77,88]
list_d = ['a','b','c','d']

result = list_c + list_d

print("result:", result)   #result: [55, 66, 77, 88, 'a', 'b', 'c', 'd']
print("list_c:", list_c)
print("list_d:", list_d)

print('_'*70)

###################################
# list repeatation: when we multiply the list with any number, then it will repeat the list values that number of times.

list_e = [7,'a',9]
result = list_e*5
print("result:",result) # result: [7, 'a', 9, 7, 'a', 9, 7, 'a', 9, 7, 'a', 9, 7, 'a', 9]

print('_'*70)
######################################
# 11/06/2025 Session

############# Remove data from list #####################

# remove() method :  This method remove specific value from given list
#                    -> Remove method does not return any value.
#                    ->  It same value repeated multiple times, then it will remove first occurrence

list_a = [9,1,5,66,35,47,98,25,11]
list_a.remove(47)
list_a.remove(66)

print("list_a:",list_a)

print('_'*70)
############# POP Method #####################
# pop() method :  pop method remove values from list using index position, and return the value.
#                 ->  default index position is -1

list_b = [4,9,74,85,62,12,55,1,2]

# remove data from default index position -1
a = list_b.pop()
print("removed value:",a) #removed value: 2
print(list_b)
# [4, 9, 74, 85, 62, 12, 55, 1]

print('_'*70)
###############################
# clear() method :  This method clear all the values from given list
list_g = [8,95,11,25,4,5,63,2]
list_g.clear()
print("list_g:",list_g) #list_g: []

print('_'*70)

###############################
# del keyword :  del keyword can remove entire variable from memory
list_m = [1,4,7,8,5,2]
del list_m
# print(list_m)
# NameError: name 'list_m' is not defined. Did you mean: 'list_1'?

# remove value with del keyword and slicing
list_n = [8,85,52,15,69,4,12,14]
del list_n[2:5]
print("list_n:",list_n) #list_n: [8, 85, 4, 12, 14]

list_o = [36,3,39,96,63,69]
# remove alternate values from list
del list_o[1::2]
print("list_o:",list_o)

print('_'*70)

######################## Other methods ##################
# replace data in the list

list_p = [8,1,6,9,'i','j']
# replace single value with index
list_p[0] = 100
print("list_p:",list_p) #list_p: [100, 1, 6, 9, 'i', 'j']

# replace multiple values with slicing
list_p[4:] = [101,202]
print("list_p:",list_p) #list_p: [100, 1, 6, 9, 101, 202]

print('_'*70)

########################
"""
# sort() method :  This method sort list data in ascending and descending order.
                   ->  This method modify the original list values
"""
list = [1,21,4,8,54,0,44,22]
# sort list in ascending order
list.sort()
print("list:",list) #list: [0, 1, 4, 8, 21, 22, 44, 54]

# sort list values in descending order
listd = [2,11,25,68,5,4,36,98,88]
listd.sort(reverse=True)
print("listd:", listd) #listd: [98, 88, 68, 36, 25, 11, 5, 4, 2]

print('_'*70)
########################
"""
# sorted() function :  This function sort list data in ascending and descending order.
                   ->  This function does not modify the original list values, it takes as input
                       and return the required output
"""

list_w = [9,7,4,52,21,4,69,85]
# sort in ascending order
result = sorted(list_w)
print("Sorted result:", result) #Sorted result: [4, 4, 7, 9, 21, 52, 69, 85]

# sort in descending order
result1 = sorted(list_w,reverse=True)
print("Sorted Result:",result1) #Sorted Result: [85, 69, 52, 21, 9, 7, 4, 4]

print('_'*70)
########################
# reverse() method :  This method reverse the list data and modify original list

list_q = [55,98,96,521,111,24,745,22]
list_q.reverse()
# Here it will modify the original list
print("list_q:",list_q) #list_q: [22, 745, 24, 111, 521, 96, 98, 55]

print('_'*70)
########################
# reversed() function :  This function reverse the list data and does not modify original list
#                          ->  It returns the reversed output in variable

# list_r = [52,41,89,56,474]
# result = list(reversed(list_r))
#
# print("result:",result)

print('_'*70)

########################
# count() method :  This method return the count of occurrences of any given value

list_g = [18,9,25,18,93,3,9,74,18]
print("count of 18:", list_g.count(18))
#count of 18: 3
print("count of 9:", list_g.count(9))

print('_'*70)

########################
# index() method :  This method return index position of any given value
#                     ->  If there is duplicate value, then it will return the first occurrence index position.

list7 = [55,12,35,4,8,96,2]
print("index of 35:",list7.index(35))
# index of 35: 2

print('_'*70)

########################
# shallow copy: in shallow copy when we assign one listA data to another listB, and modify the second listB values
#               then changes will reflect in listA as well

lista = [0,9,4,7]
listb = lista
listb.append(10)
listb.append(20)
listc = listb
listc.append("i")
print("lista:",lista) #lista: [0, 9, 4, 7, 10, 20, 'i']
print("listb:",listb) #listb: [0, 9, 4, 7, 10, 20, 'i']
print("listc:",listc) #listc: [0, 9, 4, 7, 10, 20, 'i']
print('_'*70)


###### Deep copy: ######

listQ = [8,6,1,3,7]
listR = listQ.copy()

listQ.append('new')
listR.append('hi')

print("listQ:",listQ) #listQ: [8, 6, 1, 3, 7, 'new']
print("listR:", listR) #listR: [8, 6, 1, 3, 7, 'hi']

print('_'*70)
#################################################

# 12/06/2025 Session
#################################### List comprehension ###########################
# program to get even value from list
list1 = [9,3,6,4,5,2]
output = []

for i in list1:
    if i%2==0:
        output.append(i)
    else:
        continue
print(output) #[6, 4, 2]

print('-'*70)

# solve same program with list comprehension
result = [j for j in list1 if j%2==0 ]
print("Result:", result)    #Result: [6, 4, 2]

print('_'*70)

# program to get below value from given list values
list2 = [1,4,7,2]
# output = [(1,'odd'),(4,'even'),(7,'odd'),(2,'even')]
output = []

for y in list2:
    if y%2==0:
        output.append((y,'even'))
    else:
        output.append((y,'odd'))

print("result:",output)

print('_'*70)

### solve above program with the help of list comp ####

result2 = [(y,'even') if y%2==0 else (y,'odd') for y in list2]

print(result2)
print('_'*70)

# write a python program to get given combinations
l1 = ['a','b','c','d']
l2 = [2,3]
output3 = []
# output = [('a',2),('a',3),('b',2),('b',3),('c',2),('c',3)]

for k in l1:
    for j in l2:
        print(k,j)
        output3.append((k,j))

print(output3)
# [('a', 2), ('a', 3), ('b', 2), ('b', 3), ('c', 2), ('c', 3), ('d', 2), ('d', 3)]
print('_'*70)

# generate same output with list comprehension

result3 = [(p,q) for p in l1 for q in l2]
print("Result3:",result3)

print('_'*70)

#################### max, min, sum functions  ###############
list4 = [8,2,5,99,14]
print("Max Value:", max(list4))
print("Min Value:",min(list4))
print("Sum of list:", sum(list4))