"""
Inheritance : When one class acquire the property another class, then it called inheritance.

1. singleton inheritance :  class A ->  Class B
2. multiple level inheritance :  class A -> Class B -> Class C
3. multiple inheritance :  Class A ->  Class C , Class B ->  Class C
4. Hierarchical inheritance :  Class A - > Class B,  Class A ->  Class C
"""


# multiple inheritance
# Super class/base class/ parent class
class Mother:
    def __init__(self, m_name, m_business):
        self.Mother_name = m_name
        self.Mother_business = m_business


    def show_mother_name(self):
        print("Mother Name :", self.Mother_name)

    def show_mother_business(self):
        print("Mother Business :", self.Mother_business)

    def show_mother_details(self):
        self.show_mother_name()
        self.show_mother_business()



class father:
    def __init__(self, f_name, f_business, f_car):
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car

    def show_father_name(self):
        print("Father name :", self.father_name)

    def show_father_business(self):
        print("Father business :", self.father_business)

    def show_father_car(self):
        print("Father car :", self.father_car)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()

# child class/ derived class
# When we setup, multiple inheritance fow two classes, then order of class being called with get priority to initialize the
# the constructor in the child class constructor, these concept is known MRO (Method resolution order)
class son(Mother, father):
    def __init__(self, son_name, m_name, m_business, f_name, f_business, f_car):
        super().__init__(m_name, m_business)
        self.son_name = son_name
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car

    def show_son_name(self):
        print("Son name  :", self.son_name)

    def show_family_details(self):
        self.show_mother_details()
        self.show_father_details()
        self.show_son_name()




obj = son('Rahul', 'Pooja', 'Fashion', 'Sachine', 'IT Business', 'TATA Harrier')
obj.show_family_details()
