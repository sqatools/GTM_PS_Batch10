from student_class import Students

class School(Students):

    def __init__(self,school_name,school_address):
        super().__init__()
        self.school_name = school_name
        self.school_address = school_address

    def show_school_details(self):
        print("Schhol Name:",self.school_name)
        print("School Address:",self.school_address)

obj = School('St.Xaviers High School','Nagpur')


obj.show_school_details()
obj.show_Students_details()
obj.show_teacher_details()
obj.show_admin_depr_details()
obj.show_account_depart_details()