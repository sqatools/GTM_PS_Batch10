"""16). Python tuple program to multiply adjacent elements of a tuple.
Input = (1,2,3,4)
Output =  (2,6,12)"""
inp1=(1,2,3,4)
out=[]
for i in range(len(inp1)):
    if i+1<len(inp1):
        l1=inp1[i]*inp1[i+1]
        out.append(l1)
print(tuple(out))


"""17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
Input:
[(3,6,7),(7,8,4),(7,3),(3,0,5)]
Output:
[(3,6,7,0,5),(7,8,4,3)]"""
inp2=[(3,6,7),(7,8,4),(7,3),(3,0,5)]
out=[]
set1={}
for j in range (len(inp2)):#0,n
    for k in range (j+1,len(inp2)):#1,n
        if inp2[j][0] == inp2[k][0]:
            l1=list(inp2[j])+list(inp2[k])
            set1=set(l1)
            l2=list(set1)
            out.append(l2)

print(tuple(out))

"""18). Python tuple program to convert a list into a tuple and multiply each element by 2.
Input = [12,65,34,77]
Output = (24, 130, 68, 154)"""

in3=[12,65,34,77]
out1=[]
for i in in3:
    out1.append((i*2))
print(tuple(out1))


"""19). Python tuple program to remove an item from a tuple.
Input:
A=(p,y,t,h,o,n)
Output: (p,y,t,o,n)"""

A=('p','y','t','h','o','n')
o1=[]
for i in A:
    if i not in'h':
        o1.append(i)
print(tuple(o1))


"""20). Python tuple program to slice a tuple.
Input:
A=(5,7,3,4,9,0,2)
Output:
(5,7,3)
(3,4,9)"""
A=(5,7,3,4,9,0,2)
print(A[:3])
print(A[2:5])




