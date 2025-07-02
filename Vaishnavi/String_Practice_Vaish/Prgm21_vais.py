"""Write a Python to remove unwanted characters from the given string.
Input = “Prog^ra*m#ming”
Output = “Programming”"""
input1="Prog^ra*m#ming"
result=''
for i in input1:

    if i.isalpha():
        result=result+i
    else:
        continue
print(result)
