#Write a program to check value is not in the list and is even or not

list2 = [20,25,26,40,41,60,75,90,99,34,21]
v1 = input("Enter the value")
v1= int(v1)
print("The value is :" , v1, type(v1))

print("-"*50)

if v1 not in list2 and v1%2==0:
    print("Value not in list and value is even")
elif v1 not in list2 and v1%2==1:
    print("Value not in list and value is odd")
else:
    print("Value is in list")