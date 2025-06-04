# PYTHON LOOPS PROGRAM

# 1. Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)

print('_'*70)
'''
2. Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
for i in range(1,6):
    for j in range(0,i):
        print("*", end=" ")

    print()

for k in range(1,5):
    for l in range(5,k,-1):
        print("*",end=" ")

    print()

print()
print('_'*70)

# 5. Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.


for i in range(0,7):
    if i==3 or i==6:
        continue
    print(i)

print('_'*70)

# 7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.

for i in range(1,31):
    if i%3==0 and i%5==0:
        print("FizzBuzz", i)
    elif i%3 == 0:
        print("Fizz",i)
    elif i%5 ==0:
        print("Buzz",i)

print('_'*70)

