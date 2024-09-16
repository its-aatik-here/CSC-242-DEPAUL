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
    def withdraw(self,value):
        self.balance -= value
        return
    

class animal(object) :
   
    def __init__(self,_species,language="default"):
        self.species=_species
        self.language=language
        return
    def setSpecies (self,_species):
       self.species = _species
       return
    def setLanguage (self,language):
       self.language = language
       return
    def speak(self):
       res = "I am a " +self.species+ " and I "+self.language
       return res
    def __repr__(self):
        return f"animal(self.species), (self.language)"
    def __str__(self):
        return self.speak
    
    
       


code.interact(local=dict(globals(), **locals()))