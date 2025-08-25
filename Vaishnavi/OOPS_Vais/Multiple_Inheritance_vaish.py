class Mother:
    def __init__(self,mother_name,mother_property):
        self.mother_name=mother_name
        self.mother_property=mother_property

    def Mother_details(self):
        print("Mother name :",self.mother_name)
        print("Mother Property :", self.mother_property)

class Father:
    def __init__(self, f_name, f_bussiness, f_car):
        self.Father_name=f_name
        self.fatheer_business=f_bussiness
        self.father_car=f_car

    def Show_father_name(self):
        print("Father Name:",self.Father_name)

    def Show_father_business(self):
        print("father business:",self.fatheer_business)

    def show_father_car(self):
        print("Father Car",self.father_car)

    def show_father_deatils(self):
        self.Show_father_name()
        self.show_father_car()
        self.Show_father_business()



class Son(Father,Mother):
    def __init__(self, son_name, f_name, f_bussiness, f_car, mother_name, mother_property):
        super().__init__(f_name, f_bussiness, f_car)
        self.son_name=son_name
        self.mother_name = mother_name
        self.mother_property = mother_property

    def show_son_name(self):
        print("Son name :",self.son_name)

    def show_family_details(self):
        self.show_father_deatils()
        self.show_son_name()
        self.Mother_details()

obj=Son("Akassh","mohan","Diamond dealer","BMW","leela","Actor")
obj.show_family_details()

