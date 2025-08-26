a=val=int(input("enter the value"))
str1=str(val)
l1=len(str1)
temp=0
for i in range(0,l1):
    rem=(val%10)**l1
    temp=temp+rem
    val=val//10
if temp==a:
    print("is ARmstrong")
else:
    print("Not armstrong")


