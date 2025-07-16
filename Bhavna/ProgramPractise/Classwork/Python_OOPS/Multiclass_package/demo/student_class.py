from teacher_class import Teacher

class Students(Teacher):
    def __init__(self,Student_head="Aasta Jadhav",Student_assist="Latika Agrawal"):
        super().__init__()

        self.Student_head = Student_head
        self.Student_Assistant = Student_assist

    def show_Students_details(self):
        print("Student Head:",self.Student_head)
        print("Student Assistant:",self.Student_Assistant)
