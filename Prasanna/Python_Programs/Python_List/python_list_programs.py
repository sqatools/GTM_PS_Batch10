# Q1. Python program to calculate the square of each number from the given list.
list1 = [5, 8, 9, 2, 11]
output = []
for val in list1:
    if val % 2 == 0:
        print("Each number is:,", val, "and its Square is:", val**2)
    else:
        print("The value in List: odd", val, " and its cube is :", val**3)
# Q2 Python program to combine two lists.
# Using Concatination
list1 = [1, 2, 3, 4, 5]
list2 = [2, 5, 6, 7, 8]
combine_list = list1 + list2
print(combine_list)
list1.extend(list2)
print(list1)
# 3).Python program to calculate the sum of all elements from a list
list5 = [2, 5, 8, 0, 1]
# Printing output
print(sum(list5))
# 4)Python program to find a product of all elements from a given list.
list6 = [5, 7, 8, 5,2]
var = 1
for val in list6:
    var = val * var
print("Product of all Values is:", var)

# 5) Python program to find the minimum and maximum elements from the list.

list7 = [2, 25, 56, 78, 89]
min_value = min(list7)
max_value = max(list7)
print("minimum Value :",min_value, "\n","Maximum value :", max_value)

# 6)  Python program to differentiate even and odd elements from the given list.
list8 = [ 23, 56, 76, 78, 45, 72]
list_even = []
list_odd = []
for val in list8:
    if val%2 == 0:
        list_even.append(val)
    else:
        list_odd.append(val)
print(list_even)
print(list_odd)

# 8)Python program to remove all duplicate elements from the list.
list9 = [2, 2, 3, 5, 7, 8, 9, 8, 9, 7, 8]
dup_list = []
for val in list9:
    if val not in dup_list:
        dup_list.append(val)
print(dup_list)
# 8) Python program to print a combination of 2 elements from the list whose sum is 10.
# Importing itertools
import itertools

#Input list
list1 = [2,5,8,5,1,9]

#Creating variable
var = 10

#Creating empty list
list3 = []

for i in range(len(list1)):
    for combi in itertools.combinations(list1,i):
        if sum(combi) == var:
            list3.append(combi)

#Printing output
print(list3)

# 10) Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Odd = []
even = []
# Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
for val in Input:
    if val % 2 == 0:
        even.append(val)
    else:
        Odd.append(val)
Odd.extend(even)
print(Odd)
# 11).  Python program to get common elements from two lists.
# Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
# Output : [4, 5, 7, 2]
common_list = []
for val in list1:
    if val in list2:
        common_list.append(val)
print(common_list)

# 12). Python program to reverse a list with for loop.
list12 = [3, 5, 7, 8, 9]
reverse_list = []
#for val in range(len(list3)):
#    reverse_list = list3[::-1]
print(reverse_list)
for i in range(len(list12)-1, -1, -1):
    print(list12[i], end=" ")
print("*"*50)
# 13). Python program to reverse a list with a while loop.
a = [1, 2, 3, 4, 5, 6]
count = len(a) - 1
while count >= 0:
    print(a[count], end=" " )
    count -= 1
print()
print("-"*50, end="")

# 14) Python program to reverse a list using index slicing.
b = [11, 12, 13, 14, 15, 16]
print(b[::-1])
# 15). Python program to reverse a list with reversed and reverse methods.
c = [34, 67, 78, 98]
reverse_list = list(reversed(c))
print(reverse_list)
d = [42, 47, 98, 58]
print(d.reverse())
