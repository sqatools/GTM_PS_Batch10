a = 10
b = 20
str1 = a
str2 = b
a = str2
b = str1

print("The value of a :" , a)
print("The value of b :" , b)

a , b = b , a

print("The value of a :" , a)
print("The value of b :" , b)
