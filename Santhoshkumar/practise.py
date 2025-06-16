n1=5689
f1=float(n1)
print(f1,type(f1))

print("_"*50)

str1="programming"
print(str1,type(str1))
print("_"*50)

str2="tuple"
tup1=tuple(str2)
print(tup1,type(str2))

print("_"*50)

s7="python programming"
set1=set(s7)
print(set1,type(set1))
print("_"*50)

s8=""
b1=bool(s8)
print(b1,type(b1))

print("_"*50)

list1=[5, 7, 8, 2]
str1=str(list1)
print(str1, type(str1),str1[0])
#print(str1, type(str1), str1[0] , str1[1] )

print("_"*50)

tup2=tuple(list1)
print(tup2,type(tup2))

print("_"*50)

list2=[5,4,7,8]
list3=[9,2,4,1]
output=dict(zip(list2,list3))
print(output,type(output))

print("_"*50)

list4=[6,5,2,7,8,1,4]
set3=set(list4)
print(set3,type(set3))

print("_"*50)

list5=[2]
b1=bool(list5)
print(b1,type(b1))

print("_"*50)

tup3=(5,2,8,3)
str3=str(tup3)
print(str3,type(str3))

print("_"*50)

tup4=(6,7,8,9,2,1,3)
list4=list(tup4)
print(list4,type(list4))

print("_"*50)

tup5=('q','w','e','r','t','y')
tup6=(34,35,36,338,39,40)
output=dict(zip(tup5,tup6))
print(output,type(output))

print("_"*50)

tup6=(4,7,8,9)
set3=set(tup6)
print(set3,type(set3))

print("_"*50)

tup1=tuple("ljk")
b1=bool(tup1)
print(b1,type(b1))

print("_"*50)

dict1={'q': 34, 'w': 35, 'e': 36, 'r': 338, 't': 39, 'y': 40}
str4=str(dict1)
print(str4,type(str4))

print("_"*50)

dict2={'q': 34, 'w': 35, 'e': 36, 'r': 338, 't': 39, 'y': 40}
list5=list(dict2)
print(list5,type(list5))

print("_"*50)

dict3={'q': 34, 'w': 35, 'e': 36, 'r': 338, 't': 39, 'y': 40}
tup7=tuple(dict2)
print(tup7,type(tup7))

print("_"*50)

dict4={'q': 34, 'w': 35, 'e': 36, 'r': 338, 't': 39, 'y': 40}
set2=set(dict4)
print(set2,type(set2))

print("_"*50)

dict5={'A':'Programming','B':'Python'}
b2=bool(dict5)
print(b2,type(b2))

print("_"*50)

str1="hello \nworld i am \nexpert in python"
print(str1)

print("_"*50)

str1="hello \tworld i am \texpert in python"
print(str1)

print("_"*50)

a=20
b=30
if a==b:
    print("a and b are same value")
else:
    print("a and b are not same value")

print("_"*50)

num1=16
if num1%2==0:
    print("num is even:",num1)
else:
    print("not even it is a odd:",num1)

print("_"*50)

num2=31
if num2%3==0 and num2%5==0:
    print("It is divisble by 3 and 5:",num2)
else:
    print("It is not divisle by 3 and 5:",num2)

print("_"*50)

num3=14
if num3%3==0 or num3%5==0:
    print("It is divisble by 3 or 5:",num3)
else:
    print("It is not divisble 3 or 7:",num3)

print("_"*50)

q=50
w=75
e=12

if q>w and q>r:
    print("q is greater value:",q)
elif w>q and w>e:
    print("w is greater than:",w)
elif e>q and e>w:
    print("e is greater than",e)
else:
    print("no one is greater value")

print("_"*50)

list6=[1,5,4,78,56,6,30]
val1=30
val2=0
if val1 in list6:
    print("val1 in the list6:",val1)
else:
    print("val1 is not in the list6",val1)

print("_"*50)

if val2 in list6:
    print("val2 in the list6:",val2)
else:
    print("val2 in the list6:",val2)

print("_"*50)

str1="hello"
if str1 is not None:
    print("str1 has a value")
else:
    print("str1 is empty in string")

print("_"*50)

var1=True
num=30
if var1 is True:
    print("var1 is true:",num,num**2)
else:
    print("var2 is False:",num,num**3)

print("_"*50)

for i in range(5,20,3):
    print(i,end=" ")

print("_"*50)

for val in range(1,31):
    if val%2==0:
        print(val)
    else:
        pass

print("_"*50)

for val in range(1,31):
    if val%2==0:
        print("even:",val,end=" ")
    else:
        print("odd:",val,end=" ")

print()
print("_"*50)

for m in range(1,31):
    if m%2!=0:
        print(m,end=" ")
    else:
        pass
print()
print("_"*50)

str1="hello python programming"
vowels="aeiou"
for char in str1:
    if char in vowels:
        print("char:",vowels)
    else:
        print(char)
print()
print("_"*50)

list6=[5,7,8,9,5,6,3,2,1,0]
for i in list6:
    if i%2==0:
        print("square:",i,i**2)
    else:
        print("cube:",i,i**3)

print()
print("_"*50)

p1="hello"
if p1 is "hello":
    print("p1 contains hello")
