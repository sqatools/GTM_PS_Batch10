# LIST ASSIGNMENT

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


# 13/06/2025 Session
# Assignment List

# Q1 :  write a python program to get all possible combination of values in the list whose sum is 10
# list_d = [1, 7, 8, 2, 3, 9, 5, 6, 4]
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

list_d = [1, 7, 8, 2, 3, 9, 5, 6, 4]
output = []
for i in range(len(list_d)):
    for j in range((i+1),len(list_d)):
        if list_d[i] + list_d[j] == 10:
            output.append((list_d[i],list_d[j]))
        for k in range((j+1),len(list_d)):
            if list_d[i]+list_d[j]+list_d[k] == 10:
                output.append((list_d[i],list_d[j],list_d[k]))
            for l in range((k+1),len(list_d)):
                if list_d[i]+list_d[j]+list_d[k]+list_d[l] == 10:
                    output.append((list_d[i], list_d[j], list_d[k], list_d[l]))

        else:
            continue
print("output:",output)
