dict1 = {'A': 567, 'B': 789,'C': 456}
dict2 = {}
temp = dict1.copy
for val in temp:
    v1 = dict1.pop(val)
    dict2[val] = v1
print("dictionary", dict1)
print("dictionary", dict2)

