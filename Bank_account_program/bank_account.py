class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def getBalance(self):
        return self.balance
