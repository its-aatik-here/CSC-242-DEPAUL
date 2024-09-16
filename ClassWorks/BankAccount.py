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

    def __repr__(self):
        return "Account({})".format(self.balance)

    def __str__(self):
        return f"${self.balance:.2f}"

if __name__ == '__main__':
    acct1 = Account()
    assert acct1.get() == 0, f"get on a default Account failed"
    acct2 = Account(100)
    # Change this one so that it references acct1 and will trigger
    assert repr(acct2) == 'Account(100)', 'wrong representation for Account(100)'

