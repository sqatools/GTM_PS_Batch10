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
num = 0
num1 = 10
num2 = 4545435
num3 = 56564356456456453635463456
num4 = -5678

print("num :", num, type(num))  # 0 <class 'int'>
print("num1 :", num1, type(num1))  # 10 <class 'int'>
print("num2 :", num2, type(num2))  # 4545435 <class 'int'>
print("num3 :", num3, type(num3))  # 56564356456456453635463456 <class 'int'>
print("num4 :", num4, type(num4))  # -5678 <class 'int'>

a = 100
print(a)  # 100
a = 200
print(a)  # 200

print("_" * 50)