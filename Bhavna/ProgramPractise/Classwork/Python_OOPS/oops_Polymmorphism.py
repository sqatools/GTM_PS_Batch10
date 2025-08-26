# 11/07/2025 Session - Absent

"""
polymorphism :  This stand for one person/operator/method is performing multiple task.
1.  Method Overriding : when we setup inheritance between 2 classes, and both parent and child class has same method,
                        then child class method will override the parent class method.
2.  Method Overloading :  Python does not support method overloading
                       ->  When one class has 2 method with same name, but different parameters, then it is called
                           method overloading.

                      ->  If create method overloading concept in Python, then it will consider latest defined method only
3.  Operator overloading:  If one single operator is performing task, then it is called operator overloading
                          e.g. Plus icon(+) can add two integers, can add 2 lists, can add 2 float, can add 2 strings.
"""

class abc():

    def greeting(self,msg):
        print("---abc---")
        print(msg)

    def repeat_string(self,str1,num):
        print(str1*num)

class xyz():

    def greeting(self,msg):
        print("---xyz---")
        print(msg)

    def addition(self,n1,n2):
        print("Addition:",n1+n2)

    def addition(self,n1,n2,n3):
        print("Addition of values:",n1+n2+n3)

obj = xyz()
obj.greeting("Good Evening")

"""
---xyz---
Good Evening
"""
# access method overloading, method.
# obj.addition(50,60)
# TypeError: xyz.addition() missing 1 required positional argument: 'n3'

obj.addition(20,30,40)
# Addition of values: 90

print('_'*70)

############################### Operator overloading ##########################
v1 = 200
v2 = 300
s1 = "Hi"
s2 = "Python Course"
print("Addition:",v1+v2)
print("Addition:",v1.__add__(v2))
print("combine string:",s1.__add__(s2))
print(dir(str))
print(dir(list))
print(dir(float))

n1 = 10
n2 = 20
print("Multiplication of the number:",n1*n2) #200
print("Multiplication of the number:",n1.__mul__(n2)) #200