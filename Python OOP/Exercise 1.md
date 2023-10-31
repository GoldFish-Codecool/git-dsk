**Banking System Mini Project**

Imagine you are tasked with building a simple banking system with the following requirements:

1. Create a `BankAccount` class that allows users to create and manage bank accounts. Each account should have the following attributes:
   - `account_number` (a unique identifier for each account)
   - `account_holder` (the name of the account holder)
   - `balance` (the current account balance)
   
2. Implement the following instance methods for the `BankAccount` class:
   - `__init__(self, account_holder, initial_balance)`: Initializes a new account with an account number, account holder's name, and initial balance.
   - `deposit(self, amount)`: Adds the specified amount to the account balance.
   - `withdraw(self, amount)`: Subtracts the specified amount from the account balance, if sufficient funds are available.
   - `get_balance(self)`: Returns the current account balance.

3. Implement a class variable to keep track of the total number of accounts created.

4. Create subclasses of `BankAccount` for specific account types, such as `SavingsAccount` and `CheckingAccount`. Customize these subclasses by adding class-specific attributes and methods.

5. Implement a class method to display the total number of accounts created.

6. Create instances of the `BankAccount`, `SavingsAccount`, and `CheckingAccount` classes, and demonstrate the following actions:
   - Creating accounts with different account types and initial balances.
   - Depositing and withdrawing funds from accounts.
   - Checking account balances.
   - Displaying the total number of accounts.

7. Demonstrate inheritance by showing how the subclasses inherit attributes and methods from the parent `BankAccount` class.

8. Implement additional features or customization to further showcase your understanding of classes in Python.
