#Consider the function sumLen() that takes a list of strings as a parameter and returns the sum of the lengths of all the strings.
import code

# def sumLen(lst):
#     'return the sum of the lengths of the strings in the list lst'
#     total = 0
#     for astr in lst:
#         assert type(astr) == str, "The input is not string"
#         total += len(astr)
#     return total

# lst = [1,2,3,4,5,6]



class Account (object):

    def set(self,value):
        self.balance = value
    
    def get(self):
        return self.balance
    
    def deposit (self,value):
        self.balance += value
    
    def withdraw(self,value):
        self.balance -=value
    
    def __str__(self):
        return f'Account ({self.balance})'
    
    def __repr__(self):
        return f"$ {self.balance:.2f}"


class Animal ():
    def __init__(self,species= "default",language= "default"):
        self.species = species
        self.language = language


    def setSpecies(self,value):
        self.species = value
    def setLanguage (self,value):
        self.language = value
    def speak(self):
        return f"I am a {self.species} and I {self.language}"
    def __str__(self):
        return self.speak()
    def __repr__(self):
        return f"animal({self.species} {self.language})"
    

code.interact(local=dict(globals(), **locals()))