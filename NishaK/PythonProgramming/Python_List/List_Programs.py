# get max value from given list

list1 = [4, 7, 12, 67, 34, 25]
max_val = 0
for val in list1:
    if val > max_val:
        max_val = val
    else:
        continue
print("Max value :", max_val)
# Max value : 67


print("-"*50)
# program to get combination of 2 values whose sum is 10 from list.
#        i=0 j=1
list4 = [1, 5, 7, 2, 3, 8, 6, 4, 12, 9]
# output = [(1, 9), (7, 3), (2, 8), (6, 4)]
output = []

for i in range(len(list4)):
    for j in range(i+1, len(list4)):
        if list4[i] + list4[j] == 10:
            output.append((list4[i], list4[j]))
        else:
            continue
print("Output :", output)
# Output : [(1, 9), (7, 3), (2, 8), (6, 4)]


print("-"*50)
# write a python program to add all the duplicate values in the child list

list_c = [2, 7, [3, 5, 7], [2, 4, 6, 4], [8, 1, 4, 8]]
# output = [2, 7, [3, 5, 7], [2, 8, 6], [16, 1, 4]]

output5 = []
for val in list_c:
    if isinstance(val, list):
        print(val)
        temp = []
        temp2 = []
        for v1 in val:
            v1_count = val.count(v1)
            if v1_count > 1 and v1 not in temp2:
                temp.append(v1*v1_count)
                temp2.append(v1)
            elif v1 in temp2:
                continue
            else:
                temp.append(v1)
        print("temp :", temp)
        output5.append(temp)
    else:
        output5.append(val)
print("Output :", output5)
# Output : [2, 7, [3, 5, 7], [2, 8, 6], [16, 1, 4]]


print("-"*50)
list_z = [2, 7, [3, 5, 7, 5, 7, 5, 8], [2, 4, 6, 4, 6, 9, 6, 4], [8, 1, 4, 8, 5, 8]]
# Output = [2, 7, [3, 15, 14, 8], [2, 12, 18, 9], [24, 1, 4, 5]]

output6 = []
for val in list_z:
    if isinstance(val, list):
        print(val)
        temp = []
        temp2 = []
        for v1 in val:
            v1_count = val.count(v1)
            if v1_count > 1 and v1 not in temp2:
                temp.append(v1*v1_count)
                temp2.append(v1)
            elif v1 in temp2:
                continue
            else:
                temp.append(v1)
        print("temp :", temp)
        output6.append(temp)
    else:
        output6.append(val)
print("Output :", output6)
# Output : [2, 7, [3, 15, 14, 8], [2, 12, 18, 9], [24, 1, 4, 5]]
