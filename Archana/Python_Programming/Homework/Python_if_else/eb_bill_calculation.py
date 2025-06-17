# 1. Program to calculate the Eb bill

print("Calculate the EB Bill")
print("_"*50)
units_Consumed = int(input("Enter the Units consumed :"))
if units_Consumed < 100:
    units_per_charge = 15
    print("The Unit per charge is :", units_per_charge)
    print("The EB bill charged is :", units_per_charge * units_Consumed)
elif units_Consumed > 100 and units_Consumed < 200:
    units_per_charge = 20
    print("The Unit per charge is :", units_per_charge)
    print("The EB bill charged is :", units_per_charge * units_Consumed)
elif units_Consumed > 200:
    units_per_charge = 25
    print("The Unit per charge is :", units_per_charge)
    print("The EB bill charged is :", units_per_charge * units_Consumed)
else:
    print("There is no EB bill charged this month ")
