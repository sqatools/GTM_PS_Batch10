# Q1. write a program to check the person is eligible to vote on the basis age > 18
# Q2. write a program to calculate the electricity bill amount on the basic of unit consumtion.
# 1. unit < 100 : per unit charge is 15
# 2. unit > 100  and num < 200 : per unit charge is 200
# 3. unit > 200 : per unit charge is 25


# Q1. write a program to check the person is eligible to vote on the basis age > 18



age = int(input("Please enter Candidate the age for Vote :"))
if age >=18:
    print("The Candidate is eligible for Vote")
else:
    print("The Candidate is not Eligible for Vote")
####################################################################

# unit1 = float(input("Enter the electricity bill amount : "))
# if unit1 < 100:
#     charge = unit1 * 15
# elif unit1 <= 200:
#     charge = unit1 * 20
# else: charge = unit1 * 25
# print("The Total Bill amount is :",charge)


