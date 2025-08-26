"""Python Loops program to find the sum of all natural numbers between 1 to n using python."""
n=int(input("enter the value"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)