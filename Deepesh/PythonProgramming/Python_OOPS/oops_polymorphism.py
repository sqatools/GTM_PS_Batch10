"""
polymorphism :  This stand for one person/operator/method is performing multiple task.
1.  Method Overriding : when we setup inheritance between 2 classes, and both parent and child class has same method,
                        then child class method will override the parent the class method.
2.  Method Overloading :  Python does not support method overloading
                       ->  When one class has 2 method with same name, but different parameters, then it is called
                           method overloading.

                      ->  If create method overloading concept in Python, then it will consider latest defined method only
3.  Operator overloading:  If one single operator is performing task, then it is called operator overloading
                          e.g. Plus icon(+) can add two integers, can add 2 lists, can add 2 float, can add 2 strings.
"""

class xyz:

    def greeting(self, msg):
        print("---xyz--")
        print(msg)


    def repeat_String(self, str1, num):
        print(str1*num)


class ABC(xyz):

    def greeting(self, msg):
        print("----ABC---")
        print(msg)


    def addition(self, num1, num2):
        print("addition value :", num1+num2)


    def addition(self, num1, num2, num3):
        print("Addition of three values :", num1+num2+num3)



obj = ABC()
obj.greeting("Good Morning")
"""
----ABC---
Good Morning
"""

# access method overloading, method.
#obj.addition(50, 60)
# TypeError: ABC.addition() missing 1 required positional argument: 'num3'

obj.addition(50, 60, 70)
# Addition of three values : 180

print("_"*50)
############################### Operator overloading ##########################

v1 = 400
v2 = 500
s1 = "Hello"
s2 = "Python Programming"
print("addition :", v1+v2)
print("addition :", v1.__add__(v2))
print("combine string :", s1.__add__(s2))
print(dir(str)) # 500
print(dir(list))
print(dir(float))


n1 = 50
n2 = 10
print("multiplication of the number, :", n1*n2) # 500
print("multiplication of the number, :", n1.__mul__(n2)) # 500