#Python program to check given number is a prime number or not.

input1=int(input("enter the value"))
count=0
for i in range(2,input1):
    if input1%i==0:
        count+=1
if count>0:
            print("its not a prime no")

else:
        print("its a prime no")


