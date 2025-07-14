tup3 = (4, 6, 8, 12, 56, (3, 5), [4, 7, 1], 'Hello')
tup2=tup3 [5][1]
tup4=tup3 [6][2::-1]
print(tup2)
print(tup4)

print(dir(list))


# Q1 write a tuple program to get factorial of numbers.
tup4 = (2, 3, 4, 5, 6)
i=1

output=[]
for val in tup4:
    fact = 1
    while(val>0):#2>0,1>0
        fact=fact*val#1*2=2,2*1
        val-=1 #val=1,0
    output.append(fact)
print(tuple(output))

print("-*"*50)

tuple1=(121,242,243,244)
out1=[]

for val1 in tuple1:
    pal = 0
    temp=val1
    while(val1>0):
      rem=val1%10
      pal=pal*10+rem
      val1=val1//10
    if pal==temp:
        print(f"{temp} is palindrome")
    else:
        print(f"{temp} not is palindrome")






