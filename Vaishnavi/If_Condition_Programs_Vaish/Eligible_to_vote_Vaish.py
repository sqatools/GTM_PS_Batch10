# Q1. write a program to check the person is eligible to vote on the basis age > 18

Age = input("Enter the Age")
Age=int(Age) # input is taking as string
print(Age , type(Age))

if Age >= 18 :
    print("Eligible for voting")
else:
    print("Not eligible for voting")


