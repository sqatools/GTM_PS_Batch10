# 04/06/2025 Session
# Srings

str1 = "Hello Python Programming"
print(str1, type(str1))

# String Formatting
a = "Hello my name is Ryan and age is 25 and living in Bangalore "
name = "Isha"
age = 20
place = "Nagpur"

# 1. String Concatenation:

val = "Hello" + " Good Morning"
print(val)
result = "Hello my name is "+name+" and age is "+str(age)+" and living in "+place
print(result)

# 2. Format Method:
result1 = "Hello my name is {} and age is {} and living in {}".format(name,age,place)
print(result1)

# 3.F string Formatting:
result2 = f"Hello my name is {name} and age is {age} and living in {place}"
print(result2)

print('_'*70)
##############################################
# Apply loop on string data

str2 = "Python"
# loop without indexing
for i in str2:
    print(i)

print('_'*70)

# loop with indexing
string_length = len(str2)
print(string_length)

for i in range(string_length):
    print(i, str2[i])

print('_'*70)

for i in range(-1, -string_length,-1):
    print(i, str2[i])

print('_'*70)
######### get character with index #########

print(str2[3])
print(str2[-5])

print('_'*70)

######### slicing in string #########

"""
Rule1 : str[start_index: last index]
->  Default step value is 1
->  Result will include start_index character and exclude last index char in the output
->  Result value will always print from left to right:
->  start and end index value could be positive or negative
->  If we dont provide the last index the default last index would end of string. 
    e.g.  str[4:] # here output will be from 4 to end of string.
->  Default start_index is zero str[:3] # Here output will output value from 0 to 2

"""
str3 = "Good Morning"

print(str3[0:6])        #Good M
print(str3[-7:-2])      #Morni
print(str3[-7:])        #Morning
# This will include output from -7 to end of string

# This will include output from 0 to 7
print(str3[:8])         #Good Mo

print(str3[4:1])        #Empty
print(str3[2:-1])       #od Mornin
print(str3[-9:10])      #d Morni
print(str3[:])          #Good Morning

print('_'*70)

"""
Rule2 : str[start_index: last_index: step_value]
->  Output will include start_index and exclude last_index and return output as per the step value
->  default start_index is 0 and default last_index is end of string with positive step value
->  default start_index is -1 and default last_index is begining of string with negative step value
->  default step value is  1
"""

str4 = "Very Good Morning"

print(str4[5:9:1])      #Good
# here output will include 2 to 7 with 1 step value

print(str4[2:10:2])     #r od
# here output will include 2 to 9 with 2 step value

# default start_index is 0 and default last_index is end of string with positive step value
print(str4[:7:1])       #Very Go
print(str4[2::2])       #r odMrig

# default start_index is -1 and default last_index is begining of string with negative step value
print(str4[:8:-1])      #gninroM
print(str4[5::-1])      #G yreV

# ->  default step value is  1
print(str4[2:14:])      #ry Good Morn
print(str4[-1:-10:])       #empty output

print('_'*70)

######## ASSIGNMENT_3 ###########
"""
# str1 = "Virat is greate Indian Player"
output1 = "Player is greate Indian Virat"
output2 = "VVirat is greate Indian Playerr"
output3 = "VViratt iiss ggreatee IIndiann PPlayerr"
output4 = "(Virat is greate): reverse this part : Indian Player"
"""

str1 = "Virat is great Indian Player"
name = "Virat"
Profession = "Player"
output1 = f"{Profession} is great Indian {name}"
print("Output1:", output1)
print("Output2:",str1[0] + str1 + str1[-1])

a = str1[0]*2+str1[1:4]+str1[4]*2
b = str1[6]*2 + str1[7]*2
c = str1[9]*2 + str1[10:13] + str1[13]*2
d = str1[15]*2 + str1[16:20] + str1[20]*2
e = str1[-6]*2 + str1[-5:-1] + str1[-1]*2
print("Output3:",a+" "+b+" "+c+" "+d+" "+e)

Output4 = str1[13::-1] + str1[14:28]
print("Output4:", Output4)
print('_'*70)
