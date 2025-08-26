#1). Python program to calculate the square of each number from the given list.

list =[3,72,23,1,50,4]
for value in list:
    print("Square of the number is",value*2)
"""
Output:Square of the number is 6
Square of the number is 144
Square of the number is 46
Square of the number is 2
Square of the number is 100
Square of the number is 8
"""
 #2). Python program to combine two lists.
list1 = [5,34,98,34,'w','f']
list2 = ['xyz',100,3,'r']
output = list1+list2
print(output)
"""
output:
[5, 34, 98, 34, 'w', 'f', 'xyz', 100, 3, 'r']
"""
#3). Python program to calculate the sum of all elements from a list.

list3 =[3,5,9,10]
list4 = [2,6,100,200]
val = sum(list4+list3)
print("Sum of the two list is",val)
"""
Output:
Sum of the two list is 335
"""
# 4.Python program to find the minimum and maximum elements from the list.
list5 = [99,5,34,90,1,0]
maxi =max(list5)
mini = min(list5)
print ("maximum values",maxi)
print("minimum values",mini)
"""
Outpot:
maximum values 99
minimum values 0
"""
#Python program to differentiate even and odd elements from the given list.
list6 = [4,7,12,9,11,78,111,44]
even = []
odd = []
for i in list6:
    if i%2 ==0:
        even.append(i)
    else:
        odd.append(i)
print("odd numbers are",odd)
print("even numbers are:", even)
"""
Output:
odd numbers are [7, 9, 11, 111]
even numbers are: [4, 12, 78, 44]
"""
##Python program print the number lesser than by 10 and square of the number.
list7 = [3,7,2,8,10,30,1]

eve =[]
for k in list7:
    if k % 2 == 0:
     eve.append(k**2)
print("Square of the numbers is", eve)
"""
Output:
Square of the numbers is [4, 64, 100, 900]
"""
#8). Python program to print a combination of 2 elements from the list whose sum is 10.
my_list = [1,45,9,5,4,5]
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] + my_list[j] == 10:

            print(my_list[i],"+",my_list[j],"=10")
"""
output:
1 + 9 =10
5 + 5 =10
"""
#). Python program to print a combination of 2 elements from the list whose sum is 10.
test = [12,6,4,23,9,2,30,5]
for i in range(len(test)):
    for j in range(i+1,len(test)):
        if test[i]* test[j] == 60:
            print(test[i],"*",test[j],"=60")
"""
Output:
12 * 5 =60
2 * 30 =60
"""
#). Python program to print a numbers divided by 2 and 3
test_list =[2,20,9,6,18,100]
for i in test_list:
    if i%2== 0 and i%3 ==0:
        print(i)
"""
output
6
18
"""
#14). Python program to reverse a list using index slicing.

mylist = [ 3,87,9,12,56,78,99]
rev =mylist[-1:-8:-1]
print("Reversed value is:",rev)
"""
Output
Reversed value is: [99, 78, 56, 12, 9, 87, 3]
"""
#13). Python program to reverse a list with a while loop.
#Input list
list1 = [1,2,3,4,55,78]

for i in range(len(list1)-1,-1,-1):
    print(list1[i], end=" ")
"""
Output:
78 55 4 3 2 1 
"""
