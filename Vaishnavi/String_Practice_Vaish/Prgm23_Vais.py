"""Write a Python program to get common words from strings.
Input String1 = “Very Good Morning, How are You”
Input String1 = “You are a Good student, keep it up”
Output = “You Good are”"""
i1="Very Good Morning, How are You"
i2="You are a Good student, keep it up"
result=""
for i in i1.split():
    for k in i2.split():
        if i==k:
            result=result+" "+i
print(result)

