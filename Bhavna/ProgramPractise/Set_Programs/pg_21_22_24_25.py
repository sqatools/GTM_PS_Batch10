# SET PRACTICE PROGRAMS

# 21). Python program to check if a set is a proper subset of another set.

s1 = {1,2,3,4,5,6}
s2 = {5,6}

Result = s2.issubset(s1)
print(Result)

print('_'*70)

# 22). Python program to find the cartesian product of two sets.

s1 = {1,2,3}
s2 = {4,5,6}
output = set()

for i in s1:
    for j in s2:
        output.add((i,j))

print(output)

print('_'*70)

# 24). Python program to remove all elements from a set.

s3 = {1,2,3,4,5,6}
s3.clear()
print(s3)

print('_'*70)

# 25). Python program to remove a random element from a set.

s1 = {9,8,7,6,5,4,8}
output = s1.pop()
print("Removed Value:",output)
print(s1)

print('_'*70)

# 26). Python program to find the difference between two sets using the “-” operator.
s1 = {9,8,7}
s2 = {7,8,4}
s3 = s1-s2
print(s3)
