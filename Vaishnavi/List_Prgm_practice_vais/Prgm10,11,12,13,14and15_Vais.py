"""10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]"""
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
odd=[]
even=[]
for i in Input:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
output=odd+even

print(even)
print(odd)
print(output)#[5, 7, 11, 17, 19, 2, 8, 12, 22]

"""11).  Python program to get common elements from two lists.
Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]"""
list1 = [4, 5, 7, 9, 2,2, 1]
list2 = [2, 5, 8, 3, 4, 7]
output=[]
for i in list1:
    for j in list2:
        if i==j:
            if i not in output:
               output.append(i)
        else:
            continue
print(output) #[4, 5, 7, 2]


#12). Python program to reverse a list with for loop.

list3 = [2, 5, 8, 3, 4, 7]
len1=len(list3)
for i in range(len1-1,-1,-1):
    print(list3[i])
print("-"*50)
#13). Python program to reverse a list with a while loop.
len2=len(list3)
count=len2-1
while count>-1:
    print(list3[count])
    count-=1
print("-"*50)
#14). Python program to reverse a list using index slicing.
output=list3[-1::-1]
print(output)

print("-"*50)
#15). Python program to reverse a list with reversed and reverse methods.

list3 = [2, 5, 8, 3, 4, 7,8]
list3.reverse()
print(list3) #[8, 7, 4, 3, 8, 5, 2]

print("-"*50)

list4 = [2, 5, 8, 3, 4, 7,8]
out1= list(reversed(list4))
print(list4)
print(out1)#[8, 7, 4, 3, 8, 5, 2]







