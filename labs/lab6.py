# import code


# Exercise 1
def findMinimum(lst):
    if  len(lst) == 1:
        return lst[0]
    min_rest  = findMinimum(lst[1:])
    if lst [0] <  min_rest:
        return lst [0]
    else:
        return min_rest

        
# Exercise 2
def changePi(s):
    if len(s) < 2:
        return s
    elif s[:2] == "pi":
        return "3.14" + changePi(s[2:])
    else:
        return s[0] + changePi(s[1:])
    
# Exercise 3
def checkSorted(siuu):
    if len(siuu) == 1:
        return True
    elif siuu[0] <= siuu[1]:
        return  checkSorted(siuu[1:])
    else:
        return False

# code.interact(local=dict(globals(), **locals()))