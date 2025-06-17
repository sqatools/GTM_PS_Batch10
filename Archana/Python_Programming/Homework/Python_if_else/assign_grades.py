# Program to assign grades as per total marks.
eng_Mark = int(input("Enter mark in English:"))
lang_Mark = int(input("Enter mark in Language:"))
math_Mark = int(input("Enter mark in Math:"))
sci_Mark = int(input("Enter mark in Science:"))
comp_mark = int(input("Enter mark in Computer:"))

Avg_Mark = (eng_Mark + lang_Mark + math_Mark + sci_Mark + comp_mark) // 5

print("Average Mark:", Avg_Mark)

if Avg_Mark < 40:
    print("Grade: 'Fail'")
elif Avg_Mark >= 40 and Avg_Mark <= 50:
    print("Grade: 'C'")
elif Avg_Mark >= 51 and Avg_Mark <= 60:
    print("Grade: 'B'")
elif Avg_Mark >= 61 and Avg_Mark <= 70:
    print("Grade: 'A'")
elif Avg_Mark >= 71 and Avg_Mark <= 80:
    print("Grade: 'A+'")
elif Avg_Mark >= 81 and Avg_Mark <= 90:
    print("Grade: 'A++'")
elif Avg_Mark >= 91 and Avg_Mark <= 100:
    print("Grade: 'OutStanding'")