# 1. program to print square of even values and cube of odd values
list_a = [5, 8, 9, 2, 11]
even_output = []
odd_output = []

for i in range(len(list_a)):
    if list_a[i] % 2 == 0:
        even_output.append(list_a[i] ** 2)
    else:
        odd_output.append(list_a[i] ** 3)
print("even_output", even_output)
print("odd_output", odd_output)

# 2.Python program to calculate the square of each number from the given list.
list_b = [4, 3, 6, 2]
list_b_output = []
for num in range(len(list_b)):
    list_b_output.append(list_b[num] ** 2)
print("Square of given list :", list_b_output)

# 3.Python program to combine two lists.
list_c = [4, 3, 6, 2]
list_d = ['a', 'b', 'c']
output = list_c + list_d
print(output)

# 4. Python program to combine two lists using extend method
list_c = [4, 3, 6, 2]
list_d = ['a', 'b', 'c']
output1 = list_c.extend(list_d)
print(output)

# 5. Problem to print the sum of all elements in a list.
list_e = [10, 20, 30, 40]

sum1 = 0

for val in list_e:
    sum1 += val
print(sum1)

# 6.  program to remove duplicate values from given list
list_f = [5, 8, 9, 2, 11, 5, 8, 2, 11]
# output = [5, 8, 9, 2, 11]
output2 = []
for i in range(len(list_f)):
    if list_f[i] not in output2:
        output2.append(list_f[i])
    else:
        continue
print(output2)
