import code 

class account (object):
    def __init__(self,initial_value=0):
        self.balance = initial_value
    def set (self,value):
        self.balance = value
    def get(self):
        return self.balance
    
    def deposit(self,value):
        self.balance += value
        return
    
code.interact(local=dict(globals(), **locals()))