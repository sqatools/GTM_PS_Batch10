

class Account:
    def __init__(self, account_head='Mr Mishra', account_assis='Mr Verma'):
        self.account_head = account_head
        self.account_assistant = account_assis

    def show_account_depart_details(self):
        print("Accounts Head :", self.account_head)
        print("Accounts Assistant :", self.account_assistant)


