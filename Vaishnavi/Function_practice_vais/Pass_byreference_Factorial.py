x=3
def factorial(x):
    fact1=1
    for i in range(1,x+1,1):
        fact1=fact1*i
    print(fact1)

factorial(x)

def add(n1,n2=30):
    sum=n1+n2
    print(sum)
add(20,40)