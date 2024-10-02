
import code 
class Animal(object):
    'a class that abstracts an animal'
    def __init__(self, spec = 'default', lang = 'default'):
        self.species = spec
        self.language = lang
        
    def setSpecies(self, name):
        'sets the species of the animal'
        self.species = name
        
    def setLanguage(self, lang):
        'sets the language of the animal'
        self.language = lang
        
    def speak(self):
        return f'I am a {self.species} and I {self.language}'
    
    def __repr__(self):
        return f'Animal({self.species}, {self.language})'

    def __str__(self):
        return self.speak()
    

# updates
from BankAccount import Account

class EstateAnimal(object):
    'a class that abstracts an estate animal'
    def __init__(self, spec='default', lang='default'):
        self.species = spec
        self.language = lang
        self.account = Account()

    def setSpecies(self, name):
        'sets the species of the animal'
        self.species = name
        
    def setLanguage(self, lang):
        'sets the language of the animal'
        self.language = lang
        
    def speak(self):
        return f'I am a {self.species} and I {self.language}'

    def __repr__(self):
        return f'EstateAnimal({self.species}, {self.language}, {self.account})'

    def addFunds(self, amount):
        self.account.deposit(amount)

    def withdrawFunds(self, amount):
        self.account.withdraw(amount)



class saving(Account):
    def __init__(self):
        super().balance
        self.balance = 0
    def setRate (self,value):
        self.rate = value
    def addInterest (self):
        self.balance += self.balance * (self.rate/12)
    def get(self):
        print (f"balance = ${self.balance} \ nrate = {self.rate}")


code.interact(local=dict(globals(), **locals()))
