a , b = 10,200
x, y = a, b
print("x values is:",x)
print("y values is :",y)

print("&&__--&&"*10)

m =10
n = 20
o =m
if m==o:
    print(o)
else:
    print(m)

print("&&__--&&"*10)
g = 70
n= 90
if g==n:
    print("both are  same",g)
else:
    print("both are different:",g,n)
######## import

from datetime import datetime
date= datetime.now().strftime('%H:%M:%S')
print(date)

###       **
##     **    **
 #        **

print("*"*50)

for i in range(1,5):
    for j in range(1,4):
        if i in(3,5):
            if j in(1,2,4,5):
                print("*",end=" ")
            else:
                print(" ",end= " ")
        elif i in(2,3,4):
           if j in(3,4,5):
               print("&",end=" ")
           else:
               print(" ",end=" ")
    print("%",end=" ")


