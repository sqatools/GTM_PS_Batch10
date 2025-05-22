print("hello world")
print("_"*40)

a=35
b=65
print("adding: ",a+b)

print("_"*50)

x=987
y=654
print("subract:", x-y)

print("_"*50)

w=100
e=175
print("multiply:",w*e)
print("_"*50)

str1="SQATools"
print(str1*5)
print("_"*50)

a = 40
b = 50
c = 30
print("Average:",a+b+c)
add=(a+b+c)
avg= add / 3
print("avg=",avg)

print("_"*50)

a = 10
b = 20
a,b = b,a
print("value of a:",a)
print("vzlue of b:",b)

print("_"*50)

#(a – b)2 = a^2 + b^2 – 2ab

a=2
b=3
RHS=a**2 + b**2 - 2*a*b
print("(a-b)2:",RHS)

print("_"*50)

a=3
b=2
RHS=(a-b)*(a+b)
print("a2-b2=",RHS)

print("_"*50)

a=3
b=2
RHS=a**3+3*a*b*(a+b)+b**3
print("(a+b)^3:",RHS)
print("_"*50)

#(a – b)3 = a3 – 3a2b + 3ab2 – b3

a=3
b=5
#RHS= a**3–3*a**2*b+3*a*b**2+b**3
RHS= a**3-3*a**2*b+3*a*b**2+b**3
print("#(a – b)3=",RHS)

print("_"*50)

sq=int(input("enter a side of square:"))
print("Area of a square:",sq**2)

print("_"*50)

radius=int(input("enter area of circle:"))
area=3.14*radius*radius
print("area of circle:",area)

print("_"*50)

side=int(input("enter side of cube:"))
cube=6*side*side
print("Area of cube",cube)

print("_"*50)

#cyclinder
#2*PI*r*h + 2*PI*r*r

r=int(input("enter a radius:"))
h=int(input("enter a height"))
PI=3.14
area=2*PI*r*h + 2*PI*r*r
print("area of the cyclinder: ",area)
print("_"*50)




print("_"*50)
#simple interset
P=200000
R=2
T=6
SI=(P+R+T)/100
print("Simple Interest: ",SI)

print("_"*50)

#compound Interset

#CI=P(1+r/n)^nt - P

#P=500000
#r=8
#n=5
#t=10
#Compound = P (1+r/n)**(n*t) - P
#print("compounding amount in 5 years:", Compound)

p=int(input("enter principal amount:"))
r=float(input("enter interset rate:"))
n=int(input("enter number of years"))
t=int(input("enter number of years compunded:"))
amount=p*((1+r/100)**(n*t))
print("compund interset:",amount)






