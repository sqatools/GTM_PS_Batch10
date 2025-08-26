#Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
# (both included).
input1=int(input("enter the start node"))
input2=int(input("enter the end node"))
if input2>input1:
    for i in range(input1,input2):
        if i%7==0 and i%5==0:
            print("divisible by 7 and multiple of 5",i)
        else:
            continue
else:
    for i in range(input1,input2,-1):
        if i%7==0 and i%5==0:
            print("divisible by 7 and multiple of 5",i)
        else:
            continue

    print()
