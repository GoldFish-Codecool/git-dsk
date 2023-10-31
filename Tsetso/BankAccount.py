class BankAccount:

    total accounts = 0

    def _init_(self, account_holder, initial_balance):
        self.account_number = BankAccount.total_accounts + 1
        BankAccount.total_accounts += 1
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount => 0
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else 
            print("Invalid deposit")


    def withdraw (self, amount):
        if amount => 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawed {amount}. New Balance: {self.balance"}")
        else
            print ("Invalid withdrawal")

    
    def get_balance (self)
        return self.balance
        

        
