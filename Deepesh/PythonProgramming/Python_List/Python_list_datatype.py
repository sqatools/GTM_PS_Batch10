list1 = [3, 6, 8, 'a', 'b', 'c']
print(list1, type(list1))
# [3, 6, 8, 'a', 'b', 'c'] <class 'list'>


print("_"*50)
list2 = [4, 7, 12, 68, 34, 90]
# apply loop on list values

# loop without indexing
for val in list2:
    print(val)

"""
4
7
12
68
34
90
"""

print()
print("_"*50)

# loop with indexing
for i in range(len(list2)):
    print(i, list2[i])

"""
0 4
1 7
2 12
3 68
4 34
5 90
"""

print("_"*50)
############################# slicing in list values #######################
list3 = [5, 8, 12, 'a', 'b', 'c', 'd', 'Hello', [4, 7, 9]]
print(list3[3:7])  # ['a', 'b', 'c', 'd']
print(list3[-3:-7:-1]) # ['d', 'c', 'b', 'a']
print(list3[0::2]) # [5, 12, 'b', 'd', [4, 7, 9]]
print(list3[-1::-1]) # [[4, 7, 9], 'Hello', 'd', 'c', 'b', 'a', 12, 8, 5]
print(list3[::-1]) # [[4, 7, 9], 'Hello', 'd', 'c', 'b', 'a', 12, 8, 5]
print(list3[-2:-7:-2]) # ['Hello', 'c', 'a']
print(list3[-2][-4]) # e
print(list3[-1][:2]) # [4, 7]


print("_"*50)
############################ List Methods ###################
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


####################### Add data to the list ##########################
# append() method :  This method add new value at end of the list.
list_a = ['a', 'b', 'c', 'd']
list_a.append(100)
print("list_a :", list_a) # list_a : ['a', 'b', 'c', 'd', 100]

list_a.append(500)
print("list_a :", list_a) # list_a : ['a', 'b', 'c', 'd', 100, 500]


print("_"*50)
###################################
# insert() method:  This method add value to specified index location

list_b = ['a', 'b', 'c', 'd']
list_b.insert(2, 200)
print("list_b :", list_b) # list_b : ['a', 'b', 200, 'c', 'd']

list_b.insert(-1, 500)
print("list_b :", list_b) # ['a', 'b', 200, 'c', 500, 'd']

list_b.insert(1, [5, 7, 8])
print("list_b :", list_b) # ['a', [5, 7, 8], 'b', 200, 'c', 500, 'd']


print("_"*50)
###################################
# extend() method: This method extend one list data to another list, each value will have its own index position.

list_c = [4, 99, 11, 44]
list_d = ['a', 'b', 'c', 'd']

# It will modify original list_d and include all the values of list_c into list_d
list_d.extend(list_c)
print("list_d :", list_d) # ['a', 'b', 'c', 'd', 4, 99, 11, 44]
print("list_c :", list_c)


print("_"*50)
###################################
# list concatenation : List concatenation takes two lists values and generate the updated list data and return.
#                      does not modify the original list

list_e = [4, 99, 11, 44]
list_f = ['a', 'b', 'c', 'd']

result = list_f + list_e
print("list_e :", list_e)
print("list_f:", list_f)
print("result:", result) # ['a', 'b', 'c', 'd', 4, 99, 11, 44]


print("_"*50)
###################################
# list repeatation: when we multiply the list with any number, then it will repeat the list values that number of times.

list_g = [5, 7, 8]
result = list_g*5
print("repeatation result :", result) # [5, 7, 8, 5, 7, 8, 5, 7, 8, 5, 7, 8, 5, 7, 8]