else:
    print("p1 is not contain hello")

print()
print("_"*50)

out=5
#output="even" if num%2==0 else "odd"
#print("output:",output,out)
print("even" if num%2==0 else "odd")

print("_"*50)

for i in range(20):
    print(i,end=" ")

print()
print("_"*50)


for i in range(1,20):
    print(i,end=" ")

print()
print("_"*50)

for i in range(0,20,2):
    print(i,end=" ")

print()
print("_"*50)

for j in range(2,15):
    print(j,end=" ")

print()
print("_"*50)

num=7
for j in range(1,11):
    print(num,"*",j,":",j*num)

print()
print("_"*50)

num=17
for j in range(1,21):
    print(num,"*",j,":",j*num)

print()
print("_"*50)

for i in range(-10,1,1):
    print(i,end=" ")

print()
print("_"*50)

for val in range(1,31):
    if val%2!=0:
        print(val)

print()
print("_"*50)

for i in range(1,31):
    if i%2==0:
        print("even:",i)
    else:
        pass

print()
print("_"*50)

for i in range(1,6):
    print("address:",i)
    for j in range(1,4):
        print("item:",j)

print()
print("_"*50)

"""
*
* *
* * *
* * * *
* * * * * 
"""

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")

    print()

print()
print("_"*50)

"""
* * * * * 
* * * *
* * *
* *
*
"""

for i in range(1,6):
    for j in range(1,7-i):
        print("*",end=" ")
    print()

print()
print("_"*50)

"""

- * * * -   # i=1
* - - - *   # i=2
* - - - *   # i=3
* - - - *   # i=4
* - - - *   # i=5
- * * * -   # i=6

"""

for i in range(1,7):
    for j in range(1,6):
        if i in[1,6]:
            if j in[2,3,4]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i in [2,3,4,5]:
            if j in [1,5]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

print()
print("_"*50)

num=27
prime=True
for i in range(2,num//2):
    if num%i==0:
        prime=False
    else:
        continue
        pass
if prime:
    print("this is prime number:",num)
else:
    print("this is nor a prime number:",num)

print()
print("_"*50)

num=100
for num in range(1,100):
    prime=True
    for i in range(2,num//2):
        if num%i==0:
            prime=False
        else:
            continue
    if prime:
        print(num,end=" ")

print()
print("_"*50)

for i in range(1,10):
    if i==5 or i==6:
        continue
    print(i)

print()
print("_"*50)

for i in range(1,10):
    if i==5 or i==6:
        break
    print(i)

print()
print("_"*50)

n=1
while n<10:
    print(n)
    n+=1

print()
print("_"*50)

num=123
reverse=0
while num>0:
    temp=num%10
    reverse=reverse*10+temp
    num=num//10
print("reverse value:",reverse)

print()
print("_"*50)

char='a'
print(ord(char))


print()
print("_"*50)

print(chr(98))

print()
print("_"*50)

"""
A
B C
D E F
G H I J
K L M N O
"""
num=65
for i in range(1,6):
    for j in range(1,1+i):
        print(chr(num),end=" ")
        num+=1
    print()
for k in range(1,5):
    for l in range(5,0+k,-1):
        print(chr(num),end=" ")
        num+=1
    print()

print()
print("_"*50)

num=9
if num%3==0:
    print("it is divisible by 3")
else:
    print("it is not divisible by 3")

print()
print("_"*50)

#num4=int(input("enter a number:"))
for i in range(1,31):
    if i%3==0:
        print(i,end=" ")
    else:
        continue

print()
print("_"*50)

"""
Marks less than 40: Fail
Marks between 40-50: Grade C
Marks between 51-60: Grade B
Marks between 61-70: Grade A
Marks between 71-80: Grade A+
Marks between 81-90: Grade A++
Marks between 91-100: Excellent

marks=int(input("enter a marks:"))
if marks<40:
    print("fail")
elif marks>=40 and  marks<=50:
    print("Grade C")
elif marks>=50 and marks<=60:
    print("Grade B")
elif marks>=60 and marks<=70:
    print("Grade A")
elif marks>=70 and marks<=80:
    print("Grade A+")
elif marks>=80 and marks<=90:
    print("Grade A++")
elif marks>=90 and marks<=100:
    print("Excellent")
else:
    print("Invalid number")

print()
print("_"*50)
"""

num5=15
if num5%3==0 and num5%5==0:
    print("it is divisible by 3 and 5:",num5)
else:
    print("it is not divisble by 3 and 5:",num5)

print()
print("_"*50)

num6=22
if num6%11==0:
    print("it is divisble by 11:",num6**2)
else:
    print("it is not divisble by 11:",num6**3)

print()
print("_"*50)

num7=30
count=0
for i in range(2,num7):
    if num7%i==0:
        count+=1
if count>0:
    print("it is not a prime number",num7)
else:
    print("it is a prime number",num7)

print()
print("_"*50)

num=88
if num%2==0:
    print("it is even number:",num)
else:
    print("it is odd number:",num)

print()
print("_"*50)

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#num=int(input("enter a number:"))
if num in fib:
    print("it is my part of fib")
else:
    print("it is not part of fib")

print()
print("_"*50)

