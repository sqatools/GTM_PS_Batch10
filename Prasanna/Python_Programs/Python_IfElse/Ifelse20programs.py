"""#1). Python program to check given number is divided by 3 or not.
number = int(input("Enter the number you want"))
if number % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

#2)If else program to get all the numbers divided by 3 from 1 to 30.
for number in range(1, 31):
    if number % 3 == 0:
        print(number,end=" ")
    else :
        continue

If else program to assign grades as per total marks.
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
marks = int(input("Enter marks: "))
# Assign grades based on marks
if marks<40:
    print("Fail")
elif marks>=40 and marks>=50:
    print("Grade C")
elif marks>50 and marks<=60:
    print("Grade B")
elif marks>60 and marks<=70:
    #  marks is greater than 60 and less than 70 then got A grade.
    print("Grade A")
elif marks>70 and marks<=80:
    #  marks is g

