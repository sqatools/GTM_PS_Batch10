# LISTPRACTICE PROGRAMS

# 1). Python program to calculate the square of each number from the given list.

list = [1,2,3,4,5]
output = []

for i in list:
    output.append(i**2)
print("Square of each no.:",output)

print('_'*70)

# 2.Python program to combine two lists.

l1 = [1,4,7,2]
l2 = [5,8,3,6]
Result = l1+l2
print(Result)

print('_'*70)

# 3). Python program to calculate the sum of all elements from a list.
list1 = [8,5,2,3,9,1,2]
print("Sum of list:",sum(list1))

print('_'*70)

# 5. Python program to find the minimum and maximum elements from the list.
list2 = [8,12,36,14,75]
print("Max value:",max(list2))
print("Min Value:", min(list2))

print('_'*70)

# 6. Python program to differentiate even and odd elements from the given list.

l1 = [1,5,6,3,8,4,52,74,39]
even = []
odd = []

for i in l1:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even No.:",even)
print("Odd No.:",odd)

print('_'*70)

# 7. Python program to remove all duplicate elements from the list.

list3 = [8,9,5,9,4,56,67,95,12,95]
output = []

for j in list3:
    if j not in output:
        output.append(j)

print("output:",output)

print('_'*70)

# 9). Python program to print squares of all even numbers in a list.

list4 = [1,2,3,4,5,6]
output = []

for k in list4:
    if k%2 == 0:
        output.append(k**2)
    else:
        continue
print(output)
