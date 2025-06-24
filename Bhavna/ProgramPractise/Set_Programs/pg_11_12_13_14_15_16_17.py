# SET PRACTICE PROGRAMS

# 11). Python program to check if two sets are disjoint.

s1 = {1.1,2,35,'True'}
s2 = {1.5,8,96,'False'}

print("Disjoint:",s1.isdisjoint(s2))

print('_'*70)

# 12). Python program to convert a list to a set.

l1 = [1,2,9,'j']
print("List to set:",set(l1))

print('_'*70)

# 13). Python program to convert a set to a list.
s3 = {78,98,52,2,2,'a'}
print("Set to list:",list(s3))

print('_'*70)

# 14). Python program to find the maximum element in a set.
s3 = {78,98,52,2,2}
max = max(s3)
print("Maximum value:",max)

print('_'*70)

# 15). Python program to find the minimum element in a set.
s3 = {78,98,52,2,2}
print("Minimum Value:", min(s3))

print('_'*70)

# 16). Python program to find the sum of elements in a set.

s3 = {78,98,52,2,2}
print("Sum:",sum(s3))

print('_'*70)

# 17). Python program to find the average of elements in a set.

s3 = {78,98,52,2,2}
average = sum(s3)/len(s3)
print(average)

print('_'*70)
