# p1.  program to print square of even and cube odd values in the list
list_a = [5, 8, 9, 2, 11]
# output = [125, 64, 729, 4, 1331]

output2 = []
for val in list_a:
    if val % 2 == 0:
        output2.append(val**2)
    else:
        output2.append(val**3)
print("Output :", output2)
# Output : [125, 64, 729, 4, 1331]


print("-"*50)
# p2.  program to remove duplicate values from given list
list_b = [5, 8, 9, 2, 11, 5, 8, 2, 11]
# output = [5, 8, 9, 2, 11]

output1 = []
for val in list_b:
    if val not in output1:
        print(val)
        output1.append(val)
print("Output :", output1)
# Output : [5, 8, 9, 2, 11]
