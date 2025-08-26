"""11). Python tuple program to check whether an element exists in a tuple or not.
Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
P in A
Output=
True"""
Input=('p','y','t','h','o','n')
for i in Input:
    if i in 'p':
        print(i,"True")
    else:
        print(i,"Flase")

print("-*"*50)


"""12). Python tuple program to add a list in the tuple.
Input:
L=[12,67]
A=(6,8,4)
Output:
A=(6,8,4,12,67)"""
L=[12,67]
A=(6,8,4)
A=list(A)+L
print(tuple(A))

print("-*"*50)


"""13). Python tuple program to find sum of elements in a tuple.
Input:
A=(4,6,2)
Output:
12"""

A=(4,6,2)
out=sum(A)
print("Sum :",out)

print("-*"*50)

"""14). Python tuple program to add row-wise elements in Tuple Matrix
Input:
A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
B = (3,6)
Output:
[[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]"""

A = [[('sqa', 4)], [('tools', 8)]]
B = (3,6)
out=[]
for i in range (len(A)):
    l1=list(A[i][0])
    print(l1)
    if i < len(B):
        l1.append(B[i])
        out.append(tuple(l1))
print(out)
print("*"*50)

a = [[[('sqa', 4)]], [[('tools', 8)]],[[('A',10)]]]
b = (3,6,'a')
out=[]
for i in range(len(a)):
    l1=list(a[i][0][0])
    if i<len(b):
        l1.append(b[i])
        out.append(l1)
print(tuple(out))


print("$"*50)
a1=[('sqa', 4), ('tools', 8),('A',10)]
b1 = (3,6,'a')
o2=[]
for j in range(len(a1)):
    l1=list(a1[j])
    print(l1)
    if j < len(b1):
        l1.append(b1[j])
        o2.append(l1)
print(o2)
print("*"*50)

"""15). Python tuple program to create a tuple having squares of the elements from the list.
Input = [1, 9, 5,  7, 6]
Output = (1, 81, 25, 49, 36)"""
Input1= [1, 9, 5,  7, 6]
out2=[]
for i1 in Input1:
    i1=i1**2
    out2.append(i1)
print(tuple(out2))





