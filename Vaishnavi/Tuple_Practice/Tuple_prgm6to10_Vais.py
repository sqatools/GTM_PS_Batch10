"""6). Python tuple program to create a tuple and find an element from it by its index no.
Input = (4, 8, 9, 1)
Index = 2
Output = 9"""

Input = (4, 8, 9, 1)
out=Input[2]
print(out)
for i in range(len(Input)):
    print(Input[i]," Index : ", i)

print("-*"*50)

"""7). Python tuple program to assign values of tuples to several variables and print them.
Input = (6,7,3)
Variables = a,b,c
Output:
a, 6
b, 7
c, 3
"""
Input1= (6,7,3)
(a,b,c)=Input1
print("a",a)
print("b",b)
print("c",c)

print("-*"*50)

"""8). Python tuple program to add an item to a tuple.
Input= ( 18, 65, 3, 45)
Output=(18, 65, 3, 45, 15)"""
Inpt= ( 18, 65, 3, 45)
L2=list(Inpt)
L2.append(15)
print(tuple(L2))

print("-*"*50)

"""9). Python tuple program to convert a tuple into a string.
Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
Output = Sqatools"""

inpi=('s', 'q', 'a', 't', 'o', 'o','l','s')
output = ""
for i in inpi:
    str1=str(i)
    output=output+str1
print(output)
print("-*"*50)

"""10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
Output=
q
o"""

inpi1=('s', 'q', 'a', 't', 'o', 'o','l','s')

for i in range(len(inpi1)):
    if i in [1, 5]:
        print(inpi1[i])




