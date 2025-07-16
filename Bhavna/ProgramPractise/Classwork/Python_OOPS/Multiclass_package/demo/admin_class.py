
from Bhavna.ProgramPractise.Classwork.Python_OOPS.Multiclass_package.demo.account_class import Account

class Admin(Account):

    def __init__(self,admin_head="Mr.Rajesh Kar",admin_assis="Mr.Rajeev"):
        super().__init__()
        self.admin_head = admin_head
        self.admin_assistant = admin_assis

    def show_admin_depr_details(self):
        print("Admin Head:",self.admin_head)
        print("Admin Assistant",self.admin_assistant)