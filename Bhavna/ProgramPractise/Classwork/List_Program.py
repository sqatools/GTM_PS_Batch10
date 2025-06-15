# 13/06/2025 SESSION CONTINUE

#### get max value from given list #####
list1 = [8,7,25,74,70]
max_value = 0

for val in list1:
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

print('_'*70)

#######################################
# 13/06/2025 Session
# write a python program to add all the duplicate values in the child list
# list_c = [2, 7, [3, 5, 7], [2, 4, 6, 4], [8, 1, 4, 8]]
# ouptut = [2, 7, [3, 5, 7], [2, 8, 6], [16, 1, 4]]


list_c = [2, 7, [3, 5, 7], [2, 4, 6, 4], [8, 1, 4, 8]]

output = []
# apply loop and get each value from list
for val in list_c:
    # check given val is a child list
    if isinstance(val, list):
        print(val)
        temp = []
        temp2 = []
        # apply loop on child
        for v1 in val:
            # get value count from child list
            v1_count = val.count(v1)

            if v1_count>1 and v1 not in temp2:
                temp.append(v1*v1_count)
                temp2.append(v1)
            elif v1 in temp2:
                continue
            else:
                temp.append(v1)

        print("temp:",temp)
        output.append(temp)
    else:
        output.append(val)
print(output)

print('_'*70)

