#16). Python program to copy or clone one list to another list.
list4 = [2, 5, 8, 3, 4, 7,8]
list5=list4.copy()
print(list5)#[2, 5, 8, 3, 4, 7, 8]
print(list4)#[2, 5, 8, 3, 4, 7, 8]

#17). Python program to return True if two lists have any common member.
l4 = [2, 5, 8, 3, 4, 7,8]
l5 = [2, 5, 8, 3, 4, 7,8]

if l4==l5:
    print("true")#true
else:
    print("false")

#18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.

l6 = [2, 5, 8, 3, 4, 7,8,10]
output=[]
for i in range(len(l6)):
    if i not in(1,3,6):
        output.append(l6[i])
print(output)

#19). Python program to remove negative values from the list.

l6 = [2, 5, 8, 3, 4, 7,-18,10]
for val in l6:
    if val>0:
      print(val)

#20). Python program to get a list of all elements which are divided by 3 and 7.
l6 = [2, 5, 8, 3, 4, 7,18,10,21, 42, 63, 84, 105, 126, 147, 168, 189, 210]
result=[val for val in l6 if val%3==0 and val%7==0]
print(result) #[21, 42, 63, 84, 105, 126, 147, 168, 189, 210]

