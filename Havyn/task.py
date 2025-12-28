# user = [user_id, wallet_id, txn_rf]
# balance, wallet_id

class Wallet(self, user_id, balance):
    self.user_id = user_id
    self.txn = {} #(txn_ref, user_id) => result
    self.balances = {} #user_id => balance


    def credit(self, user_id, amount, txn_rf):
        if amount <= 0:
            return ("Error balance should be more than 0")

        if (user_id, txn_rf) in self.seen:
            return ("Transaction done before, balance after transaction:", self.txn[(user_id, txn_rf)])

        self.balances[user_id] += amount
        self.txn[(user_id, txn_rf)] = self.balance
        return ("Transaction success", self.balance)

    def debit(self, user_id, amount, txn_ref):
        if amount <= 0:
            return ("Error balance should be more than 0")

        if txn_rf in self.txn:
            return ("Transaction done before, balance after transaction:", self.txn[txn_rf])
        
        if self.balance - amount < 0:
            return ("Error balance can not be negative")

        self.balance -= amount
        self.txn[txn_rf] = self.balance
        return ("Transaction success", self.balance)

    def get_balance(user_id):
        return self.balances[user_id]



self.seen = {} #(txn_ref, user_id) => result
self.balances = {} #user_id => balance

        
        
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# thisdict["color"] = "red"
# print(thisdict["brand"])
# def deposit(user_id, amount, txn_rf):
#     user = Wallet()
#     user.user_id = 1
#     user.balance = 0
