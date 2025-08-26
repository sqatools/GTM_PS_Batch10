def sum(n1,n2):
    print(n1+n2)

p=100
q=101
sum(n1=p,n2=q)

def Isprime1(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
        else:
            continue

    if count > 2:
        print("False")
    else:
        print("true")

if __name__=="__main__":
    Isprime1(7)
