#Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
Num=int(input("Enter the value"))

if Num%3==0 and  Num%2==0:
    print("Number is divisible by 2 and 3 :",Num)
    print("Square of num is:",Num**2)
else:
    print("Number is not divisible by 2 and 3 :",Num)