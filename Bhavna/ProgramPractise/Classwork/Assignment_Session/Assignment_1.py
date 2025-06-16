# Assignment 1
# Q1. write a program to check the person is eligible to vote on the basis age > 18

age = 20

if age > 18:
    print("The person is eligible to vote.")
else:
    print("The person is not eligible to vote.")


print('_'*70)

# Q2. write a program to calculate the electricity bill amount on the basic of unit consumption.
# 1. unit < 100 : per unit charge is 15
# 2. unit > 100  and num < 200 : per unit charge is 20
# 3. unit > 200 : per unit charge is 25

unit = 50

if unit < 100:
    print("The per unit charge is 15")
elif unit > 100 and unit < 200:
    print("The per unit charge is 20")
elif unit > 200:
    print("The per unit charge is 25")
else:
    print("The per unit charge is 0")
