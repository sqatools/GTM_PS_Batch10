"""
# properties:
->  Set is mutable data type, we can modify the set values.
->  Set only contains unique data, duplicate data is not allowed.
->  Only immutable data type can be member in the set.
    e.g. int, float, string, tuple, boolean.
->  Set store values in random order.
->  Set does not follow indexing.
->  Set store data in curly with comma separated.
"""

s1 = {2,6.6,'hi',(7,8,9),False,9.9,5,6}
print(s1,type(s1))
# {False, 2, 5, 6.6, 6, 9.9, (7, 8, 9), 'hi'} <class 'set'>

print('_'*70)

# apply loop on set data type
for val in s1:
    print(val)
'''
False
hi
2
5
6.6
6
9.9
(7, 8, 9)
'''
print('_'*70)

######################## Set Methods #######

print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']

print('_'*70)
########################
# add method() :  This method add one single value at time to set data.

s2 = {5,9,5.6,5,'m','y',89}
s2.add(100)
print("s2:",s2)
# s2: {89, 100, 5, 5.6, 'y', 9, 'm'}
s2.add((8,9,10))
s2.add(False)
s2.add('Python')
print("S2:",s2)

# s2.add([9,8,7])
# print(s2)
# TypeError: unhashable type: 'list'

print('_'*70)

########################
# update method() :  This method update one set to data to another set.

s3 = {5,9,7.9,'k','i'}
s4 = {'True','T','U'}
s4.update(s3)
print("s3:",s3)
print("S4:",s4)

print('_'*70)
########################
# union method() :  This method combine two sets data and return as set output.
#                   ->>  It does not modify the original set.

s5 = {9,9.9,True,'a'}
s6 = {False,'b',8,9,10,'l'}
result = s5.union(s6)
print(result)

print('S5:',s5)
print('S6:',s6)

print('_'*70)

########################
# remove method() :  This method remove any specific value from set
#                    ->  If the target value is not available, then it will throw error.

s7 = {77,88,99,'m','n','o'}
# remove existing value.
s7.remove(88)
print(s7)
# {'o', 99, 'm', 'n', 77}
# remove non-existing value. :  If value is not available, it will throw error
'''
s7.remove('q')
print(s7)   #KeyError: 'q'
'''

print('_'*70)

########################
# discard method() : This method remove any specific value from set, as like remove method.
#                   ->  It does not throw error if the target value is not available.

s8 = {100,200,300,400,500,'a','b'}
# discard existing value : It will work without any error
s8.discard(500)
print('s8:',s8)
# s8: {400, 'a', 100, 'b', 200, 300}

# discard non-existing value : If value is not available, it will not throw any error.
s8.discard(800)
print(s8)
# {400, 'a', 100, 200, 'b', 300}

print('_'*70)

########################
# pop method(): This method remove any random value and return it.

s9 = {700,800,900,600,'p','q'}
output = s9.pop()
print("removed value:",output) #removed value: 800
print(s9) #{900, 'q', 600, 700, 'p'}

print('_'*70)

########################
# difference method(): This return the different values from set1 to set2.

set1 = {'A','B','C','D'}
set2 = {1,2,3,4,'C','D'}

# check diff from set1 to set2
result1 = set1.difference(set2)
print('result1:',result1) #result1: {'A', 'B'}

# check diff from set2 to set1
result2 = set2.difference(set1)
print("result2:",result2) #result2: {1, 2, 3, 4}

print(set1)
print(set2)

print('_'*70)

########################
# difference_update method():  This method get the difference from one to another set and update difference value
# into target set.

set3 = {77,88,99,100}
set4 = {'a','b',88,99}

set4.difference_update(set3)
print('set4:',set4)
# set4: {'b', 'a'}
print('set3:',set3) # set3: {88, 99, 100, 77}

print('_'*70)
########################
# intersection method(): This method return the common values between 2 sets.

set_1 = {'a','b','c',70,80,90}
set_2 = {70,80,90,'d','e','f'}
result = set_2.intersection(set_1)
print(result) #{80, 90, 70}

print(set_1) # {80, 'b', 'c', 70, 'a', 90}
print(set_2) # {80, 90, 'd', 'f', 70, 'e'}

# intersection_update() :  This method update the common values between 2 sets into target set.
set_1.intersection_update(set_2)
print('set_1:',set_1) # set_1: {80, 90, 70}
print('set_2:',set_2) # set_2: {80, 'e', 90, 70, 'd', 'f'}

