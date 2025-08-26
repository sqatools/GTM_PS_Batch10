i=int(input("enter the value of i"))
j=int(input("enter the value of j"))

for val in range (i,j,1):
 if val%3==0:
    print(val,":Divisible by 3")
else:
    pass


print("_"*80)

for i in range(1,30,1):
    if i%3==0:
        print(i)
    else:
        pass