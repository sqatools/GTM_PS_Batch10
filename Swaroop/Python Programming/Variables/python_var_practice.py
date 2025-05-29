#simple intrest
"""
p = 100000
r = 2.5
t = 1
s = ("simple intrest :", p * r * t/100)
print(s)
"""

#compount intrest
""""
p = 10000
r = 5
t = 1
n = 2
c = p * (1+r/n) ** (n*t)-p
print(c)
"""

#Find area of sphere
pi = 3.21
r = 2
f = 4 * pi * r **2
print(f)

#Addin two numbers
a = 10
b = 20
print("Adding two numbers:", a+b)
print("address of a:", id(a))
print("address of b:", id(b))

#Susbtract two nubers
c = 1
d = 2
print("Substract values :", d-c)

#multiply two numbers
e = 4
f = 5
print("Multiply two values:", 4*5)

#Repeat a string 5 times
str1 = "hello"
g = 5
print("multiple times string:", str1 * 5)

#Average of given numbers
h = 10
i = 20
j = 30
print("average of all the numbers :", h+i+j/3)

#sort the program
values = [20,30,10,50]

values.sort()
print(values)
n = len(values)
print(n)
if n%2 == 1:
    median_value = values[n//2]
else:
    median_value = (values[n//2-1]+values [n//2])/2
print(f"The median is : {median_value}")


#Print square and cube of given number
num1 = 5
print("square of number:",num1**2)
print("cube of number:", num1**3)

#Python interchange values between variable
g = 10
f = 20
g,f = f,g
print("changed values between variables:",g,f)

#Pythogrous theorem
a = 3
b = 4
c = a**2 + b**2
print("values of c:", c)
z = c/5
print(z)
"""""
#calculate area of square
side = int(input("Enter the square:"))
print ("area of square:",side**2)
"""



#solve a^2+b2=2ab formula
l = 10
j = 20
r = ("show formula result:",a**2+b**2+2*a*b)
print(r)

#Math formula a2-b2 =(a-b)(a+b)
a = 2
b = 4
r =("print the value a2-b2:",(a-b)*(a+b))
print(r)

#Armstrong number
"""
n = 153
rev = 0
while n>0:
    rem = n%10
    rev = rev +rem**3
    n = n//10
if rev == n:
    print("it's an armstrong")
else:
    print("it's not  armstrong")
 """"
#current date
import datetime
date = datetime.datetime.now()
print(date.strftime("%y %b %d"))






