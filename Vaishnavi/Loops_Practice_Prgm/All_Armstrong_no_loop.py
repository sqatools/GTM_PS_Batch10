#Python loops program to print all Armstrong numbers between 1 to n using Python Loops

n=int(input("enter the value"))
for i in range(1,n+1):
    sum=0
    num=temp=i
    while temp>0:
        rem=temp%10
        sum+=rem**len(str(i))
        temp=temp//10
    if num==sum:
        print("Armstrong Number",sum)