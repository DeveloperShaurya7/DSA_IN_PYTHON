class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance
    
account = BankAccount(10000)
print("Balance:", account.get_balance())    
