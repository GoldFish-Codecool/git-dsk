from BankAccount import BankAccount


if __name__ == "__main__":

    bank_account_john = BankAccount ("John", 500)
    bank_account_john.deposit(300)
    bank_account_john.withdraw(150)

    print(f"John's bank account number is: {bank_account_john.account_number}, and his balance is: {bank_account_john.get_balance()}")


