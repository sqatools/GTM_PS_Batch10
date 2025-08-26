def fib(**kwargs):
    a=0
    b=1
    temp=0
    for key,value in kwargs.items():
        value=kwargs['key']
    for val in range(0,value,1):
                #print(val)
                sum=a+b
                a=b
                b=sum
                print(f"{value}",sum)

fib(key=30,key1=6)
