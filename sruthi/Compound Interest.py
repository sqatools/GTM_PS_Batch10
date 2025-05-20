p = int(input("Enter principle amount: "))
r = float(input("Enter interest rate: "))
n = int(input("Enter number of years: "))

amount = p*((1+r/100)**n)

print("Compoud interest: ",amount)