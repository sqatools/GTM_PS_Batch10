#31). Python program to merge all elements of the list in a single entity using a special character.
l2=['a','3','b']
print("$".join(l2))

"""#32). Python program to get the difference between two lists.

l1=[2,3,4,5,6]
l3=[4,5,6,7,8,9]
result=[]

for i in l1:
    for j in l3:
        if j not in i:
            result.append(j)
print(result)"""

"""#33). Python program to reverse each element of the list.
Input = [‘Sqa’, ‘Tools’, ‘Online’, ‘Learning’, ‘Platform’]
output = [‘aqS’, ‘slooT’, ‘enilno’, ‘gninraeL’, ‘mroftalP’]
"""
input1=['Sqa','Tools','Online','Learning','Platform']
output=[]
for val in input1:
   val= val[-1::-1]
   output.append(val)
print(output)

"""34). Python program to combine two list elements as a sublist in a list.
list1 = [3, 5, 7, 8, 9]
list2 = [1, 4, 3, 6, 2]
Output = [[3, 1], [5, 4], [7, 3], [8, 6], [9, 2]]"""
list1 = [3, 5, 7, 8, 9]
list2 = [1, 4, 3, 6, 2]
out1=[]

for (i,j) in zip(list1,list2):
    out1.append(list((i,j)))
print(out1)

#Sort a List Without Using
nums = [5, 2, 9, 1]

for i in range (len(nums)):

    for j in range(i+1, len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j] = nums[j] , nums[i]
            print(nums)
print(nums)



