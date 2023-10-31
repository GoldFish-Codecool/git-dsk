from BankAccount import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, account_holder, initial_balance, interest_rate):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    
    def apply_interest(self):
        self.balance = self.balance * (1 + self.interest_rate / 100)
        print(f"Interest applied. New balance: {self.balance}")
