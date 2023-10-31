from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

if __name__ == "__main__":

    bank_account_list = []

#    bank_account_list.append(CheckingAccount("John", 500, 100))
#    bank_account_list[0].deposit(300)
#    bank_account_list[0].withdraw(150)

#    print(f"John's bank account number is: {bank_account_list[0].account_number}, and his balance is: {bank_account_list[0].get_balance()}")

#    bank_account_list[0].deposit(-100)

#    bank_account_list[0].withdraw(1000)

#    bank_account_list.append(BankAccount("Mary", 600))

#    bank_account_of_jake = SavingsAccount("Jake", 1000, 10)

#    bank_account_list.append(bank_account_of_jake)

#   for i in range(10):
#        bank_account_of_jake.apply_interest()

    name = input("Account holder's name:")
    balance = int(input("Balance:"))

    bank_account_list.append(BankAccount(name, balance))
    
    for account in bank_account_list:
        print(account)