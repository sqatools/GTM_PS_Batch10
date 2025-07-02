"""Write a Python program to find the longest capital letter word from the string.
Input = “Learning PYTHON programming is FUN”"""
input1="Learning PYTHON programming is FUN FANTASTICCC"
result=""
for i in input1.split():
    if i.isupper():
        result=result+" "+i
result=result.split()
print(max(result, key=len))

