str1 = "Hello Python Programming"

print(str1, type(str1))
# Hello Python Programming <class 'str'>

# string formatting
str2 = "Hello my name is Rahul and age is 25 and living in Mumbai"
name = "Pankaj"
age = 30
city = "Pune"

# 1. String Concatenation:
val = "Hello"+" Good Morning"
print(val)
result1 =  "Hello my name is "+name+" and age is "+str(age)+" and living in "+city
print(result1)
# Hello my name is Pankaj and age is 30 and living in Pune

# 2. Format Method:
result2 =  "Hello my name is {} and age is {} and living in {}".format(name, age, city)
print(result2)
# Hello my name is Pankaj and age is 30 and living in Pune

# 3. F string formatting:
result3 =  f"Hello my name is {name} and age is {age} and living in {city}"
print(result3)
# Hello my name is Pankaj and age is 30 and living in Pune



print("_"*50)
##############################################
# Apply loop on string data

str5 = "Programming"
# loop without indexing
for char in str5:
    print(char)

print("_"*50)
# loop with indexing
string_length = len(str5)
print(string_length)

for i in range(string_length):
    print(i, str5[i])

print("_"*50)
# loop with indexing
for i in range(-1, -string_length, -1):
    print(i, str5[i])

print("_"*50)
######### get character with index #########
str6 = "Python"

print(str6[3]) # h
print(str6[-5]) # y


print("_"*50)
######### slicing in string #########
"""
Rule1 : str[start_index: last index]
->  Default step value is 1
->  Result will include start_index character and exclude last index char in the output
->  Result value will always print from left to right:
->  start and index index value could be positive or negative
->  If we dont provide the last index the default last index would end of string. 
    e.g.  str[4:] # here output will be from 4 to end of string.
->  Default start_index is zero str[:3] # Here output will output value from 0 to 2

"""

str7 = "Good Morning"
print(str7[0:4]) # Good
print(str7[-7:-1]) # Mornin
# This will include output from -7 to end of string
print(str7[-7:]) # Morning
# This will include output from 0 to 7
print(str7[:8]) # Good Mor

print(str7[5:1])  # EMPTY
print(str7[2:-1]) # od Mornin
print(str7[-9:10]) # d Morni
print(str7[:]) # Good Morning


print("_"*50)
##################################
"""
Rule2 : str[start_index: last_index: step_value]
->  Output will include start_index and exclude last_index and return output as per the step value
->  default start_index is 0 and default last_index is end of string with positive step value
->  default start_index is -1 and default last_index is begining of string with negative step value
->  default step value is  1
"""
str8 = "Very Good Morning"
# here output will include 2 to 7 with 1 step value
print(str8[5:9:1])  # Good
# here output will include 2 to 14 with 2 step value
print(str8[2:15:2])  # r odMri

# default start_index is 0 and default last_index is end of string with positive step value
print(str8[:10:1]) # Very Good
print(str8[2::2]) # r odMrig

# default start_index is -1 and default last_index is begining of string with negative step value
print(str8[:8:-1]) # gninroM

print(str8[::-1]) # gninroM dooG yreV
# [-1:-len(str):-1]


# ->  default step value is  1
print(str8[2:14:])  # ry Good Morn
print(str8[-1:-10:])  # EMPTY output


