from teacher_class import Teachers

class Students(Teachers):
    def __init__(self, student_head='Mr Shobit', student_assis='Mr Jatin'):
        super().__init__()
        self.student_head = student_head
        self.student_assistant = student_assis

    def show_student_deprt_details(self):
        print("students Head :", self.student_head)
        print("students Assistant :", self.student_assistant)


