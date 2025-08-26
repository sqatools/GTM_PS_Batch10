# 10/07/2025 Session Continue - Absent

# Hierarchical inheritance
# Super class/base class/ parent class

class Father:
    def __init__(self,f_name,f_car):
        self.father_name = f_name
        self.father_car = f_car

    def show_father_name(self):
        print("Father Name:",self.father_name)

    def show_father_car(self):
        print("Father car:",self.father_car)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_car()

# child class/ derived class

class Son(Father):
    def __init__(self,son_name,son_job,f_name,f_car):
        super().__init__(f_name,f_car)
        self.son_name = son_name
        self.son_job = son_job

    def show_son_name(self):
        print("Son Name:",self.son_name)

    def show_son_job(self):
        print("Son Job:",self.son_job)

    def show_family_details(self):
        self.show_son_name()
        self.show_son_job()
        self.show_father_details()

class Daughter(Father):
    def __init__(self,d_name,d_car,f_name,f_car):
        super().__init__(f_name,f_car,)
        self.daughter_name = d_name
        self.daughter_car = d_car

    def show_daughter_name(self):
        print("Daughter Name:",self.daughter_name)

    def show_daughter_car(self):
        print("Daughter car:",self.daughter_car)

    def show_family1_details(self):
        self.show_father_details()
        self.show_daughter_name()
        self.show_daughter_car()

# with the help of son class object, we can access all method/variables of father and son class
obj = Daughter('Anamika','Tiago','Shailesh Rana','Innova')
obj.show_family1_details()

print('_'*70)
obj1 = Son('Aarav','abc','rajan','it')
obj1.show_family_details()