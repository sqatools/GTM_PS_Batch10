"""
Inheritance : When one class acquire the property another class, then it called inheritance.

1. singleton inheritance :  class A ->  Class B
2. multiple level inheritance :  class A -> Class B -> Class C
3. multiple inheritance :  Class A ->  Class C , Class B ->  Class C
4. Hierarchical inheritance :  Class A - > Class B,  Class A ->  Class C
"""


# multilevel inheritance
# Super class/base class/ parent class
class GrandFather:
    def __init__(self, gf_name, gf_property):
        self.grandfather_name = gf_name
        self.grandfather_property = gf_property


    def show_grand_father_name(self):
        print("Grand Father Name :", self.grandfather_name)

    def show_grand_father_property(self):
        print("Grand Father Property :", self.grandfather_property)


    def show_grand_father_details(self):
        self.show_grand_father_name()
        self.show_grand_father_property()



class father(GrandFather):
    def __init__(self, f_name, f_business, f_car, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
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
class son(father):
    def __init__(self, son_name, f_name, f_business, f_car, gf_name='Daya Ram', gf_property='100 Acr Land'):
        # initialize the constructor of father class
        super().__init__(f_name, f_business, f_car, gf_name, gf_property)
        self.son_name = son_name

    def show_son_name(self):
        print("Son name  :", self.son_name)

    def show_family_details(self):
        self.show_grand_father_details()
        self.show_father_details()
        self.show_son_name()

# with the help of son class object, we can access all method/variables of father and son class
obj = son('Mohit', 'Mohan Sharma', 'Construction', 'BMW Car')
obj.show_family_details()

print("_"*50)

obj = son('Mohit', 'Mohan Sharma', 'Construction', 'BMW Car', 'Manmohan', '50 Acr Land')
obj.show_family_details()