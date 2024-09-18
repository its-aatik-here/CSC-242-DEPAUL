class Account(object):
    'a bank account class'

    def set(self, value):
        'set the balance to value'
        self.balance = value

    def get(self):
        'return the current balance on the account'
        return self.balance

    def deposit(self, value):    
        'updates the bank account by depositing value amount'
        self.balance += value      

    def withdraw(self, value):  
        'updates the bank account by withdrawing value amount'
        self.balance -= value

    def __init__(self, value = 0.0):
        'the constructor'
        self.balance = value

    def __init__(self, value = 0.0):
        'the constructor'
        self.balance = value

    def __repr__(self):
        return f"Account({self.balance})"

    def __str__(self):
        return f"${self.balance:.2f}" 

class Savings(Account):
    'a savings account'

    def __init__(self, amount = 100.0, rate = 0.001):
        'the constructor'
        Account.__init__(self, amount)
        self.rate = rate
    
    def setRate(self, value):
        'set the yearly interest rate'
        self.rate = value

    def addInterest(self):
        'add one month of interest to the balance'
        self.balance += self.balance*(self.rate/12)
        
    def get(self):
        'returns the value of the balance as a string'
        return f'balance = ${self.balance:.2f}\nrate = {self.rate}'

    def __repr__(self):
        return f"Savings({self.balance}, {self.rate})"

    def __str__(self):
        return self.get()
