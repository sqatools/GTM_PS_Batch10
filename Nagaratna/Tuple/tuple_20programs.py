
# 2). Python tuple program to find the maximum value from a tuple.
value = (41, 15, 69, 55)
output=max(value)
print(output)
"""
Output: 
69
"""
#3). Python tuple program to find the minimum value from a tuple.
value2 = (36,5,79,25)
output2 = min(value2)
print(output2)

# Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
input1 = [4, 6, 3, 8]
output = []

for num in input1:
    output.append((num, num * num))

print(output)
"""
output:
[(4, 16), (6, 36), (3, 9), (8, 64)]
"""
#Python tuple program to create a tuple and find an element from it by its index no.
tup = (4,8,20,90)
print("Number in the tuple with index 2: ",tup[2])
print("*_*"*20)
#16). Python tuple program to multiply adjacent elements of a tuple.
val1 = (1,2,3,4)
test=[]
for m in val1:
    for n in val1:
        z=m*n
    test.append(z)
val1=test
print(val1)

#Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
# take input list value that contains multiple tuples
l1 = [(3, 6, 7), (7, 8, 4), (7, 3), (3, 0, 5)]

outcme = []
for i in range(len(l1)):
 for j in range(i+1, len(l1)):
        if l1[i][0] == l1[j][0]:
            outcme.append(tuple(tuple(l1[i]) + tuple(l1[j][1:])))

print(outcme)