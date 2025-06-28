#Python program to get the Average of given numbers.
a = 40
b = 50
c = 30
avg = (a+b+c)/3
print(avg) #40.0

#Python program to get the median of given numbers.
#Note: all the numbers should be arranged in ascending order
#Formula : (n+1)/2
#Input : [45, 60, 61, 66, 70, 77, 80]
input1= [45, 60, 66, 61, 77, 70, 80]
input1.sort() #ascending order
print(input1)
c1= len(input1)
print(c1)
ph=((c1+1)/2)
print(ph)
print(input1[int(ph-1)])
   #print(input1[ph])

#Python program to print the square and cube of a given number.
ip1=int(input("enter the value"))
print("square:",ip1**2)
print("Cube:",ip1**3)
"""square: 36
Cube: 216
"""

#Python program to interchange values between variables.
a = 10
b = 20
temp=a
a=b
b=temp
print("a:",a,"b:",b) #a: 20 b: 10

print("*"*50)


