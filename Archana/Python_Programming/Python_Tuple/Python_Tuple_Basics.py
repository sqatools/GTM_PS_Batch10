# 1. Write a tuple program to get factorial of numbers
tuple4 = (2, 3, 4, 5, 6)
# output3 = (2*1, 3*2*1, 4*3*2*1, 5*4*3*2*1, 6*5*4*3*2*1)
output3 = []
for val in tuple4:
    print(val)
    fact = 1
    for i in range(val, 0, -1):
        fact = fact * i
    output3.append(fact)
print(tuple(output3))

# 2. Write a tuple program to get the common values from the tuples given
tup6 = (4, 7, 9, 23, 5, 6)
tup7 = (12, 4, 7, 9, 34, 6, 45)
output4 = []

for val in tup7:
    if val in tup6:
        output4.append(val)
    else:
        continue
print(tuple(output4))

# 3. Write a tuple program to print the email from the list of tuples values given
tup5 = ('user1@gmail.com',
        984078659898,
        'user2@gmail.coim',
        984078659898,
        'user3@gmail.cm')
output5 = []
for val in tup5:
    if isinstance(val, str) and "@" in val:
        output5.append(val)
print(output5)

# 4. Python tuple program to create a tuple with 2 lists of data.
list1 = [4, 6, 8]
list2 = [7, 1, 4]
# Output= ((4, 7), (6, 1), (8, 4))
output6 = []
output6 = tuple(zip(list1,list2))
print(output6)





