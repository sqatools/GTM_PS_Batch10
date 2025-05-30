#HW :
# Q1. write a program to check the person is eligible to vote on the basis age > 18
# Q2. write a program to calculate the electricity bill amount on the basic of unit consumtion.
# 1. unit < 100 : per unit charge is 15
# 2. unit > 100  and num < 200 : per unit charge is 200
# 3. unit > 200 : per unit charge is 25
#Q1 answer
age = int(input("Enter the person age :"))
if age > 18:
    print("The person is eligible for Voting")
else:
    print("The person is not eligible for Voting")
print("="*50)
#Q2 Answer:
total_unit = float(input("Enter the total number of units for electricity consumption :"))
if total_unit < 100:
    bill_amount = total_unit * 15
    print("The bill is $",bill_amount)
elif total_unit < 200:
    bill_amount = total_unit * 20
    print("The bill is $",bill_amount)
elif total_unit > 200:
    bill_amount = total_unit * 25
    print("The bill is $",bill_amount)