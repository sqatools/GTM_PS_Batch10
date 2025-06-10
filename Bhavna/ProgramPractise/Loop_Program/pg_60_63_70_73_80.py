# PYTHON LOOPS PRACTICE PROGRAM

# 60). Write a program to print a table of 5 using for loop using Python Loops.
# Output :
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

t = 5
a = 0

for n in range(1,11):
    a = n*t
    print(n,"*",t," ",a)

print('_'*70)

# 63). Write a program to print each word in a string on a new line using Python Loops.
# Input = Sqatools

str = "Sqatools"
for i in str:
    print(i)

print('_'*70)

# 70). Write a program to print a table of 2 using a while loop in Python.

num = 2
output = 0

for l in range(1,11):
    output = num*l
    print(num,"*",l,"=",output)

print('_'*70)

# 73). Print numbers from 1-10 except 5,6 using a while loop in Python.
h = 1
while h<=10:
    if h!=5 and h!=6:
        print(h)
    h+=1
print('_'*70)

# 80). Write a program to print 1-10 natural numbers but it should stop when the number is 6 using a while loop in Python.
c = 1
while c<=10:
    if c!=6:
        print(c)
    else:
        break
    c+=1

print('_'*70)
