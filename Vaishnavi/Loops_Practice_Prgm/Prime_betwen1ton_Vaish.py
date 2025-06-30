#Write a program to print all Prime numbers between 1 to n using Python Loops.
#Python loops program to find the sum of all prime numbers between 1 to n using Python

n=int(input("value plz"))
count=0
sum=0
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
        else:
            continue
    if count > 2:
        print("it is not prime no", i)
    else:
        print("its prime no :", i)
        sum += i
print(sum)
