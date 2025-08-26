
a = 20
b = 30
print(a == b)
if a == b:
    print(" a and b are equal")
else:
    print(" a and b are not equal")
print("_" * 50)
# write a program to check the given value is even or odd
num1 = int (input("num1 = "))
if num1%2 == 0:
    print("a is even",num1)
else:
    print("a is odd")
print("_"*50)
# write a python program to check given number is divisible by 3 and 5
num2 = int (input("num2 = "))
if num2%3 ==0 and num2%5 ==0:
    print("Given number is divisible by 3 and 5",num2)
else:
    print("Given number is not divisible by 3 and 5 and the number is2",num2)
print("_"*50)

# write a python program to check given number is divisible by 5 or 7
num3 = int (input("num3 = "))
if num3%5 ==0 or num3%7 ==0:
    print("Given number is divisible by 5 and 7 and the number is:",num3)
else:
    print("Given number is not divisible by 5 and 7 and the number is:",num3)
print("_"*50)

############################# if-elif- else condition #####################
# program to check which number has greater value
p = 100
q = 100
r = 200
if p > q and p > r:
    print("P is greater value",p)
elif q > p and q > r:
    print("Q is greater value",q)
elif r > p and r > q:
    print("R is greater value",r)
else:
    print("No one has greater value")

###################### Nested If condition #################
"""
if cond1:
    code1
    if cond2:
        code2
        if cond3:
            code3
        else:
            code3
    else:
        else code2

else:
    else code1
"""
print("_" * 50)
# write a program to for interview process with the help of nested if condition.
round1 = "pass"
round2 = "pass"
round3 = "fail"
if round1 == "pass" :
    print("You cleared First round")
    if round2 == "pass" :
        print("You cleared Second round")
        if round3 == "pass" :
            print("You cleared Third round")
        else:
            print("Sorry you not cleared Third round")
    else:
        print("Sorry you are not cleared Second round")
else:
    print("Sorry you are not cleared First round")
