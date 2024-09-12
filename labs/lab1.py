# import code 

#EXERCISE 1


def isPositive(num):
    if num > 0:
        return True
    else:
        return False

assert isPositive (10) == True
assert isPositive (-10) == False
assert isPositive (0) == False



def areBothStrings(val1,val2):
    if type(val1)==str and type (val2) == str:
        return True
    else:
        return False
assert areBothStrings("a","b") == True
assert areBothStrings("1",1) == False  
assert areBothStrings(1,1) == False


def secondString (randomword,second=" "):
    if len(randomword)>2:
        second = randomword [1]
    return second

assert secondString ("hello") == "e"
assert secondString ("1") == " "
assert secondString ("bye") == "y"





# Exercise 2

class socialAccount (object):
    def __init__(self,follower=0 ):
        self.follower=follower
    def add_follower(self):
        self.follower += 1
    def remove_follower(self):
        if self.follower > 0:
            self.follower -= 1
    def status (self):
        print(f"you have {self.follower} followers")

# code.interact(local=dict(globals(), **locals()))