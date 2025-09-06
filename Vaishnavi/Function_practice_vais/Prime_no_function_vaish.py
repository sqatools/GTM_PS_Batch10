def Prime(value):
    count=0
    for i in range(1,value+1):
        if value%i==0:
            count+=1
        else:
            continue
    print(f"{count} is the count")
    if count>2:
        print(f"{value} is not prime number")
    else:
        print(f"{value} is prime number")


Prime(10)