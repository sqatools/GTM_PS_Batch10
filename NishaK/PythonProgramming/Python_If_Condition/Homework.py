# Q1. write a program to check the person is eligible to vote on the basis age > 18
"""
age = int(input("Please enter age : "))
if age >= 18:
    print("Person is eligible for voting as age is :", age)
else:
    print("Person is not eligible for voting as age is :", age)

# Please enter age : 18
# Person is eligible for voting as age is : 18

#Please enter age :16
#Person is not eligible for voting as age is : 16
"""


print("-"*50)
# Q2. write a program to calculate the electricity bill amount on the basic of unit consumtion.
# 1. unit < 100 : per unit charge is 15
# 2. unit > 100  and unit < 200 : per unit charge is 20
# 3. unit > 200 : per unit charge is 25

unit = int(input("Please enter number of units consumed : "))
if unit <= 100:
    print("Electricity Bill amount :", unit*15)
elif unit <= 200:
    print("Electricity Bill amount :", (unit*15) + (unit-100)*20)
elif unit > 200:
    print("Electricity Bill amount :", (unit*15) + (unit*20) + (unit-200*25))
else:
    print("Electricity Bill amount : 0")
