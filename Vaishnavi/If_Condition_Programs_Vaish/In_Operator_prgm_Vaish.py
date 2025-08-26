#Write a program to check value is in the list and is even or not

list2 = [20,25,26,40,41,60,75,90,99,34,21]
v1 = input("Enter the value")
v1= int(v1)
print("The value is :" , v1, type(v1))

print("-"*50)
if v1 in list2 and v1%2==0:
    print("Value in the list and is even")
elif v1 in list2 and v1%2==1 :
    print("Value in the list and is odd")
else:
    print("Value is not in list")
