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



set1 = {1, 3.5, 'Hello', (4, 6, 7), True, 4, 5, 3.5, 1}
print(set1, type(set1))
# {1, 3.5, 4, 5, 'Hello', (4, 6, 7)} <class 'set'>


print("-"*50)
# Apply loop on set
for val in set1:
    print(val)
# 1
# 3.5
# 4
# 5
# (4, 6, 7)
# Hello


print("-"*50)
# SET METHODS
print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'


print("-"*50)
# add method() :  This method add one single value at time to set data.
set_a = {4, 7, 2, 9, 'a', 'b', 56}
set_a.add(50)
print("set_a :", set_a)
# set_a : {2, 50, 4, 7, 56, 9, 'a', 'b'}

set_a.add((4, 6, 8))
set_a.add('Python')
set_a.add(True)
print("set_a :", set_a)
# set_a : {True, 2, 4, 7, 9, 'b', 'a', (4, 6, 8), 50, 56, 'Python'}


print("-"*50)
# update method() :  This method update one set to data to another set.

set_b = {2, 50, 4, 'a', 7, 56, 9, 'b'}
set_c = {'P', 'Q', 'R'}
set_c.update(set_b)
print("set_b :", set_b)
# set_b : {2, 4, 7, 9, 'b', 50, 56, 'a'}
print("set_c :", set_c)
# set_b : {2, 4, 7, 9, 'b', 50, 56, 'a'}
# set_c : {2, 4, 7, 9, 'b', 50, 'P', 56, 'Q', 'R', 'a'}


print("-"*50)
# union method() :
# This method combine two sets data and return as set output.
# It does not modify the original set.

set_d = {2, 50, 4, 'a', 'b'}
set_e = {'P', 'Q', 'R', 'S', 'T', 'a'}
result = set_d.union(set_e)
print("result :", result)
# result : {2, 4, 'T', 'P', 'R', 'a', 'b', 'Q', 50, 'S'}
print("set_d :", set_d)
# set_d : {2, 50, 4, 'a', 'b'}
print("set_e :", set_e)
# set_e : {'Q', 'T', 'S', 'P', 'R', 'a'}


print("-"*50)
# remove method() :
# This method remove any specific value from set
# If the target value is not available, then it will throw error.

set_f = {2, 50, 4, 'a', 'b', 456, 78}

# remove existing value.
set_f.remove(456)
print(set_f)
# {'a', 2, 50, 4, 78, 'b'}

# remove non-existing value. :  It value is not available, it will throw error
"""
set_f.remove('P')
KeyError: 'P'
"""

print("-"*50)
# discard method() :
# This method remove any specific value from set, as like remove method.
# It does not throw error if the target value is not available.

set_g = {200, 50, 4, 'a', 'b', 456, 78, 100}

# discard existing value : It will work without any error
set_g.discard(78)
print("set_g:", set_g)
# set_g: {100, 4, 'a', 456, 200, 50, 'b'}


# discard non-existing value : If value is not available, it will now throw any error.
set_g.discard(500)
print("set_g:", set_g)
# set_g: {100, 4, 'b', 456, 200, 50, 'a'}


print("-"*50)
# pop method(): This method remove any random value and return it.

set_h = {200, 50, 400, 'A', 'B', 456, 78, 100}

v1 = set_h.pop()
print("removed value :", v1)
# removed value : 100
print("set_h :", set_h)
# set_h : {200, 456, 'A', 78, 400, 50, 'B'}


print("-"*50)
# difference method(): This return the different values from set1 to set2.

set_h = {'A', 'B', 456, 78, 100}
set_j = {'P', 'Q', 'R', 'A', 'B', 100}

# check diff from set_h to set_j
result1 = set_h.difference(set_j)
print("result1 :", result1)
# result1 : {456, 78}

# check diff from set_j to set_h
result2 = set_j.difference(set_h)
print("result2 :", result2)
# result2 : {'P', 'Q', 'R'}

print("set h :", set_h)
# set h : {'A', 100, 'B', 456, 78}
print("set j :", set_j)
# set j : {'R', 100, 'A', 'B', 'Q', 'P'}


print("-"*50)
# difference_update method():
# This method get the difference from one to another set and update difference value into target set.

set_k = {'A', 'B', 456, 78, 100}
set_l = {'P', 'Q', 'R', 'A', 'B', 100}
set_l.difference_update(set_k)

print("set_k :", set_k)
# set_k : {'B', 100, 'A', 456, 78}
print("set_l :", set_l)
# set_l : {'P', 'R', 'Q'}


print("-"*50)
# intersection method():
# This method return the common values between 2 sets.

set_p = {'A', 'B', 456, 78, 100, 30, 40}
set_q = {'P', 'Q', 'R', 'A', 'B', 100, 40}

