from errno import EILSEQ

#Homework
# eligible to vote basis of 18

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible for vote")
else:
    print("not Eligible for vote")

#electricity amount on the basis of unit of consumption
# Python Program to Calculate Electricity Bill

units = int(input(" Please enter Number of Units you Consumed : "))

if (units > 100):
    surcharge = 15
elif (units < 200):
    surcharge = 20
elif (units >= 200):
    surcharge = 30
total = surcharge
print("\nElectricity Bill:", total)











