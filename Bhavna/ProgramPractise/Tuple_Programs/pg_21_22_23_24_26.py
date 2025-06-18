# Tuple Practice Programs

# 21). Python tuple program to find an index of an element in a tuple.
A = ('s','q','a','t','o','o','l','s')
b = A.index('a')
print("Index of a:",b)

print('_'*70)

# 22). Python tuple program to find the length of a tuple.
A = ('v','i','r','a','t')

print("Length of A:",len(A))

print('_'*70)

# 23). Python tuple program to convert a tuple into a dictionary.
A=((5,'s'),(6,'l'))

Dict = dict(A)
print(Dict)

print('_'*70)
# 24). Python tuple program to reverse a tuple.

Input = ( 4, 6, 8, 3, 1)
Reverse = Input[::-1]
print("Reverse Tuple:",Reverse)

print('_'*70)

# 26). Python tuple program to pair all combinations of 2 tuples.

A = (2,6)
B = (3,4)

for i in A:
    for j in B:
        print((i,j), end=" ")
        print((j,i),end=" ")
print()
print('_'*70)