result = set_p.intersection(set_q)
print("Intersection result :", result)
# Intersection result : {40, 'B', 100, 'A'}

print("set_p :", set_p)
# set_p : {100, 30, 'A', 456, 40, 78, 'B'}
print("set_q :", set_q)
# set_q : {'R', 100, 'Q', 'A', 40, 'B', 'P'}


print("-"*50)
# intersection_update() :
# This method update the common values between 2 sets into target set.

set_p.intersection_update(set_q)

print("set_p :", set_p)
# set_p : {40, 'A', 100, 'B'}
print("set_q :", set_q)
# set_q : {'P', 100, 'A', 'Q', 'R', 40, 'B'}


print("-"*50)
# symmetric_difference() method:
# This method return the difference value from both the sets.

set_r = {'A', 'B', 456, 78, 100, 30, 40}
set_s = {'P', 'Q', 'R', 'A', 'B', 100, 40}

# difference values from both the sets
result = set_r.symmetric_difference(set_s)
print("result :", result)
# result : {'P', 'Q', 456, 78, 'R', 30}
print("set_r :", set_r)
# set_r : {100, 'B', 30, 456, 'A', 40, 78}
print("set_s :", set_s)
# set_s : {'P', 100, 'Q', 'B', 40, 'A', 'R'}


print("-"*50)
# isdisjoint() method:
# This method compare 2 sets values, if the target value has common value, then it is not disjoint
# If any of data in both sets is common, then isdisjoint value is False

set_u = {'A', 'B', 456, 78, 100, 30, 40}
set_v = {'P', 'Q', 'R', 'A', 'B', 100, 40}
set_w = {'RR', 'QQ', 'NM', 'RE'}

print(set_u.isdisjoint(set_v))
# False
print(set_w.isdisjoint(set_u))
# True
print("output 1  from set_v:", set_w.isdisjoint(set_v))
# output 1  from set_v: True


print("-"*50)
# issuperset()
# is_sub_set

set_x = {'A', 'B', 456, 78, 100, 30, 40, 'P1', 'P2'}
set_y = {'A', 'B'}
set_z = {'P', 'Q', 'R'}

print("is subset :", set_y.issubset(set_x))
# is subset : True
print("set result is dis-joined")

print("is superset :", set_x.issuperset(set_x))
# issubset : True
print("is superset :", set_x.issuperset(set_y))
# is superset  : False


print("-"*50)
# copy method
# shallow copy

set_x1 = {'A', 'B', 456, 78, 'P1', 'P2'}
set_y1 = set_x1
set_y1.add(600)

print("set_x1 :", set_x1)
# {'A', 456, 'B', 600, 'P1', 'P2', 78}
print("set_y1 :", set_y1)
# {'A', 456, 'B', 600, 'P1', 'P2', 78}


print("-"*50)
# deep copy :
# This method copy content from one set to another, if we can changes any of the set, then
# changes will not reflect on another set.


set_aa = {'A', 'B', 456, 78, 'P1', 'P2'}
set_bb = set_aa.copy()
print(set_bb)
set_bb.add(700)

print("set_bb :", set_bb)
# {'B', 'A', 456, 'P2', 700, 'P1', 78}
print("set_aa :", set_aa)
# {'B', 'A', 456, 'P2', 'P1', 78}


print("-"*50)
# write a python program to remove all the duplicated from once users details.

l1 = ['Python', 'Programming', 'Automation', 'Python', 'Python']
s1 = set(l1)
print("set result :", s1)
# set result : {'Programming', 'Python', 'Automation'}
print("set result :", list(s1))
# ['Programming', 'Python', 'Automation']


print("-"*50)
# Q : HW: write a python program to get all values from any person
l2 = {'Python', 'Programming', 'Language'}
# output1 = {'Py', 'Pr', 'La', 'on', 'ng', 'ge'}
# output2 = {'Python', 'Progra',  'Langua'}

output1 = set()
for word in l2:
    first_two = word[:2]
    last_two = word[-2:]
    output1.add(first_two)
    output1.add(last_two)

print("output1 :", output1)
# {'Py', 'on', 'La', 'ge', 'ng', 'Pr'}


print("_"*50)
output2 = set()
for word in l2:
    sub_str = word[:6]
    output2.add(sub_str)

print("output :", output2)
# {'Langua', 'Progra', 'Python'}


print("-"*50)
#####################################
# frozenset :  This is the set data type, which is immutable in nature.
list1 = [40, 50, 60, 7, 20, 40, 8, 40]
var1 = frozenset(list1)
print(var1)
# frozenset({7, 40, 8, 50, 20, 60})

# var1[1] = 700
# TypeError: 'frozenset' object does not support item assignment

# var1.add(100)
#     ^^^^^^^^
# AttributeError: 'frozenset' object has no attribute 'add'
