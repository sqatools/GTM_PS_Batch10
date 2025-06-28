"""
1.Python Loops program to print all natural numbers from 1 to n using a while loop in python
2.Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
"""
n=int(input("enter the value"))
count=0
while count<n:
    count+=1
    print(count)

print("_"*80)

n1=int(input("enter the value"))
count=n1
print(count)
while count!=0 and count>0:
    print(count)
    count-=1
