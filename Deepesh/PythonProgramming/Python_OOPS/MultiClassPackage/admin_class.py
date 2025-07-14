from Deepesh.PythonProgramming.Python_OOPS.MultiClassPackage.demo.account_class import Account

class Admin(Account):
    def __init__(self, admin_head='Mr Rahul Agrawal', admin_assis='Mr Mohit More'):
        super().__init__()
        self.admin_head = admin_head
        self.admin_assistant = admin_assis

    def show_admin_deprt_details(self):
        print("Admin Head :", self.admin_head)
        print("Admin Assistant :", self.admin_assistant)


