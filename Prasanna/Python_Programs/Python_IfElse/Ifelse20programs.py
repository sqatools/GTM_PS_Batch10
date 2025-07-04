# 1). Python program to check given number is divided by 3 or not.
number = int(input("Enter the number you want"))
if number % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

# 2)If else program to get all the numbers divided by 3 from 1 to 30.
for number in range(1, 31):
    if number % 3 == 0:
        print(number,end=" ")
    else :
        continue

"""If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
# Take marks through the user
# Take marks through the user
marks = int(input("Enter marks: "))
# Assign grades based on marks
if marks<40:
    # marks is less than 40 then print Fail
    print("Fail")
elif marks>=40 and marks<=50:
    # marks is greater than 40 and less than 50 then got C grade.
    print("Grade C")
elif marks>50 and marks<=60:
    #  marks is greater than 50 and less than 60 then got B grade.
    print("Grade B")
elif marks>60 and marks<=70:
    #  marks is greater than 60 and less than 70 then got A grade.
    print("Grade A")
elif marks>70 and marks<=80:
    #  marks is greater than 70 and less than 80 then got A+ grade.
    print("Grade A+")
elif marks>80 and marks<=90:
    #  marks is greater than 80 and less than 90 then got A++ grade.
    print("Grade A++")
elif marks>90 and marks<=100:
    #  marks is greater than 90 and less than 100 then got Excellent grade.
    print("Excellent")
else:
    # marks is greater than 100 than consider as invalid number..
    print("Invalid marks")

# 4). Python program to check the given number divided by 3 and 5.
number = int(input("Enter The Number:\n"))
if number%3 == 0 and number%5 == 0:
    print("The Given number is divisible by 3 and 5: and number is",number)
else:
    print("The number is not divisible by 3 and 5")

# 5)Python program to print the square of the number if it is divided by 11.
number = int(input("Enter the Number"))
if number%11 == 0:
    print("The square of that number is:",number**2)
else:
    print("The number is not divisible by 11")

# 6). Python program to check given number is a prime number or not.
number = int(input("Enter the number"))
count = 0
for i in range(2, number):
    if number%i == 0:
        count = count+1
if count>0:
    print("The number is not prime")
else:
    print("The number is prime")

# 7). Python program to check given number is odd or even.
number = int(input("Enter the number"))
if number%2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
number = int(input("enter the number"))
if number in fib:
    print("The number is part of Fibonacci")
else:
    print("Not a part of Fibonacci")

# 9). Python program to check authentication with the given username and password.
username = (input("Enter user name:"))
password = (input("Enter password"))
if username == password:
    print("Valid User")
else:
    print("Not a valid user ")

# 10). Python program to validate user_id in the list of user_ids.
user_ids = [ "prasanna", "qualcomm", "beaglebone", "raspberrypi"]
user_id = input("Enter User Id")
if user_id in user_ids:
    print("It is Valid User Id")
