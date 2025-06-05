# PYTHON LOOPS PRACTICE PROGRAM

# 11. Python Loops program to print all natural numbers from 1 to n using a while loop in python.

n = int(input("Enter the n number:"))
a = 1

while n>=a:
    print(a)
    a+=1

print('_'*70)

# 13. Python Loops program to print all alphabets from a to z using for loop
#         Take chr method help to print characters with ASCII values
#         chr(65) = ‘A’
#         A-Z ASCII Range  65-90
#         a-z ASCII Range  97-122

for i in range(97,123):
    print(chr(i), end=" ")

print()
print('_'*70)
# 14. Python Loops program to print all even numbers between 1 to 100 in python.

for i in range(1,100):
    if i%2 == 0:
        print(i, end=" ")

print()
print('_'*70)
# 15. Python Loops program to print all odd numbers between 1 to 100 using python.

for j in range(1,100):
    if j%2 != 0:
        print(j, end=" ")
print()
print('_'*70)

# 24.Python loops program to enter a number and print its reverse using python.

num = 5254
reverse = 0

while num>0:
    temp = num%10
    reverse = reverse*10+temp
    num = num//10

print(reverse)