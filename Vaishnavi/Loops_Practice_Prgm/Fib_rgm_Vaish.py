"""
Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
"""
a=0
b=1
sum=0
print(a)
print(b)
for i in range (0,21):
    sum=a+b
    a=b
    b=sum
    print(sum)
