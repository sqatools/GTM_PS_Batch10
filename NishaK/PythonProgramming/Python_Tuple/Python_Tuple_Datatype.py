# tuple has all the properties as like list, but once we define the data in the tuple
# then we can not change it.


tup1 = (4, 'a', 8.8, (4, 6, 7), 5, 13)
print(tup1, type(tup1))
# (4, 'a', 8.8, (4, 6, 7), 5, 13) <class 'tuple'>


print("-"*50)
# Apply loop on the tuple ######

# Loop without indexing
for val in tup1:
    print(val, end=" ")
# 4 a 8.8 (4, 6, 7) 5 13


print()
print("_"*50)

# Loop with indexing
for i in range(len(tup1)):
    print(i, tup1[i])

"""
0 4
1 a
2 8.8
3 (4, 6, 7)
4 5
5 13
"""

print("_"*50)

# Slicing in the tuple #################
tup2 = (4, 6, 8, 12, 56, (3, 5), [4, 7, 1], 'Hello')

print(tup2[4:-2])  # (56, (3, 5))
print(tup2[-2][::-1])  # [1, 7, 4]
print(tup2[-1::-2])  # ('Hello', (3, 5), 12, 6)
print(tup2[::-2])  # ('Hello', (3, 5), 12, 6)
print(tup2[-1][-3])  # l
print(tup2[::-1])  # ('Hello', [4, 7, 1], (3, 5), 56, 12, 8, 6, 4)


print("_"*50)
# Methods in tuple #################
print(dir(tuple))
# 'count', 'index'


print("-"*50)
# count() method
tup_a = (5, 16, 44, 53, 4, 16, 44, 4)
print("count of 4:", tup_a.count(4))
# count of 4: 2


print("-"*50)
# index() method
print("Index of 53 :", tup_a.index(53))
# Index of 53 : 3


print("-"*50)
# Tuple variable ##########################
result = tup_a*2
print(result)
# (5, 16, 44, 53, 4, 16, 44, 4, 5, 16, 44, 53, 4, 16, 44, 4)
