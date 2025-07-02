"""# Python function program that take a number as a parameter and checks whether the number is prime or not.
Input : 7
Output : True"""

def Isprime1(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
        else:
            continue

    if count > 2:
        print("False")
    else:
        print("true")
Isprime1(7)