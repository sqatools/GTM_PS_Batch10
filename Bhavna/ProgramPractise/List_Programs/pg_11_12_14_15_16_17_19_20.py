# LIST PRACTICE PROGRAMS

# 11).  Python program to get common elements from two lists.

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
output = []

for i in list1:
    if i in list2:
        output.append(i)
    else:
        continue
print(output)

print('_'*70)

# 12). Python program to reverse a list with for loop.

list_1 = [1,8,9,7,4,6]

list_1.reverse()
print(list_1)

print('_'*70)

# 14). Python program to reverse a list using index slicing.

list_2 = [99,88,77,44]
Reverse = list_2[::-1]
print(Reverse)

print('_'*70)

# 15). Python program to reverse a list with reversed and reverse methods.
list3 = [22,23,24,25,26]
#reverse method
list3.reverse()
print(list3)

# reversed function
list3 = [33,66,99,88]
result = list(reversed(list3))
print(result)

print('_'*70)
# 16). Python program to copy or clone one list to another list.
l1 = [1,2,3,4,5]
l2 = l1
print(l2)

l3 = [8,6,4,5]
l5 = l3.copy()
print("Output:",l5)
print('_'*70)

# 17). Python program to return True if two lists have any common member.

li = [1,2,3,4]
li1 = [1,8,5,4]

for i in li:
    if i in li1:
        print(True)
    else:
        continue

print('_'*70)

# 19). Python program to remove negative values from the list.
list_a = [8,7,-4,6,52,-36,87,41,-99]

for i in list_a:
    if i>=0:
        print(i)

print('_'*70)

# 20). Python program to get a list of all elements which are divided by 3 and 7.

list_b = [3,14,21,9,7]
output = []
for j in list_b:
    if j%3 == 0 and j%7 == 0:
        output.append(j)

print("Output:",output)
print('_' * 70)
