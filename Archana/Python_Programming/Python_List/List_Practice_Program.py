# 1. program to print square of even values and cube of odd values
list_a = [5, 8, 9, 2, 11]
even_output = []
odd_output = []

for i in range(len(list_a)):
    if list_a[i] % 2 == 0:
        even_output.append(list_a[i]**2)
    else:
        odd_output.append(list_a[i]**3)
print("even_output", even_output)
print("odd_output", odd_output)
