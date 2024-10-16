def vertical(n):         
    if n < 10:           
        print(n)         
    else:                
        print(n % 10)    
        vertical (n//10) 

def printLst(lst):
    if len(lst) == 0:
        return
    else:
        print(lst[0])
        printLst(lst[1:])
        
def cheer(n):
    if n <= 1:
        print ("Hurrah")
    else:
        print("Hip")
        cheer(n-1)

def cheer2(n):
    'create a cheer in a string'
    if n <= 1:
        return "Hurrah!"
    else:
        s = cheer2(n-1)
        return "Hip " + s

def pattern(n):
    if n <= 1:
        print (1, end = " ")
    else:
        pattern(n-1)
        print(n, end = " ")
        pattern(n-1)

def makePattern(n):
    if n <= 1:
        return "1"
    else:
        s = makePattern(n-1)
        return s + " {} ".format(n) + s

def recLenLst(lst):
    'return the length of lst recursively'
    if lst == []:
        return 0
    else:
        return 1 + recLenLst(lst[1:])

def countInts(lst):
    'return the number of integers in lst'
    if lst == []:
        return 0
    elif type(lst[0]) == int:
        return 1 + countInts(lst[1:])
    elif type(lst[0]) == list:
        return countInts(lst[0]) + countInts(lst[1:])
    else:
        return countInts(lst[1:])

def findMax(lst):
    'find the maximum in a list of numbers'
    if len(lst) == 0:
        return 0
    elif type(lst[0]) == int or type(lst[0]) == float:
        val = findMax(lst[1:])
        if lst[0] > val:
            return lst[0]
        else:
            return val
    elif type(lst[0]) == list:
        val1 = findMax(lst[0])
        val2 = findMax(lst[1:])
        if val1 > val2:
            return val1
        else:
            return val2
    else:
        return findMax(lst[1:])
