class BankAccount:

    total_accounts = 0

    def __init__(self, account_holder, initial_balance):

        self.account_number = BankAccount.total_accounts + 1
        BankAccount.total_accounts += 1
        self.account_holder = account_holder
        self.balance = initial_balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit")


    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal")


    def get_balance(self):
        return self.balance
    

    def __str__(self):
        return(
f"""Account holder: {self.account_holder},
bank account number: {self.account_number},
balance: {self.balance}""")
