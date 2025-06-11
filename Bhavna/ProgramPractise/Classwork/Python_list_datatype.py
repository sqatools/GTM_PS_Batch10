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