from BankAccountSol import Account

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

    def __add__(self, other):
        return Animal(self.species + "/" +other.species,\
                      self.language + "/" + other.language)

class Bird(Animal):
    'a class that extends Animal for a bird'
    
    def fly(self, n):
        'returns a message about the height of flight'
        return 'I am flying {} feet!'.format(n)
    
    def __init__(self, lang = 'chirp'):
        Animal.__init__(self, 'bird', lang)

    def __repr__(self):
        return "Bird({})".format(self.language)

    def __str__(self):
        return Animal.speak(self)
        
class EstateAnimal(Animal):
    'an abstraction of an animal with funds for its care'

    def __init__(self, species = 'dodo bird', language = 'squawk',init_money=0):
        'the constructor'
        Animal.__init__(self,species,language)
        self.acct = Account(init_money)

    def addFunds(self, value):
        'add some money to the Account for the animal'
        self.acct.deposit(value)

    def __repr__(self):
        'the representation'
        return f"EstateAnimal({self.species}, {self.language}, {self.acct})"

    def __str__(self):
        'the string representation'
        return self.speak()

    # def setLanguage(self, lang):
    #     'set the language'
    #     self.language = lang

    # def setSpecies(self, species):
    #     'sets the species'
    #     self.species = species

    # def speak(self):
    #     'returns the animal speaking'
    #     return f"I am a {self.species} and I {self.language}"