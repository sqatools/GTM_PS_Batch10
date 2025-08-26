"""
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

marks=int(input("enter the marks"))
if marks<40:
    print("fail")
elif marks>=40 and marks<50:
    print("grade C")
elif marks>=50 and marks<60:
    print("grade B")
elif marks >= 60 and marks < 70:
    print("grade A")
elif marks >= 70 and marks < 80:
    print("grade A+")
elif marks >= 80 and marks < 90:
    print("grade A++")
elif marks >= 90 and marks <= 100:
    print("grade Excellent")
else:
    print("Invalid marks")