class Account(object):
    'a more complete bank account class'

    def __init__(self, val = 0):
        'the constructor'
        assert type(val) == int or type(val) == float, f'{val} not numeric'
        assert val >= 0, 'parameter negative'
        self.__balance = val

    def set(self, value):
        'set the balance to value'
        assert type(value) == int or type(value) == float, f'{value} not numeric'
        assert value >= 0, 'parameter negative'
        self.__balance = value

    def get(self):
        'return the current balance on the account'
        return self.__balance
    
    def deposit(self, val):
        'deposit val dollars into the account'
        assert type(val) == int or type(val) == float, f'{val} not numeric'
        assert val > 0, 'parameter not positive'
        self.__balance += val

    def withdraw(self, value):
        'withdraw value dollars from the account'
        assert type(value) == int or type(value) == float, f'{value} not numeric'
        assert value > 0, 'parameter not positive'
        assert value <= self.__balance, 'insufficient funds'
        self.__balance -= value

    def __repr__(self):
        'the representation of an Account'
        return f"Account({self.__balance})"

    def __str__(self):
        'the string representation of an Account'
        return f"${self.__balance:.2f}"

