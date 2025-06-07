# Python program to print the square of the number if it is divided by 11.
print("*-_-" * 20)
i = int(input("enter your value"))
if i % 11 == 0:
    print("square of the values is", i ** 2)
else:
    print("i is not divicible by 11", i)
#####Program to get all numbers divided by 3 between 1 to 30
for i in range(1,31):
        if i%3 ==0:
            print(i,end=" ")
        else:
            continue
            print(" *",end= " ")

########If else program to assign grades as per total marks.
print("*-_-*"*10)
marks = int(input("enter your marks"))
if marks<40:
        print("fail")
elif marks >=40 and marks<=50:
    print("C grade")
elif marks>50 and marks<=60:
    print("D grade")
elif marks>60 and marks<=70:
    print("A Grade")
elif marks > 70 and marks <= 80:
    print("Grade A+")
elif marks > 80 and marks <= 90:
    print("Grade A++")
elif marks > 90 and marks <= 100:
    print("Excellent")
else:
   print("Invalid marks")

#Program to check whether the number is a prime number.
print("*-_-"*20)
num = int(input("Enterrequired number"))
count =0
if i in range(2,num):
    if num%i==0:
        count+=1
    if count>0:
        print("entered number is a prime number")
else:
        print("its not a prime number")
#################################
j = int(input("Enter your j values"))
count = 0
if i in range(1,j):
    count+=1
    if i%j==1:
        if count>1:
            print("its a odd number")
else:
    print("its not prime number")