print('_'*70)

########################
# symmetric_difference() method: This method return the difference value from both the sets.

set_r = {'A', 'B', 456, 78, 100, 30, 40}
set_s = {'P', 'Q', 'R', 'A', 'B', 100, 40}

# difference values from both the sets
result = set_r.symmetric_difference(set_s)
print(result)
# {456, 'P', 78, 'R', 'Q', 30}

print("set_r:",set_r) # set_r: {'B', 100, 'A', 30, 456, 40, 78}
print("set_s:",set_s) # set_s: {'B', 'Q', 100, 'R', 'A', 'P', 40}

print('_'*70)

# symmetric_difference_update() method:  This method update the symmetric difference update in any of the target set/

set_s.symmetric_difference_update(set_r)
print("set_s:",set_s)
# set_s: {456, 78, 'Q', 'R', 'P', 30}
print("set_r:",set_r)
# set_r: {'B', 100, 'A', 30, 456, 40, 78}

print('_'*70)

########################
# isdisjoint() method: This method compare 2 sets values, if the target value has common value, then it is not didjoint
#              -> If any  of data in both sets is common, then isdisjoint value is False

s_1 = {'a','b',1.1,2,3}
s_2 = {'R','S',1.1,2,100}
s_3 = {'TU','MI','AN'}

print(s_1.isdisjoint(s_2)) # False
print(s_3.isdisjoint(s_1)) # True
print(s_2.isdisjoint(s_3)) # True

print('_'*70)

########################
# issupertset(), is_sub_set

s_4 = {'A','B','C','D',10,20,30}
s_5 = {10,20,30}
s_6 = {55,33,99}

print(s_5.issubset(s_4)) # True

print(s_4.issuperset(s_4)) # True
print(s_4.issuperset(s_5)) # True

print("_"*70)
######################## copy method #####################
# shallow copy

s1 = {'a','s',9.9,8.8}
s2 = s1
s2.add(7.7)

print('s1:',s1) # s1: {7.7, 8.8, 9.9, 's', 'a'}
print("s2:",s2) # s2: {7.7, 8.8, 9.9, 's', 'a'}

print("_"*70)

# deep copy :  This method copy content from one set to another, if we change any of the set, then
#               changes will not reflect on another set.

s1 = {'a','s',9.9,8.8}
s2 = s1.copy()
print(s2)
s2.add(10)

print('s1:',s1) # s1: {'a', 9.9, 's', 8.8}
print('s2:',s2) # s2: {'a', 8.8, 9.9, 10, 's'}

print("_"*70)

##############################################
# write a python program to remove all the duplicated from once users details.

l1 = ['Python', 'Programming', 'Automation', 'Python', 'Python']
s1 = set(l1)
print("Set result:",s1)
# Set result: {'Python', 'Automation', 'Programming'}
print("set result:",list(s1))
# set result: ['Automation', 'Programming', 'Python']

print('_'*70)

#Q : HW: write a python program to get all values from any person

l2 = {'Python', 'Programming', 'Language'}
# output1 = {'Py', 'Pr', 'La', 'on', 'ng', 'age'}
# output2 = {'Python', 'Progmin',  'Langue'}

output1 = set()
output2 = set()
for i in l2:
    output1.add(i[0:2])
    output1.add(i[-2:])

    output2.add(i[0:6])

print('output1:',output1)
print('output2:',output2)

print('_'*70)

#####################################
# frozenset :  This is the set data type, which is immutable in nature.

list = [10,20,30,40,50,60]
a = frozenset(list)
print(a)
# frozenset({40, 10, 50, 20, 60, 30})

# a[1]= 100
# TypeError: 'frozenset' object does not support item assignment
print('_'*70)

# Q2 :  str1 = "We are Learning Python Programming"
# i) : get reverse of the longest word in the string.
# output = 'gnimmargorP'

str1 = "We are Learning Python Programming"

a = str1.split()
print(a)
max = " "

for i in a:
    if len(i)>len(max):
        max = i
print("Longest Word:",max)
print("Reverse:",max[::-1])

# ii). Find out the second large word from givens tring.
# output = "Learning"

str1 = "We are Learning Python Programming"
b = str1.split()
max = " "
sec = " "
for i in a:
    if len(i)>len(max):
        max = i
    if len(i)>len(sec) and len(max)>len(sec):
        sec = i
print(sec)
print("Longest Word:",max)
