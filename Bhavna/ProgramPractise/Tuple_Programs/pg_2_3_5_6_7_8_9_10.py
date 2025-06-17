
# Tuple Practice Programs

# 2). Python tuple program to find the maximum value from a tuple.
Input = (41, 15, 69, 55)
print("Max Value:",max(Input))

print('_'*70)

# 3). Python tuple program to find the minimum value from a tuple.
Input = (36,5,79,25)
print("Min Value:", min(Input))

print('_'*70)

# 5). Python tuple program to create a tuple with different datatypes.

tup = (2.6, 1, 'Python', True, [5, 6, 7], (5, 1, 4), {'a': 123, 'b': 456})
print(tup)

print('_'*70)

# 6). Python tuple program to create a tuple and find an element from it by its index no.
Input = (4, 8, 9, 1)
# Index = 2

print("Output:",Input[2])

# 7). Python tuple program to assign values of tuples to several variables and print them.

Input = (6,7,3)
# Variables = a,b,c
(a,b,c) = Input

print("a:",a)
print("b:",b)
print("c:",c)

print('_'*70)

# 8). Python tuple program to add an item to a tuple.
Input = (18, 65, 3, 45)
list = list(Input)
list.append(41)
print(tuple (list))

print('_'*70)

# 9). Python tuple program to convert a tuple into a string.
Input = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
for i in Input:
    print(i, end="")
print(type(i))

print('_'*70)

# 10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
Input = ('s', 'q', 'a', 't', 'o', 'o' ,'l', 's')

print(Input[1])
print(Input[-3])

print('_'*70)
