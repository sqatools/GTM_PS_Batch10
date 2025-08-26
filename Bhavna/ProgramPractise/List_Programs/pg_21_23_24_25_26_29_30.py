# LIST PRACTICE PROGRAMS

# 21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).

a = [1,2,3,4,6,2]
b = []

b = a[::-1]
if b == a:
    print("The list is palindrome")
else:
    print("The list is not a palindrome")

print('_'*70)


# 23). Python program to add 2 lists with extend method.

l7 = [55,84,2,12]
l8 = [92,62,77,36]

l7.extend(l8)
print("Extended list:", l7)

print('_'*70)

# 24). Python program to sort list data, with the sort and sorted method.

a = [4,8,5,25,998,89,96]

# Sort method
a.sort()
print("Result of sort:",a)

b = [88,45,112,14,69,4,7,826]
result = sorted(b)
print("Result of sorted:",result)

print('_'*70)

# 25). Python program to remove data from the list from a specific index using the pop method.

c = [8,7,4,'a',15,6,2,3]
c.pop(3)
print(c)

print('_'*70)

# 26). Python program to get the max, min, and sum of the list using in-built functions.

list = [21,65,41,88,74,2]

print("Max Value:", max(list))
print("Min Value:", min(list))
print("Sum of Values:", sum(list))

print('_'*70)

# 29). Python program to find the second largest number from the list.

list_1 = [12,99,85,42,32,21]

list_1.sort()
print(list_1[-2])

print('_'*70)

# 30). Python program to find the second smallest number from the list.
list_1 = [12,1,99,85,42,32,21]

list_1.sort()
print(list_1[1])

print('_'*70)
