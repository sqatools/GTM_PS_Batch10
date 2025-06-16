# p1.  program to print square of even and cube odd values in the list
list_a = [5, 8, 9, 2, 11]
# output = [125, 64, 729, 4, 1331]
even_output=[]
odd_output=[]

for i in range(len(list_a)):
    if list_a[i] % 2 == 0:
        even_output.append(list_a[i] ** 2)
    else:
        odd_output.append(list_a[i] ** 3)
print("even_output", even_output)
print("odd_output", odd_output)

print("_"*50)
# p2.  program to remove duplicate values from given list
list_b = [5, 8, 9, 2, 11, 5, 8, 2, 11]
# output = [5, 8, 9, 2, 11]
output2 = []
for i in range(len(list_b)):
     if list_b[i] not in output2:
        output2.append(list_b[i])
     else:
       continue
     print( output2)
