#Python function program to find the sum of all the numbers in a list.
def Sum_Of_List(*args):
    sum=0
    for i in args:
        if isinstance(i,list):
            len1=len(i)
            for j in range(len1):
                sum+=i[j]
        else:
            continue
    print(sum)


Sum_Of_List(2,3,4,"hi",[12,11,2,2,3])
