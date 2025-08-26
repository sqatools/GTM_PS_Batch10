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

p1 = 10 + 20j
print("p1 : ", p1, type(p1))
# p1 :  (10+20j) <class 'complex'>

p2 = -400 - 500j
print("p2 :", p2, type(p2))
# p2 : (-400-500j) <class 'complex'>

print("real number :", p2.real, type(p2.real))
# real number : -400.0 <class 'float'>

print("imaginary number :", p2.imag, type(p2.imag))
# imaginary number : -500.0 <class 'float'>