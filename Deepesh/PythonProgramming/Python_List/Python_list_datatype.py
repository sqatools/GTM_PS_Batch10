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


print("_"*50)
###############################Remove data from list #############################

# remove() method :  This method remove specific value from given list
#                    -> Remove method does not return any value.
#                    ->  It same value repeated multiple times, then it will remove first occurrence

list_j = [5, 7, 8, 11, 44, 77, 44]
list_j.remove(44)

print("list_j :", list_j)
# list_j : list_j : [5, 7, 8, 11, 77, 44]


print("_"*50)
###############################
# pop() method :  pop method remove values from list using index position, and return the value.
#                 ->  default index position is -1

list_k = [5, 7, 8, 11, 44, 77, 44, 70]

# remove data from default index position -1
v1 = list_k.pop()
print("removed value :", v1) # removed value : 70
print("list_k :", list_k)
# list_k : [5, 7, 8, 11, 44, 77, 44]

# remove value from specific index position
v2 = list_k.pop(3)
print("removed value :", v2) # removed value : 11
print("list_k :", list_k)
# list_k : [5, 7, 8, 44, 77, 44]


print("_"*50)
###############################
# clear() method :  This method clear all the values from given list
list_t = [5, 7, 8, 11, 44, 77, 44, 70, 22, 13]
list_t.clear()
print("list_t :", list_t)
# list_t : []


print("_"*50)
###############################
# del keyword :  del keyword can remove entire variable from memory
list_y = [5, 44, 70, 22, 13]
del list_y
#print("list_y :", list_y)
# NameError: name 'list_y' is not defined. Did you mean: 'list_a'?


# remove value with del keyword and slicing
list_x = [5, 44, 70, 22, 13, 66, 23, 45]
# It will remove three values 44, 70, 22
del list_x[1:4]
print("list_x :", list_x) # list_x : [5, 13, 66, 23, 45]


list_z = [5, 44, 70, 22, 13, 66, 23, 45]
# remove alternate values from list
del list_z[1::2]
print("list_z :", list_z)  # [5, 70, 13, 23]


print("_"*50)
######################## Other methods ##################
# replace data in the list

list_o = [5, 7, 9, 2, 'a', 'b', 'c']
# replace single value with index
list_o[0] = 500
print("list_o :", list_o)  # [500, 7, 9, 2, 'a', 'b', 'c']

# replace multiple values with slicing
list_o[4:] = [100, 200, 300]
print("list_o :", list_o)  # [500, 7, 9, 2, 100, 200, 300]


print("_"*50)
########################
"""
# sort() method :  This method sort list data in ascending and descending order.
                   ->  This method modify the original list values
"""
list_p = [5, 7, 9, 2, 10, 21, 12, 35]
# sort list in ascending order
list_p.sort()
print("list_p :", list_p)  # [2, 5, 7, 9, 10, 12, 21, 35]


list_q = [5, 17, 91, 2, 110, 21, 12, 35]
# sort list values in descending order
list_q.sort(reverse=True)
print("list_q :", list_q) # [110, 91, 35, 21, 17, 12, 5, 2]


print("_"*50)
########################
"""
# sorted() function :  This function sort list data in ascending and descending order.
                   ->  This function does not modify the original list values, it takes as input
                       and return the required output
"""

list_w = [5, 17, 91, 12, 110, 211, 12, 100]
# sort in ascending order
result = sorted(list_w)
print("sorted result :", result)  # [5, 12, 12, 17, 91, 100, 110, 211]


# sort in descending order
result2 = sorted(list_w, reverse=True)
print("sorted result :", result2)  # [211, 110, 100, 91, 17, 12, 12, 5]



print("_"*50)
########################
"""
# reverse() method :  This method reverse the list data and modify original list
                   
"""

list_u = [15, 17, 91, 112, 110, 211, 12, 130]
list_u.reverse()
# Here it will modify the original list
print("list_u :", list_u)
# [130, 12, 211, 110, 112, 91, 17, 15]



print("_"*50)
########################
"""
# reversed() function :  This function reverse the list data and does not modify original list
                         ->  It returns the reversed output in variable
                    
"""
list_f = [15, 17, 91, 112, 110, 211, 12, 130]
result = list(reversed(list_f))
print("result :", result)
#  [130, 12, 211, 110, 112, 91, 17, 15]

print("list_f :", list_f)
# [15, 17, 91, 112, 110, 211, 12, 130]



print("_"*50)
########################
"""
# count() method :  This method return the count of occurrences of any given value
"""
list_g = [15, 17, 91, 21, 110, 21, 12, 130, 91, 17, 21]
print("count of 21 :", list_g.count(21))
# count of 21 : 3
print("count of 17 :", list_g.count(17))
# count of 17 : 2


print("_"*50)
########################
"""
# index() method :  This method return index position of any given value
                    ->  If there is duplicate value, then it will return the first occurrence index position.
"""

list_h = [15, 17, 91, 21, 110, 21, 12, 130, 91, 17, 21]
print("index of 110 :", list_h.index(110)) # index of 110 : 4

# repeated value index
print("index of 21 :", list_h.index(21))
# index of 21 : 3





print("_"*50)
########################
# shallow copy: in shallow copy when we assign one listA data to another listB, and modify the second listB values
#               then changes will reflect in listA as well
list_v = [5, 8, 0, 23]
list_n = list_v
list_n.append(100)
list_n.append(200)
list_m = list_n
list_m.append('a')

print("list_v :", list_v) # [5, 8, 0, 23, 100, 200, 'a']
print("list_n :", list_n) # [5, 8, 0, 23, 100, 200, 'a']
print("list_m :", list_m) # [5, 8, 0, 23, 100, 200, 'a']


print("_"*50)
###### Deep copy: ######
list_A = [5, 8, 2, 6, 12]
list_B = list_A.copy()

list_B.append(101)
list_A.append('Python')

print("list_A :", list_A) # [5, 8, 2, 6, 12, 'Python']
print("list_B:", list_B)  # [5, 8, 2, 6, 12, 101]
