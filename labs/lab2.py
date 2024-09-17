from clicker import Clicker


# Exercise 1


class MarathonCounter:
    def __init__(self):
        self.clicker = Clicker ()
    def new_race(self):
        self.clicker.clear()
        print ("Clearing clicker for new race")
    def next_runner(self):
        self.clicker.press()
    def __str__(self):
        return f"{self.clicker.get_total()} runners have completed the Chicago Marathon."


#Exercise 2


class Animal:
    def speak(self):
        print ("I am an Animal")
class Mammal(Animal):
    def speak (self):
        Animal.speak(self)
        print ("I am a Mammal")
class cat (Mammal):
    def speak (self):
        Mammal.speak(self)
        print ("I am a cat")
        print ("Miau")
class Primate (Mammal):
    def speak (self):
        Mammal.speak(self)
        print ("I am a Primate")
class Hacker (Primate):
    def speak (self):
        Primate.speak(self)
        print ("I am a Hacker")
        print ("I love Bugs")


#Exercise 3

from my_funcs import str_to_list
from my_funcs import makeExcited
from my_funcs import double_evens
def test_asserts():
    assert str_to_list("AatikAli") == ["A","a","t","i","k","A",'l',"i"]
    assert str_to_list("Ali") == ["A",'l',"i"]
    assert str_to_list("apple") == ["a",'p',"p","l","e"]

    assert makeExcited("You are lazy.") == ("You are Lazy!")
    assert makeExcited("siuuuuu.") == ("siuuuuu!")
    assert makeExcited("I wanna sleep.") == ("I wanna sleep!")

    assert double_evens([9,10,11,12]) == ([9,20,11,24])
    assert double_evens([0,2,4,6,8]) == ([0,4,8,12,16])
    assert double_evens([1,3,5,7,9]) == ([1,3,5,7,9])
