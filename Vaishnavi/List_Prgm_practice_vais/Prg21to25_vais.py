#21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).

l1=[101, 111, 121, 131,243,453,768]
output=[]
for val in l1:
    rev=0
    rem=0
    temp = val
    while(val>0):
        rem=val%10
        rev=rev*10+rem
        val=val//10
    if temp==rev:
     output.append(temp)
print(output)

"""#22). Python Program to get a list of words which has vowels in the given string.
Input: “www Student ppp are qqqq learning Python vvv”
Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]"""
i1="www Student ppp are qqqq learning Python vvv"
vowel="aeiou"
i2=i1.split()
output=[]
for word in i2:
    for i in word:
        if i in vowel and word not in output:
            output.append(word)
print(output)

#23). Python program to add 2 lists with extend method.

l1=[101, 111, 121, 131,243,453,768]
l2=[2,3,4]
l1.extend(l2)
print(l1,":l1")#[101, 111, 121, 131, 243, 453, 768, 2, 3, 4]
print(l2,":l2")

print("_*_"*50)
#24). Python program to sort list data, with the sort and sorted method

l1=[101,20,2345, 111, 121,800, 131,243,453,768]
l1.sort()
print(l1)#[20, 101, 111, 121, 131, 243, 453, 768, 800, 2345]
l1.sort(reverse=True)
print(l1)#[2345, 800, 768, 453, 243, 131, 121, 111, 101, 20]
l5=[12,34,56,32,31,87,98,54,33]
l3=sorted(l5)
l4=sorted(l5,reverse=True)
print(l3,":list 3")
print(l4,":list 4")
"""
[12, 31, 32, 33, 34, 54, 56, 87, 98] :list 3
[98, 87, 56, 54, 34, 33, 32, 31, 12] :list 4
"""

#25). Python program to remove data from the list from a specific index using the pop method.
l7=[12,34,56,32,31,87,98,54,33]
result1=l7.pop(3)
print(result1) #32
print(l7)#[12, 34, 56, 31, 87, 98, 54, 33]
r2=l7.remove(56)
print(r2)#None wont return any value
print(l7)#[12, 34, 31, 87, 98, 54, 33]

