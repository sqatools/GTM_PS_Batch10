n=int(input("enter the value"))
odd=0
even=0
for i in range(1,n+1):
    print(i,end="")
    if i%2==0:
        even+=i
    else:
        odd+=i
print("sum of odd",odd)
print("sum of even",even)