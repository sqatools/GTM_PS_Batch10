"""Write a Python program to remove duplicate words from the string.
Input = “John jany sabi row john sabi”
output = “John jany sabi row”"""
Input = "John jany sabi row john sabi"
Input=Input.lower()
output=Input.split()
result=""
for word in output:
    if word not in result:
        result=result+" "+''.join(word)
    else:
        continue
print(result)
