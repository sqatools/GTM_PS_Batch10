#Python function program to multiply all the numbers in a list
#[-8, 6, 1, 9, 2]
def multiply(*args):
    mul=1
    for i in args:
        if isinstance(i,list):
            len1=len(i)
            for j in range(len1):
                print(i[j])
                mul*=i[j]
        else:
            continue
        print(mul)

multiply([-8, 6, 1, 9, 2],"k",12.3)