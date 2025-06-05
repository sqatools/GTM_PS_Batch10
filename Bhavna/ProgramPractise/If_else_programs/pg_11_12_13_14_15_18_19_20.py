# IF_ELSE PYTHON PRACTISE PROGRAM

# 11. Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

num = 21

if num%2 == 0 or num%3 ==0:
    print("This number is divisible by 2 or 3:", num)
else:
    print("This number is not divisible by 2 or 3:", num)

print('_'*70)

# 12. Python program to describe the interview process.

Round_1 = "Pass"
Round_2 = "Fail"
Round_3 = "Fail"

if Round_1 == "Pass":
    print("Your first round is cleared")
    if Round_2 == "Pass":
        print("Your second round is cleared")
        if Round_3 == "Pass":
            print("Your third round is cleared")
        else:
            print("your third round is not cleared")
    else:
        print("your second round is not cleared")
else:
    print("your first round is not cleared")

print('_'*70)

#13. Python program to determine whether a given number is available in the list of numbers or not.

num1 = 85
list_1 = [5, 23, 85, 9, 9, 78, 995, 121]

if num1 in list_1:
    print("The given number is available in the list")
else:
    print("The given number is not available in the list")

print('_'*70)

# 14). Python program to find the largest number among three numbers.

t = 147
y = 258
u = 36

if t>y and t>u:
    print("t has greater value:", t)
elif y>u and y>t:
    print("y has greater value:", y)
elif u>t and u>y:
    print("u has greater value:", u)
else:
    print("None has greater Value")

print('_'*70)

# 15. Python program to check any person eligible to vote or not

Age = int(input("Enter the age:"))

if Age>=18:
    print("The person is eligible to vote.")
else:
    print("The person is not eligible to vote.")

print('_'*70)

# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# Input = Enter marks: 45
# Output = Pass

Marks = int(input("Enter the marks:"))

if Marks>35:
    print("Pass")
else:
    print("Fail")

print('_'*70)

# 19). Python program to check whether the given number is positive or not.
# Input = 20
# Output = True

input = 20

if input>0:
    print("True")
else:
    print("False")

print('_'*70)

# 20). Python program to check whether the given number is negative or not.
# Input = -45
# Output = True

input_1 = -20

if input_1<0:
    print("True")
else:
    print("False")

print('_'*70)


