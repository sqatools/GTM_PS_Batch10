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

if(units > 100):
    amount = units * 15
elif(units < 200):
    amount = units * 20
elif(units > 200):
    amount = units * 25


    total= amount
print("\nelectricity bill:", total)









