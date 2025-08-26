"""Write a program to calculate the frequency of each character in a string.
Input = “sqatools”"""
Input="sqatools"
result=dict()
r1=''
for i in Input:
    if i not in r1:
        r1=r1+i
        result[i]=Input.count(i)
print(result)