# String Basics
str1 = "Hello Python Programming"
print(str1, type(str1))

# string Formatting
print("-" * 50)
print("string Formatting")
print("=" * 18)
str1 = "Welcome to basic Python Programming "
str2 = " An Easy and fun way of coding"
new_str = str1 + str2
print(new_str)

# 1. String Concatenation:
print("-" * 50)
print("# 1. String Concatenation:")
str3 = "My name is Archana, Am living in Chennai city, am 25 years old"
print(str3)

name = "Hishal"
city = "Bangalore"
age = 26
str4 = "My name is " + name + " Am living in  " + city + " am " + str(age) + " years old"
print(str4)

# 2. Format Method
print("# 2. Format Method")
print("=" * 18)
str5 = "My name is {} , Am living in  {} and am {}  years old".format(name, city, age)
print(str5)

# 3. F string formatting
print("# 3. F string formatting")
print("=" * 18)
str6 = f"My name is {name}, Am living in {city} and am {age}  years old"
print(str5)


## Slicing in String
"""
Rule1 : str[start_index  : last index]
->  Default step value is 1
->  Result will include start_index character and exclude last index char in the output
->  Result value will always print from left to right:
->  start and last index value could be positive or negative
->  If we dont provide the last index the default last index would end of string. 
    e.g.  str[4:] # here output will be from 4 to end of string.
->  Default start_index is zero str[:3] # Here output will output value from 0 to 2
        012345
 str = "Hello"
       -5-4-3-2-1
"""

str7 = "Hello Internet"
print(str7[-8:]) # Internet
print(str7[0:]) # Hello Internet
print(str7[0:5]) # Hello

print("_"*50)
##################################
"""
Rule2 : str[start_index: last_index: step_value]
->  Output will include start_index and exclude last_index and return output as per the step value
->  default start_index is 0 and default last_index is end of string with positive step value
->  default start_index is -1 and default last_index is begining of string with negative step value
->  default step value is  1
"""
str8 = "Mastering in Python"
## here output will include 0 to 9 with 1 step value
print(str8[0:9:1]) #Mastering

## here output will include 0 to 9 with 2 step value
print(str8[0:9:2]) #Mseig


# default start_index is 0 and default last_index is end of string with positive step value
print(str8[:13:1]) #Mastering in
print(str8[2::2]) #seigi yhn

# default start_index is -1 and default last_index is begining of string with negative step value
# prints in reverse
print(str8[::-1])
print(str8[:8:-1]) # nohtyP ni

