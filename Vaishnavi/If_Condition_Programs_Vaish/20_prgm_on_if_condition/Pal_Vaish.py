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