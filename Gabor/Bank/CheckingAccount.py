from BankAccount import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, account_holder, initial_balance, overdraft_limit):
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit


    def withdraw(self, amount):
        if amount <= self.overdraft_limit:
            return super().withdraw(amount)
        else:
            print("Over the limit")