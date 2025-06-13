# 13/06/2025 SESSION CONTINUE

#### get max value from given list #####
list = [8,7,25,74,70]
max_value = 0

for val in list:
    if val>max_value:
        max_value = val
    else:
        continue
print("max_value:",max_value)
print('_'*70)

# program to get combination of 2 values whose sum is 10 from list.
list1 = [1,5,7,2,3,8,6,4,12,9]
output = []

for i in range(len(list1)):
    for j in range((i+1),len(list1)):
        if list1[i] + list1[j] == 10:
            output.append((list1[i],list1[j]))
        else:
            continue
print("output:",output)

print('_'*70)
# p1.  program to print square of even and cube of odd values in the list
list_a = [5, 8, 9, 2, 11]
# output = [125, 64, 729, 4, 1331]
output = []

for i in list_a:
    if i % 2 ==0:
        output.append(i**2)
    else:
        output.append(i**3)
print(output)

print('_'*70)

# p2.  program to remove duplicate values from given list
list_b = [5, 8, 9, 2, 11, 5, 8, 2, 11]
# output = [5, 8, 9, 2, 11]

output = []

for j in list_b:
    if j not in output:
        output.append(j)

print(output)