from admin_class import Admin

class Teacher(Admin):
    def __init__(self,teacher_head="Pooja Sharma",teacher_assist="Vedika Rana"):
        super().__init__()
        self.teacher_head = teacher_head
        self.teacher_assistant = teacher_assist

    def show_teacher_details(self):
        print("Teacher Head:",self.teacher_head)
        print("Teacher Assistant:",self.teacher_assistant)