import pytest
from bank import Account

@pytest.fixture
def empty_account():
    return Account("User", 0)

@pytest.fixture
def loaded_account():
    return Account("User", 100)

def test_initial_balance(empty_account):
    assert empty_account.balance == 0

def test_deposit(empty_account):
    empty_account.deposit(50)
    assert empty_account.balance == 50

def test_withdraw(loaded_account):
    loaded_account.withdraw(30)
    assert loaded_account.balance == 70

def test_insufficient_funds(empty_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        empty_account.withdraw(10)