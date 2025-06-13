#Python program to check a given number is part of the Fibonacci series from 1 to 10
#0,1,1,2,3,5,8,13

i=int(input("enter the range"))
a=0
b=1
temp=0
print(a)
print(b)
for count in range(0,i,1):
    sum=a+b
    temp=b
    a=b
    b=sum
    print(sum)











