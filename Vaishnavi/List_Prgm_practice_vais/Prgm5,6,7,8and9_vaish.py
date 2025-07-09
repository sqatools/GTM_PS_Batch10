#5:Python program to find the minimum and maximum elements from the list.
list2=[23,34,12,12,9,76,46]
max_num=max(list2)
min_num=min(list2)
print("min:",min_num)
print("max:",max_num)
"""
min: 9
max: 76

"""
#6). Python program to differentiate even and odd elements from the given list.
list3=[23,34,12,12,9,76,46]
result=[(i,'even') if i%2==0 else (i,'odd') for i in list3]
print(result)#[(23, 'odd'), (34, 'even'), (12, 'even'), (12, 'even'), (9, 'odd'), (76, 'even'), (46, 'even')]

#7). Python program to remove all duplicate elements from the list.
l4=[2,4,3,5,6,5,4,3,2,5,4]
output=[]
for i in l4:
    if i not in output:
        output.append(i)
    else:
        continue
print(output)

#8 Python program to print a combination of 2 elements from the list whose sum is 10

l5=[1,2,3,4,4,5,8,7]
sum=0
output=[]
for i in l5:
    for j in l5:
        if i+j==10:
            output.append((i,j))
        else:
            continue
print(output)

#9). Python program to print squares of all even numbers in a list.
l6=[1,2,3,4,4,5,8,7]
result=[(i**2,"even",i) for i in l6 if i%2==0]
print(result)




