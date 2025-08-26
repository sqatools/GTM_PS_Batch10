#### get max value from given list #####
list3 = [4, 7, 12, 67, 34, 25]
max_val = 0
for val in list3:
    if val > max_val: # 4 > 0 | 7 > 4 | 12 > 7 | 67 > 12 | 34 > 67 | 25 > 67
        max_val = val # 4, 7, 12, 67
    else:
        continue

print("max val:", max_val) # max val: 67


#### #####
# program to get combination of 2 values whose sum is 10 from list.
#        i=0 j=1
list4 = [1, 5, 7, 2, 3, 8, 6, 4, 12, 9]
#output = [(1, 9), (7, 3), (2, 8), (6, 4)]
output = []

for i in range(len(list4)):
    for j in range(i+1, len(list4)):
        if list4[i]+ list4[j] == 10:
            output.append((list4[i], list4[j]))
        else:
            continue

print("output :", output)
# [(1, 9), (7, 3), (2, 8), (6, 4)]

##################################
# p1.  program to print square of even and cube odd values in the list
list_a = [5, 8, 9, 2, 11]
# output = [125, 64, 729, 4, 1331]

# p2.  program to remove duplicate values from given list
list_b = [5, 8, 9, 2, 11, 5, 8, 2, 11]
# output = [5, 8, 9, 2, 11]


print("_"*50)
#############################################
# write a python program to add all the duplicate values in the child list

# list_c = [2, 7, [3, 5, 7], [2, 4, 6, 4], [8, 1, 4, 8]]
#ouptut = [2, 7, [3, 5, 7], [2, 8, 6], [16, 1, 4]]


list_c = [2, 7, [3, 5, 7, 5, 7, 5, 8], [2, 4, 6, 4, 6, 9, 6, 4], [8, 1, 4, 8, 5, 8]]
#         [2, 7, [3, 15, 14, 8], [2, 12, 18, 9], [24, 1, 4, 5]]

output = []
# apply loop and get each value from list
for val in list_c:
    # check given val is a child list
    if isinstance(val, list):
        print(val)
        temp = []  # empty list1 # 2, 8, 6
        temp2 = [] # empty list1 # 4
        # apply loop on child
        for v1 in val: # 2, 4, 6, 4
            # get value count from child list
            v1_count = val.count(v1) # 1, 2, 2

            if v1_count > 1 and v1 not in temp2: # 2 > 1 and 4 not in temp2
                temp.append(v1*v1_count) # 8
                temp2.append(v1)  # 4
            elif v1 in temp2:
                continue
            else:
                temp.append(v1)

        print("temp :", temp)
        output.append(temp)
    else:
        output.append(val)

print(output)
# [2, 7, [3, 5, 7], [2, 8, 6], [16, 1, 4]]
# [2, 7, [3, 15, 14, 8], [2, 12, 18, 9], [24, 1, 4, 5]]

# Q1 :  write a python program to get all possible combination of values in the list whose sum is 10

list_d = [1, 7, 8, 2, 3, 9, 5, 6, 4]
"""
output:
[1, 9]
[7, 3]
[8, 2]
[6, 4]
[1, 7, 2]
[1, 5, 4]
[2, 3, 5]
[1, 2, 3, 4]
"""