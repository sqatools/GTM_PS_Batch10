print("Hello Python")
print("---"*50)

print("Average of given five numbers:")
n1 = float(input("Enter First number: "))
n2 = float(input("Enter Second number: "))
n3 = float(input("Enter Third number: "))
n4 = float(input("Enter Fourth number: "))
n5 = float(input("Enter Fifth number: "))

Average = (n1 + n2 + n3 + n4 + n5) / 5
print("Average of given numbers: {:.2f}".format(Average))

print("---"*50)

print("Code for Simple Intrest")
P = float(input("Enter Principal Amount: "))
T = float(input("Enter the Time Period (in years): "))
R = float(input("Enter the Rate of Interest (% per annum): "))

I = (P * T * R) / 100
print("Interest: {:.2f}".format(I))

print("---"*50)

print ("Area of Sphere:")
R = float(input("Enter the Radious of Sphere:"))
A = 4 * 3.14159 * (R**2)
print("Area of Sphere: {:.2f}".format(A))

print("---"*50)
print("Compound Intrest:")
N = float (input("Enter the number of times interest applied per time period:"))
P = float(input("Enter Principal Amount: "))
R = float(input("Enter the Rate of Interest (% per annum): "))
T = float(input("Enter the number of time periods elapsed: "))
Amount = (P *(1 +R/100))*T
CI = Amount - P
print ("Compound Intrest: {:.2f}".format(CI))

print("---"*50)
