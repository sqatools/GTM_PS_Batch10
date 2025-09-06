# 10/07/2025 Session Continue - Absent
# multilevel inheritance
# Super class/base class/ parent class

class Grandfather:
    def __init__(self,gf_name,gf_business):
        self.grandfather_name = gf_name
        self.grandfather_business = gf_business

    def show_grandfather_name(self):
        print("Grandfather Name:",self.grandfather_name)

    def show_grandfather_business(self):
        print("Grandfather Business:",self.grandfather_business)

    def show_grandfather_details(self):
        self.show_grandfather_name()
        self.show_grandfather_business()


class Father(Grandfather):
    def __init__(self,f_name,f_business,gf_name,gf_business):
        super().__init__(gf_name,gf_business)
        self.father_name = f_name
        self.father_business = f_business

    def show_father_name(self):
        print("Father Name:",self.father_name)

    def show_father_business(self):
        print("Father Business:",self.father_business)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()

# child class/ derived class
class Son(Father):
    def __init__(self,son_name,f_name,f_business,gf_name = 'Raja Khan',gf_business = 'Textile'):
        # initialize the constructor of father class
        super().__init__(f_name,f_business,gf_name,gf_business)
        self.son_name = son_name

    def show_son_name(self):
        print("Son Name:",self.son_name)

    def show_family_details(self):
        self.show_grandfather_details()
        self.show_father_details()
        self.show_son_name()

# with the help of son class object, we can access all method/variables of father and son class

obj = Son('Ryan','Varun','Engineer')
obj.show_family_details()
"""
Grandfather Name: Raja Khan
Grandfather Business: Textile
Father Name: Varun
Father Business: Engineer
Son Name: Ryan
"""
print('_'*70)

obj = Son('Ryan','Varun','Engineer','Shakti Singh','Contractor')
obj.show_family_details()
'''
Grandfather Name: Shakti Singh
Grandfather Business: Contractor
Father Name: Varun
Father Business: Engineer
Son Name: Ryan
'''