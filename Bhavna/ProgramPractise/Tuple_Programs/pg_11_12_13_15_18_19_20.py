# Tuple Practice Programs

# 11). Python tuple program to check whether an element exists in a tuple or not.
Input = ('p','y', 't', 'h', 'o', 'n')

if 'p' in Input:
    print("True")
else:
    print("False")

print('_'*70)

# 12). Python tuple program to add a list in the tuple.

L = [12,67]
A = (6,8,4)

output = L + list(A)
print(tuple(output))

print('_'*70)

# 13). Python tuple program to find sum of elements in a tuple.

A = (4,6,2)
print("Sum of elements:",sum(A))

print('_'*70)

# 15). Python tuple program to create a tuple having squares of the elements from the list.
Input = [1, 9, 5,  7, 6]
output = []
for i in Input:
    j = i**2
    output.append(j)

print(tuple(output))

print('_'*70)

# 18). Python tuple program to convert a list into a tuple and multiply each element by 2.

Input = [12,65,34,77]

Output = []
for i in Input:
    a = i*2
    Output.append(a)
print(tuple(Output))

print('_'*70)

# 19). Python tuple program to remove an item from a tuple.

A = ('p','y','t','h','o','n')
c = list(A)
c.pop()
# print(c)
output = tuple(c)
print("Output:",output)

print('_'*70)

# 20). Python tuple program to slice a tuple.

A = (5,7,3,4,9,0,2)

print(A[0:3])
print(A[2:5])

print('_'*70)
