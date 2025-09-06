#Check if a Number is Palindrome
temp=value=int(input("enter the value"))
str1=str(value)
length=len(str1)
tem=0
for i in range(0,length):
    rev=value%10
    tem=tem*10+rev
    value=value//10
print(tem)
print(temp)
if tem==temp:
    print("is palindrome")
else:
    print("Not palindrome")



list_e = [4, 99, 11, 44]
list_f = ['a', 'b', 'c', 'd']
r1=list_e+list_f
print(r1)
print(list_f,)
print(list_e)

print("_"*50)

list_A = [5, 8, 2, 6, 12]

list_A.append('Python')
list_B = list_A.copy()
list_B.append(101)


print("list_A :", list_A) # [5, 8, 2, 6, 12, 'Python']
print("list_B:", list_B)