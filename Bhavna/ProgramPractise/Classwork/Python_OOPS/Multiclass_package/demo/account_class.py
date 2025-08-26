

class Account:
    def __init__(self,account_head = "Mr.Singh",account_assi = "Mr. Raathi"):
        self.account_head = account_head
        self.account_Assistant = account_assi


    def show_account_depart_details(self):
        print("Account Head:", self.account_head)
        print("Account Assistant:",self.account_Assistant)