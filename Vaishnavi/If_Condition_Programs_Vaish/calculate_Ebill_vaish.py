# Q2. write a program to calculate the electricity bill amount on the basic of unit consumtion.
# 1. unit < 100 : per unit charge is 15
# 2. unit > 100  and num < 200 : per unit charge is 200
# 3. unit > 200 : per unit charge is 25

Unit = input("Enter the Unit :")
Unit = int(Unit)
print(Unit, type(Unit))

if Unit < 100 :
    print("Per unit charge is 15")
elif Unit > 100 and Unit < 200 :
    print("Per unit charge is 200")
else:
    print("Per unit charge is 25")