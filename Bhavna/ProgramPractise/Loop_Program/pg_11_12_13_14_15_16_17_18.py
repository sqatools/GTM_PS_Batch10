# PYTHON LOOPS PRACTICE PROGRAM

# 11. Python Loops program to print all natural numbers from 1 to n using a while loop in python.

n = int(input("Enter the n number:"))
a = 1

while n>=a:
    print(a)
    a+=1

print('_'*70)

# 12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.

n1 = int(input("Enter the n no.:"))
b=1
while n1>=b:
    print(n1,end=" ")
    n1-=1
print()


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
###############################################
# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
c = 0
n = int(input("Enter the number:"))
for k in range(1,n+1):
    c+=k
print(c)

print('_'*70)

# 17). Python program to find the sum of all even numbers between 1 to n using python.

even = 0
n = int(input("Enter the no.:"))
for j in range(1,n+1):
    if j%2==0:
        even+=j
print("sum of all even no.:", even)

print('_'*70)

# 18). Python Loops program to find the sum of all odd numbers between 1 to n using python.

odd = 0
p = int(input("Enter the n no.:"))
for k in range(1,n+1):
    if k%2!=0:
        odd+=k
print("Sum of all odd no.:", odd)

print('_'*70)
