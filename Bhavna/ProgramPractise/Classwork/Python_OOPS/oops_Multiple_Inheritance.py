# 10/07/2025 Session Continue - Absent

# multiple inheritance
# Super class/base class/ parent class

class mother:
    def __init__(self,m_name,m_business):
        self.mother_name = m_name
        self.mother_business = m_business

    def show_mother_name(self):
        print("Mother Name:",self.mother_name)

    def show_mother_business(self):
        print("Mother business:",self.mother_business)

    def show_mother_details(self):
        self.show_mother_name()
        self.show_mother_business()

class Father:

    def __init__(self,f_name,f_business):
        self.Father_name = f_name
        self.Father_business = f_business

    def show_father_name(self):
        print("Father Name:",self.Father_name)

    def show_father_business(self):
        print("Father Business:",self.Father_business)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()

# child class/ derived class
# When we setup, multiple inheritance fow two classes, then order of class being called with get priority to initialize
# the constructor in the child class constructor, these concept is known MRO (Method resolution order)

class son(mother,Father):
    def __init__(self,son_name,m_name,m_business,f_name,f_business):
        super().__init__(m_name,m_business)
        self.son_name = son_name
        self.Father_name = f_name
        self.Father_business = f_business

    def show_son_name(self):
        print("Son Name:",self.son_name)

    def show_family_details(self):
        self.show_mother_details()
        self.show_father_details()
        self.show_son_name()

obj = son('Aditya','Meena','Tailor','Arvind','Professor')
obj.show_family_details()

'''
Mother Name: Meena
Mother business: Tailor
Father Name: Arvind
Father Business: Professor
Son Name: Aditya
'''