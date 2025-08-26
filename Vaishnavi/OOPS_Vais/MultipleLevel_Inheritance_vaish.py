class GrandFather:
    def __init__(self,gf_name,gf_property):
        self.Gf_name=gf_name
        self.Gf_property=gf_property

    def grandfather_details(self):
        print("garanfather name :",self.Gf_name)
        print("Grandfather Property :", self.Gf_property)

class Father(GrandFather):
    def __init__(self, f_name, f_bussiness, f_car, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
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
        self.grandfather_details()


class Son(Father):
    def __init__(self, son_name, f_name, f_bussiness, f_car, gf_name, gf_property):
        super().__init__(f_name, f_bussiness, f_car, gf_name, gf_property)
        self.son_name=son_name

    def show_son_name(self):
        print("Son name :",self.son_name)

    def show_family_details(self):
        self.show_father_deatils()
        self.show_son_name()

obj=Son("Akassh","mohan","Diamond dealer","BMW","Ramlaal","Bangloow")
obj.show_family_details()

