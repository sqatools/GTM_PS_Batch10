print("Hello Python")

# n1 = int(input("Enter First number:")),
# n2 = int(input("Enter Second number:")),
# n3 = int(input("Enter Third number:")),
# n4 = int(input("Enter Fourth number:")),
# n5 = int(input("Enter Fifth number:"))
# print ("Average of given numbers" ,n1+n2+n3+n4+n5/

P = float(input("Enter Principal Amount: "))
T = float(input("Enter the Time Period (in years): "))
R = float(input("Enter the Rate of Interest (% per annum): "))

I = (P * T * R) / 100
print("Interest: {:.2f}".format(I))

R = float(input("Enter the Radious of Sphere:"))
A = 4 * 3.14159 * (R**2)
print("Area of Sphere: {:.2f}".format(A))

N = float (input("Enter the number of times interest applied per time period:"))
P = float(input("Enter Principal Amount: "))
R = float(input("Enter the Rate of Interest (% per annum): "))
T = float(input("Enter the number of time periods elapsed: "))
Amount = (P *(1 +R/100))*T
CI = Amount - P
print ("Compound Intrest: {:.2f}".format(CI))


