"""Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”"""

input1="Programming"
result=''
for char in input1:
    if char in result:
        result=result+'$'
    else:
        result=result+char
print(result)

input2="Programming"
result=''
for char in input2:
    if input2.count(char)>=2:
        input2=input2.replace(char,'#',1)
        input2=input2.replace(char,'$',1)
        input2=input2.replace('#',char,1)
print(input2)