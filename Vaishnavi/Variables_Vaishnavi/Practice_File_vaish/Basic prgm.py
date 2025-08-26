"""###Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)
a=10
b=30
c=30
out1=(a**2+b**2)
out2=c**2
print(out1==out2)

#Python program to check whether the given number is an Armstrong number or not.
input1=int(input("Enter the values"))
num=str(input1)
n=len(num)
temp=0
for i in num:
    sum=int(i)**n
    temp+=sum
    print(temp)
if temp==input1:
    print("Armstrong number")
else:
    print("Not Armstrong number")

#Python program to print the current date in the given format
import datetime
date = datetime.datetime.now()
print(date) #2025-06-28 11:57:42.187102

#Python program to calculate days between 2 dates.

from datetime import date
date1=date(2023,4,5)
date2=date(2024,5,6)
r1=(date2-date1).days
print(r1)

#Python program to get the factorial of the given number.
fac1=int(input("enter the value to find factorial"))
temp=1
fact=0
for i in range(fac1,0,-1):
    fact=i*temp
    temp+=fact

print(temp)"""

#Python program to reverse a given number.
num1=2345
n=len(str(num1))
temp=0
while num1>0:
    reverse_1 = num1 % 10
    temp = temp * 10 + reverse_1
    num1 = num1 // 10
    print(temp)


#Python program to get the Fibonacci series between 0 to 50
fib=0
a=0
b=1
temp=0
print(a)
print(b)
for i in range(0,50,1):
    sum=a+b
    a=b
    b=sum
    print(sum)

#Python program to check given number is palindrome or not.
p=pal=124
temp=0
while pal>0:
    rem1=pal%10
    temp=temp*10+rem1
    pal=pal//10

if p==temp:
    print("palindrome",temp)
else:
    print("Not palindrome",temp)

#prime
num=24
c1=0
for i in range(1,num+1):
     if num%i==0:
         c1 += 1

if c1==2:
    print("prime number")
else:
    print("not Prime number")

#Python program to check leap year.
year1=int(input("value plz"))
if year1%400==0 or year1%100!=0 and year1%4==0:
    print("leap year")
else:
    print("not leaap year")

#random number generation
import random
for i in range(2):
    print(random.random(),end=" ")
    print(random.randint(1,10))
