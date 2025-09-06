from student_class import Students

class School(Students):
    def __init__(self, school_name, school_address):
        super().__init__()
        self.school_name = school_name
        self.school_address = school_address


    def show_school_name(self):
        print("School Name :", self.school_name)

    def show_school_address(self):
        print("School Address :", self.school_address)


obj = School('Prestige International School', 'Mumbai Thane')

obj.show_account_depart_details()
obj.show_admin_deprt_details()
obj.show_teacher_depart_details()
obj.show_student_deprt_details()