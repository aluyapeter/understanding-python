class WalletSystem:
    def __init__(self):
        self.wallets = {}
        self.txns = {}
    
    def get_balance(self, user_id):
        return self.wallets.get(user_id, 0)

wallet = WalletSystem()

print(wallet.get_balance("alice"))

wallet.wallets["alice"] = 200000
print(wallet.get_balance("alice"))