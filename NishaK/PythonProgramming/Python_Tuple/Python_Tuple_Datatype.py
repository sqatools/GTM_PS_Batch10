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


print("_"*50)
# Get Max, Min, and sum of all value in  given tuple ###################

tup4 = (5, 7, 2, 3, 55, 77, 23, 56)
print("Max value :", max(tup4))
# Max value : 77
print("Min value :", min(tup4))
# Min value : 2
print("Sum value :", sum(tup4))
# Sum value : 228


print("_"*50)
# Q1 write a tuple program to get factorial of numbers.
tup4 = (2, 3, 4, 5, 6)
# output = (2*1, 3*2*1, 4*3*2*1, 5*4*3*2*1, 6*5*4*3*2*1)
# OUTPUT = (2, 6, 24, 120, 720)
output = []

for val in tup4:
    print(val)
    fact = 1
    for i in range(val, 0, -1):
        fact = fact*i
    output.append(fact)
print(tuple(output))
# (2, 6, 24, 120, 720)


print("-"*50)
# p2 :  write a python program to get all email from given tuple value

tup5 = (
    'user1@gmail.coim',
    98098098908,
    'user2@gmail.com',
    'user3@gmail.cm',
    999909890890
)

output_list = []
for val in tup5:
    if isinstance(val, str) and "@" in val:
        print(val)
        output_list.append(val)
    else:
        continue
print("User defined email :", output_list)
# User defined email : ['user1@gmail.coim', 'user2@gmail.com', 'user3@gmail.cm']


print("-"*50)
# get common values from both tuples
tup1 = (4, 7, 9, 23, 5, 6, 12)
tup2 = (12, 4, 7, 9, 14, 6, 45)

output = []
for val in tup1:
    if val in tup2:
        output.append(val)
print(tuple(output))
# (4, 7, 9, 6, 12)
