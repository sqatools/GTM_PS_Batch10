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
# {1, 3.5, 4, 5, (4, 6, 7), 'Hello'} <class 'set'>

print("_"*50)
# apply loop on set data type
for val in set1:
    print(val)
"""
1
3.5
4
5
(4, 6, 7)
Hello
"""

print("_"*50)
######################## Set Methods #######
print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']

print("_"*50)
########################
# add method() :  This method add one single value at time to set data.
set_a = {4, 7, 2, 9, 'a', 'b', 56}
set_a.add(50)
print("set_a :", set_a)
# set_a : {2, 50, 4, 'a', 7, 56, 9, 'b'}

set_a.add((4, 6, 8))
set_a.add('Python')
set_a.add(True)
print("set_a :", set_a)
# {True, 2, 4, 'a', 7, 9, 'Python', 'b', (4, 6, 8), 50, 56}

# set_a.add([5, 7, 232, 667])
# print("set_a :", set_a)
# TypeError: unhashable type: 'list'


print("_"*50)
########################
# update method() :  This method update one set to data to another set.

set_b = {2, 50, 4, 'a', 7, 56, 9, 'b'}
set_c = {'P', 'Q', 'R'}
set_c.update(set_b)
print("set_c :", set_c) # {'R', 2, 4, 7, 9, 'P', 'b', 50, 'Q', 56, 'a'}
print("set_b :", set_b)  # {2, 4, 7, 9, 'b', 50, 56, 'a'}


print("_"*50)
########################
# union method() :  This method combine two sets data and return as set output.
#                   ->>  It does not modify the original set.

set_d = {2, 50, 4, 'a', 'b'}
set_e = {'P', 'Q', 'R', 'S', 'T', 'a'}
result = set_d.union(set_e)
print("result :", result)   #{2, 4, 'Q', 'S', 'R', 'a', 'P', 'b', 50, 'T'}

print("set_D :", set_d) # {2, 50, 4, 'a', 'b'}
print("set_e :", set_e) # {'Q', 'S', 'R', 'a', 'P', 'T'}


print("_"*50)
########################
# remove method() :  This method remove any specific value from set
#                    ->  If the target value is not available, then it will throw error.

set_f = {2, 50, 4, 'a', 'b', 456, 78}

# remove existing value.
set_f.remove(456)
print(set_f) # {2, 50, 4, 'b', 78, 'a'}

# remove non-existing value. :  It value is not available, it will throw error
"""
set_f.remove('P')
print(set_f)  # KeyError: 'P'
"""



print("_"*50)
########################
# discard method() : This method remove any specific value from set, as like remove method.
#                   ->  It does not throw error if the target value is not available.

set_g = {200, 50, 4, 'a', 'b', 456, 78, 100}

# discard existing value : It will work without any error
set_g.discard(78)
print("set_g:", set_g)  #
# set_g: {100, 4, 456, 'b', 200, 50, 'a'}

# discard non-existing value : If value is not available, it will now throw any error.
set_g.discard(500)
print("set_g:", set_g) # {100, 4, 456, 200, 50, 'a', 'b'}



print("_"*50)
########################
# pop method(): This method remove any random value and return it.

set_h = {200, 50, 400, 'A', 'B', 456, 78, 100}

v1 = set_h.pop()
print("removed value :", v1)
# removed value : B

print("set_h :", set_h)
# set_h : {100, 456, 200, 78, 'A', 400, 50}


print("_"*50)
########################
# difference method(): This return the different values from set1 to set2.

set_h = {'A', 'B', 456, 78, 100}
set_j = {'P', 'Q', 'R', 'A', 'B', 100}

# check diff from set_h to set_j
result1 = set_h.difference(set_j)
print("result1 :", result1) # {456, 78}

# check diff from set_j to set_h
result2 = set_j.difference(set_h)
print("result2 :", result2)   # {'R', 'Q', 'P'}

print("set h :", set_h) # {100, 456, 'A', 'B', 78}
print("set j :", set_j) # {'P', 100, 'R', 'A', 'Q', 'B'}


print("_"*50)
########################
# difference_update method():  This method get the difference from one to another set and update difference value
# into target set.

set_k = {'A', 'B', 456, 78, 100}
set_l = {'P', 'Q', 'R', 'A', 'B', 100}
set_l.difference_update(set_k)

print("set_k :", set_k) #  {'A', 100, 'B', 456, 78}
print("set_l :", set_l) # {'Q', 'P', 'R'}



print("_"*50)
########################
# intersection method(): This method return the common values between 2 sets.

set_p = {'A', 'B', 456, 78, 100, 30, 40}
set_q = {'P', 'Q', 'R', 'A', 'B', 100, 40}

result = set_p.intersection(set_q)
print("intersection result :", result)  # {40, 100, 'A', 'B'}

print("set_p :", set_p) # {100, 'B', 30, 456, 40, 'A', 78}
print("set_q :", set_q) # {100, 'P', 'Q', 'B', 40, 'R', 'A'}

# intersection_difference_update() :  This method update the common values between 2 sets into target set.
set_p.intersection_update(set_q)

print("set_p :", set_p) # {40, 'A', 100, 'B'}
print("set_q :", set_q) # {'A', 100, 40, 'Q', 'P', 'B', 'R'}
