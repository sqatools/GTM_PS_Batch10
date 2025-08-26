#write a phython function to get a fib values from 1 to 100
def fibonacci(i):
    a=0
    b=1
    for count in range(1,i,1):
        sum=a+b
        a=b
        b=sum
        print(sum,end=" " )

fibonacci(100)
