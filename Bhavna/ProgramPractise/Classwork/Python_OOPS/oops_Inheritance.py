# 10/07/2025 Session - Absent

"""
Inheritance : When one class acquire the property of another class, then it called inheritance.

1. singleton inheritance :  class A ->  Class B
2. multilevel inheritance :  class A -> Class B -> Class C
3. multiple inheritance :  Class A ->  Class C , Class B ->  Class C
4. Hierarchical inheritance :  Class A - > Class B,  Class A ->  Class C
"""


# singleton inheritance
# Super class/base class/ parent class

class father:
    def __init__(self,f_name,f_business,f_car):
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car

    def show_father_name(self):
        print("Father name:",self.father_name)

    def show_father_business(self):
        print("Father Business:",self.father_business)

    def show_father_car(self):
        print("Father Car:",self.father_car)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()

# Child class/ derived class

class son(father):
    def __init__(self,son_name,f_name,f_business,f_car):
        # initialize the constructor of father class
        super().__init__(f_name,f_business,f_car)
        self.son_name = son_name

    def show_son_name(self):
        print("Son Name:",self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()

# with the help of son class object, we can access all method/variables of father and son class
obj = son('Amit','Ajay Singh','Contractor','Audi car')
obj.show_family_details()