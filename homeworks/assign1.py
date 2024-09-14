import code 

#EXERCISE 1

def remove_whitespace (word):
    assert isinstance (word,str), "input must be a string"
    return word.replace(" ", "")

def assert_short_name (name):
    assert len(name)<6, "name is too long"
    return f"{name} is a short name"

def average_positives (list):
    for num in list:
        assert num > 0, "not_a positive value"
    average = sum(list)/len(list)
    return average


# EXERCISE 2
def test_asserts():
    # Test the remove_whitespace function
    assert remove_whitespace("hello world") == "helloworld"
    assert remove_whitespace("Linus torvalds") == "Linustorvalds"
    assert remove_whitespace("Python is best") == "Pythonisbest"
    print ("Completed function 1 Test")
    # Test the assert_short_name function
    assert assert_short_name("John") == "John is a short name"
    assert assert_short_name("Doe") == "Doe is a short name"
    assert assert_short_name("linus") == "linus is a short name"
    print ("Completed function 2 Test")
    # Test the average_positives function
    assert average_positives ([1,2,3,4,5]) == 3
    assert average_positives ([1,1,1,1,1]) == 1
    assert average_positives ([2,2,2,2,2]) == 2
    print ("Completed function 3 Test")

test_asserts()

import code 

#Exercise 3 and 4
class Weather:
        def __init__(self,temperature = 0):
            self.temperature = temperature
        def set_temp(self, temperature):
            self.temperature = temperature
        def get_temp(self):
            return self.temperature
        def convert(self):
            celsius = self.temperature
            fahrenheit = (celsius * 9/5) + 32
            return fahrenheit
        def __str__(self):
            return f"Temperature: {self.temperature} degrees celcius"

code.interact(local=dict(globals(), **locals()))