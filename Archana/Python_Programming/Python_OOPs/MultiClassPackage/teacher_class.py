from admin_class import Admin

class Teachers(Admin):
    def __init__(self, teacher_head='Mrs Pooja Mehra', teacher_assis='Mrs Vidya Verma'):
        super().__init__()
        self.teacher_head = teacher_head
        self.teacher_assistant = teacher_assis

    def show_teacher_depart_details(self):
        print("teachers Head :", self.teacher_head)
        print("teachers Assistant :", self.teacher_assistant)


