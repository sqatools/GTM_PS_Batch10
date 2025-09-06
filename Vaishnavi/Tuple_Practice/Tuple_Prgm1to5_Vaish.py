"""1). Python tuple program to create a tuple with 2 lists of data.
Input lists:
list1 = [4, 6, 8]
list2 = [7, 1, 4]
Output= ((4, 7), (6, 1), (8, 4))"""

list1 = [4, 6, 8]
list2 = [7, 1, 4]
output=[]
for (i,j) in zip(list1,list2):
    print(i,":i")
    print(j,":j")
    output.append((i,j))
print(tuple(output))

print("-*"*50)

"""2). Python tuple program to find the maximum value from a tuple.
Input = (41, 15, 69, 55)
Output = 69"""
Input = (41, 15, 69, 55)
output1=max(Input)
print(output1)

print("-*"*50)

"""3). Python tuple program to find the minimum value from a tuple.
Input = (36,5,79,25)
Output = 5"""
Input1 = (36,5,79,25)
out2=min(Input1)
print(out2)

print("-*"*50)

"""4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
Input = [4,6,3,8]
Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]"""

Input2 = [4,6,3,8]
output=[]
for i in Input2:
    output.append((i,i**2))
print(output)

print("-*"*50)

"""5). Python tuple program to create a tuple with different datatypes.
Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})"""

tup1= ( 2.6, 1, 'Python', True, [5, 6, 7], (5, 1, 4), {'a': 123, 'b': 456})
print(tup1)