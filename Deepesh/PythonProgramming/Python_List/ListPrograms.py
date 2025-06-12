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





