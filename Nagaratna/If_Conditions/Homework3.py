    #####Program to get all numbers divided by 3 between 1 to 30
for i in range(1,31):
        if i%3 ==0:
            print(i,end=" ")
        else:
            continue
            print(" *",end= " ")

########If else program to assign grades as per total marks.
print("*-_-*"*10)
marks = int(input("enter your marks"))
if marks<40:
        print("fail")
elif marks >=40 and marks<=50:
    print("C grade")
elif marks>50 and marks<=60:
    print("D grade")
elif marks>60 and marks<=70:
    print("A Grade")
elif marks > 70 and marks <= 80:
    print("Grade A+")
elif marks > 80 and marks <= 90:
    print("Grade A++")
elif marks > 90 and marks <= 100:
    print("Excellent")
else:
   print("Invalid marks")


