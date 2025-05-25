"""
Python Data Types
1.  Number data type
    i). Integer
    ii). Float
    iii). Complex Number

2.  Sequential data type
    i). String
    ii). List
    ii). Tuple

3.  Dictionary Data type
4.  Set Data type
5.  Boolean Data type

"""

######### Integer Data Type ######
"""
Properties:
->  Integer is immutable data type, once it is defined we can not update.
->  Integer data type only contains whole number.
->  Integer can be positive or negative
->  There is no specific limit for integer datatype, we can assign any long number
    as integer value.


"""
######### Float Data Type ######
"""
Properties:
->  Float is immutable data type, once it is defined we can not update.
->  Float data type only contains pointer value number.
->  Float number can be positive or negative.
->  There is no specific limit for float datatype, we can assign any long number
    as float value.
"""
######### Complex Data Type ######
"""
Properties:
1.  complex data type is immutable data type
2.  complex data type is combination of real and imaginary number
    e.g x+yj
    x :  real number
    y :  imaginary number
3.  complex data type could be positive and negative both
"""
"""
str="santhoshkumar"
if len(str)<2:
    print(True)
else:
#    print(str[:2]+str[-2:])
     print(str[2:] + str[:-2])

"""

string="i", "am", "happy", "to", "in", "the", "community"
str=len(string)
print(str)

print("_"*50)

str="sqatools"
print(str[-2::]*4)

print("_"*50)

string = "sqatools"

if len(string) % 4 == 0:
    print(string[::-1])

print("_"*50)

string = "sqatoolspythonspy"
sub= "spy"
str = string.count("spy")
print(str)