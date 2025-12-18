The Task:

Create a file bank.py.

Create a class Account.

__init__(self, owner, balance=0): Sets owner name and initial balance.

deposit(self, amount): Adds amount to balance.

withdraw(self, amount): Subtracts amount. If insufficient funds, raise ValueError.

Create a file test_bank.py.

Create a fixture named empty_account that returns an Account for "User" with 0 balance.

Create a fixture named loaded_account that returns an Account for "User" with 100 balance.

Test 1: test_initial_balance: Use empty_account to verify balance is 0.

Test 2: test_deposit: Use empty_account, deposit 50, assert balance is 50.

Test 3: test_withdraw: Use loaded_account, withdraw 30, assert balance is 70.

Test 4: test_insufficient_funds: Use empty_account, try to withdraw 10, assert ValueError is raised.