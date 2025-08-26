
# SET PRACTICE PROGRAMS

# 1). Python program to create a set with some elements.

set_1 = {1,2.2,3,(4,5,6),True}
print(set_1,type(set_1))

print('_'*70)

# 2). Python program to add an element to a set.

set_2 = {1,2.2,3,(4,5,6),True}
set_2.add(100)

print("Adding a element:",set_2)

print('_'*70)

set_3 = {1,2.2,3,(4,5,6),True}
set_3.remove(2.2)
print("set_3:",set_3)

print('_'*70)

# 4). Python program to find the length of a set.

set_4 = {1,2.2,3,(4,5,6),True}
r = len(set_4)
print(r)

print('_'*70)

# 5). Python program to check if an element is present in a set.

set_5 = {1,2.2,3,(4,5,6),True}
if 2.2 in set_5:
    print("Yes")
else:
    print("No")

print('_'*70)

# 6). Python program to find the union of two sets.

set_6 = {3,4.4,'r','d'}
set_7 = {'a','g',3,1.6,7}
result = set_6.union(set_7)
print("Union:",result)

print('_'*70)

# 7). Python program to find the intersection of two sets.

set_8 = {3,4.4,'r','d',7}
set_9 = {'a','g',3,1.6,7}
result = set_8.intersection(set_9)
print("Intersection:",result)

print('_'*70)

# 8). Python program to find the difference of two sets.
set_8 = {3,4.4,'r','d',7}
set_9 = {'a','g',3,1.6,7}
result = set_9.difference(set_8)
print("Difference:",result)

print('_'*70)

# 9). Python program to find the symmetric difference of two sets.
set_8 = {3,4.4,'r','d',7}
set_9 = {'a','g',3,1.6,7}
result = set_8.symmetric_difference(set_9)
print("Symmetric difference:",result)

print('_'*70)

# 10). Python program to show if one set is a subset of another set.

set_8 = {3,4.4,'r','d',7}
set_9 = {3,7}
print("Subset:",set_9.issubset(set_8))

print('_'*70)
