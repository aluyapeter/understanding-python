class WalletSystem:
    def __init__(self):
        self.wallets = {}
        self.txns = {}
    
    def get_balance(self, user_id):
        return self.wallets.get(user_id, 0)

    def credit(self, user_id, amount, txn_key):
        if amount < 0:
            return ("AMOUNT CANNOT BE NEGATIVE")
        if txn_key in self.txns:
            return self.wallets.get(user_id)
        
        current_balance = self.get_balance(user_id)
        new_balance = current_balance + amount

        self.wallets[user_id] = new_balance
        self.txns[txn_key] = True

        return (self.wallets.get(user_id))
    
    def debit(self, user_id, amount, txn_key):
        if amount < 0:
            return ("AMOUNT CANNOT BE NEGATIVE")
        if txn_key in self.txns:
            return self.wallets.get(user_id)
        current_balance = self.get_balance(user_id)
        if current_balance < amount:
            return "Insufficient funds"
        
        new_balance = current_balance - amount
        self.wallets[user_id] = new_balance
        self.txns[txn_key] = True

        return (self.wallets.get(user_id))


wallet = WalletSystem()

# print(wallet.get_balance("alice"))

# wallet.wallets["alice"] = 200000
# print(wallet.get_balance("alice"))

# wallet.credit("Jay", 200, "txn1")
# wallet.credit("Jay", 2000, "txn2")
# print(wallet.get_balance("Jay"))

wallet.credit("Sam", 200, "txn1")
print(wallet.get_balance("Sam"))

wallet.debit("Sam", 1000, "txn2")
print(wallet.get_balance("Sam"))