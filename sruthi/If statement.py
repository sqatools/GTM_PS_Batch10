from errno import EILSEQ

#Homework
# eligible to vote basis of 18

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible for vote")
else:
    print("not Eligible for vote")

#electricity amount on the basis of unit of consumption
unit = int(input("Enter unit: "))
if unit< 100:
    print("per unit charge is 15")
if unit> 200:
    print("per unit charge is 20")
    if unit> 300:
        print("per unit charge is 30")
    else:
        print("no bill")






