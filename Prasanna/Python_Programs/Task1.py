n1=20
n2=30
n3=80
n4=100
n5=200

average=(n1+n2+n3+n4+n5)/5
print("average of numbers is:",average)


################################

'''Simple Intrest Program'''
principal_amount = 8
time_period = 6
rate_of_intrest = 8
SI = (principal_amount * time_period * rate_of_intrest)/100

print("Simple Intrest is:",SI)

############################################

'''Compound Intrest Program'''

P = Principal_Amount = 1200
r = rate_of_Intrest = 5.4
t = time_in_year = 2

Amount = P*(1+(r/100))**t
CI = Compund_Interest = Amount - P
print("Compound Intrest is:",CI)

################################################

'''Find the Area Of Sphere'''

PI = 3.14
Radius = int(input("Enter the Radius of the Sphere is:"))
Area_Of_Sphere = 4*PI*Radius**2
print("Area Of Sphere is:",Area_Of_Sphere)
