# IF_ELSE PYTHON PRACTISE PROGRAM

# 1. Python program to check given number is divided by 3 or not.

a = 9

if (a%3 == 0):
    print("This number is divisible by 3.")
else:
    print("This number is not divisible by 3.")

print('_'*70)

# 2. If else program to get all the numbers divided by 3 from 1 to 30.

for i in range(1,31):
    if i%3 == 0:
        print(i, end=" ")
    else:
        pass

print()
print('_'*70)

# 3. If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks

marks = 55

if marks < 40:
    print("Fail")
elif marks >= 40 and marks <= 50:
    print("grade C")
elif marks > 50 and marks <= 60:
    print("grade B")
elif marks > 60 and marks <= 70:
    print("grade A")
elif marks > 70 and marks <= 80:
    print("grade A+")
elif marks > 80 and marks <= 90:
    print("grade A++")
elif marks > 90 and marks <= 100:
    print("grade Excellent ")
else:
    print("Invalid marks ")

print('_'*70)

# 4. Python program to check the given number divided by 3 and 5.

num = 30

if num%3 == 0 and num%5 == 0:
    print("This number is divisible by 3 and 5.")
else:
    print("This number is not divisible by 3 and 5.")

print('_'*70)

# 5. Python program to print the square of the number if it is divided by 11.

num = 22

if (num%11 == 0):
    print(num**2)
else:
    print("The number is not divisible by 11.")

print('_'*70)
# 7. Python program to check given number is odd or even.

a = 23

if a%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print('_'*70)

# 10. Python program to validate user_id in the list of user_ids.

user_ids = [1, 8, 12, 7, 65, 52, 47]

id = 11

if id in user_ids:
    print("User ID is present")
else:
    print("User ID is not present.")
