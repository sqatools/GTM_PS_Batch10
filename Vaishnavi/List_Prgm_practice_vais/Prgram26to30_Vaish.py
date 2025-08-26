#26). Python program to get the max, min, and sum of the list using in-built functions.

l1=[2,3,34,23,54,67,34,56,78,90,12,34]
print(min(l1),":min")
print(max(l1),":max")
print(sum(l1),":Sum")

#27). Python program to check whether a list contains a sublist.
l2=[2,3,34,23,54,67,34,56,78,90,12,34]
l2=list(set(l2))
l3=[3,34,54,67]
count=0
for i in l3:
    for j in l2:
        if i==j:
            count+=1
        else:
            continue
print(count)
print(len(l3))
if count==len(l3):
    print("list contains a sublist")
else:
    print("Not a sublist")

#28). Python program to generate all sublists with 5 or more elements in it from the given list

#29). Python program to find the second largest number from the list.
l2=[2,3,34,23,54,67,34,56,78,90,12,34]
l2.sort()
print(l2)
print("the second largest no is: ", l2[-2])

#30). Python program to find the second smallest number from the list.
l2=[2,3,34,23,54,67,34,56,78,90,12,34]
l2.sort(reverse=True)
print(l2)
print("the second smallest no is: ", l2[-2])


